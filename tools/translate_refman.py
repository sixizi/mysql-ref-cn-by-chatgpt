#!/usr/bin/env python3
"""Translate changed MySQL Reference Manual sections from a local PDF."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests
from pypdf import PdfReader


@dataclass
class OutlineNode:
    depth: int
    title: str
    page: int
    key: str | None
    leaf: bool
    path: tuple[str, ...]
    raw_path: tuple[str, ...]


def section_key(title: str) -> str | None:
    match = re.match(r"^(?:Chapter\s+)?([A-Z]?\.?\d+(?:\.\d+)+)\s+", title)
    return match.group(1) if match else None


def normalize_title(title: str) -> str:
    value = re.sub(r"^[A-Z]?\.?\d+(?:\.\d+)*\s*", "", title)
    return re.sub(r"\s+", " ", value.replace("\xa0", " ")).strip().lower()


def outline_nodes(reader: PdfReader) -> list[OutlineNode]:
    flat: list[dict[str, Any]] = []

    def walk(
        items: list[Any],
        depth: int,
        normalized_ancestors: tuple[str, ...],
        raw_ancestors: tuple[str, ...],
    ) -> None:
        last_title = ""
        for item in items:
            if isinstance(item, list):
                if last_title:
                    walk(
                        item,
                        depth + 1,
                        normalized_ancestors + (normalize_title(last_title),),
                        raw_ancestors + (last_title,),
                    )
                else:
                    walk(item, depth + 1, normalized_ancestors, raw_ancestors)
            else:
                title = str(item.title)
                last_title = title
                flat.append(
                    {
                        "depth": depth,
                        "title": title,
                        "page": reader.get_destination_page_number(item),
                        "path": normalized_ancestors + (normalize_title(title),),
                        "raw_path": raw_ancestors + (title,),
                    }
                )

    walk(reader.outline, 0, (), ())
    nodes: list[OutlineNode] = []
    for index, item in enumerate(flat):
        is_leaf = index + 1 >= len(flat) or flat[index + 1]["depth"] <= item["depth"]
        nodes.append(
            OutlineNode(
                depth=item["depth"],
                title=item["title"],
                page=item["page"],
                key=section_key(item["title"]),
                leaf=is_leaf,
                path=tuple(item["path"]),
                raw_path=tuple(item["raw_path"]),
            )
        )
    return nodes


def load_pages(text_path: Path) -> list[str]:
    pages = text_path.read_text(encoding="utf-8", errors="ignore").split("\f")
    cleaned: list[str] = []
    for page in pages:
        lines: list[str] = []
        for line in page.splitlines():
            stripped = line.strip()
            if re.fullmatch(r"MySQL (?:8\.0|9\.7|26\.7|26\.10) Reference Manual", stripped):
                continue
            if re.fullmatch(r"\d{1,4}", stripped):
                continue
            if stripped in {"Next", "Previous", "Prev", "Home", "Up", "Contents"}:
                continue
            if re.match(r"^\.![^!]+!", stripped):
                continue
            lines.append(line)
        cleaned.append("\n".join(lines).strip())
    return cleaned


def extract_section(
    nodes: list[OutlineNode], pages: list[str], key: str, title: str
) -> str:
    matches = [node for node in nodes if node.key == key]
    if not matches:
        raise RuntimeError(f"Outline section not found: {key}")
    index = nodes.index(matches[0])
    node = nodes[index]
    following = nodes[index + 1] if index + 1 < len(nodes) else None
    end_page = following.page if following else min(node.page + 1, len(pages) - 1)
    if end_page < node.page:
        end_page = node.page
    text = "\n".join(pages[node.page : end_page + 1])
    title_pattern = re.escape(title.replace("\xa0", " "))
    start_match = re.search(rf"^\s*{title_pattern}\s*$", text, re.MULTILINE)
    if start_match:
        text = text[start_match.start() :]
    if following:
        end_match = re.search(
            rf"^\s*{re.escape(following.title.replace('\xa0', ' '))}\s*$",
            text,
            re.MULTILINE,
        )
        if end_match:
            text = text[: end_match.start()]
    return text.strip()


def numeric_sort_key(key: str) -> str | None:
    if re.fullmatch(r"\d+(?:\.\d+)*", key):
        return ".".join(f"{int(value):02d}" for value in key.split("."))
    appendix = re.fullmatch(r"([A-Z])(.*)", key)
    if appendix:
        prefix = appendix.group(1)
        remainder = appendix.group(2).lstrip(".")
        if not remainder:
            return prefix
        if re.fullmatch(r"\d+(?:\.\d+)*", remainder):
            return ".".join([prefix] + [str(int(value)) for value in remainder.split(".")])
    return None


def build_markdown_index(
    root: Path,
) -> tuple[dict[str, list[Path]], dict[str, list[Path]], dict[str, list[Path]]]:
    numeric: dict[str, list[Path]] = {}
    appendix: dict[str, list[Path]] = {}
    english_titles: dict[str, list[Path]] = {}
    for path in root.rglob("*.md"):
        match = re.match(r"^([A-Z])((?:\.\d+){1,3})", path.name)
        if match:
            parts = [match.group(1)] + match.group(2).lstrip(".").split(".")
            appendix.setdefault(".".join(parts), []).append(path)
            continue
        match = re.match(r"^(\d{2}(?:\.\d{2}){0,3})", path.name)
        if match:
            numeric.setdefault(match.group(1), []).append(path)
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for match in re.finditer(r"\[([^\]]{3,240})\]\((https?://[^)\s]+)\)", content):
            title = normalize_title(match.group(1))
            if title and path not in english_titles.setdefault(title, []):
                english_titles[title].append(path)
    return numeric, appendix, english_titles


def path_for_key(key: str, numeric: dict[str, list[Path]], appendix: dict[str, list[Path]]) -> list[Path]:
    sort_key = numeric_sort_key(key)
    if not sort_key:
        return []
    if sort_key.startswith(("A.", "B.", "C.")):
        return appendix.get(sort_key, [])
    return numeric.get(sort_key, [])


def title_path_index(nodes: list[OutlineNode]) -> dict[tuple[str, ...], list[OutlineNode]]:
    result: dict[tuple[str, ...], list[OutlineNode]] = {}
    for node in nodes:
        if node.key:
            path = node.path[1:] if len(node.path) > 1 else node.path
            result.setdefault(path, []).append(node)
    return result


def choose_old_path(
    item: dict[str, Any],
    target_nodes: list[OutlineNode],
    old_nodes: list[OutlineNode],
    numeric: dict[str, list[Path]],
    appendix: dict[str, list[Path]],
    english_titles: dict[str, list[Path]],
) -> tuple[Path | None, str]:
    key = item["key"]
    direct = path_for_key(key, numeric, appendix)
    if direct:
        return direct[0], "direct"

    matches = [node for node in target_nodes if node.key == key and node.leaf]
    if not matches:
        return None, "no-target-outline"
    target_path = matches[0].path[1:] if len(matches[0].path) > 1 else matches[0].path
    old_by_path = title_path_index(old_nodes)
    candidates = old_by_path.get(target_path, [])
    if not candidates:
        return None, "new"
    if len(candidates) > 1:
        try:
            chapter = int(key.split(".")[0])
            candidates = [node for node in candidates if node.key and node.key.split(".")[0].isdigit() and int(node.key.split(".")[0]) == chapter]
        except ValueError:
            pass
    if len(candidates) != 1:
        return None, "ambiguous-title-path"
    mapped = path_for_key(candidates[0].key or "", numeric, appendix)
    if mapped:
        return mapped[0], f"title-path:{candidates[0].key}"
    english_matches = english_titles.get(normalize_title(item["title_b"]), [])
    try:
        chapter = int(key.split(".")[0])
        chapter_prefix = f"{chapter:02d}."
        english_matches = [
            path
            for path in english_matches
            if path.relative_to(Path.cwd()).parts[0].startswith(chapter_prefix)
        ]
    except ValueError:
        pass
    if len(english_matches) == 1:
        return english_matches[0], "english-title"
    return None, "old-title-without-file"


def split_source(source: str, target_words: int = 3500) -> list[str]:
    paragraphs = re.split(r"\n\s*\n", source)
    chunks: list[str] = []
    current: list[str] = []
    words = 0
    for paragraph in paragraphs:
        paragraph_words = len(paragraph.split())
        if current and words + paragraph_words > target_words:
            chunks.append("\n\n".join(current))
            current = []
            words = 0
        current.append(paragraph)
        words += paragraph_words
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def call_model(
    session: requests.Session,
    endpoint: str,
    api_key: str,
    model: str,
    system: str,
    user: str,
    max_tokens: int,
) -> tuple[str, dict[str, Any]]:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.1,
        "max_tokens": max_tokens,
    }
    for attempt in range(4):
        try:
            response = session.post(
                endpoint,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=300,
            )
            if response.status_code not in {200, 408, 429} and response.status_code < 500:
                raise RuntimeError(f"HTTP {response.status_code}: {response.text[:500]}")
            if response.status_code == 200:
                break
        except requests.RequestException as error:
            if attempt == 3:
                raise RuntimeError(f"Model request failed: {error}") from error
        if attempt < 3:
            time.sleep(2 ** attempt)
    else:
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:500]}")
    body = response.json()
    message = body["choices"][0]["message"]
    content = message.get("content", "").strip()
    if message.get("reasoning_content"):
        content = message["reasoning_content"].strip() + "\n\n" + content if content else message["reasoning_content"].strip()
    return content, body.get("usage", {})


def translate_section(
    source: str,
    section_title: str,
    target_version: str,
    endpoint: str,
    api_key: str,
    model: str,
) -> tuple[str, list[dict[str, Any]]]:
    system = (
        "你是专业的 MySQL 官方参考手册翻译引擎。将英文 PDF 提取文本转换为准确、自然的简体中文 Markdown。"
        "第一行必须是 Markdown 标题：保留章节编号，并将标题正文译成中文，例如 `### 1.2.2 MySQL 的主要特性`。"
        "将 PDF 提取出的项目符号规范为 Markdown `- ` 列表，不要保留圆点或额外缩进。"
        "保留代码、SQL、命令、选项、变量、表名、文件名、路径、产品名和版本号为英文原样；"
        "链接地址保持不变，链接文字翻译。不要添加说明、前言、结语或代码围栏。只输出译文。"
    )
    chunks = split_source(source)
    translated: list[str] = []
    usages: list[dict[str, Any]] = []
    with requests.Session() as session:
        for index, chunk in enumerate(chunks, start=1):
            user = (
                f"MySQL {target_version} Reference Manual\n"
                f"Section: {section_title}\n"
                f"Chunk {index} of {len(chunks)}\n\n"
                "Translate the following source to Simplified Chinese Markdown. "
                "Continue exactly where the source begins and stop exactly where it ends. "
                "Do not summarize and do not add commentary.\n\n"
                f"{chunk}"
            )
            content, usage = call_model(
                session, endpoint, api_key, model, system, user, max_tokens=20000
            )
            if not content:
                raise RuntimeError(f"Empty model response for chunk {index}/{len(chunks)}")
            if re.fullmatch(r"```(?:markdown)?\n.*\n```", content, re.DOTALL):
                content = re.sub(r"^```(?:markdown)?\n", "", content)
                content = re.sub(r"\n```$", "", content)
            translated.append(content.strip())
            usages.append(usage)
    return "\n\n".join(translated), usages


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="\n", dir=path.parent, delete=False
    ) as handle:
        handle.write(content.rstrip() + "\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def replace_versions(root: Path, source: str, target: str) -> int:
    changed = 0
    for path in root.rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        updated = original.replace(source, target)
        if updated != original:
            atomic_write(path, updated)
            changed += 1
    return changed


def safe_filename(title: str) -> str:
    value = title.replace("\xa0", " ")
    value = re.sub(r"^(?:Chapter\s+)?(?:[A-Z]\.)?\d+(?:\.\d+)*\s*", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"[\\/:*?\"<>|]", "-", value)
    return value[:160].rstrip(" .")


def new_file_path(root: Path, key: str, raw_path: tuple[str, ...]) -> Path:
    display_titles = [safe_filename(title) for title in raw_path]
    appendix_match = re.fullmatch(r"([A-Z])(?:\.(\d+)){1,3}", key)
    if appendix_match:
        letter = appendix_match.group(1)
        base_dirs = sorted(path for path in root.glob(f"{letter}.*") if path.is_dir())
        base = base_dirs[0] if base_dirs else root / letter
        numeric_parts = list(appendix_match.groups()[1:])
        if len(numeric_parts) <= 2:
            return base / f"{key}.{display_titles[-1]}.md"
        parent_key = ".".join([letter] + numeric_parts[:-1])
        parent_dirs = [path for path in base.rglob(f"{parent_key}.*") if path.is_dir()]
        parent = parent_dirs[0] if parent_dirs else base / parent_key
        return parent / f"{key}.{display_titles[-1]}.md"
    parts = key.split(".")
    sort_key = numeric_sort_key(key)
    if not sort_key:
        raise RuntimeError(f"Cannot create path for nonnumeric section {key}")
    prefixes = [".".join(f"{int(value):02d}" for value in parts[:length]) for length in range(len(parts), 0, -1)]
    base = root
    matched_length = 0
    for prefix in prefixes:
        candidates = [path for path in root.rglob(f"{prefix}.*") if path.is_dir()]
        if candidates:
            base = min(candidates, key=lambda path: len(path.parts))
            matched_length = len(prefix.split("."))
            break
    remaining = len(parts) - matched_length
    for offset in range(remaining - 1):
        component = matched_length + offset + 1
        prefix = ".".join(f"{int(value):02d}" for value in parts[:component])
        title_index = component - 1
        base = base / f"{prefix}.{display_titles[title_index]}"
        base.mkdir(parents=True, exist_ok=True)
    return base / f"{sort_key}.{display_titles[-1]}.md"


def cmd_translate(args: argparse.Namespace) -> int:
    root = Path.cwd()
    pdf_path = root / args.pdf
    old_pdf_path = root / args.old_pdf
    text_path = Path(args.text)
    diff_path = Path(args.diff_json)
    items = json.loads(diff_path.read_text(encoding="utf-8"))
    if args.limit:
        items = items[args.offset : args.offset + args.limit]
    else:
        items = items[args.offset :]

    target_nodes = outline_nodes(PdfReader(pdf_path))
    old_nodes = outline_nodes(PdfReader(old_pdf_path))
    pages = load_pages(text_path)
    numeric, appendix, english_titles = build_markdown_index(root)

    endpoint = os.environ["BITDEER_API_URL"].rstrip("/") + "/chat/completions"
    api_key = os.environ["BITDEER_API_KEY"]
    model = args.model
    state_path = Path(args.state)
    state: dict[str, Any] = {}
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))

    plan: list[tuple[dict[str, Any], Path]] = []
    for item in items:
        key = item["key"]
        if state.get(key) == "done" and not args.force:
            continue
        existing, reason = choose_old_path(
            item, target_nodes, old_nodes, numeric, appendix, english_titles
        )
        matches = [node for node in target_nodes if node.key == key and node.leaf]
        raw_path = matches[0].raw_path if matches else (item["title_b"],)
        path = existing if existing else new_file_path(root, key, raw_path)
        plan.append((item, path))

    print(
        f"Sections: {len(plan)}; model={model}; workers={args.workers}; state={state_path}",
        flush=True,
    )
    failures: list[tuple[str, str]] = []
    completed = 0
    started = time.monotonic()

    def worker(entry: tuple[dict[str, Any], Path]) -> tuple[str, str | None]:
        item, path = entry
        key = item["key"]
        try:
            source = extract_section(target_nodes, pages, key, item["title_b"])
            translated, _ = translate_section(
                source,
                item["title_b"],
                args.version,
                endpoint,
                api_key,
                model,
            )
            atomic_write(path, translated)
            return key, None
        except Exception as error:
            return key, f"{type(error).__name__}: {error}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_item = {executor.submit(worker, entry): entry[0] for entry in plan}
        for future in concurrent.futures.as_completed(future_to_item):
            key, error = future.result()
            completed += 1
            if error:
                failures.append((key, error))
                state[key] = {"status": "error", "error": error}
                print(f"FAIL {key}: {error}", flush=True)
            else:
                state[key] = {"status": "done"}
                print(f"DONE {key} ({completed}/{len(plan)})", flush=True)
            if completed % 10 == 0 or completed == len(plan):
                state_path.write_text(
                    json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
                )

    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    elapsed = time.monotonic() - started
    print(
        f"Completed {len(plan) - len(failures)}/{len(plan)} in {elapsed:.1f}s; failures={len(failures)}",
        flush=True,
    )
    return 1 if failures else 0


def cmd_plan(args: argparse.Namespace) -> int:
    root = Path.cwd()
    target_nodes = outline_nodes(PdfReader(root / args.pdf))
    old_nodes = outline_nodes(PdfReader(root / args.old_pdf))
    numeric, appendix, english_titles = build_markdown_index(root)
    rows = []
    for item in json.loads(Path(args.diff_json).read_text(encoding="utf-8")):
        existing, reason = choose_old_path(
            item, target_nodes, old_nodes, numeric, appendix, english_titles
        )
        matches = [node for node in target_nodes if node.key == item["key"] and node.leaf]
        raw_path = matches[0].raw_path if matches else (item["title_b"],)
        path = existing if existing else new_file_path(root, item["key"], raw_path)
        rows.append(
            {
                "key": item["key"],
                "title": item["title_b"],
                "path": str(path),
                "mapping": reason,
            }
        )
    Path(args.output).write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(rows)} rows to {args.output}")
    return 0


def cmd_clean_whitespace(_: argparse.Namespace) -> int:
    result = subprocess.run(
        ["git", "ls-files", "--modified", "--others", "--exclude-standard", "--", "*.md"],
        check=True,
        capture_output=True,
        text=True,
    )
    paths = [Path(path) for path in result.stdout.splitlines() if path]
    for path in paths:
        content = path.read_text(encoding="utf-8")
        cleaned = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)
        if cleaned != content:
            path.write_text(cleaned, encoding="utf-8")
    print(f"Cleaned trailing whitespace in {len(paths)} Markdown files")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    replace_parser = subparsers.add_parser("replace-versions")
    replace_parser.add_argument("--source", required=True)
    replace_parser.add_argument("--target", required=True)
    replace_parser.set_defaults(func=lambda args: print(
        f"Updated {replace_versions(Path.cwd(), args.source, args.target)} files"
    ) or 0)

    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("--pdf", required=True)
    plan_parser.add_argument("--old-pdf", required=True)
    plan_parser.add_argument("--diff-json", required=True)
    plan_parser.add_argument("--output", required=True)
    plan_parser.set_defaults(func=cmd_plan)

    clean_parser = subparsers.add_parser("clean-whitespace")
    clean_parser.set_defaults(func=cmd_clean_whitespace)

    translate_parser = subparsers.add_parser("translate")
    translate_parser.add_argument("--version", required=True)
    translate_parser.add_argument("--pdf", required=True)
    translate_parser.add_argument("--old-pdf", required=True)
    translate_parser.add_argument("--text", required=True)
    translate_parser.add_argument("--diff-json", required=True)
    translate_parser.add_argument("--model", default=os.environ.get("BITDEER_MODEL", "claude-haiku"))
    translate_parser.add_argument("--workers", type=int, default=10)
    translate_parser.add_argument("--offset", type=int, default=0)
    translate_parser.add_argument("--limit", type=int, default=0)
    translate_parser.add_argument("--state", required=True)
    translate_parser.add_argument("--force", action="store_true")
    translate_parser.set_defaults(func=cmd_translate)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args) or 0)


if __name__ == "__main__":
    sys.exit(main())
