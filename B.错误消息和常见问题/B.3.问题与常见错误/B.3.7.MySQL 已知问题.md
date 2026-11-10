## B.3.7 MySQL 中的已知问题

本节列出了最近版本的 MySQL 中的已知问题。

有关特定平台的问题，请参阅第 2.1 节"通用安装指南"和第 7.9 节"调试 MySQL"中的安装和调试说明。

以下问题是已知的：

- IN 的子查询优化不如 = 的优化有效。

- 即使使用 lower_case_table_names=2（使 MySQL 能够记住数据库和表名使用的大小写），MySQL 也不会记住 DATABASE() 函数或各种日志中数据库名使用的大小写（在不区分大小写的系统上）。

- 删除 FOREIGN KEY 约束在复制中不起作用，因为该约束在副本上可能有另一个名称。

- REPLACE（以及带有 REPLACE 选项的 LOAD DATA）不会触发 ON DELETE CASCADE。

- 如果不使用 DISTINCT 列表中的所有且仅有这些列，DISTINCT 与 ORDER BY 在 GROUP_CONCAT() 内不起作用。

- 将大整数值（介于 2^63 和 2^64−1 之间）插入十进制或字符串列时，由于该数字在有符号整数上下文中被计算，它被插入为负值。

- 使用基于语句的二进制日志记录时，源服务器将执行的查询写入二进制日志。这是一种非常快速、紧凑且高效的日志记录方法，在大多数情况下都能完美工作。但是，如果查询的设计方式使得数据修改是非确定性的（通常不是推荐的做法，即使在复制之外也是如此），源和副本上的数据可能会变得不同。

  例如：

  - CREATE TABLE ... SELECT 或 INSERT ... SELECT 语句将零值或 NULL 值插入 AUTO_INCREMENT 列。

  - DELETE 如果从具有 ON DELETE CASCADE 属性的外键的表中删除行。

  - REPLACE ... SELECT、INSERT IGNORE ... SELECT 如果插入的数据中有重复的键值。

  当且仅当前面的查询没有保证确定性顺序的 ORDER BY 子句时。

  例如，对于没有 ORDER BY 的 INSERT ... SELECT，SELECT 可能以不同的顺序返回行（这导致行具有不同的排名，因此在 AUTO_INCREMENT 列中获得不同的数字），具体取决于源和副本上优化器所做的选择。

  只有在以下情况下，查询在源和副本上的优化才会不同：

  - 表在源上使用的存储引擎与在副本上使用的存储引擎不同。（可以在源和副本上使用不同的存储引擎。例如，如果副本的可用磁盘空间较少，可以在源上使用 InnoDB，但在副本上使用 MyISAM。）

  - MySQL 缓冲区大小（key_buffer_size 等）在源和副本上不同。

  - 源和副本运行不同的 MySQL 版本，这些版本之间的优化器代码不同。

  此问题也可能影响使用 mysqlbinlog|mysql 的数据库恢复。

  避免此问题的最简单方法是向前面提到的非确定性查询添加 ORDER BY 子句，以确保行始终以相同的顺序存储或修改。使用基于行的或混合日志记录格式也可以避免此问题。

- 如果不使用启动选项指定文件名，日志文件名基于服务器主机名。如果将主机名更改为其他名称，要保留相同的日志文件名，必须显式使用选项，如 --log-bin=old_host_name-bin。请参阅第 7.1.7 节"服务器命令选项"。或者，重命名旧文件以反映主机名更改。如果这些是二进制日志，还必须编辑二进制日志索引文件并修复其中的二进制日志文件名。（副本上的中继日志也是如此。）

- mysqlbinlog 不会删除 LOAD DATA 语句后留下的临时文件。请参阅第 6.6.9 节"mysqlbinlog — 用于处理二进制日志文件的实用程序"。

- RENAME 不适用于 TEMPORARY 表或 MERGE 表中使用的表。

- 使用 SET CHARACTER SET 时，不能在数据库、表和列名中使用已翻译的字符。

- 服务器在比较数据值时仅使用前 max_sort_length 个字节。这意味着如果值仅在前 max_sort_length 个字节之后不同，则不能可靠地在 GROUP BY、ORDER BY 或 DISTINCT 中使用这些值。要解决此问题，请增加变量值。max_sort_length 的默认值为 1024，可以在服务器启动时或运行时更改。

- 数值计算使用 BIGINT 或 DOUBLE 进行（两者通常为 64 位长）。获得的精度取决于函数。一般规则是位函数使用 BIGINT 精度执行，IF() 和 ELT() 使用 BIGINT 或 DOUBLE 精度，其余的使用 DOUBLE 精度。应避免使用无符号长整数值，如果它们解析为大于 63 位（9223372036854775807）的值，除非用于位字段。

- 一个表中最多可以有 255 个 ENUM 和 SET 列。

- 在 MIN()、MAX() 和其他聚合函数中，MySQL 目前按字符串值而不是字符串在集合中的相对位置比较 ENUM 和 SET 列。

- 在 UPDATE 语句中，列从左到右更新。如果引用已更新的列，将获得更新后的值而不是原始值。例如，以下语句将 KEY 增加 2，而不是 1：

  ```
  mysql> UPDATE tbl_name SET KEY=KEY+1,KEY=KEY+1;
  ```

- 可以在同一查询中引用多个临时表，但不能多次引用任何给定的临时表。例如，以下不起作用：

  ```
  mysql> SELECT * FROM temp_table, temp_table AS t2;
  ERROR 1137: Can't reopen table: 'temp_table'
  ```

- 当在联接中使用"隐藏"列时，优化器可能会以不同的方式处理 DISTINCT，而不是不使用隐藏列时。在联接中，隐藏列被计为结果的一部分（即使它们未显示），而在普通查询中，隐藏列不参与 DISTINCT 比较。

  这方面的一个例子是：

  ```
  SELECT DISTINCT mp3id FROM band_downloads
         WHERE userid = 9 ORDER BY id DESC;
  ```

  和

  ```
  SELECT DISTINCT band_downloads.mp3id
         FROM band_downloads,band_mp3
         WHERE band_downloads.userid = 9
         AND band_mp3.id = band_downloads.mp3id
         ORDER BY band_downloads.id DESC;
  ```

  在第二种情况下，可能会在结果集中获得两个相同的行（因为隐藏 id 列中的值可能不同）。

  注意这仅发生在结果中没有 ORDER BY 列的查询中。

- 如果在返回空集的查询上执行 PROCEDURE，在某些情况下 PROCEDURE 不会转换列。

- 创建 MERGE 类型的表不会检查基础表是否为兼容类型。

- 如果使用 ALTER TABLE 向 MERGE 表中使用的表添加 UNIQUE 索引，然后在 MERGE 表上添加普通索引，如果表中有旧的非 UNIQUE 键，则表的键顺序会不同。这是因为 ALTER TABLE 将 UNIQUE 索引放在普通索引之前，以便尽早检测重复键。

- 涉及临时表的 UPDATE 语句与定义了触发器的非临时表的联接可能导致错误，即使 update 语句仅读取非临时表，在以下情况下：

  - 启用只读模式（通过使用 SET GLOBAL read_only = 1）。

  - 事务级别设置为 READ_ONLY（即使用 SET GLOBAL TRANSACTION READ ONLY 或 SET SESSION TRANSACTION READ ONLY）。
