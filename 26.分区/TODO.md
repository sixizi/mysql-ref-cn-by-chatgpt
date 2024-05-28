## 第26章 分区

目录

- [26.1 MySQL中的分区概述](./26.01.MySQL中的分区概述.md)
- [26.2 分区类型](./26.02.分区类型/26.02.00.分区类型.md)
- [26.3 分区管理](./26.03.分区管理/26.03.00.分区管理.md)
- [26.4 分区修剪](./26.04.分区修剪.md)
- [26.5 分区选择](./26.05.分区选择.md)
- [26.6 分区的限制与局限](./26.06.分区的限制与局限/26.06.00.分区的限制与局限.md)

本章讨论用户定义的分区。

> **注意**
>
> 表分区不同于窗口函数使用的分区。关于窗口函数的信息，请参见[第14.20节，"窗口函数"](#1420-window-functions)。

在MySQL 8.0中，分区支持由`InnoDB`和`NDB`存储引擎提供。

MySQL 8.0当前不支持使用`InnoDB`或`NDB`以外的任何存储引擎对表进行分区，例如`MyISAM`。尝试使用不提供本地分区支持的存储引擎创建分区表会因`ER_CHECK_NOT_IMPLEMENTED`而失败。

Oracle提供的MySQL 8.0社区版二进制文件包括`InnoDB`和`NDB`存储引擎提供的分区支持。有关MySQL企业版二进制文件中提供的分区支持的信息，请参见[第32章，MySQL企业版](#chapter-32-mysql-enterprise-edition)。

如果您从源码编译MySQL 8.0，配置构建时包含`InnoDB`支持即可生成支持`InnoDB`表分区的二进制文件。更多信息，请参见[第2.8节，"从源码安装MySQL"](#28-installing-mysql-from-source)。

无需做任何其他操作即可启用`InnoDB`的分区支持（例如，`my.cnf`文件中不需要特殊条目）。

无法禁用`InnoDB`存储引擎的分区支持。

有关分区和分区概念的介绍，请参见[第26.1节，"MySQL中的分区概述"](#261-overview-of-partitioning-in-mysql)。

支持多种类型的分区，以及子分区；请参见[第26.2节，"分区类型"](#262-partitioning-types)和[第26.2.6节，"子分区"](#2626-subpartitioning)。

[第26.3节，"分区管理"](#263-partition-management)涵盖了添加、删除和更改现有分区表中分区的方法。

[第26.3.4节，"分区的维护"](#2634-maintenance-of-partitions)讨论了用于分区表的表维护命令。

`INFORMATION_SCHEMA`数据库中的`PARTITIONS`表提供有关分区和分区表的信息。更多信息请参见[第28.3.21节，"INFORMATION_SCHEMA PARTITIONS表"](#28321-the-information_schema-partitions-table)；一些查询此表的示例，请参见[第26.2.7节，"MySQL分区如何处理NULL"](#2627-how-mysql-partitioning-handles-null)。

有关MySQL 8.0中分区的已知问题，请参见[第26.6节，"分区的限制与局限"](#266-restrictions-and-limitations-on-partitioning)。

在使用分区表时，您可能还会发现以下资源有用。

### 其他资源
其他关于MySQL中用户定义分区的信息来源包括：

- **MySQL分区论坛**

  这是对MySQL分区技术感兴趣或进行实验的人的官方讨论论坛。它提供来自MySQL开发人员和其他人的公告和更新。分区开发和文档团队的成员会对其进行监控。

- **PlanetMySQL**

  一个MySQL新闻网站，特色是MySQL相关博客，对于使用MySQL的任何人来说都应该很感兴趣。我们鼓励您在此查找那些从事MySQL分区工作的人的博客链接，或者将您的博客添加到涵盖的博客中。