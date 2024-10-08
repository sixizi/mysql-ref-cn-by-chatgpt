# MySQL 术语表

这些术语常用于MySQL数据库服务器的信息中。

[TOC]

## A

**.ARM 文件**

ARCHIVE表的元数据。与 `.ARZ` 文件对比。具有此扩展名的文件总是包含在MySQL Enterprise Backup产品的`mysqlbackup`命令生成的备份中。

参见 `.ARZ` 文件, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `mysqlbackup` 命令。

**.ARZ 文件**

ARCHIVE表的数据。与 `.ARM` 文件对比。具有此扩展名的文件总是包含在MySQL Enterprise Backup产品的`mysqlbackup`命令生成的备份中。

参见 `.ARM` 文件, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `mysqlbackup` 命令。

**ACID**

代表原子性、一致性、隔离性和持久性的缩写。这些属性在数据库系统中都是理想的，并且与事务的概念密切相关。InnoDB的事务功能遵循ACID原则。

事务是可以提交或回滚的原子工作单元。当一个事务对数据库进行多项更改时，要么在事务提交时所有更改都成功，要么在事务回滚时所有更改都被撤销。

数据库在任何时候都保持一致状态——在每次提交或回滚后，以及事务进行过程中。如果跨多个表更新相关数据，查询要么看到所有旧值，要么看到所有新值，而不是旧值和新值的混合。

事务在进行时是相互隔离的；它们不能相互干扰，也不能看到彼此未提交的数据。这种隔离通过锁定机制来实现。经验丰富的用户可以调整隔离级别，在确保事务确实不会相互干扰时，以牺牲部分保护为代价来提高性能和并发性。

事务的结果是持久的：一旦提交操作成功，该事务所做的更改就不会受到电源故障、系统崩溃、竞争条件或其他许多非数据库应用程序易受的潜在危险的影响。持久性通常涉及写入磁盘存储，并有一定程度的冗余以防止在写入操作期间发生电源故障或软件崩溃。（在InnoDB中，`doublewrite buffer`有助于持久性。）

参见 `atomic`, `commit`, `concurrency`, `doublewrite buffer`, `isolation level`, `locking`, `rollback`, `transaction`。

**adaptive flushing**

一种用于InnoDB表的算法，可以平滑因检查点引入的I/O开销。MySQL不会一次性将缓冲池中所有修改过的页面刷新到数据文件，而是定期刷新少量修改过的页面。自适应刷新算法通过根据刷新速率和`redo log`生成速度估算最佳的定期刷新速率，来扩展此过程。

参见 `buffer pool`, `checkpoint`, `data files`, `flush`, `InnoDB`, `page`, `redo log`。

**adaptive hash index**

一种用于InnoDB表的优化，可以通过在内存中构建哈希索引来加速使用`=`和`IN`操作符的查找。MySQL监控对InnoDB表的索引搜索，如果查询可以从哈希索引中受益，它会自动为经常访问的索引页面构建一个。在某种意义上，自适应哈希索引使MySQL在运行时利用大量主内存，更接近于主内存数据库的架构。此功能由`innodb_adaptive_hash_index`配置选项控制。由于此功能对某些工作负载有益而对其他工作负载无益，并且用于哈希索引的内存在`buffer pool`中保留，通常应在启用和禁用此功能的情况下进行基准测试。

哈希索引总是基于表上现有的B树索引构建的。MySQL可以根据对索引的搜索模式，在B树定义的键的任意长度前缀上构建哈希索引。哈希索引可以是部分的；整个B树索引不需要缓存在`buffer pool`中。

参见 `B-tree`, `buffer pool`, `hash index`, `page`, `secondary index`。

**ADO.NET**

一种用于使用.NET技术（如ASP.NET）构建的应用程序的对象关系映射(ORM)框架。这类应用程序可以通过`Connector/NET`组件与MySQL进行接口连接。

参见 `.NET`, `ASP.NET`, `Connector/NET`, `Mono`, `Visual Studio`。

**AIO**

异步I/O的缩写。您可能会在InnoDB消息或关键字中看到这个缩写。

参见 `asynchronous I/O`。

**ANSI**

在ODBC中，一种支持字符集和其他国际化方面的替代方法。与`Unicode`对比。`Connector/ODBC 3.51`是一个ANSI驱动程序，而`Connector/ODBC 5.1`是一个Unicode驱动程序。

参见 `Connector/ODBC`, `ODBC`, `Unicode`。

**API**

API为客户端程序提供对MySQL协议和MySQL资源的低级访问。与`Connector`提供的高级访问方式对比。

参见 `C API`, `client`, `connector`, `native C API`, `Perl API`, `PHP API`, `Python API`, `Ruby API`。

**application programming interface (API)**

一组函数或过程。API提供一组稳定的函数名、过程名、参数和返回值类型。

**apply**

当MySQL Enterprise Backup产品生成的备份不包含备份过程中发生的最新更改时，将这些更改更新到备份文件中的过程称为`apply`步骤。该步骤由`mysqlbackup`命令的`apply-log`选项指定。

在应用这些更改之前，我们将文件称为`raw backup`。在应用更改之后，我们将文件称为`prepared backup`。这些更改记录在`ibbackup_logfile`文件中；`apply`步骤完成后，此文件不再需要。

参见 `hot backup`, `ibbackup_logfile`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `prepared backup`, `raw backup`。

**AS**

Kerberos身份验证服务器。`AS`也可以指身份验证服务器提供的身份验证服务。

参见 `authentication server`。

**ASP.net**

一种使用.NET技术和语言开发基于Web的应用程序的框架。这类应用程序可以通过`Connector/NET`组件与MySQL进行接口连接。

另一种使用MySQL编写服务器端网页的技术是`PHP`。

参见 `.NET`, `ADO.NET`, `Connector/NET`, `Mono`, `PHP`, `Visual Studio`。

**assembly**

.NET系统中的一个已编译代码库，通过`Connector/NET`访问。存储在`GAC`中，以允许版本控制而不会发生命名冲突。

参见 `.NET`, `GAC`。

**asynchronous I/O**

一种I/O操作类型，允许在I/O完成之前进行其他处理。也称为非阻塞I/O，缩写为`AIO`。InnoDB在某些操作中使用这种类型的I/O，这些操作可以并行运行，而不会影响数据库的可靠性，例如将未被实际请求但可能很快需要的页面读取到缓冲池中。

历史上，InnoDB仅在Windows系统上使用异步I/O。从`InnoDB Plugin 1.1`和`MySQL 5.5`开始，InnoDB在Linux系统上使用异步I/O。这一变化引入了对`libaio`的依赖。Linux系统上的异步I/O通过`innodb_use_native_aio`选项配置，默认情况下启用。在其他类似Unix的系统上，InnoDB仅使用同步I/O。

参见 `buffer pool`, `nonblocking I/O`。

**atomic**

在SQL上下文中，事务是完全成功（当提交时）或完全无效（当回滚时）的工作单元。事务的不可分割（“原子”）属性是ACID缩写中的“A”。

参见 `ACID`, `commit`, `rollback`, `transaction`。

**atomic DDL**

原子DDL语句是将与DDL操作相关的数据字典更新、存储引擎操作和二进制日志写入合并到单个原子事务中的语句。即使服务器在操作期间停止，事务也会完全提交或回滚。MySQL 8.0中添加了对原子DDL的支持。有关更多信息，请参见 [15.1.1节 “Atomic Data Definition Statement Support”](https://dev.mysql.com/doc/refman/8.0/en/atomic-ddl.html)。

参见 `binary log`, `data dictionary`, `DDL`, `storage engine`。

**atomic instruction**

由CPU提供的特殊指令，以确保关键的低级操作不会被中断。

**authentication server**

在Kerberos中，一种服务，它提供获取`ticket-granting ticket (TGT)`所需的初始票证，而获取其他票证（来自`ticket-granting server (TGS)`）又需要`TGT`。`authentication server (AS)`与`TGS`一起组成`key distribution center (KDC)`。

参见 `key distribution center`, `ticket-granting server`。

**auto-increment**

表列的一个属性（通过`AUTO_INCREMENT`关键字指定），该属性自动在列中添加递增的值序列。

它为开发人员节省了在插入新行时生成新唯一值的工作。它为查询优化器提供了有用的信息，因为该列已知不为空并具有唯一值。由于这些值是自动生成的，因此在各种上下文中可以用作查找键，并且因为它们是自动生成的，所以没有理由更改它们；因此，主键列通常指定为自增列。

在基于语句的复制中，自增列可能会有问题，因为在副本上重放这些语句时，可能不会产生与源相同的列值，这是由于时间问题造成的。如果您有一个自增主键，则只能在`innodb_autoinc_lock_mode=1`设置下使用基于语句的复制。如果您使用`innodb_autoinc_lock_mode=2`，它允许插入操作具有更高的并发性，请使用基于行的复制而不是基于语句的复制。除非出于兼容性目的，否则不应使用`innodb_autoinc_lock_mode=0`设置。

在MySQL 8.0.3之前，默认的锁模式是连续模式（`innodb_autoinc_lock_mode=1`）。从MySQL 8.0.3开始，默认是交错锁模式（`innodb_autoinc_lock_mode=2`），这反映了默认复制类型从基于语句的复制更改为基于行的复制。

参见 `auto-increment locking`, `innodb_autoinc_lock_mode`, `primary key`, `row-based replication`, `statement-based replication`。

**auto-increment locking**

使用自增主键的便利性在并发性方面涉及一些权衡。在最简单的情况下，如果一个事务正在向表中插入值，则任何其他事务必须等待，才能向该表中插入自己的值，以便由第一个事务插入的行接收到连续的主键值。InnoDB包含一些优化功能以及`innodb_autoinc_lock_mode`选项，以便您可以在自增值的可预测序列和插入操作的最大并发性之间配置和达到最佳平衡。

参见 `auto-increment`, `concurrency`, `innodb_autoinc_lock_mode`。

**autocommit**

一个设置，使每个SQL语句后都进行提交操作。对于处理跨越多个语句的InnoDB表的事务，不推荐使用此模式。对于InnoDB表上的只读事务，它可以提高性能，因为它最小化了锁定和生成撤销数据的开销，特别是在MySQL 5.6.4及以上版本中。它也适用于MyISAM表的操作，因为在MyISAM表中事务并不适用。

参见 `commit`, `locking`, `read-only transaction`, `SQL`, `transaction`, `undo`。

**availability**

应对并在必要时从主机上的故障中恢复的能力，包括MySQL、操作系统或硬件的故障，以及可能导致停机的维护活动。通常与可扩展性配对，作为大规模部署中的关键方面。

参见 `scalability`。

**B-tree**

一种广泛用于数据库索引的树形数据结构。B-tree结构始终保持排序状态，从而实现快速查找精确匹配（等于运算符）和范围（例如，大于、小于和`BETWEEN`运算符）。此类索引可用于大多数存储引擎，例如`InnoDB`和`MyISAM`。

由于B-tree节点可以有多个子节点，因此B-tree不同于二叉树，后者每个节点仅限于两个子节点。

与仅在`MEMORY`存储引擎中可用的`hash index`形成对比。如果某些查询使用范围运算符，您应为`MEMORY`表选择B-tree索引。

术语B-tree旨在指代一般的索引设计类别。MySQL存储引擎使用的B-tree结构可能由于包含了一些经典B-tree设计中不存在的复杂性而被视为变体。有关相关信息，请参阅MySQL Internals手册中的[InnoDB Page Structure Fil Header](https://dev.mysql.com/doc/internals/en/innodb-fil-header.html)部分。

参见 `hash index`。

**backticks**

在MySQL SQL语句中，如果标识符包含特殊字符或保留字，则必须使用反引号字符（\`）将其括起来。例如，要引用名为FOO#BAR的表或名为SELECT的列，您需要将标识符指定为\`FOO#BAR和SELECT\`。由于反引号提供了额外的安全性，在程序生成的SQL语句中广泛使用，因为这些语句中的标识符名称可能无法提前确定。

许多其他数据库系统使用双引号（"）来包围此类特殊名称。为了提高可移植性，您可以在MySQL中启用`ANSI_QUOTES`模式，并使用双引号代替反引号来限定标识符名称。

参见 `SQL`。

**backup**

将MySQL实例中的部分或全部表数据和元数据复制以进行安全保存的过程。也可以指代复制的文件集。这是数据库管理员的一个重要任务。此过程的逆操作是还原操作。

在MySQL中，物理备份由`MySQL Enterprise Backup`产品执行，逻辑备份由`mysqldump`命令执行。这些技术在备份数据的大小、表示形式和速度（尤其是还原操作的速度）方面具有不同的特性。

备份根据对正常数据库操作的干扰程度进一步分类为热备份、温备份或冷备份。（热备份干扰最小，冷备份干扰最大。）

参见 `cold backup`, `hot backup`, `logical backup`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `mysqldump`, `physical backup`, `warm backup`。

**base column**

一个非生成表列，其上基于存储生成列或虚拟生成列。换句话说，基列是生成列定义的一部分的非生成表列。

参见 `generated column`, `stored generated column`, `virtual generated column`。

**beta**

软件产品生命周期的早期阶段，通常仅用于评估，通常没有明确的发行版本号或版本号小于1。InnoDB不使用`beta`称号，更倾向于经历几个小版本的早期采用者阶段，最终发布`GA`版本。

参见 `early adopter`, `GA`。

**binary log**

一个包含所有试图更改表数据的语句或行更改的记录文件。在复制场景中，可以重放二进制日志的内容以使副本更新，或者在从备份还原表数据后使数据库更新。可以开启和关闭二进制日志功能，但Oracle建议，如果您使用复制或执行备份，则应始终启用它。

您可以使用`mysqlbinlog`命令检查二进制日志的内容，或在复制或恢复期间重放日志。有关二进制日志的全部信息，请参见[7.4.4节 “The Binary Log”](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html)。有关二进制日志的MySQL配置选项，请参见[19.1.6.4节 “Binary Logging Options and Variables”](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html)。

对于`MySQL Enterprise Backup`产品，在复制上下文中进行备份时，二进制日志的文件名和文件中的当前位置是重要信息。您可以指定`--slave-info`选项来记录源的这些信息。

在MySQL 5.0之前，类似功能称为更新日志。在MySQL 5.0及更高版本中，二进制日志取代了更新日志。

参见 `binlog`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `replication`。

**binlog**

二进制日志文件的非正式名称。例如，您可能会在电子邮件或论坛讨论中看到此缩写。

参见 `binary log`。

**blind query expansion**

一种通过`WITH QUERY EXPANSION`子句启用的全文本搜索特殊模式。它执行两次搜索，第二次搜索的搜索短语是原始搜索短语与第一次搜索中最相关的几个文档的组合。此技术主要适用于短搜索短语，可能只有一个单词。它可以发现没有在文档中出现的精确搜索词的相关匹配项。

参见 `full-text search`。

**BLOB**

一种SQL数据类型（`TINYBLOB`、`BLOB`、`MEDIUMBLOB`和`LONGBLOB`），用于包含任意大小的二进制数据对象。用于存储文档、图像、声音文件和其他不能轻易分解为MySQL表中的行和列的各种信息。在MySQL应用程序中处理BLOB的技术因每个`Connector`和`API`而异。`MySQL Connector/ODBC`将BLOB值定义为`LONGVARBINARY`。对于大型自由格式的字符数据集合，业界术语是`CLOB`，由MySQL的`TEXT`数据类型表示。

参见 `API`, `CLOB`, `connector`, `Connector/ODBC`。

**bottleneck**

系统中尺寸或容量受限的部分，限制整体吞吐量的部分。例如，内存区域可能小于所需大小；对单一必需资源的访问可能会阻止多个CPU内核同时运行；或等待磁盘I/O完成可能会阻止CPU充分运转。消除瓶颈往往可以提高并发性。例如，能够拥有多个`InnoDB`缓冲池实例可以减少多个会话同时读取和写入缓冲池时的竞争。

参见 `buffer pool`, `concurrency`。

**bounce**

关闭操作后立即重新启动。理想情况下，经过相对较短的预热期后，性能和吞吐量迅速恢复到较高水平。

参见 `shutdown`。

**buddy allocator**

一种用于管理`InnoDB`缓冲池中不同大小页面的机制。

参见 `buffer pool`, `page`, `page size`。

**buffer**

用于临时存储的内存或磁盘区域。数据缓存在内存中，以便可以通过少量大型I/O操作而不是许多小型I/O操作高效地写入磁盘。数据缓存在磁盘上，以提高可靠性，即使在最糟糕的时间点发生崩溃或其他故障时，数据也可以恢复。`InnoDB`使用的主要缓冲区类型是缓冲池、双写缓冲区和更改缓冲区。

参见 `buffer pool`, `change buffer`, `crash`, `doublewrite buffer`。

**buffer pool**

一个保存`InnoDB`表和索引缓存数据的内存区域。为了提高大容量读取操作的效率，缓冲池被分为可以容纳多行的页面。为了提高缓存管理的效率，缓冲池实现为一个页面链表；使用`LRU`算法的变体将很少使用的数据从缓存中逐出。在具有大内存的系统上，您可以通过将缓冲池分为多个缓冲池实例来提高并发性。

几个`InnoDB`状态变量、`INFORMATION_SCHEMA`表和`performance_schema`表有助于监控缓冲池的内部工作。从MySQL 5.6开始，您可以通过在服务器关闭时保存缓冲池状态，并在服务器启动时将缓冲池恢复到相同状态，来避免在重启服务器后经历较长的预热期，特别是对于具有大缓冲池的实例。参见[17.8.3.6节 “Saving and Restoring the Buffer Pool State”](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html#innodb-buffer-pool-saving)。

参见 `buffer pool instance`, `LRU`, `page`, `warm up`。

**buffer pool instance**

缓冲池可以分为的多个区域中的任意一个，由`innodb_buffer_pool_instances`配置选项控制。`innodb_buffer_pool_size`指定的总内存大小在所有缓冲池实例之间划分。通常，具有多个缓冲池实例适用于为InnoDB缓冲池分配多个GB的系统，每个实例为1GB或更大。在系统从许多并发会话中加载或查找大量数据到缓冲池时，具有多个缓冲池实例可以减少对管理缓冲池的数据结构的排他访问的竞争。

参见 buffer pool。

**built-in**

MySQL内置的InnoDB存储引擎是该存储引擎的原始发行形式。与InnoDB插件形成对比。从MySQL 5.5开始，InnoDB插件被重新合并到MySQL代码库中，成为内置的InnoDB存储引擎（称为InnoDB 1.1）。

这个区别主要在MySQL 5.1中非常重要，因为某些特性或错误修复可能适用于InnoDB插件，但不适用于内置的InnoDB，反之亦然。

参见 `InnoDB`。

**business rules**

构成商业软件基础的关系和动作顺序，用于运营商业公司。这些规则有时由法律规定，其他时候由公司政策决定。通过仔细规划，可以确保数据库编码和执行的关系，以及通过应用逻辑执行的动作，准确反映公司的实际政策并能处理现实生活中的情况。

例如，员工离职可能会触发人力资源部门的一系列动作。人力资源数据库可能还需要灵活地表示已被录用但尚未开始工作的人员数据。关闭在线服务的账户可能会导致数据从数据库中删除，或者数据可能会被移动或标记，以便在账户重新开启时恢复。一家公司可能会建立关于工资的最大值、最小值和调整的政策，此外还包括基本的合理性检查，例如工资不能为负数。一个零售数据库可能不允许带有相同序列号的商品被退回超过一次，或者不允许特定信用卡购买超过某个金额，而一个用于检测欺诈的数据库可能会允许这些操作。

参见 `relational`。

## C

**.cfg file**

一种与InnoDB可传输表空间功能配合使用的元数据文件。它由`FLUSH TABLES ... FOR EXPORT`命令生成，将一个或多个表置于一致状态，可以复制到另一台服务器上。在`ALTER TABLE ... IMPORT TABLESPACE`步骤中，`.cfg`文件与相应的`.ibd`文件一起复制，并用于调整`.ibd`文件的内部值，如`space ID`。

参见 `.ibd file`, `space ID`, `transportable tablespace`。

**C**

一种编程语言，结合了可移植性、性能和对低级硬件功能的访问，使其成为编写操作系统、驱动程序和其他系统软件的热门选择。许多复杂的应用程序、语言和可重用模块都包含用C编写的部分，并与其他语言编写的高级组件结合在一起。C的核心语法对C++、Java和C#开发人员来说都很熟悉。

参见 `C API`, `C++`, `C#`, `Java`。

**C API**

C API代码随MySQL一起分发。它包含在`libmysqlclient`库中，使C程序能够访问数据库。

参见 `API`, `C`, `libmysqlclient`。

**C#**

一种编程语言，结合了强类型和面向对象的特性，运行在Microsoft .NET框架或其开源对应的Mono中。通常用于使用ASP.net框架创建应用程序。其语法对C、C++和Java开发人员来说很熟悉。

参见 `.NET`, `ASP.net`, `C`, `Connector/NET`, `C++`, `Java`, `Mono`。

**C++**

一种编程语言，其核心语法对C开发人员来说很熟悉。它结合了对低级操作的访问以提高性能，同时提供了高级数据类型、面向对象的特性和垃圾回收功能。要编写MySQL的C++应用程序，您可以使用`Connector/C++`组件。

参见 `C`, `Connector/C++`。

**cache**

用于存储数据副本以便频繁或高速检索的任何内存区域的通用术语。在InnoDB中，主要的缓存结构是`buffer pool`。

参见 `buffer`, `buffer pool`。

**cardinality**

表列中不同值的数量。当查询引用具有相关索引的列时，每列的基数会影响最有效的访问方法。例如，对于具有唯一约束的列，不同值的数量等于表中的行数。如果一个表有一百万行，但某一列只有10个不同的值，则每个值（平均）出现100,000次。类似`SELECT c1 FROM t1 WHERE c1 = 50;`的查询可能返回1行或大量行，数据库服务器可能根据c1的基数以不同方式处理查询。

如果列中的值分布非常不均匀，则基数可能不是确定最佳查询计划的好方法。例如，`SELECT c1 FROM t1 WHERE c1 = x;`可能在`x=50`时返回1行，而在`x=30`时返回一百万行。在这种情况下，您可能需要使用索引提示来传递有关某个特定查询的更高效查找方法的建议。

基数也可以适用于多个列中存在的不同值的数量，如在组合索引中。

参见 `column`, `composite index`, `index`, `index hint`, `persistent statistics`, `random dive`, `selectivity`, `unique constraint`。

**change buffer**

一种特殊的数据结构，用于记录对二级索引页面的更改。这些值可能由SQL INSERT、UPDATE或DELETE语句（DML）生成。涉及更改缓冲区的功能集合统称为`change buffering`，包括`insert buffering`、`delete buffering`和`purge buffering`。

只有当二级索引的相关页面不在`buffer pool`中时，才会在`change buffer`中记录更改。当相关索引页面在相关更改仍在`change buffer`中时被加载到`buffer pool`中，这些页面的更改将使用`change buffer`中的数据在`buffer pool`中应用（合并）。定期运行的清除操作将在系统主要空闲时或慢速关闭期间，将新索引页面写入磁盘。清除操作可以比每个值立即写入磁盘时更有效地写入一系列索引值的磁盘块。

从物理上看，`change buffer`是系统表空间的一部分，因此索引更改在数据库重启后仍保持缓冲状态。只有当页面因其他读取操作被加载到`buffer pool`时，才会应用（合并）更改。

`change buffer`中存储的数据种类和数量由`innodb_change_buffering`和`innodb_change_buffer_max_size`配置选项控制。要查看`change buffer`中当前数据的信息，请执行`SHOW ENGINE INNODB STATUS`命令。

以前称为`insert buffer`。

参见 `buffer pool`, `change buffering`, `delete buffering`, `DML`, `insert buffer`, `insert buffering`, `merge`, `page`, `purge`, `purge buffering`, `secondary index`, `system tablespace`。

**change buffering**

涉及`change buffer`功能的总称，包括`insert buffering`、`delete buffering`和`purge buffering`。由SQL语句生成的索引更改通常涉及随机I/O操作，通过后台线程定期执行，从而减少I/O开销。这一操作序列可以比每个值立即写入磁盘时更有效地写入一系列索引值的磁盘块。受`innodb_change_buffering`和`innodb_change_buffer_max_size`配置选项控制。

参见 `change buffer`, `delete buffering`, `insert buffering`, `purge buffering`。

**checkpoint**

当数据页面在`buffer pool`中被修改时，这些更改会在稍后写入数据文件，这个过程称为`flush`。`checkpoint`是已成功写入数据文件的最新更改的记录（由LSN值表示）。

参见 `buffer pool`, `data files`, `flush`, `fuzzy checkpointing`, `LSN`。

**checksum**

在InnoDB中，当从磁盘读取表空间中的页面到InnoDB的`buffer pool`时，用于检测损坏的验证机制。此功能由MySQL 5.5中的`innodb_checksums`配置选项控制。在MySQL 5.6.3中，`innodb_checksums`已被弃用，取而代之的是`innodb_checksum_algorithm`。

`innochecksum`命令通过在MySQL服务器关闭时测试指定表空间文件的校验和值，帮助诊断损坏问题。

MySQL还使用校验和来进行复制。有关详细信息，请参阅配置选项`binlog_checksum`、`source_verify_checksum`或`master_verify_checksum`，以及`replica_sql_verify_checksum`或`slave_sql_verify_checksum`。

参见 `buffer pool`, `page`, `tablespace`。

**child table**

在外键关系中，子表是指其行引用（或指向）另一个表中的行，并在特定列上具有相同的值。此表包含`FOREIGN KEY ... REFERENCES`子句，以及可选的`ON UPDATE`和`ON DELETE`子句。必须先存在父表中的对应行，然后才能在子表中创建行。子表中的值可以阻止对父表进行删除或更新操作，或者根据创建外键时使用的`ON CASCADE`选项，在子表中自动删除或更新。

参见 `foreign key`, `parent table`。

**clean page**

InnoDB `buffer pool`中的一个页面，其中所有在内存中进行的更改也已写入（`flush`）到数据文件。与`dirty page`相对。

参见 `buffer pool`, `data files`, `dirty page`, `flush`, `page`。

**clean shutdown**

在完成前无错误并将所有更改应用到InnoDB表的关闭操作，与崩溃或快速关闭相对。`slow shutdown`的同义词。

参见 `crash`, `fast shutdown`, `shutdown`, `slow shutdown`。

**client**

在数据库服务器外部运行的程序，通过`Connector`或客户端库提供的API与数据库通信。它可以在与数据库服务器相同的物理机器上运行，也可以在通过网络连接的远程机器上运行。它可以是专用的数据库应用程序，也可以是像`mysql`命令行处理器这样的通用程序。

参见 `API`, `client libraries`, `connector`, `mysql`, `server`。

**client libraries**

包含用于处理数据库的函数集合的文件。通过将程序与这些库一起编译，或将它们安装在与应用程序相同的系统上，可以在未安装MySQL服务器的机器上运行数据库应用程序（称为客户端）；应用程序通过网络访问数据库。对于MySQL，您可以使用MySQL服务器本身的`libmysqlclient`库。

参见 `client`, `libmysqlclient`。

**client-side prepared statement**
一种准备语句，其缓存和重用在本地管理，模拟服务器端准备语句的功能。历史上，一些`Connector/J`、`Connector/ODBC`和`Connector/PHP`开发人员使用它来解决服务器端存储过程的问题。对于现代MySQL服务器版本，建议使用服务器端准备语句以提高性能、可扩展性和内存效率。

参见 `Connector/J`, `Connector/ODBC`, `Connector/PHP`, `prepared statement`。

**CLOB**
一种SQL数据类型（`TINYTEXT`、`TEXT`、`MEDIUMTEXT`或`LONGTEXT`），用于包含任意大小的字符数据对象。用于存储基于文本的文档，并具有相关的字符集和排序规则。在MySQL应用程序中处理CLOB的技术因每个`Connector`和`API`而异。`MySQL Connector/ODBC`将`TEXT`值定义为`LONGVARCHAR`。对于存储二进制数据，等效的数据类型是`BLOB`。

参见 `API`, `BLOB`, `connector`, `Connector/ODBC`。

**clustered index**

InnoDB中的主键索引术语。InnoDB表存储是基于主键列的值进行组织的，以加速涉及主键列的查询和排序。为了获得最佳性能，应根据最关键的性能查询仔细选择主键列。由于修改聚簇索引的列是一个开销较大的操作，因此应选择很少或从不更新的主键列。

在Oracle数据库产品中，这种类型的表称为索引组织表。

参见 `index`, `primary key`, `secondary index`。

**cold backup**

在数据库关闭时进行的备份。对于繁忙的应用程序和网站，这可能不太实际，您可能更倾向于使用温备份或热备份。

参见 `backup`, `hot backup`, `warm backup`。

**column**

行中的数据项，其存储和语义由数据类型定义。每个表和索引在很大程度上由其包含的列集定义。

每个列都有一个基数值。一个列可以是其表的主键，或主键的一部分。一个列可以受到唯一约束、`NOT NULL`约束或两者的约束。即使在不同的表中，不同列中的值也可以通过外键关系链接。

在讨论MySQL内部操作时，有时`field`被用作同义词。

参见 `cardinality`, `foreign key`, `index`, `NOT NULL constraint`, `primary key`, `row`, `table`, `unique constraint`。

**column index**

在单个列上的索引。

参见 `composite index`, `index`。

**column prefix**

当使用长度规范创建索引时，例如`CREATE INDEX idx ON t1 (c1(N))`，只有列值的前N个字符存储在索引中。保持索引前缀较小可以使索引紧凑，并且内存和磁盘I/O的节省有助于提高性能。（尽管将索引前缀设置得太小可能会通过使具有不同值的行在查询优化器中看起来像是重复项来阻碍查询优化。）

对于包含二进制值或长文本字符串的列，在排序不是主要考虑因素并且将整个值存储在索引中会浪费空间的情况下，索引会自动使用值的前N个（通常为768）字符进行查找和排序。

参见 `index`。

**command interceptor**

`statement interceptor`的同义词。`interceptor`设计模式的一个方面，可用于`Connector/NET`和`Connector/J`。`Connector/NET`称之为`command`，`Connector/J`称之为`statement`。与`exception interceptor`形成对比。

参见 `Connector/J`, `Connector/NET`, `exception interceptor`, `interceptor`, `statement interceptor`。

**commit**

一个SQL语句，用于结束一个事务，使事务所做的任何更改永久生效。它与`rollback`相对，后者撤销事务中所做的任何更改。

InnoDB使用一种乐观提交机制，因此更改可以在提交实际发生之前写入数据文件。此技术使提交本身更快，但代价是在发生回滚的情况下需要更多的工作。

默认情况下，MySQL使用`autocommit`设置，在每个SQL语句之后自动发出提交。

参见 `autocommit`, `optimistic`, `rollback`, `SQL`, `transaction`。

**compact row format**

一种用于InnoDB表的行格式。从MySQL 5.0.3到MySQL 5.7.8，`COMPACT`行格式是默认行格式。在MySQL 8.0中，默认行格式由`innodb_default_row_format`配置选项定义，默认设置为`DYNAMIC`。`COMPACT`行格式为`NULL`和可变长度列提供了比`REDUNDANT`行格式更紧凑的表示。

有关InnoDB `COMPACT`行格式的更多信息，请参见[17.10节 “InnoDB Row Formats”](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html)。

参见 `dynamic row format`, `file format`, `redundant row format`, `row format`。

**composite index**

包含多个列的索引。

参见 `index`。

**compressed backup**

`MySQL Enterprise Backup`产品的压缩功能使每个表空间的压缩副本，并将扩展名从`.ibd`更改为`.ibz`。压缩备份数据使您可以保留更多备份，并减少将备份传输到另一台服务器所需的时间。在还原操作期间，数据被解压缩。当压缩备份操作处理已经压缩的表时，它会跳过该表的压缩步骤，因为再次压缩不会节省多少空间。

由`MySQL Enterprise Backup`产品生成的一组文件，其中每个表空间都被压缩。压缩后的文件重命名为`.ibz`文件扩展名。

在备份过程开始时应用压缩有助于避免压缩过程中的存储开销，并在将备份文件传输到另一台服务器时避免网络开销。应用二进制日志的过程需要更长时间，并且需要解压缩备份文件。

参见 `apply`, `binary log`, `compression`, `hot backup`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `tablespace`。

**compressed row format**

一种启用InnoDB表数据和索引压缩的行格式。大字段存储在与保存其余行数据的页面分离的位置，就像在`dynamic row format`中一样。索引页面和大字段都被压缩，从而节省了内存和磁盘空间。根据数据的结构，内存和磁盘使用量的减少可能会抵消使用数据时解压缩的性能开销，也可能不会。有关使用详情，请参见[17.9节 “InnoDB Table and Page Compression”](https://dev.mysql.com/doc/refman/8.0/en/innodb-table-compression.html)。

有关InnoDB `COMPRESSED`行格式的更多信息，请参见`DYNAMIC Row Format`。

参见 `compression`, `dynamic row format`, `row format`。

**compressed table**

其数据以压缩形式存储的表。对于InnoDB，这是一个使用`ROW_FORMAT=COMPRESSED`创建的表。有关更多信息，请参见[17.9节 “InnoDB Table and Page Compression”](https://dev.mysql.com/doc/refman/8.0/en/innodb-table-compression.html)。

参见 `compressed row format`, `compression`。

**compression**

一种具有广泛好处的功能，包括使用更少的磁盘空间、执行更少的I/O以及使用更少的内存进行缓存。

InnoDB支持表级和页级压缩。InnoDB页压缩也称为透明页压缩。有关InnoDB压缩的更多信息，请参见[17.9节 “InnoDB Table and Page Compression”](https://dev.mysql.com/doc/refman/8.0/en/innodb-table-compression.html)。

另一种压缩类型是`MySQL Enterprise Backup`产品的压缩备份功能。

参见 `buffer pool`, `compressed backup`, `compressed row format`, `DML`, `transparent page compression`。

**compression failure**

实际上不是错误，而是在将压缩与DML操作结合使用时可能发生的开销较大的操作。它发生在以下情况下：对压缩页面的更新溢出页面上保留的用于记录修改的区域；页面再次压缩，所有更改都应用于表数据；重新压缩的数据不适合原始页面，需要MySQL将数据拆分为两个新页面并分别压缩它们。要检查此情况的发生频率，请查询`INFORMATION_SCHEMA.INNODB_CMP`表，并检查`COMPRESS_OPS`列的值超过`COMPRESS_OPS_OK`列的值的程度。理想情况下，压缩失败不应经常发生；当发生时，您可以调整`innodb_compression_level`、`innodb_compression_failure_threshold_pct`和`innodb_compression_pad_pct_max`配置选项。

参见 `compression`, `DML`, `page`。

**concatenated index**

参见 `composite index`。

**concurrency**

多个操作（在数据库术语中为事务）同时运行而不相互干扰的能力。并发性还与性能有关，因为理想情况下，多个同时事务的保护机制具有最小的性能开销，使用高效的锁定机制。

参见 `ACID`, `locking`, `transaction`。

**configuration file**

保存MySQL启动时使用的选项值的文件。传统上，在Linux和Unix上此文件名为`my.cnf`，在Windows上名为`my.ini`。您可以在文件的`[mysqld]`部分下设置与InnoDB相关的多个选项。

有关MySQL搜索配置文件位置的信息，请参见[6.2.2.2节 “Using Option Files”](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)。

使用`MySQL Enterprise Backup`产品时，通常使用两个配置文件：一个指定数据来源及其结构（可能是服务器的原始配置文件），另一个仅包含少量选项，指定备份数据的去向及其结构。与`MySQL Enterprise Backup`产品一起使用的配置文件必须包含通常在常规配置文件中省略的某些选项，因此您可能需要为`MySQL Enterprise Backup`添加选项到现有配置文件中。

参见 `my.cnf`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `option`, `option file`。

**connection**

应用程序与MySQL服务器之间的通信通道。数据库应用程序的性能和可扩展性受以下因素的影响：数据库连接建立的速度、可以同时建立的连接数量以及连接的持续时间。诸如主机、端口等参数在`Connector/NET`中表示为连接字符串，在`Connector/ODBC`中表示为DSN。高流量系统利用一种称为连接池的优化。

参见 `connection pool`, `connection string`, `Connector/NET`, `Connector/ODBC`, `DSN`, `host`, `port`。

**connection pool**

一个缓存区域，允许在同一应用程序或不同应用程序中重用数据库连接，而不是为每个数据库操作设置和关闭一个新连接。这种技术在J2EE应用服务器中很常见。使用`Connector/J`的Java应用程序可以使用`Tomcat`和其他应用服务器的连接池功能。重用对应用程序是透明的；应用程序仍然像往常一样打开和关闭连接。

参见 `connection`, `Connector/J`, `J2EE`, `Tomcat`。

**connection string**

数据库连接参数的表示形式，编码为字符串文字，以便可以在程序代码中使用。字符串的各个部分表示连接参数，例如主机和端口。连接字符串包含几个键值对，以分号分隔。每个键值对通过等号连接。通常用于`Connector/NET`应用程序；有关详细信息，请参见[创建Connector/NET连接字符串](https://dev.mysql.com/doc/connector-net/en/connector-net-connections.html)。

参见 `connection`, `Connector/NET`, `host`, `port`。

**connector**

MySQL `Connectors`为客户端程序提供与MySQL服务器的连接。多种编程语言和框架各自有其相关的`Connector`。与API提供的低级访问形成对比。

参见 `API`, `client`, `Connector/C++`, `Connector/J`, `Connector/NET`, `Connector/ODBC`。

**Connector/C++**

`Connector/C++ 8.0`可用于访问实现文档存储的MySQL服务器，或通过传统方式使用SQL查询。它支持使用`X DevAPI`开发C++应用程序，或使用`X DevAPI for C`开发纯C应用程序。它还支持使用`Connector/C++ 1.1`中的基于JDBC的旧API开发C++应用程序。有关详细信息，请参见[MySQL Connector/C++ 9.0开发者指南](https://dev.mysql.com/doc/connector-cpp/9.0/en/)。

参见 `client`, `connector`, `JDBC`。

**Connector/J**

一个JDBC驱动程序，为使用Java编程语言开发的客户端应用程序提供连接。MySQL `Connector/J`是一个JDBC Type 4驱动程序：一个纯Java实现的MySQL协议，不依赖于MySQL客户端库。有关完整信息，请参见[MySQL Connector/J开发者指南](https://dev.mysql.com/doc/connector-j/8.0/en/)。

参见 `client`, `client libraries`, `connector`, `Java`, `JDBC`。

**Connector/NET**

一个用于编写应用程序的MySQL连接器，支持使用C#、.NET、Mono、Visual Studio、ASP.net和ADO.net等语言、技术和框架的开发人员。

参见 `ADO.NET`, `ASP.net`, `connector`, `C#`, `Mono`, `Visual Studio`。

**Connector/ODBC**

MySQL `ODBC`驱动程序系列，通过行业标准的`Open Database Connectivity (ODBC)` API提供对MySQL数据库的访问。以前称为`MyODBC`驱动程序。有关完整信息，请参见[MySQL Connector/ODBC开发者指南](https://dev.mysql.com/doc/connector-odbc/en/)。

参见 `connector`, `ODBC`。

**Connector/PHP**

针对Windows操作系统优化的`mysql`和`mysqli` APIs版本。

参见 `connector`, `PHP`, `PHP API`。

**consistent read**

一种读取操作，使用快照信息基于某个时间点呈现查询结果，而不考虑同时运行的其他事务所执行的更改。如果查询的数据已被另一个事务更改，则基于撤销日志的内容重建原始数据。此技术避免了一些锁定问题，这些问题可能会通过迫使事务等待其他事务完成来降低并发性。

使用`REPEATABLE READ`隔离级别时，快照基于第一次读取操作的时间。使用`READ COMMITTED`隔离级别时，快照在每次一致读取操作时重置。

一致读取是InnoDB在`READ COMMITTED`和`REPEATABLE READ`隔离级别中处理`SELECT`语句的默认模式。由于一致读取不会在其访问的表上设置任何锁，因此在对表执行一致读取时，其他会话可以自由地修改这些表。

有关适用的隔离级别的技术细节，请参见[17.7.2.3节 “Consistent Nonlocking Reads”](https://dev.mysql.com/doc/refman/8.0/en/innodb-consistent-read.html)。

参见 `concurrency`, `isolation level`, `locking`, `READ COMMITTED`, `REPEATABLE READ`, `snapshot`, `transaction`, `undo log`。

**constraint**

一种自动测试，可以阻止数据库更改以防止数据不一致。（在计算机科学术语中，一种与不变条件相关的断言。）约束是ACID理念的关键组成部分，以维护数据一致性。MySQL支持的约束包括外键约束和唯一约束。

参见 `ACID`, `foreign key`, `unique constraint`。

**counter**

一种由特定InnoDB操作递增的值。用于衡量服务器的繁忙程度，排除性能问题的根源，并测试更改（例如对配置设置或查询使用的索引）的低级效果是否如预期一样。有不同种类的计数器可通过`Performance Schema`表和`INFORMATION_SCHEMA`表获取，尤其是`INFORMATION_SCHEMA.INNODB_METRICS`。

参见 `INFORMATION_SCHEMA`, `metrics counter`, `Performance Schema`。

**covering index**

包含查询检索到的所有列的索引。查询不使用索引值作为指针来查找完整的表行，而是直接从索引结构返回值，从而节省了磁盘I/O。InnoDB可以将这种优化技术应用于比MyISAM更多的索引，因为InnoDB的二级索引还包含主键列。在事务修改过的表上运行查询时，InnoDB在该事务结束之前无法应用此技术。

在适当的查询条件下，任何列索引或复合索引都可以充当覆盖索引。设计索引和查询时，应尽可能利用这种优化技术。

参见 `column index`, `composite index`, `index`, `primary key`, `secondary index`。

**CPU-bound**

一种主要瓶颈是内存中的CPU操作的工作负载。通常涉及读取密集型操作，其结果可以全部缓存在`buffer pool`中。

参见 `bottleneck`, `buffer pool`, `workload`。

**crash**

MySQL使用术语“crash”来指代任何无法正常清理的意外关闭操作。例如，由于数据库服务器机器或存储设备的硬件故障、电源故障、潜在的数据不匹配导致MySQL服务器停止、由DBA发起的快速关闭或其他原因，都可能导致崩溃。InnoDB表的强大自动崩溃恢复功能确保在服务器重新启动时数据一致，无需DBA进行额外工作。

参见 `crash recovery`, `fast shutdown`, `InnoDB`, `shutdown`。

**crash recovery**

MySQL在崩溃后重新启动时发生的清理活动。对于InnoDB表，使用来自`redo log`的数据重放未完成事务的更改。对于在崩溃前提交但尚未写入数据文件的更改，通过`doublewrite buffer`重建。当数据库正常关闭时，这类活动通过`purge`操作在关闭期间执行。

在正常操作期间，已提交的数据可以在一段时间内存储在`change buffer`中，然后再写入数据文件。保持数据文件的更新（这在正常操作期间引入了性能开销）和缓冲数据（这可能使关闭和崩溃恢复时间更长）之间总是存在权衡。

参见 `change buffer`, `commit`, `crash`, `data files`, `doublewrite buffer`, `InnoDB`, `purge`, `redo log`。

**CRUD**

“create, read, update, delete”的缩写，是数据库应用程序中常见的一系列操作。通常表示一类相对简单的数据库使用（基本的DDL、DML和SQL查询语句）应用程序，可以快速在任何语言中实现。

参见 `DDL`, `DML`, `query`, `SQL`。

**cursor**

MySQL中表示SQL语句结果集的内部数据结构。通常与准备好的语句和动态SQL一起使用。它的工作方式类似于其他高级语言中的迭代器，根据请求生成结果集中的每个值。

尽管SQL通常会为您处理游标的处理，您在处理性能关键的代码时可能会深入研究其内部工作原理。

参见 `dynamic SQL`, `prepared statement`, `query`。

## D

**data definition language**

参见 `DDL`。

**data dictionary**

用于跟踪数据库对象（如表、索引和表列）的元数据。MySQL的数据字典在MySQL 8.0中引入，元数据物理上位于`mysql`数据库目录下的InnoDB每表独立表空间文件中。而InnoDB的数据字典元数据则物理上位于InnoDB系统表空间中。

由于`MySQL Enterprise Backup`产品总是备份InnoDB系统表空间，因此所有备份都包含InnoDB数据字典的内容。

参见 `column`, `file-per-table`, `.frm file`, `index`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `system tablespace`, `table`。

**data directory**

每个MySQL实例保存InnoDB数据文件和表示各个数据库的目录的目录。由`datadir`配置选项控制。

参见 `data files`, `instance`。

**data files**

物理上包含表和索引数据的文件。

InnoDB系统表空间包含InnoDB数据字典，并能够存储多个InnoDB表的数据，表示为一个或多个`.ibdata`数据文件。

每表独立表空间，存储单个InnoDB表的数据，表示为一个`.ibd`数据文件。

通用表空间（在MySQL 5.7.6中引入），可以存储多个InnoDB表的数据，也表示为一个`.ibd`数据文件。

参见 `data dictionary`, `file-per-table`, `general tablespace`, `.ibd file`, `ibdata file`, `index`, `system tablespace`, `table`, `tablespace`。

**data manipulation language**

参见 `DML`。

**data warehouse**

主要运行大型查询的数据库系统或应用程序。只读或大多数为只读的数据可能以非规范化形式组织以提高查询效率。在MySQL 5.6及更高版本中，可以从只读事务的优化中受益。与OLTP形成对比。

参见 `denormalized`, `OLTP`, `query`, `read-only transaction`。

**database**

在MySQL数据目录中，每个数据库由一个单独的目录表示。InnoDB系统表空间可以保存来自MySQL实例内多个数据库的表数据，并保存在位于各个数据库目录之外的数据文件中。当启用每表独立表空间模式时，表示各个InnoDB表的`.ibd`文件存储在数据库目录内，除非使用`DATA DIRECTORY`子句在其他位置创建。通用表空间（在MySQL 5.7.6中引入）也将表数据保存在`.ibd`文件中。与每表独立的`.ibd`文件不同，通用表空间`.ibd`文件可以保存来自MySQL实例内多个数据库的表数据，并且可以分配到相对于MySQL数据目录或独立于MySQL数据目录的目录中。

对于长期使用MySQL的用户，数据库是一个熟悉的概念。对于来自Oracle数据库背景的用户，MySQL的数据库概念更接近Oracle数据库所称的模式（schema）。

参见 `data files`, `file-per-table`, `.ibd file`, `instance`, `schema`, `system tablespace`。

**DCL**

数据控制语言，一组用于管理权限的SQL语句。在MySQL中，由`GRANT`和`REVOKE`语句组成。与`DDL`和`DML`形成对比。

参见 `DDL`, `DML`, `SQL`。

**DDEX provider**

允许您使用Visual Studio中的数据设计工具操作MySQL数据库中的模式和对象的功能。对于使用`Connector/NET`的MySQL应用程序，`MySQL Visual Studio Plugin`作为DDEX提供程序，与MySQL 5.0及更高版本兼容。

参见 `Visual Studio`。

**DDL**

数据定义语言，一组用于操作数据库本身而非单个表行的SQL语句。包括所有形式的`CREATE`、`ALTER`和`DROP`语句。还包括`TRUNCATE`语句，因为它的工作方式与`DELETE FROM table_name`语句不同，尽管最终效果类似。

DDL语句自动提交当前事务；它们不能被回滚。

InnoDB的在线DDL功能提高了`CREATE INDEX`、`DROP INDEX`和多种类型的`ALTER TABLE`操作的性能。有关更多信息，请参见[17.12节 “InnoDB and Online DDL”](https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl.html)。此外，InnoDB的每表独立设置可能会影响`DROP TABLE`和`TRUNCATE TABLE`操作的行为。

与`DML`和`DCL`形成对比。

参见 `commit`, `DCL`, `DML`, `file-per-table`, `rollback`, `SQL`, `transaction`。

**deadlock**

一种不同事务无法继续的情况，因为每个事务都持有对方所需的锁。由于两个事务都在等待资源变得可用，因此它们都不会释放其持有的锁。

当事务以相反的顺序锁定多个表中的行（通过`UPDATE`或`SELECT ... FOR UPDATE`等语句）时，可能会发生死锁。当此类语句锁定索引记录和间隙的范围时，由于时间问题，也可能发生死锁。

有关如何自动检测和处理死锁的背景信息，请参见[17.7.5.2节 “Deadlock Detection”](https://dev.mysql.com/doc/refman/8.0/en/innodb-deadlocks.html)。有关避免和恢复死锁条件的提示，请参见[17.7.5.3节 “How to Minimize and Handle Deadlocks”](https://dev.mysql.com/doc/refman/8.0/en/innodb-deadlocks-handling.html)。

参见 `gap`, `lock`, `transaction`。

**deadlock detection**

一种自动检测死锁发生的机制，并自动回滚涉及的事务之一（牺牲者）。可以使用`innodb_deadlock_detect`配置选项禁用死锁检测。

参见 `deadlock`, `rollback`, `transaction`, `victim`。

**delete**

当InnoDB处理`DELETE`语句时，行会立即标记为删除，并且不再通过查询返回。存储将在稍后通过称为清除操作的周期性垃圾回收过程中回收。对于删除大量数据，相关操作具有各自的性能特征，包括`TRUNCATE`和`DROP`。

参见 `drop`, `purge`, `truncate`。

**delete buffering**

将`DELETE`操作产生的二级索引页面的更改存储在`change buffer`中，而不是立即写入更改，从而物理写入可以最小化随机I/O。（由于删除操作是一个两步过程，此操作会缓冲通常将索引记录标记为删除的写入。）这是更改缓冲的一种类型；其他类型包括`insert buffering`和`purge buffering`。

参见 `change buffer`, `change buffering`, `insert buffer`, `insert buffering`, `purge buffering`。

**denormalized**

一种数据存储策略，在不同表中重复数据，而不是通过外键和连接查询链接表。通常用于数据仓库应用程序，其中数据在加载后不再更新。在此类应用程序中，查询性能比在更新期间保持一致性数据更重要。与规范化形成对比。

参见 `data warehouse`, `foreign key`, `join`, `normalized`。

**descending index**

一种索引类型，优化索引存储以处理`ORDER BY column DESC`子句。

参见 `index`。

**dictionary object cache**

字典对象缓存将以前访问过的数据字典对象存储在内存中，以便重用对象并最小化磁盘I/O。使用基于`LRU`的逐出策略，将最近最少使用的对象从内存中移除。缓存由多个分区组成，存储不同类型的对象。

有关更多信息，请参见[16.4节 “Dictionary Object Cache”](https://dev.mysql.com/doc/refman/8.0/en/dictionary-object-cache.html)。

参见 `data dictionary`, `LRU`。

**dirty page**

InnoDB `buffer pool`中的一个页面，该页面在内存中已被更新，但更改尚未写入（`flush`）到数据文件。与`clean page`相对。

参见 `buffer pool`, `clean page`, `data files`, `flush`, `page`。

**dirty read**

一种检索不可靠数据的操作，即由其他事务更新但尚未提交的数据。这种操作仅在隔离级别为`READ UNCOMMITTED`时才可能。

这种操作不符合数据库设计的ACID原则。它被认为非常危险，因为数据可能会被回滚，或在提交前进一步更新；然后，进行脏读的事务将使用从未确认为准确的数据。

其对立面是`consistent read`，InnoDB确保事务不会读取由其他事务更新的信息，即使在此期间其他事务已提交。

参见 `ACID`, `commit`, `consistent read`, `isolation level`, `READ UNCOMMITTED`, `rollback`。

**disk-based**

一种主要在磁盘存储（硬盘或等效设备）上组织数据的数据库。数据在磁盘和内存之间来回传输以进行操作。它与内存数据库相对。尽管InnoDB是基于磁盘的，但它也包含诸如`buffer pool`、多个`buffer pool instances`和`adaptive hash index`等功能，允许某些类型的工作负载主要从内存中运行。

参见 `adaptive hash index`, `buffer pool`, `in-memory database`。

**disk-bound**

一种主要瓶颈是磁盘I/O的工作负载。（也称为I/O受限。）通常涉及频繁的磁盘写入，或随机读取的数据量超过`buffer pool`的容量。

参见 `bottleneck`, `buffer pool`, `workload`。

**DML**

数据操作语言，一组用于执行`INSERT`、`UPDATE`和`DELETE`操作的SQL语句。`SELECT`语句有时被认为是`DML`语句，因为`SELECT ... FOR UPDATE`形式在锁定方面与`INSERT`、`UPDATE`和`DELETE`具有相同的考虑因素。

InnoDB表的DML语句在事务上下文中操作，因此它们的效果可以作为单个单元提交或回滚。

与`DDL`和`DCL`形成对比。

参见 `commit`, `DCL`, `DDL`, `locking`, `rollback`, `SQL`, `transaction`。

**document id**

在InnoDB全文搜索功能中，表中包含`FULLTEXT`索引的特殊列，用于唯一标识与每个`ilist`值相关联的文档。其名称为`FTS_DOC_ID`（需要大写）。该列本身必须为`BIGINT UNSIGNED NOT NULL`类型，并具有名为`FTS_DOC_ID_INDEX`的唯一索引。最好在创建表时定义此列。如果InnoDB在创建`FULLTEXT`索引时必须将列添加到表中，索引操作将显著增加开销。

参见 `full-text search`, `FULLTEXT index`, `ilist`。

**doublewrite buffer**

InnoDB使用一种称为`doublewrite`的文件刷新技术。在将页面写入数据文件之前，InnoDB首先将它们写入称为`doublewrite buffer`的存储区。只有在写入和刷新到`doublewrite buffer`完成后，InnoDB才会将页面写入到数据文件中的适当位置。如果在页面写入过程中发生操作系统、存储子系统或`mysqld`进程崩溃，InnoDB可以在崩溃恢复期间从`doublewrite buffer`中找到页面的良好副本。

尽管数据始终被写入两次，但`doublewrite buffer`不需要两倍的I/O开销或两倍的I/O操作。数据以大块顺序写入缓冲区，并使用单个`fsync()`调用操作系统。

参见 `crash recovery`, `data files`, `page`, `purge`。

**drop**

一种DDL操作，通过`DROP TABLE`或`DROP INDEX`等语句删除模式对象。它在内部映射为`ALTER TABLE`语句。从InnoDB的角度来看，这类操作的性能考虑涉及到锁定数据字典以确保所有相关对象都已更新的时间，以及更新内存结构（如`buffer pool`）的时间。对于表，删除操作与截断操作（`TRUNCATE TABLE`语句）具有略微不同的特性。

参见 `buffer pool`, `data dictionary`, `DDL`, `table`, `truncate`。

**DSN**

“数据库源名称”的缩写。它是`Connector/ODBC`中连接信息的编码。有关详细信息，请参见[在Windows上配置Connector/ODBC DSN](https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-dsn.html)。它等同于`Connector/NET`使用的连接字符串。

参见 `connection`, `connection string`, `Connector/NET`, `Connector/ODBC`。

**dynamic cursor**

ODBC支持的一种游标类型，可以在再次读取行时获取新的和更改后的结果。更改是否以及多快对游标可见，取决于所涉及的表类型（事务性或非事务性）和事务表的隔离级别。动态游标支持必须显式启用。

参见 `cursor`, `ODBC`。

**dynamic row format**

InnoDB的一种行格式。由于长可变长度列值存储在保存行数据的页面之外，因此对于包含大对象的行非常有效。由于通常不访问大字段来评估查询条件，因此它们不会经常被加载到`buffer pool`中，从而减少了I/O操作并更好地利用了缓存内存。

从MySQL 5.7.9开始，默认行格式由`innodb_default_row_format`定义，其默认值为`DYNAMIC`。

有关InnoDB `DYNAMIC`行格式的更多信息，请参见[DYNAMIC Row Format](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html#innodb-row-format-dynamic)。

参见 `buffer pool`, `file format`, `row format`。

**dynamic SQL**

一种功能，使您可以使用比将语句部分连接到字符串变量的简单方法更健壮、安全和高效的方法创建和执行准备好的语句。

参见 `prepared statement`。

**dynamic statement**

通过动态SQL创建和执行的准备好的语句。

参见 `dynamic SQL`, `prepared statement`。

## E

**early adopter**

类似于`beta`阶段，软件产品通常在非关键任务环境中进行性能、功能和兼容性评估的阶段。

参见 `beta`。

**Eiffel**

一种编程语言，包含许多面向对象的特性。它的一些概念对Java和C#开发人员来说很熟悉。有关开源的Eiffel API for MySQL，请参见[31.13节 “MySQL Eiffel Wrapper”](https://dev.mysql.com/doc/connector-eiffel/en/connector-eiffel.html)。

参见 `API`, `C#`, `Java`。

**embedded**

嵌入式MySQL服务器库（`libmysqld`）使得可以在客户端应用程序中运行功能齐全的MySQL服务器。主要优点是提高了嵌入式应用程序的速度和管理的简便性。

参见 `client`, `libmysqld`。

**error log**

一种日志，显示关于MySQL启动、关键运行时错误和崩溃信息的内容。有关详细信息，请参见[7.4.2节 “The Error Log”](https://dev.mysql.com/doc/refman/8.0/en/error-log.html)。

参见 `crash`, `log`。

**eviction**

将项目从缓存或其他临时存储区（如InnoDB缓冲池）中移除的过程。通常（但并非总是）使用`LRU`算法确定要移除的项目。当一个`dirty page`被驱逐时，其内容会被刷新到磁盘，任何脏的邻居页面也可能会被刷新。

参见 `buffer pool`, `dirty page`, `flush`, `LRU`, `neighbor page`。

**exception interceptor**

一种用于跟踪、调试或增强数据库应用程序中遇到的SQL错误的拦截器类型。例如，拦截器代码可以发出`SHOW WARNINGS`语句以检索其他信息，并添加描述性文本，甚至更改返回给应用程序的异常类型。由于拦截器代码仅在SQL语句返回错误时调用，因此在正常（无错误）操作期间不会对应用程序造成任何性能损失。

在使用`Connector/J`的Java应用程序中，设置此类拦截器涉及实现`com.mysql.jdbc.ExceptionInterceptor`接口，并在连接字符串中添加`exceptionInterceptors`属性。

在使用`Connector/NET`的Visual Studio应用程序中，设置此类拦截器涉及定义一个继承自`BaseExceptionInterceptor`类的类，并将该类名指定为连接字符串的一部分。

参见 `Connector/J`, `Connector/NET`, `interceptor`, `Java`, `Visual Studio`。

**exclusive lock**

一种锁，防止任何其他事务锁定同一行。根据事务隔离级别，这种锁可能会阻止其他事务写入同一行，或者也可能阻止其他事务读取同一行。InnoDB的默认隔离级别`REPEATABLE READ`通过允许事务读取具有排他锁的行来提高并发性，这种技术称为`consistent read`。

参见 `concurrency`, `consistent read`, `isolation level`, `lock`, `REPEATABLE READ`, `shared lock`, `transaction`。

**extent**

表空间中的一组页面。对于默认页面大小16KB，一个`extent`包含64个页面。在MySQL 5.6中，InnoDB实例的页面大小可以为4KB、8KB或16KB，由`innodb_page_size`配置选项控制。对于4KB、8KB和16KB的页面大小，`extent`大小始终为1MB（或1048576字节）。

MySQL 5.7.6中添加了对32KB和64KB InnoDB页面大小的支持。对于32KB页面大小，`extent`大小为2MB。对于64KB页面大小，`extent`大小为4MB。

InnoDB的一些特性，如`segments`、预读请求和`doublewrite buffer`，使用一次读取、写入、分配或释放一个`extent`的I/O操作。

参见 `doublewrite buffer`, `page`, `page size`, `read-ahead`, `segment`, `tablespace`。

## F

**.frm file**

包含MySQL表元数据（如表定义）的文件。.frm文件在MySQL 8.0中已被移除，但在早期的MySQL版本中仍然使用。在MySQL 8.0中，之前存储在.frm文件中的数据现在存储在数据字典表中。

参见 `data dictionary`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `system tablespace`。

**failover**

在发生故障时自动切换到备用服务器的能力。在MySQL上下文中，failover涉及一个备用数据库服务器。通常在J2EE环境中由应用服务器或框架支持。

参见 `Connector/J`, `J2EE`。

**Fast Index Creation**

最初在InnoDB插件中引入的一项功能，现在是MySQL 5.5及更高版本的一部分，通过避免完全重写关联表，加快了InnoDB二级索引的创建速度。该功能同样适用于删除二级索引的操作。

由于索引维护会给许多数据传输操作带来性能开销，可以考虑在没有任何二级索引的情况下执行操作，如`ALTER TABLE ... ENGINE=INNODB`或`INSERT INTO ... SELECT * FROM ...`，然后再创建索引。

在MySQL 5.6中，这项功能变得更加通用。您可以在创建索引时对表进行读写操作，并且许多类型的`ALTER TABLE`操作可以在不复制表的情况下执行，不会阻塞DML操作。因此，在MySQL 5.6及更高版本中，这组功能称为`online DDL`，而不是`Fast Index Creation`。

有关更多信息，请参见[17.12节 “InnoDB and Online DDL”](https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl.html)。

参见 `DML`, `index`, `online DDL`, `secondary index`。

**fast shutdown**

InnoDB的默认关闭过程，基于配置设置`innodb_fast_shutdown=1`。为了节省时间，某些`flush`操作会被跳过。这种关闭在正常使用期间是安全的，因为在下次启动时使用与崩溃恢复相同的机制执行这些`flush`操作。在数据库因升级或降级而关闭的情况下，应执行`slow shutdown`以确保在关闭期间将所有相关更改应用到数据文件中。

参见 `crash recovery`, `data files`, `flush`, `shutdown`, `slow shutdown`。

**file format**

InnoDB表的文件格式。

参见 `file-per-table`, `.ibd file`, `ibdata file`, `row format`。

**file-per-table**

受`innodb_file_per_table`选项控制的设置的通用名称，这是一个重要的配置选项，会影响InnoDB文件存储、功能可用性和I/O特性。从MySQL 5.6.7开始，默认启用`innodb_file_per_table`。

启用`innodb_file_per_table`选项后，您可以将表创建在自己的.ibd文件中，而不是在系统表空间的共享ibdata文件中。当表数据存储在单个.ibd文件中时，您可以更灵活地选择所需的行格式，以支持如数据压缩等功能。`TRUNCATE TABLE`操作也更快，并且回收的空间可以由操作系统使用，而不是保留给InnoDB。

对于存储在独立文件中的表，`MySQL Enterprise Backup`产品更灵活。例如，表可以从备份中排除，但前提是它们存储在单独的文件中。因此，此设置适用于不太频繁或在不同时间表上备份的表。

参见 `compressed row format`, `compression`, `file format`, `.ibd file`, `ibdata file`, `innodb_file_per_table`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `row format`, `system tablespace`。

**fill factor**

在InnoDB索引中，页面被索引数据占用的比例，决定了页面在拆分前的填充程度。首次将索引数据分配到页面之间时的未使用空间允许在不需要昂贵的索引维护操作的情况下更新行中的较长字符串值。如果`fill factor`过低，索引将占用比实际需要更多的空间，从而在读取索引时产生额外的I/O开销。如果`fill factor`过高，任何增加列值长度的更新都可能导致索引维护的额外I/O开销。有关更多信息，请参见[17.6.2.2节 “The Physical Structure of an InnoDB Index”](https://dev.mysql.com/doc/refman/8.0/en/innodb-index-structure.html)。

参见 `index`, `page`。

**fixed row format**

此行格式由MyISAM存储引擎使用，而不是InnoDB。如果您在MySQL 5.7.6或更早版本中使用`ROW_FORMAT=FIXED`创建InnoDB表，InnoDB将使用`compact row format`，尽管`FIXED`值可能仍会显示在诸如`SHOW TABLE STATUS`报告的输出中。从MySQL 5.7.7开始，如果指定了`ROW_FORMAT=FIXED`，InnoDB将返回错误。

参见 `compact row format`, `row format`。

**flush**

将缓存在内存区域或临时磁盘存储区域中的更改写入数据库文件。InnoDB周期性刷新的存储结构包括`redo log`、`undo log`和`buffer pool`。

`flush`操作可能因为内存区域已满且系统需要释放一些空间、提交操作意味着事务的更改可以最终确定，或`slow shutdown`操作意味着所有未完成的工作都应该最终完成。当不需要一次性刷新所有缓冲数据时，InnoDB可以使用一种称为`fuzzy checkpointing`的技术来刷新小批量页面，从而分散I/O开销。

参见 `buffer pool`, `commit`, `fuzzy checkpointing`, `redo log`, `slow shutdown`, `undo log`。

**flush list**

InnoDB的一个内部数据结构，用于跟踪`buffer pool`中的`dirty pages`，即已更改且需要写回磁盘的页面。该数据结构由InnoDB内部的迷你事务频繁更新，因此通过其自身的互斥锁保护，以允许对`buffer pool`的并发访问。

参见 `buffer pool`, `dirty page`, `LRU`, `mini-transaction`, `mutex`, `page`, `page cleaner`。

**foreign key**

一种在不同InnoDB表的行之间建立的指针关系。外键关系在父表和子表的一个列上定义。

除了实现相关信息的快速查找外，外键还通过防止在插入、更新和删除数据时使这些指针无效，从而帮助强制执行引用完整性。这种强制机制是一种约束。如果相关外键值在另一个表中不存在，则无法插入指向另一个表的行。如果删除一行或更改其外键值，并且另一个表中的行指向该外键值，则可以设置外键以防止删除，使另一个表中的相应列值变为null，或自动删除另一个表中的相应行。

设计规范化数据库的阶段之一是识别重复的数据，将这些数据分离到一个新表中，并设置外键关系，以便通过连接操作查询多个表如同单个表。

参见 `child table`, `FOREIGN KEY constraint`, `join`, `normalized`, `NULL`, `parent table`, `referential integrity`, `relational`。

**FOREIGN KEY constraint**

通过外键关系维护数据库一致性的约束类型。与其他类型的约束一样，它可以防止数据插入或更新时变得不一致；在这种情况下，防止的数据不一致是表之间的数据不一致。或者，当执行DML操作时，外键约束可以根据创建外键时指定的`ON CASCADE`选项，导致子行中的数据被删除、更改为不同的值或设置为null。

参见 `child table`, `constraint`, `DML`, `foreign key`, `NULL`。

**FTS**

在大多数情况下，是`full-text search`的缩写。在性能讨论中，有时是`full table scan`的缩写。

参见 `full table scan`, `full-text search`。

**full backup**

包含MySQL数据库中所有表和每个MySQL实例中所有数据库的备份。与`partial backup`形成对比。

参见 `backup`, `database`, `instance`, `partial backup`, `table`。

**full table scan**

一种操作，需要读取表的全部内容，而不仅仅是使用索引选择的部分。通常在小型查找表或数据仓库环境中对大型表执行此操作，在此环境中，所有可用数据都被聚合和分析。这些操作发生的频率以及表相对于可用内存的大小，对查询优化和管理`buffer pool`的算法有影响。

索引的目的是允许在大表中查找特定值或值范围，从而在可行时避免全表扫描。

参见 `buffer pool`, `index`。

**full-text search**

MySQL的一项功能，用于在表数据中查找单词、短语、布尔组合词等，速度更快、更方便、更灵活，比使用SQL `LIKE`运算符或编写自己的应用级搜索算法更高效。它使用SQL函数`MATCH()`和`FULLTEXT`索引。

参见 `FULLTEXT index`。

**FULLTEXT index**

在MySQL全文搜索机制中保存搜索索引的特殊索引类型。表示列值中的单词，省略任何指定为停用词的单词。最初，仅适用于MyISAM表。从MySQL 5.6.4开始，它也可用于InnoDB表。

参见 `full-text search`, `index`, `InnoDB`, `search index`, `stopword`。

**fuzzy checkpointing**

一种技术，将小批量的`dirty pages`从`buffer pool`中刷出，而不是一次性刷新所有脏页，以避免中断数据库处理。

参见 `buffer pool`, `dirty page`, `flush`。

## G

**GA**

“Generally available”，指软件产品离开`beta`阶段并可供销售、官方支持和生产使用的阶段。

参见 `beta`。

**GAC**

“Global Assembly Cache”的缩写。在.NET系统中用于存储库（`assemblies`）的中央区域。物理上由嵌套文件夹组成，由.NET CLR作为单个虚拟文件夹处理。

参见 `.NET`, `assembly`。

**gap**

InnoDB索引数据结构中的一个位置，新值可以插入其中。当您使用诸如`SELECT ... FOR UPDATE`之类的语句锁定一组行时，InnoDB可以创建适用于间隙以及索引中的实际值的锁。例如，如果选择所有大于10的值进行更新，间隙锁将阻止其他事务插入大于10的新值。`supremum record`和`infimum record`表示包含大于或小于所有当前索引值的所有值的间隙。

参见 `concurrency`, `gap lock`, `index`, `infimum record`, `isolation level`, `supremum record`。

**gap lock**

锁定索引记录之间的间隙，或者锁定第一条或最后一条索引记录之前或之后的间隙。例如，`SELECT c1 FROM t WHERE c1 BETWEEN 10 and 20 FOR UPDATE;`会阻止其他事务在列`t.c1`中插入值15，无论列中是否已经存在该值，因为锁定了范围内所有现有值之间的间隙。与`record lock`和`next-key lock`形成对比。

间隙锁是性能与并发性之间权衡的一部分，在某些事务隔离级别中使用，而在其他级别中不使用。

参见 `gap`, `infimum record`, `lock`, `next-key lock`, `record lock`, `supremum record`。

**general log**

参见 `general query log`。

**general query log**

一种用于诊断和故障排除由MySQL服务器处理的SQL语句的日志。可以存储在文件或数据库表中。必须通过`general_log`配置选项启用此功能才能使用它。您可以通过`sql_log_off`配置选项禁用特定连接的此功能。

记录的查询范围比慢查询日志更广。与用于复制的二进制日志不同，`general query log`包含`SELECT`语句并且不维护严格的排序。有关更多信息，请参见[7.4.3节 “The General Query Log”](https://dev.mysql.com/doc/refman/8.0/en/query-log.html)。

参见 `binary log`, `log`, `slow query log`。

**general tablespace**

使用`CREATE TABLESPACE`语法创建的共享InnoDB表空间。`general tablespace`可以在MySQL数据目录之外创建，能够容纳多个表，并支持所有行格式的表。`general tablespace`在MySQL 5.7.6中引入。

使用`CREATE TABLE tbl_name ... TABLESPACE [=] tablespace_name`或`ALTER TABLE tbl_name TABLESPACE [=] tablespace_name`语法将表添加到`general tablespace`中。

与`system tablespace`和`file-per-table tablespace`形成对比。

有关更多信息，请参见[17.6.3.3节 “General Tablespaces”](https://dev.mysql.com/doc/refman/8.0/en/general-tablespaces.html)。

参见 `file-per-table`, `system tablespace`, `table`, `tablespace`。

**generated column**

其值由列定义中包含的表达式计算得出的列。生成列可以是虚拟列或存储列。

参见 `base column`, `stored generated column`, `virtual generated column`。

**generated stored column**

参见 `stored generated column`。

**generated virtual column**

参见 `virtual generated column`。

**Glassfish**

参见 `J2EE`。

**global temporary tablespace**

一个存储用户创建的临时表的回滚段的临时表空间。

参见 `temporary tablespace`。

**global transaction**

涉及`XA`操作的一种事务。它由几个本身就是事务性的操作组成，但所有操作必须作为一个组成功完成，或者全部回滚。实质上，它将`ACID`属性扩展到多个`ACID`事务可以协同执行作为具有`ACID`属性的全局操作的组成部分。

参见 `ACID`, `transaction`, `XA`。

**group commit**

一种InnoDB优化，针对一组提交操作执行一些底层I/O操作（日志写入），而不是为每个提交单独刷新和同步。

参见 `binary log`, `commit`。

**GUID**

“globally unique identifier”的缩写，是一种ID值，可以用于跨不同数据库、语言、操作系统等关联数据。（作为使用顺序整数的替代方法，相同的值可能会出现在不同的表、数据库中，指代不同的数据。）旧版MySQL将其表示为`BINARY(16)`。当前，它表示为`CHAR(36)`。MySQL有一个`UUID()`函数返回字符格式的GUID值，一个`UUID_SHORT()`函数返回整数格式的GUID值。由于连续的GUID值不一定按升序排序，因此它不是用作大型InnoDB表主键的有效值。

## H

**hash index**

一种用于查询等值运算符（如`=`）而非范围运算符（如`>`或`BETWEEN`）的索引类型。可用于`MEMORY`表。尽管历史原因使得`MEMORY`表的默认索引是`hash index`，但该存储引擎也支持`B-tree`索引，后者通常是通用查询的更好选择。

MySQL包括此类索引的变体——`adaptive hash index`，它在运行时条件允许时自动为`InnoDB`表构建。

参见 `adaptive hash index`, `B-tree`, `index`, `InnoDB`。

**HDD**

“hard disk drive”（硬盘驱动器）的缩写。指使用旋转盘片的存储介质，通常在与`SSD`进行对比时使用。其性能特性会影响基于磁盘的工作负载的吞吐量。

参见 `disk-based`, `SSD`。

**heartbeat**

用于指示系统正常运行的定期消息。在复制上下文中，如果`source`停止发送此类消息，则其中一个副本可以代替其位置。在集群环境中的服务器之间也可以使用类似技术，以确认它们都在正常运行。

参见 `replication`, `source`。

**high-water mark**

表示上限的值，可以是在运行时不应超过的硬限制，也可以是实际达到的最大值的记录。与`low-water mark`形成对比。

参见 `low-water mark`。

**history list**

包含计划由InnoDB清除操作处理的标记为删除的记录的事务列表。记录在`undo log`中。`history list`的长度可通过`SHOW ENGINE INNODB STATUS`命令报告。如果`history list`的长度超过`innodb_max_purge_lag`配置选项的值，则每个DML操作会稍有延迟，以允许清除操作完成对删除记录的刷新。

也称为`purge lag`。

参见 `DML`, `flush`, `purge`, `purge lag`, `rollback segment`, `transaction`, `undo log`。

**hole punching**

从页面中释放空块。InnoDB透明页面压缩功能依赖于`hole punching`支持。有关更多信息，请参见[17.9.2节 “InnoDB Page Compression”](https://dev.mysql.com/doc/refman/8.0/en/innodb-page-compression.html)。

参见 `sparse file`, `transparent page compression`。

**host**

用于建立连接的数据库服务器的网络名称。通常与`port`一起指定。在某些情况下，IP地址`127.0.0.1`比特殊名称`localhost`更适合用于访问与应用程序位于同一服务器上的数据库。

参见 `connection`, `localhost`, `port`。

**hot**

行、表或内部数据结构被如此频繁地访问，以至于需要某种形式的锁定或互斥，从而导致性能或可扩展性问题的条件。

尽管“hot”通常表示不理想的情况，但`hot backup`是一种首选的备份类型。

参见 `hot backup`。

**hot backup**

在数据库运行且应用程序正在读取和写入的情况下进行的备份。备份不仅仅是简单地复制数据文件：它必须包含在备份过程中插入或更新的任何数据；必须排除在备份过程中删除的任何数据；并且必须忽略任何未提交的更改。

执行`hot backup`的Oracle产品特别适用于`InnoDB`表，但也支持`MyISAM`和其他存储引擎中的表，该产品称为`MySQL Enterprise Backup`。

`hot backup`过程包括两个阶段。初始数据文件的复制生成原始备份。`apply`步骤将备份运行时对数据库的任何更改合并。应用这些更改会生成已准备好的备份；这些文件可以随时恢复。

参见 `apply`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `prepared backup`, `raw backup`。

## I

**.ibd file**

`file-per-table`表空间和`general tablespaces`的`data file`。`file-per-table`表空间中的.ibd文件包含单个表及其关联的索引数据。`general tablespace`中的.ibd文件可能包含多个表的表和索引数据。

.ibd文件扩展名不适用于系统表空间，系统表空间由一个或多个ibdata文件组成。

如果使用`DATA DIRECTORY =`子句创建`file-per-table`表空间或`general tablespace`，则.ibd文件位于指定路径下，位于常规数据目录之外。

当`MySQL Enterprise Backup`产品在压缩备份中包含.ibd文件时，压缩后的等价文件为.ibz文件。

参见 `database`, `file-per-table`, `general tablespace`, `ibdata file`, `.ibz file`, `innodb_file_per_table`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `system tablespace`。

**.ibz file**

当`MySQL Enterprise Backup`产品执行压缩备份时，它将使用`file-per-table`设置创建的每个表空间文件从.ibd扩展名转换为.ibz扩展名。

备份期间应用的压缩与在正常操作期间保持表数据压缩的压缩行格式不同。对于已经采用压缩行格式的表空间，压缩备份操作会跳过压缩步骤，因为二次压缩会减慢备份速度，但几乎没有空间节省。

参见 `compressed backup`, `compressed row format`, `file-per-table`, `.ibd file`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `tablespace`。

**I/O-bound**

参见 `disk-bound`。

**ib-file set**

由InnoDB在MySQL数据库中管理的一组文件：系统表空间、`file-per-table`表空间文件和重做日志文件。根据MySQL版本和InnoDB配置，可能还包括`general tablespace`、`temporary tablespace`和`undo tablespace`文件。此术语有时用于深入讨论InnoDB文件结构和格式时，指代InnoDB在MySQL数据库中管理的一组文件。

参见 `database`, `file-per-table`, `general tablespace`, `redo log`, `system tablespace`, `temporary tablespace`, `undo tablespace`。

**ibbackup_logfile**

在执行`hot backup`操作期间，`MySQL Enterprise Backup`产品创建的一个补充备份文件。它包含在备份运行期间发生的任何数据更改信息。初始备份文件（包括ibbackup_logfile）被称为`raw backup`，因为备份操作期间发生的更改尚未合并。在对原始备份文件执行`apply`步骤后，生成的文件包含这些最终的数据更改，并被称为`prepared backup`。此阶段后，ibbackup_logfile文件不再需要。

参见 `apply`, `hot backup`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `prepared backup`, `raw backup`。

**ibdata file**

一组文件，命名为ibdata1、ibdata2等，构成InnoDB系统表空间。有关系统表空间ibdata文件中存储的结构和数据的信息，请参见[17.6.3.1节 “The System Tablespace”](https://dev.mysql.com/doc/refman/8.0/en/innodb-system-tablespace.html)。

ibdata文件的增长受`innodb_autoextend_increment`配置选项的影响。

参见 `change buffer`, `data dictionary`, `doublewrite buffer`, `file-per-table`, `.ibd file`, `innodb_file_per_table`, `system tablespace`, `undo log`。

**ibtmp file**

用于非压缩InnoDB临时表及相关对象的InnoDB临时表空间数据文件。配置文件选项`innodb_temp_data_file_path`允许用户为临时表空间数据文件定义相对路径。如果未指定`innodb_temp_data_file_path`，默认行为是在数据目录中创建一个名为`ibtmp1`的自动扩展12MB数据文件，位于ibdata1旁边。

参见 `data files`, `temporary table`, `temporary tablespace`。

**ib_logfile**

一组文件，通常命名为ib_logfile0和ib_logfile1，形成重做日志。有时也称为日志组。这些文件记录试图更改InnoDB表数据的语句。这些语句在启动后会自动重放，以纠正未完成事务写入的数据。

此数据不能用于手动恢复；对于这种操作，请使用二进制日志。

参见 `binary log`, `log group`, `redo log`。

**ilist**

在InnoDB全文索引中，由文档ID和标记（即特定单词）的位置信息组成的数据结构。

参见 `FULLTEXT index`。

**implicit row lock**

InnoDB为确保一致性而获取的行锁，您无需专门请求它。

参见 `row lock`。

**in-memory database**

一种数据库系统，将数据保存在内存中，以避免由于磁盘I/O和磁盘块与内存区域之间的转换带来的开销。一些内存数据库牺牲了`ACID`设计哲学中的“D”——持久性，因此易受硬件、电源和其他类型故障的影响，使它们更适合只读操作。其他内存数据库确实使用了持久性机制，例如将更改记录到磁盘或使用非易失性内存。

MySQL中用于处理同类内存密集型操作的功能包括InnoDB缓冲池、自适应哈希索引、只读事务优化、MEMORY存储引擎、MyISAM键缓存和MySQL查询缓存。

参见 `ACID`, `adaptive hash index`, `buffer pool`, `disk-based`, `read-only transaction`。

**incremental backup**

一种`hot backup`，由`MySQL Enterprise Backup`产品执行，仅保存自某个时间点以来更改的数据。拥有一个完整备份和一系列增量备份可以让您在很长时间内重建备份数据，而无需保存多个完整备份所需的存储空间。您可以恢复完整备份，然后依次应用每个增量备份，也可以通过将每个增量备份应用到完整备份来保持完整备份的最新状态，然后执行一次恢复操作。

更改数据的粒度在页面级别。一个页面实际上可能覆盖多行。每个更改的页面都包含在备份中。

参见 `hot backup`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `page`。

**index**

一种数据结构，为表的行提供快速查找功能，通常通过形成表示特定列或列集的所有值的树结构（B-tree）。

InnoDB表总是有一个表示主键的聚簇索引。它们还可以在一个或多个列上定义一个或多个二级索引。根据结构，二级索引可以分为部分索引、列索引或复合索引。

索引是查询性能的关键方面。数据库架构师设计表、查询和索引，以允许快速查找应用程序所需的数据。理想的数据库设计在可行的地方使用覆盖索引；查询结果完全由索引计算得出，而无需读取实际的表数据。每个外键约束也需要一个索引，以便有效地检查父表和子表中是否存在值。

尽管B-tree索引是最常见的，但在MEMORY存储引擎和InnoDB自适应哈希索引中，哈希索引使用不同的数据结构。R-tree索引用于多维信息的空间索引。

参见 `adaptive hash index`, `B-tree`, `child table`, `clustered index`, `column index`, `composite index`, `covering index`, `foreign key`, `hash index`, `parent table`, `partial index`, `primary key`, `query`, `R-tree`, `row`, `secondary index`, `table`。

**index cache**

保存InnoDB全文搜索标记数据的内存区域。它缓冲数据以最小化在插入或更新包含`FULLTEXT`索引的列时的磁盘I/O。当索引缓存已满时，标记数据会被写入磁盘。每个InnoDB`FULLTEXT`索引都有其自己的独立索引缓存，其大小由配置选项`innodb_ft_cache_size`控制。

参见 `full-text search`, `FULLTEXT index`。

**index condition pushdown**

索引条件下推（ICP）是一种优化，如果WHERE条件的部分条件可以使用索引中的字段进行评估，则将条件的一部分下推到存储引擎。ICP可以减少存储引擎访问基表的次数以及MySQL服务器访问存储引擎的次数。有关更多信息，请参见[10.2.1.6节 “Index Condition Pushdown Optimization”](https://dev.mysql.com/doc/refman/8.0/en/index-condition-pushdown-optimization.html)。

参见 `index`, `storage engine`。

**index hint**

用于覆盖优化器建议的索引的扩展SQL语法。例如，`FORCE INDEX`、`USE INDEX`和`IGNORE INDEX`子句。通常在索引列具有分布不均匀的值时使用，从而导致基数估计不准确。

参见 `cardinality`, `index`。

**index prefix**

在适用于多个列的索引（称为复合索引）中，索引的初始或前导列。即使查询未引用索引中的所有列，引用复合索引的前1、2、3个等列的查询也可以使用该索引。

参见 `composite index`, `index`。

**index statistics**

参见 `statistics`。

**infimum record**

索引中的伪记录，表示该索引中最小值以下的间隙。如果事务有诸如`SELECT ... FROM ... WHERE col < 10 FOR UPDATE;`之类的语句，而列中的最小值为5，则在`infimum record`上的锁会阻止其他事务插入更小的值，如0、-10等。

参见 `gap`, `index`, `pseudo-record`, `supremum record`。

**INFORMATION_SCHEMA**

提供MySQL数据字典查询接口的数据库名称。（此名称由ANSI SQL标准定义。）要检查有关数据库的信息（元数据），可以查询诸如`INFORMATION_SCHEMA.TABLES`和`INFORMATION_SCHEMA.COLUMNS`之类的表，而不是使用生成非结构化输出的SHOW命令。

`INFORMATION_SCHEMA`数据库还包含特定于InnoDB的表，这些表提供InnoDB数据字典的查询接口。您使用这些表不是为了查看数据库的结构，而是为了获取InnoDB表的实时信息，以帮助进行性能监控、调优和故障排除。

参见 `data dictionary`, `database`, `InnoDB`。

**InnoDB**

MySQL的一个组件，结合了高性能与事务能力，以确保可靠性、稳健性和并发访问。InnoDB体现了`ACID`设计哲学，作为一个存储引擎存在，处理使用`ENGINE=INNODB`子句创建或修改的表。有关架构细节和管理程序，请参见[第17章 InnoDB存储引擎](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html)，有关性能建议，请参见[10.5节 “Optimizing for InnoDB Tables”](https://dev.mysql.com/doc/refman/8.0/en/optimizing-innodb-tables.html)。

在MySQL 5.5及更高版本中，InnoDB是新表的默认存储引擎，因此不需要`ENGINE=INNODB`子句。

InnoDB表非常适合热备份。有关`MySQL Enterprise Backup`产品的信息，请参见[32.1节 “MySQL Enterprise Backup Overview”](https://dev.mysql.com/doc/mysql-enterprise-backup/en/mysql-enterprise-backup-overview.html)。

参见 `ACID`, `hot backup`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `storage engine`, `transaction`。

**innodb_autoinc_lock_mode**

`innodb_autoinc_lock_mode`选项控制自动增量锁定的算法。当您有一个自动增量的主键时，只能在设置`innodb_autoinc_lock_mode=1`时使用基于语句的复制。此设置称为连续锁定模式，因为事务内的多行插入操作将接收连续的自动增量值。如果设置为`innodb_autoinc_lock_mode=2`，它允许插入操作的更高并发性，请使用基于行的复制而非基于语句的复制。此设置称为交错锁定模式，因为同时运行的多个多行插入语句可以接收交错的自动增量值。`innodb_autoinc_lock_mode=0`的设置应仅用于兼容性目的。

在MySQL 8.0.3之前，连续锁定模式（`innodb_autoinc_lock_mode=1`）是默认设置。从MySQL 8.0.3开始，交错锁定模式（`innodb_autoinc_lock_mode=2`）成为默认设置，这反映了默认复制类型从基于语句的复制转变为基于行的复制。

参见 `auto-increment`, `auto-increment locking`, `mixed-mode insert`, `primary key`。

**innodb_file_per_table**

一个重要的配置选项，影响InnoDB文件存储的许多方面、功能的可用性和I/O特性。从MySQL 5.6.7开始，默认启用。`innodb_file_per_table`选项开启`file-per-table`模式。启用此模式后，新创建的InnoDB表及其关联索引可以存储在系统表空间之外的`file-per-table` .ibd文件中。

此选项影响许多SQL语句的性能和存储考虑因素，例如`DROP TABLE`和`TRUNCATE TABLE`。

启用`innodb_file_per_table`选项后，您可以利用诸如表压缩和在`MySQL Enterprise Backup`中进行命名表备份等功能。

有关更多信息，请参见[17.6.3.2节 “File-Per-Table Tablespaces”](https://dev.mysql.com/doc/refman/8.0/en/innodb-file-per-table-tablespaces.html)。

参见 `compression`, `file-per-table`, `.ibd file`, [MySQL Enterprise Backup](https://dev.mysql.com/doc/mysql-enterprise-backup), `system tablespace`。

**innodb_lock_wait_timeout**

`innodb_lock_wait_timeout`选项设置在等待共享资源可用与放弃并处理错误、重试或在应用程序中执行替代处理之间的平衡。当InnoDB事务等待超过指定时间以获取锁时，它会回滚该事务。如果更新由不同存储引擎控制的多个表导致死锁，此选项尤其有用；因为此类死锁不会自动检测。

参见 `deadlock`, `deadlock detection`, `lock`, `wait`。

**innodb_strict_mode**

`innodb_strict_mode`选项控制InnoDB是否在严格模式下操作，在此模式下，通常被视为警告的条件将导致错误（并且基础语句失败）。

参见 `strict mode`。

**Innovation Series**

具有相同主版本号的创新发布系列。例如，MySQL 8.1至8.3组成MySQL 8的创新系列。

参见 `LTS Series`。

**insert**

SQL中的主要DML操作之一。插入操作的性能是加载数百万行数据的`data warehouse`系统和可能同时有多个并发连接以任意顺序插入行的`OLTP`系统中的关键因素。如果插入性能对您很重要，您应该了解InnoDB的一些功能，例如在`change buffering`中使用的`insert buffer`和自动增量列。

参见 `auto-increment`, `change buffering`, `data warehouse`, `DML`, `InnoDB`, `insert buffer`, `OLTP`, `SQL`。

**insert buffer**

`change buffer`的旧名称。在MySQL 5.5中，增加了对`DELETE`和`UPDATE`操作的二级索引页更改的缓冲支持。以前，仅缓冲`INSERT`操作的更改。现在首选术语是`change buffer`。

参见 `change buffer`, `change buffering`。

**insert buffering**

将由`INSERT`操作引起的二级索引页的更改存储在`change buffer`中，而不是立即写入，从而最小化随机I/O操作。它是`change buffering`的一种类型；其他类型包括`delete buffering`和`purge buffering`。

如果二级索引是唯一的，则不使用插入缓冲，因为在新条目写入前无法验证新值的唯一性。其他类型的`change buffering`适用于唯一索引。

参见 `change buffer`, `change buffering`, `delete buffering`, `insert buffer`, `purge buffering`, `unique index`。

**insert intention lock**

在插入行之前由`INSERT`操作设置的一种间隙锁。这种锁类型表示插入意图，以便在相同索引间隙中插入的多个事务无需等待彼此，只要它们不是在间隙内的相同位置插入。有关更多信息，请参见[17.7.1节 “InnoDB Locking”](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)。

参见 `gap lock`, `lock`, `next-key lock`。

**instance**

一个管理数据目录的`mysqld`守护进程，表示一个或多个数据库及其一组表。在开发、测试和某些复制场景中，通常在同一服务器上运行多个实例，每个实例管理其自己的数据目录并监听其自己的端口或套接字。当一个实例运行磁盘密集型工作负载时，服务器可能仍有额外的CPU和内存容量来运行其他实例。

参见 `data directory`, `database`, `disk-bound`, `mysqld`, `replication`, `server`, `table`。

**instrumentation**

在源代码级别进行的修改，以收集性能数据以进行调优和调试。在MySQL中，通过`INFORMATION_SCHEMA`和`PERFORMANCE_SCHEMA`数据库使用SQL接口公开由`instrumentation`收集的数据。

参见 `INFORMATION_SCHEMA`, `Performance Schema`。

**intention exclusive lock**

参见 `intention lock`。

**intention lock**

一种应用于表的锁，用于指示事务打算在表中的行上获取的锁类型。不同的事务可以在同一个表上获取不同类型的意图锁，但第一个在表上获取意图排它锁（`IX`）的事务会阻止其他事务在该表上获取任何S或X锁。相反，第一个在表上获取意图共享锁（`IS`）的事务会阻止其他事务在该表上获取任何X锁。两阶段过程允许按顺序解决锁请求，而不会阻止兼容的锁及相应操作。有关此锁机制的更多信息，请参见[17.7.1节 “InnoDB Locking”](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)。

参见 `lock`, `lock mode`, `locking`, `transaction`。

**intention shared lock**

参见 `intention lock`。

**interceptor**

用于对应用程序的某些方面进行检测或调试的代码，可以在不重新编译或更改应用程序源代码的情况下启用。

参见 `command interceptor`, `Connector/J`, `Connector/NET`, `exception interceptor`。

**intrinsic temporary table**

由优化器使用的优化的内部InnoDB临时表。

参见 `optimizer`。

**inverted index**

一种为文档检索系统优化的数据结构，用于实现InnoDB全文搜索。InnoDB `FULLTEXT`索引作为倒排索引实现，记录每个单词在文档中的位置，而不是表行的位置。单个列值（作为文本字符串存储的文档）由倒排索引中的许多条目表示。

参见 `full-text search`, `FULLTEXT index`, `ilist`。

**IOPS**

每秒I/O操作数的缩写。对于繁忙的系统，尤其是`OLTP`应用程序，这是一个常见的度量值。如果此值接近存储设备能够处理的最大值，应用程序可能会变成磁盘密集型，从而限制可扩展性。

参见 `disk-bound`, `OLTP`, `scalability`。

**isolation level**

数据库处理的基础之一。隔离性是`ACID`缩写中的I；隔离级别是一个设置，用于微调在多个事务同时进行更改和执行查询时性能与可靠性、一致性和结果可重复性之间的平衡。

从一致性和保护级别最高到最低，InnoDB支持的隔离级别依次为：`SERIALIZABLE`, `REPEATABLE READ`, `READ COMMITTED`和`READ UNCOMMITTED`。

对于InnoDB表，许多用户可以在所有操作中保持默认隔离级别（`REPEATABLE READ`）。专家用户可能会选择`READ COMMITTED`级别，因为他们在`OLTP`处理过程中推动了可扩展性的极限，或者在数据仓库操作中，较小的不一致性不会影响大量数据的汇总结果。边缘级别（`SERIALIZABLE`和`READ UNCOMMITTED`）改变了处理行为，以至于很少使用。

参见 `ACID`, `OLTP`, `READ COMMITTED`, `READ UNCOMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`, `transaction`。

## J

**J2EE**

`Java Platform, Enterprise Edition`：Oracle的企业级Java平台。它由一个API和一个企业级Java应用程序的运行环境组成。有关详细信息，请参见[Oracle Java EE概述](http://www.oracle.com/technetwork/java/javaee/overview/index.html)。在MySQL应用程序中，通常使用`Connector/J`进行数据库访问，使用`Tomcat`或`JBoss`等应用服务器处理中间层工作，并可选择使用`Spring`等框架。J2EE堆栈中通常提供的与数据库相关的功能包括连接池和故障转移支持。

参见 `connection pool`, `Connector/J`, `failover`, `Java`, `JBoss`, `Spring`, `Tomcat`。

**Java**

一种编程语言，结合了高性能、丰富的内置功能和数据类型、面向对象机制、广泛的标准库以及大量可重用的第三方模块。企业开发由许多框架、应用服务器和其他技术支持。其语法对C和C++开发者来说非常熟悉。要使用MySQL编写Java应用程序，可以使用称为`Connector/J`的JDBC驱动程序。

参见 `C`, `Connector/J`, `C++`, `JDBC`。

**JBoss**

参见 `J2EE`。

**JDBC**

`Java Database Connectivity`的缩写，是一个用于从Java应用程序访问数据库的API。编写MySQL应用程序的Java开发人员使用`Connector/J`组件作为他们的JDBC驱动程序。

参见 `API`, `Connector/J`, `J2EE`, `Java`。

**JNDI**

参见 `Java`。

**join**

一种通过引用表中具有相同值的列从多个表中检索数据的查询。理想情况下，这些列是InnoDB外键关系的一部分，以确保参照完整性并对连接列建立索引。在规范化的数据设计中，通常通过用数字ID替换重复的字符串来节省空间并提高查询性能。

参见 `foreign key`, `index`, `normalized`, `query`, `referential integrity`。

## K

**KDC**

参见 `key distribution center`。

**key distribution center**
在`Kerberos`中，密钥分发中心（`key distribution center`，KDC）由一个认证服务器（`authentication server`，AS）和一个票据授予服务器（`ticket-granting server`，TGS）组成。

参见 `authentication server`, `ticket-granting ticket`。

**keystore**

参见 `SSL`。

**KEY_BLOCK_SIZE**

一个选项，用于指定使用压缩行格式的InnoDB表中数据页的大小。默认值为8KB。较低的值有可能会触发依赖于行大小和压缩比例的内部限制。

对于MyISAM表，`KEY_BLOCK_SIZE`可选地指定用于索引键块的大小（以字节为单位）。此值被视为提示；如果需要，可以使用不同的大小。为单个索引定义指定的`KEY_BLOCK_SIZE`值会覆盖表级别的`KEY_BLOCK_SIZE`值。

参见 `compressed row format`。

## L

**latch**

InnoDB使用的一种轻量级结构，用于实现对其内部内存结构的锁定，通常只保持几毫秒或微秒。`latch`是一个泛指术语，包括互斥锁（`mutex`，用于独占访问）和读写锁（`rw-lock`，用于共享访问）。某些`latch`是InnoDB性能调优的重点。可以通过`Performance Schema`接口获取有关`latch`使用和争用的统计信息。

参见 `lock`, `locking`, `mutex`, `Performance Schema`, `rw-lock`。

**libmysql**

`libmysqlclient`库的非正式名称。

参见 `libmysqlclient`。

**libmysqlclient**

库文件，名为`libmysqlclient.a`或`libmysqlclient.so`，通常链接到用C语言编写的客户端程序中。有时非正式地称为`libmysql`或`mysqlclient`库。

参见 `client`, `libmysql`, `mysqlclient`。

**libmysqld**

该嵌入式MySQL服务器库使得在客户端应用程序中运行一个完整功能的MySQL服务器成为可能。主要好处是提高了速度并简化了嵌入式应用程序的管理。您需要链接到`libmysqld`库，而不是`libmysqlclient`。这三个库的API是相同的。

参见 `client`, `embedded`, `libmysql`, `libmysqlclient`。

**lifecycle interceptor**

`Connector/J`支持的一种拦截器类型。它涉及实现接口`com.mysql.jdbc.ConnectionLifecycleInterceptor`。

参见 `Connector/J`, `interceptor`。

**list**

InnoDB缓冲池表示为内存页的列表。当新页被访问并进入缓冲池时，缓冲池中的页再次被访问并被视为更新页时，以及长时间未访问的页从缓冲池中被逐出时，该列表会重新排序。缓冲池被划分为子列表，替换策略是熟悉的`LRU`（最近最少使用）技术的变体。

参见 `buffer pool`, `eviction`, `LRU`, `page`, `sublist`。

**load balancing**

一种通过将查询请求发送到复制或集群配置中的不同从服务器来扩展只读连接的技术。在`Connector/J`中，负载均衡通过类`com.mysql.jdbc.ReplicationDriver`启用，并通过配置属性`loadBalanceStrategy`进行控制。

参见 `Connector/J`, `J2EE`。

**localhost**

参见 `connection`。

**lock**

控制对资源（如表、行或内部数据结构）的访问的对象的高级概念，作为锁定策略的一部分。对于深入的性能调优，您可能需要研究实现锁的实际结构，如`mutex`和`latch`。

参见 `latch`, `lock mode`, `locking`, `mutex`。

**lock escalation**

某些数据库系统中使用的一种操作，将多个行锁转换为单个表锁，从而节省内存空间，但降低对表的并发访问能力。InnoDB使用空间效率高的行锁表示，因此不需要锁升级。

参见 `locking`, `row lock`, `table lock`。

**lock mode**

共享（`S`）锁允许事务读取一行。多个事务可以同时在同一行上获取`S`锁。

排他（`X`）锁允许事务更新或删除一行。在同一时间内，其他任何事务都不能在同一行上获取任何种类的锁。

意图锁适用于表，用于指示事务打算在表中的行上获取的锁类型。不同的事务可以在同一表上获取不同类型的意图锁，但第一个在表上获取意图排他锁（`IX`）的事务会阻止其他事务在该表上获取任何`S`或`X`锁。相反，第一个在表上获取意图共享锁（`IS`）的事务会阻止其他事务在该表上获取任何`X`锁。两阶段过程允许按顺序解决锁请求，而不会阻止兼容的锁及相应操作。

参见 `intention lock`, `lock`, `locking`, `transaction`。

**locking**

保护一个事务不被其他事务查看或更改正在查询或更改的数据的系统。锁定策略必须在数据库操作的可靠性和一致性（`ACID`哲学的原则）与良好并发性所需的性能之间找到平衡。锁定策略的微调通常涉及选择隔离级别并确保所有数据库操作在该隔离级别下是安全可靠的。

参见 `ACID`, `concurrency`, `isolation level`, `locking`, `transaction`。

**locking read**

在InnoDB表上执行锁定操作的`SELECT`语句。包括`SELECT ... FOR UPDATE`或`SELECT ... LOCK IN SHARE MODE`。它有可能产生死锁，具体取决于事务的隔离级别。与非锁定读取相反。不允许在只读事务中对全局表执行锁定读取。

从MySQL 8.0.1开始，`SELECT ... FOR SHARE`替代了`SELECT ... LOCK IN SHARE MODE`，但后者仍然可用以保持向后兼容性。

有关详细信息，请参见[17.7.2.4节 “Locking Reads”](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html)。

参见 `deadlock`, `isolation level`, `locking`, `non-locking read`, `read-only transaction`。

**log**

在InnoDB上下文中，`log`或`log files`通常指的是由`ib_logfileN`文件表示的重做日志。另一种InnoDB日志是`undo log`，它是一个存储区，用于保存活动事务修改的数据副本。

在MySQL中，其他重要的日志包括`error log`（用于诊断启动和运行时问题）、`binary log`（用于复制和执行时间点恢复）、`general query log`（用于诊断应用程序问题）和`slow query log`（用于诊断性能问题）。

参见 `binary log`, `error log`, `general query log`, `ib_logfile`, `redo log`, `slow query log`, `undo log`。

**log buffer**

用于保存要写入组成重做日志的日志文件的数据的内存区域。它由`innodb_log_buffer_size`配置选项控制。

参见 `log file`, `redo log`。

**log file**

组成重做日志的`ib_logfileN`文件之一。数据从日志缓冲区内存区域写入这些文件。

参见 `ib_logfile`, `log buffer`, `redo log`。

**log group**

组成重做日志的一组文件，通常命名为`ib_logfile0`和`ib_logfile1`。（因此，有时统称为`ib_logfile`。）

参见 `ib_logfile`, `redo log`。

**logical**

涉及高级抽象方面的操作类型，例如表、查询、索引和其他SQL概念。通常，逻辑方面对于使数据库管理和应用程序开发方便和可用至关重要。与物理层相对。

参见 `logical backup`, `physical`。

**logical backup**

在不复制实际数据文件的情况下再现表结构和数据的备份。例如，`mysqldump`命令生成逻辑备份，因为其输出包含`CREATE TABLE`和`INSERT`语句，可以重新创建数据。与物理备份相对。逻辑备份提供灵活性（例如，可以在恢复之前编辑表定义或插入语句），但恢复时间可能比物理备份长得多。

参见 `backup`, `mysqldump`, `physical backup`, `restore`。

**loose_**

在服务器启动后添加到InnoDB配置选项的前缀，因此任何未被当前MySQL版本识别的新配置选项不会导致启动失败。MySQL处理以此前缀开头的配置选项，但如果前缀后的部分不是已识别的选项，则会发出警告而不是失败。

参见 `startup`。

**low-water mark**

表示下限的值，通常是指某种纠正行为开始或变得更积极的阈值。与高水位线相对。

参见 `high-water mark`。

**LRU**

`least recently used`的缩写，一种管理存储区域的常见方法。当需要缓存较新项目时，最近未使用的项目将被驱逐。InnoDB默认使用`LRU`机制管理缓冲池中的页，但在某些情况下会做例外，例如在全表扫描期间可能只读一次的页。此`LRU`算法的变体称为中点插入策略。有关更多信息，请参见[17.5.1节 “Buffer Pool”](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html)。

参见 `buffer pool`, `eviction`, `full table scan`, `midpoint insertion strategy`, `page`。

**LSN**

`log sequence number`的缩写。此任意、不断增加的值表示与重做日志中记录的操作对应的时间点。（此时间点与事务边界无关；它可能位于一个或多个事务的中间。）InnoDB在崩溃恢复期间以及管理缓冲池时内部使用它。

在MySQL 5.6.3之前，`LSN`是一个4字节的无符号整数。在MySQL 5.6.3中，`LSN`成为8字节的无符号整数，重做日志文件大小限制从4GB增加到512GB，因为需要额外的字节来存储额外的大小信息。在MySQL 5.6.3或更高版本上构建的应用程序如果使用`LSN`值，应使用64位而不是32位变量来存储和比较`LSN`值。

在`MySQL Enterprise Backup`产品中，可以指定`LSN`来表示从何时开始进行增量备份。相关的`LSN`由`mysqlbackup`命令的输出显示。一旦您获得与全备份时间相对应的`LSN`值，就可以指定该值以进行后续增量备份，其输出包含下一个增量备份的`LSN`。

参见 `buffer pool`, `crash recovery`, `incremental backup`, `MySQL Enterprise Backup`, `redo log`, `transaction`。

**LTS Series**

具有相同主要版本号的`LTS`发布版形成一个`LTS`系列。例如，所有MySQL 8.4.x版本形成MySQL 8.4 LTS系列。

注意：MySQL 8.0是一个在LTS发布模型之前的错误修复系列。

参见 `Innovation Series`。

## M

**.MRG file**

包含对其他表引用的文件，由`MERGE`存储引擎使用。具有此扩展名的文件始终包含在由MySQL企业备份产品的`mysqlbackup`命令生成的备份中。

参见 `MySQL Enterprise Backup`, `mysqlbackup command`。

**.MYD file**

MySQL用于存储`MyISAM`表数据的文件。

参见 `.MYI file`, `MySQL Enterprise Backup`, `mysqlbackup command`。

**.MYI file**

MySQL用于存储`MyISAM`表索引的文件。

参见 `.MYD file`, `MySQL Enterprise Backup`, `mysqlbackup command`。

**master**

参见 `source`。

**master thread**

InnoDB中的一个线程，执行各种后台任务。这些任务大多数与I/O相关，例如将`change buffer`中的更改写入相应的二级索引。

为了提高并发性，有时操作会从`master thread`转移到单独的后台线程。例如，在MySQL 5.6及更高版本中，脏页由`page cleaner thread`而不是`master thread`从缓冲池中刷出。

参见 `buffer pool`, `change buffer`, `concurrency`, `dirty page`, `flush`, `page cleaner`, `thread`。

**MDL**

“metadata lock”（元数据锁）的缩写。

参见 `metadata lock`。

**medium trust**

“partial trust”（部分信任）的同义词。由于信任设置范围广泛，优先使用“部分信任”一词，以避免暗示只有三个级别（低、中和完全信任）。

参见 `Connector/NET`, `partial trust`。

**memcached**

许多MySQL和NoSQL软件栈中的一个流行组件，允许对单个值进行快速读写，并将结果完全缓存于内存中。传统上，应用程序需要额外的逻辑来将相同的数据写入MySQL数据库以进行永久存储，或者当数据尚未缓存于内存中时从MySQL数据库读取数据。现在，应用程序可以使用简单的`memcached`协议，借助许多语言的客户端库，直接与使用`InnoDB`或`NDB`表的MySQL服务器通信。这些NoSQL接口使得应用程序可以实现比直接发出SQL语句更高的读写性能，并简化了已经使用`memcached`进行内存缓存的系统的应用程序逻辑和部署配置。

参见 `NoSQL`。

**merge**

将缓存于内存中的数据进行合并，例如当某页被引入缓冲池时，将`change buffer`中记录的任何适用更改合并到缓冲池中的页。更新后的数据最终通过刷出机制写入表空间。

参见 `buffer pool`, `change buffer`, `flush`, `tablespace`。

**metadata lock**

一种锁，防止在另一个事务同时使用表时对其进行DDL操作。详情见[10.11.4节 “Metadata Locking”](https://dev.mysql.com/doc/refman/8.0/en/metadata-locking.html)。

在线操作的增强功能，特别是在MySQL 5.6及更高版本中，专注于减少元数据锁定的数量。目标是在不更改表结构的DDL操作（例如InnoDB表的`CREATE INDEX`和`DROP INDEX`）在表被其他事务查询、更新等时仍能进行。

参见 `DDL`, `lock`, `online`, `transaction`。

**metrics counter**

在MySQL 5.6及更高版本中，由`INNODB_METRICS`表在`INFORMATION_SCHEMA`中实现的一个功能。您可以查询低级别InnoDB操作的计数和总数，并将结果与`Performance Schema`中的数据结合使用，以进行性能调优。

参见 `counter`, `INFORMATION_SCHEMA`, `Performance Schema`。

**midpoint insertion strategy**

一种技术，在InnoDB缓冲池中引入页时，不是将其放在列表的“最新”端，而是放在列表的中间某个位置。此点的确切位置可以根据`innodb_old_blocks_pct`选项的设置而变化。其目的是让只读一次的页，例如在全表扫描期间，可以比严格的`LRU`算法更快地从缓冲池中淘汰。有关更多信息，请参见[17.5.1节 “Buffer Pool”](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html)。

参见 `buffer pool`, `full table scan`, `LRU`, `page`。

**mini-transaction**

InnoDB处理中的一个内部阶段，在DML操作期间对内部数据结构进行物理级别更改时发生。迷你事务（`mtr`）没有回滚的概念；在单个事务中可以发生多个迷你事务。迷你事务将信息写入重做日志，该信息在崩溃恢复期间使用。迷你事务也可以在常规事务之外发生，例如在后台线程进行清除处理时。

参见 `commit`, `crash recovery`, `DML`, `physical`, `purge`, `redo log`, `rollback`, `transaction`。

**mixed-mode insert**

一种`INSERT`语句，其中为某些但不是所有新行指定了自增值。例如，多值插入语句可能在某些情况下为自增列指定值，而在其他情况下为其指定`NULL`。InnoDB为列值指定为`NULL`的行生成自增值。另一个示例是`INSERT ... ON DUPLICATE KEY UPDATE`语句，在处理为更新而非插入的任何重复行时，可能生成但不使用自增值。

在复制配置中，可能导致源服务器和副本服务器之间的一致性问题。可能需要调整`innodb_autoinc_lock_mode`配置选项的值。

参见 `auto-increment`, `innodb_autoinc_lock_mode`, `replica`, `replication`, `source`。

**MM.MySQL**

MySQL的一个较老的JDBC驱动程序，后来与MySQL产品整合为`Connector/J`。

参见 `Connector/J`。

**Mono**

由Novell开发的开源框架，适用于Linux平台上的`Connector/NET`和`C#`应用程序。

参见 `Connector/NET`, `C#`。

**mtr**

参见 `mini-transaction`。

**multi-core**

一种处理器类型，能够利用多线程程序，如MySQL服务器。

**multiversion concurrency control**
参见 `MVCC`。

**mutex**

“`mutex variable`”（互斥变量）的非正式缩写。`mutex`本身是“`mutual exclusion`”（互斥）的缩写。InnoDB用于表示和强制执行对内部内存数据结构的独占访问锁的低级对象。一旦获取了锁，任何其他进程、线程等都无法获取相同的锁。与`rw-locks`（读写锁）相对，后者用于表示和强制执行对内部内存数据结构的共享访问锁。`mutexes`和`rw-locks`统称为`latches`。

参见 `latch`, `lock`, `Performance Schema`, `Pthreads`, `rw-lock`。

**MVCC**

`multiversion concurrency control`（多版本并发控制）的缩写。此技术允许具有特定隔离级别的InnoDB事务执行一致读取操作；即查询由其他事务更新的行，并查看这些更新发生之前的值。通过允许查询在不因其他事务持有的锁而等待的情况下继续执行，这是一种强大的并发性提升技术。

这种技术在数据库领域并不普遍。某些其他数据库产品以及某些MySQL存储引擎不支持它。

参见 `ACID`, `concurrency`, `consistent read`, `isolation level`, `lock`, `transaction`。

**my.cnf**

在Unix或Linux系统上，MySQL选项文件的名称。

参见 `my.ini`, `option file`。

**my.ini**

在Windows系统上，MySQL选项文件的名称。

参见 `my.cnf`, `option file`。

**MyODBC drivers**

`Connector/ODBC`的旧名称。

参见 `Connector/ODBC`。

**mysql**

`mysql`程序是MySQL数据库的命令行解释器。它通过将请求传递给`mysqld`守护进程来处理SQL语句以及MySQL特定命令，例如`SHOW TABLES`。

参见 `mysqld`, `SQL`。

**MySQL Enterprise Backup**

一种授权产品，用于执行MySQL数据库的热备份。在备份`InnoDB`表时，它提供了最高的效率和灵活性，但也可以备份`MyISAM`和其他类型的表。

参见 `hot backup`, `InnoDB`。

**mysqlbackup command**

MySQL企业备份产品的命令行工具。它为`InnoDB`表执行热备份操作，并为`MyISAM`和其他类型的

表执行暖备份操作。有关此命令的更多信息，请参见[32.1节 “MySQL Enterprise Backup Overview”](https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysql-enterprise-backup.html)。

参见 `hot backup`, `MySQL Enterprise Backup`, `warm backup`。

**mysqlclient**

由文件`libmysqlclient`实现的库的非正式名称，扩展名为`.a`或`.so`。

参见 `libmysqlclient`。

**mysqld**

`mysqld`也称为MySQL服务器，是一个单一的多线程程序，在MySQL安装中执行大部分工作。它不产生额外的进程。MySQL服务器管理对包含数据库、表及其他信息（如日志文件和状态文件）的MySQL数据目录的访问。

`mysqld`作为Unix守护进程或Windows服务运行，持续等待请求并在后台执行维护工作。

参见 `instance`, `mysql`。

**MySQLdb**

形成MySQL Python API基础的开源Python模块的名称。

参见 `Python`, `Python API`。

**mysqldump**

执行逻辑备份的命令，备份可以是数据库、表或表数据的任意组合。结果是SQL语句，可用于重新创建原始模式对象、数据或两者。如果是大量数据，物理备份解决方案（例如MySQL企业备份）速度更快，特别是在恢复操作方面。

参见 `logical backup`, `MySQL Enterprise Backup`, `physical backup`, `restore`。

## N

**.NET**

参见 `ADO.NET`, `ASP.net`, `Connector/NET`, `Mono`, `Visual Studio`。

**native C API**

`libmysqlclient`的同义词。

参见 `libmysql`。

**natural key**

一种具有实际意义的索引列，通常作为主键。通常不建议使用自然键，原因如下：

- 如果值发生变化，可能需要大量的索引维护以重新排序聚簇索引并更新每个二级索引中重复的主键值。
- 即使看似稳定的值也可能以不可预测的方式更改，这在数据库中难以正确表示。例如，一个国家可以分裂成两个或多个，导致原来的国家代码失效。或者，唯一值的规则可能会有例外。例如，即使纳税人ID旨在唯一对应一个人，数据库也可能需要处理违反此规则的记录，例如身份盗窃的情况。纳税人ID和其他敏感ID号也不适合作为主键，因为它们可能需要加密和以不同于其他列的方式处理。

因此，通常更好的做法是使用任意的数值来形成合成键，例如使用自增列。

参见 `auto-increment`, `clustered index`, `primary key`, `secondary index`, `synthetic key`。

**neighbor page**

与特定页在同一`extent`中的任何页。当选择一个页进行刷出时，通常也会刷出任何脏的邻页，作为传统硬盘的I/O优化。在MySQL 5.6及更高版本中，此行为可以通过配置变量`innodb_flush_neighbors`进行控制；对于没有相同随机位置写入开销的`SSD`驱动器，您可能会关闭此设置。

参见 `dirty page`, `extent`, `flush`, `page`。

**next-key lock**

一种锁，结合了索引记录上的记录锁和索引记录前的间隙锁。

参见 `gap lock`, `locking`, `record lock`。

**non-locking read**

不使用`SELECT ... FOR UPDATE`或`SELECT ... LOCK IN SHARE MODE`子句的查询。它是只读事务中允许对全局表执行的唯一查询类型，是锁定读取的对立面。参见[17.7.2.3节 “Consistent Nonlocking Reads”](https://dev.mysql.com/doc/refman/8.0/en/innodb-consistent-read.html)。

在MySQL 8.0.1中，`SELECT ... FOR SHARE`取代了`SELECT ... LOCK IN SHARE MODE`，但后者仍可用于向后兼容。

参见 `locking read`, `query`, `read-only transaction`。

**non-repeatable read**

在查询检索数据后，同一事务中的后续查询检索应为相同的数据，但由于其他事务在此期间提交的更改，查询返回不同的结果。

这种操作违反了数据库设计的`ACID`原则。在一个事务内，数据应该是一致的，并且关系应该是可预测和稳定的。

在不同的隔离级别中，`serializable read`和`repeatable read`级别可以防止不可重复读取，而一致读取（`consistent read`）和读未提交（`read uncommitted`）级别允许这种情况发生。

参见 `ACID`, `consistent read`, `isolation level`, `READ UNCOMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`, `transaction`。

**nonblocking I/O**

行业术语，与`asynchronous I/O`（异步I/O）同义。

参见 `asynchronous I/O`。

**normalized**

一种数据库设计策略，通过将数据拆分为多个表并将重复值压缩为由ID表示的单行，避免存储、查询和更新冗余或冗长的值。通常用于`OLTP`应用程序。

例如，可能为地址分配一个唯一ID，这样在人口普查数据库中可以通过将此ID与家庭中的每个成员关联来表示居住在此地址的关系，而不是存储如“123 Main Street, Anytown, USA”这样的复杂值的多个副本。

再比如，虽然简单的地址簿应用程序可能将每个电话号码与一个人的姓名和地址存储在同一个表中，但电话公司数据库可能会为每个电话号码分配一个特殊的ID，并将这些号码和ID存储在一个单独的表中。这种规范化的表示可以在区号分裂时简化大规模更新。

并非总是推荐使用规范化。主要以查询为主且仅通过删除和重新加载进行更新的数据通常保持在较少且更大的表中，包含冗余的重复值副本。这种数据表示称为非规范化，通常出现在数据仓库应用程序中。

参见 `denormalized`, `foreign key`, `OLTP`, `relational`。

**NoSQL**

用于一组不以`SQL`语言作为主要数据读写机制的数据访问技术的广义术语。某些`NoSQL`技术仅作为键值存储，仅接受单值读取和写入；有些则放宽了`ACID`方法论的限制；还有一些不需要预先规划的模式。MySQL用户可以通过使用`memcached API`直接访问某些MySQL表，将`NoSQL`风格的处理速度和简单性与`SQL`操作的灵活性和便利性相结合。

参见 `ACID`, `memcached`, `schema`, `SQL`。

**NOT NULL constraint**

一种约束，指定列不能包含任何`NULL`值。它有助于维护引用完整性，因为数据库服务器可以识别具有错误缺失值的数据。它还通过允许优化器预测索引中条目的数量，有助于查询优化中的算术运算。

参见 `column`, `constraint`, `NULL`, `primary key`, `referential integrity`。

**NULL**

`SQL`中的一个特殊值，表示数据缺失。任何涉及`NULL`值的算术操作或相等性测试都会生成`NULL`结果。（因此它类似于IEEE浮点概念中的`NaN`，即“非数字”）。任何汇总计算（如`AVG()`）在确定除以的行数时会忽略具有`NULL`值的行。唯一可以与`NULL`值一起使用的测试是使用`SQL`惯用语`IS NULL`或`IS NOT NULL`。

`NULL`值在索引操作中起到了一定作用，因为数据库必须尽量减少跟踪缺失数据值的开销。通常，`NULL`值不会存储在索引中，因为使用标准比较运算符测试索引列的查询永远不可能匹配具有`NULL`值的行。因此，唯一索引不会阻止`NULL`值；这些值根本不会在索引中表示。为列声明`NOT NULL constraint`提供了没有行被排除在索引之外的保证，从而允许更好的查询优化（准确计数行数并估算是否使用索引）。

由于主键必须能够唯一标识表中的每一行，单列主键不能包含任何`NULL`值，而多列主键不能包含在所有列中都为`NULL`值的行。

虽然`Oracle`数据库允许`NULL`值与字符串连接，但`InnoDB`将此类操作的结果视为`NULL`。

参见 `index`, `primary key`, `SQL`。

## O

**.OPT file**

包含数据库配置信息的文件。具有此扩展名的文件会包含在由 MySQL Enterprise Backup 产品的 `mysqlbackup` 命令生成的备份中。

参见 `MySQL Enterprise Backup`, `mysqlbackup command`。

**ODBC**

`Open Database Connectivity` 的缩写，一种行业标准的API。通常用于基于 Windows 的服务器，或需要通过`ODBC`与 MySQL 通信的应用程序。MySQL 的 ODBC 驱动程序称为 `Connector/ODBC`。

参见 `Connector/ODBC`。

**off-page column**

包含变长数据（如 `BLOB` 和 `VARCHAR`）的列，这些数据长度过长，无法放入 `B-tree` 页中。数据存储在溢出页中。`DYNAMIC` 行格式比旧的 `COMPACT` 行格式在此类存储中更为高效。

参见 `B-tree`, `compact row format`, `dynamic row format`, `overflow page`。

**OLTP**

“`Online Transaction Processing`”的缩写。用于处理大量事务的数据库系统或应用程序，通常涉及频繁的写入和读取，每次操作的数据量较少。例如，航空公司预订系统或处理银行存款的应用程序。数据可能以规范化形式组织，以在`DML`（插入/更新/删除）效率和查询效率之间取得平衡。与数据仓库形成对比。

由于其行级锁定和事务能力，`InnoDB`是用于`OLTP`应用程序的 MySQL 表的理想存储引擎。

参见 `data warehouse`, `DML`, `InnoDB`, `query`, `row lock`, `transaction`。

**online**

涉及数据库无停机、无阻塞或无限制操作的操作类型。通常应用于 `DDL`。缩短受限操作期间的操作（如快速索引创建）已在 MySQL 5.6 中演变为更广泛的在线`DDL`操作集。

在备份上下文中，热备份是一种在线操作，暖备份部分是在线操作。

参见 `DDL`, `Fast Index Creation`, `hot backup`, `online DDL`, `warm backup`。

**online DDL**

一种在 `DDL`（主要是 `ALTER TABLE`）操作期间提高 `InnoDB`表的性能、并发性和可用性的功能。详细信息参见[17.12节 “InnoDB and Online DDL”](https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl.html)。

具体操作方式根据操作类型而异。在某些情况下，可以在 `ALTER TABLE`进行时同时修改表。操作可能无需复制表，或者使用特别优化的表复制类型。就地操作的 `DML` 日志空间使用量由配置选项`innodb_online_alter_log_max_size`控制。

该功能是 MySQL 5.5 中快速索引创建功能的增强版。

参见 `DDL`, `Fast Index Creation`, `online`。

**optimistic**

指导关系数据库系统低级实现决策的方法论。关系数据库的性能和并发性要求操作必须快速启动或分派。而一致性和引用完整性的要求意味着任何操作都可能失败：事务可能被回滚，`DML`操作可能违反约束，请求锁可能导致死锁，网络错误可能导致超时。乐观策略假设大多数请求或尝试会成功，因此为失败情况做的准备工作相对较少。当这种假设成立时，数据库几乎不会做多余的工作；当请求失败时，必须做额外的工作来清理和撤销更改。

`InnoDB`在锁定和提交等操作中使用乐观策略。例如，事务更改的数据可以在提交之前写入数据文件，从而使提交本身非常快，但如果事务被回滚，则需要更多工作来撤销更改。

乐观策略的对立面是悲观策略，其中系统针对不可靠且频繁失败的操作进行优化。这种方法论在数据库系统中很少见，因为要非常仔细地选择可靠的硬件、网络和算法。

参见 `commit`, `concurrency`, `DML`, `locking`, `pessimistic`, `referential integrity`。

**optimizer**

MySQL 组件，确定查询中使用的最佳索引和连接顺序，基于相关表的特征和数据分布。

参见 `index`, `join`, `query`, `table`。

**option**

MySQL 的配置参数，可以存储在配置文件中或通过命令行传递。

对于适用于`InnoDB`表的选项，每个选项名称都以前缀`innodb_`开头。

参见 `InnoDB`, `option`, `option file`。

**option file**

存储 MySQL 实例配置选项的文件。传统上，在 Linux 和 Unix 上该文件名为 `my.cnf`，在 Windows 上则为 `my.ini`。

参见 `configuration file`, `my.cnf`, `my.ini`, `option`。

**overflow page**

分配给包含变长列（如`BLOB`和`VARCHAR`）的磁盘页，这些列太长，无法放入`B-tree`页中。关联的列称为页外列。

参见 `B-tree`, `off-page column`, `page`。

## P

**.par file**

包含分区定义的文件。在由 MySQL Enterprise Backup 产品的 `mysqlbackup` 命令生成的备份中，会包含具有此扩展名的文件。

自 MySQL 5.7.6 引入对 InnoDB 表的原生分区支持后，不再为分区 InnoDB 表创建 `.par` 文件。在 MySQL 5.7 中，分区 MyISAM 表仍使用 `.par` 文件。在 MySQL 8.0 中，分区支持仅由 InnoDB 存储引擎提供，因此从 MySQL 8.0 开始，不再使用 `.par` 文件。

参见 `MySQL Enterprise Backup`, `mysqlbackup command`。

**page**

表示 InnoDB 在任何时候在磁盘（数据文件）和内存（缓冲池）之间传输的数据量的单位。一个页可以包含一行或多行，具体取决于每行中的数据量。如果一行无法完全放入单个页中，InnoDB 会设置额外的指针式数据结构，以便在一个页中存储关于该行的信息。

一种在每页中容纳更多数据的方法是使用压缩行格式。对于使用 BLOB 或大文本字段的表，紧凑行格式允许将这些大列与行的其余部分分开存储，从而减少 I/O 开销并减少对不引用这些列的查询的内存使用。

当 InnoDB 以批处理方式读取或写入页集以提高 I/O 吞吐量时，它一次读取或写入一个区间。

一个 MySQL 实例中的所有 InnoDB 磁盘数据结构共享相同的页大小。

参见 `buffer pool`, `compact row format`, `compressed row format`, `data files`, `extent`, `page size`, `row`。

**page cleaner**

一个 InnoDB 后台线程，用于从缓冲池中刷新脏页。在 MySQL 5.6 之前，此活动由主线程执行。页清理线程的数量由在 MySQL 5.7.4 中引入的配置选项 `innodb_page_cleaners` 控制。

参见 `buffer pool`, `dirty page`, `flush`, `master thread`, `thread`。

**page size**

在 MySQL 5.5 及以前的版本中，每个 InnoDB 页的大小固定为 16 KB。这一值代表了平衡：足够大以容纳大多数行的数据，同时足够小以尽量减少将不需要的数据传输到内存的性能开销。不支持其他值。

从 MySQL 5.6 开始，InnoDB 实例的页大小可以为 4KB、8KB 或 16KB，由 `innodb_page_size` 配置选项控制。从 MySQL 5.7.6 开始，InnoDB 还支持 32KB 和 64KB 页大小。对于 32KB 和 64KB 页大小，不支持 `ROW_FORMAT=COMPRESSED`，且最大记录大小为 16KB。

页大小在创建 MySQL 实例时设置，之后保持不变。相同的页大小适用于所有 InnoDB 表空间，包括系统表空间、file-per-table 表空间和常规表空间。

对于使用小块大小的存储设备（特别是用于磁盘绑定工作负载的 SSD 设备，例如 OLTP 应用程序），较小的页大小有助于提高性能。随着单个行的更新，复制到内存、写入磁盘、重新组织、锁定等的数据量较少。

参见 `disk-bound`, `file-per-table`, `general tablespace`, `instance`, `OLTP`, `page`, `SSD`, `system tablespace`, `tablespace`。

**parent table**

在外键关系中，持有初始列值的表，这些值来自子表的引用。根据外键定义中的 `ON UPDATE` 和 `ON DELETE` 子句，对父表中行的删除或更新的后果有所不同。子表中具有相应值的行可能会自动被删除或更新，或这些列可能会被设置为 `NULL`，或者操作可能会被阻止。

参见 `child table`, `foreign key`。

**partial backup**

包含 MySQL 数据库中部分表或 MySQL 实例中部分数据库的备份。与完全备份形成对比。

参见 `backup`, `full backup`, `table`。

**partial index**

仅表示部分列值的索引，通常是长 `VARCHAR` 值的前 N 个字符（前缀）。

参见 `index`, `index prefix`。

**partial trust**

托管服务提供商通常使用的执行环境，其中应用程序具有某些权限但没有其他权限。例如，应用程序可能能够通过网络访问数据库服务器，但在读取和写入本地文件方面处于“沙盒”环境中。

参见 `Connector/NET`。

**Performance Schema**

MySQL 5.5 及更高版本中的 `performance_schema` 模式，提供了一组可以查询的表，用以获取有关 MySQL 服务器内部许多部分性能特征的详细信息。参见 [第 29 章, “MySQL Performance Schema”](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html)。

参见 `INFORMATION_SCHEMA`, `latch`, `mutex`, `rw-lock`。

**Perl**

一种编程语言，起源于 Unix 脚本和报告生成。结合了高性能正则表达式和文件 I/O。通过类似 `CPAN` 的仓库可以获取大量可重用模块。

参见 `Perl API`。

**Perl API**

一种用于编写 Perl 语言的 MySQL 应用程序的开源 API。通过 `DBI` 和 `DBD::mysql` 模块实现。详情请参见[31.9节 “MySQL Perl API”](https://dev.mysql.com/doc/refman/8.0/en/apis-interfaces.html)。

参见 `API`, `Perl`。

**persistent statistics**

一种将 InnoDB 表的索引统计信息存储在磁盘上的功能，从而为查询提供更好的计划稳定性。详情请参见[17.8.10.1节 “配置持久化优化器统计参数”](https://dev.mysql.com/doc/refman/8.0/en/innodb-persistent-stats.html)。

参见 `index`, `optimizer`, `plan stability`, `query`, `table`。

**pessimistic**

一种为了安全性而牺牲性能或并发性的策略。当大比例的请求或尝试可能会失败，或失败请求的后果严重时，这种策略是合适的。`InnoDB` 使用称为悲观锁定的策略，以最大限度地减少死锁的可能性。在应用程序级别，您可以通过在事务开始时获得所需的所有锁来避免死锁。

许多内置的数据库机制使用相反的乐观策略。

参见 `deadlock`, `locking`, `optimistic`。

**phantom**

在查询结果集中出现的行，但不在早期查询的结果集中。例如，如果在事务内运行两次查询，而在此期间，另一个事务在插入新行或更新行后提交，以使其与查询的 `WHERE` 子句匹配。

这种现象称为幻读。比不可重复读更难防范，因为锁定第一次查询结果集中的所有行并不能阻止导致幻影出现的更改。

在不同的隔离级别中，幻读被可串行化读级别阻止，而在可重复读、一致读和未提交读级别中允许。

参见 `consistent read`, `isolation level`, `non-repeatable read`, `READ UNCOMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`, `transaction`。

**PHP**

一种起源于 web 应用程序的编程语言。代码通常作为块嵌入到网页源代码中，并在网页由 web 服务器传输时将输出替换到页面中。这与生成整个网页的应用程序（如 `CGI` 脚本）形成对比。`PHP` 编码风格用于高度交互和动态的网页。现代 `PHP` 程序也可以作为命令行或 `GUI` 应用程序运行。

MySQL 应用程序使用 `PHP API` 之一编写。可重用模块可以用 `C` 语言编写，并从 `PHP` 中调用。

另一种使用 MySQL 编写服务器端网页的技术是 `ASP.net`。

参见 `ASP.net`, `C`, `PHP API`。

**PHP API**

有几种 API 可用于用 PHP 语言编写 MySQL 应用程序：原始 MySQL API (`Mysql`)、MySQL Improved Extension (`Mysqli`)、MySQL Native Driver (`Mysqlnd`)、MySQL 函数 (`PDO_MYSQL`) 和 `Connector/PHP`。详情请参见 [MySQL and PHP](https://dev.mysql.com/doc/refman/8.0/en/apis-interfaces.html)。

参见 `API`, `PHP`。

**physical**

一种涉及硬件相关方面（如磁盘块、内存页、文件、位、磁盘读取等）的操作类型。通常，物理方面在专家级性能调优和问题诊断中很重要。与逻辑形成对比。

参见 `logical`, `physical backup`。

**physical backup**

一种复制实际数据文件的备份。例如，MySQL Enterprise Backup 产品的 `mysqlbackup` 命令生成物理备份，因为其输出包含可由 `mysqld` 服务器直接使用的数据文件，从而使恢复操作更快。与逻辑备份形成对比。

参见 `backup`, `logical backup`, `MySQL Enterprise Backup`, `restore`。

**PITR**

`point-in-time recovery` 的缩写。

参见 `point-in-time recovery`。

**plan stability**

查询执行计划的属性，优化器为给定查询每次做出的选择相同，从而性能一致且可预测。

参见 `query`, `query execution plan`。

**point-in-time recovery**

将备份恢复到特定日期和时间以重新创建数据库状态的过程。通常缩写为`PITR`。由于指定时间不太可能与备份时间完全一致，因此通常需要物理备份和逻辑备份的组合来实现此技术。例如，使用 MySQL Enterprise Backup 产品，可以恢复在指定时间之前拍摄的最后一次备份，然后重播二进制日志中的更改，直到 `PITR` 时间。

参见 `backup`, `binary log`, `logical backup`, `MySQL Enterprise Backup`, `physical backup`。

**port**

数据库服务器监听的 TCP/IP 套接字的端口号，用于建立连接。通常与主机一起指定。根据网络加密的使用情况，可能有一个端口用于未加密流量，另一个端口用于 `SSL` 连接。

参见 `connection`, `host`, `SSL`。

**prefix**

参见 `index prefix`。

**prepared backup**

由 MySQL Enterprise Backup 产品在应用所有二进制日志和增量备份的步骤完成后生成的备份文件集。生成的文件已准备好恢复。在应用步骤之前，这些文件称为 `raw backup`。

参见 `binary log`, `hot backup`, `incremental backup`, `MySQL Enterprise Backup`, `raw backup`, `restore`。

**prepared statement**

一种提前分析以确定高效执行计划的 SQL 语句。可以多次执行，而无需每次解析和分析的开销。通过使用占位符，可以为 `WHERE` 子句中的字面量每次替换不同的值。此替换技术提高了安全性，防止某些类型的 `SQL` 注入攻击。您还可以减少将返回值转换并复制到程序变量的开销。

尽管可以通过 SQL 语法直接使用预处理语句，但各种连接器都有用于操作预处理语句的编程接口，这些 API 比通过 SQL 更高效。

参见 `client-side prepared statement`, `connector`, `server-side prepared statement`。

**primary key**

能够唯一标识表中每一行的一组列，以及基于该组列的索引。因此，它必须是一个不包含任何 `NULL` 值的唯一索引。

`InnoDB` 要求每个表都具有这样的索引（也称为聚簇索引或聚集索引），并根据主键的列值组织表存储。

选择主键值时，请考虑使用任意值（合成键），而不是依赖于其他来源派生的值（自然键）。

参见 `clustered index`, `index`, `natural key`, `synthetic key`。

**principal**

Kerberos 术语中，表示命名实体，如用户或服务器。

参见 `service principal name`, `user principal name`。

**process**

正在执行的程序实例。操作系统在多个正在运行的进程之间切换，允许一定程度的并发性。在大多数操作系统上，进程可以包含共享资源的多个执行线程。在线程之间的上下文切换比进程之间的切换要快。

参见 `concurrency`, `thread`。

**pseudo-record**

索引中的一个人工记录，用于锁定当前不存在的键值或范围。

参见 `infimum record`, `locking`, `supremum record`。

**Pthreads**

POSIX 线程标准，定义了在 Unix 和 Linux 系统上用于线程和锁操作的 API。在 Unix 和 Linux 系统上，InnoDB 使用该实现来管理 `mutexes`。

参见 `mutex`。

**purge**

由一个或多个单独的后台线程（由 `innodb_purge_threads` 控制）执行的垃圾收集类型，按周期计划运行。`Purge` 解析并处理来自历史列表的撤销日志页，以删除标记为删除且不再用于 `MVCC` 或回滚的聚簇和二级索引记录。处理后，`Purge` 释放历史列表中的撤销日志页。

参见 `history list`, `MVCC`, `rollback`, `undo log`。

**purge buffering**

将由于 `DELETE` 操作导致的二级索引页的更改存储在更改缓冲区中，而不是立即写入更改，以便可以执行物理写入，以最小化随机 `I/O`。由于删除操作是一个两步过程，此操作缓冲了通常清除先前标记为删除的索引记录的写操作。这是更改缓冲的类型之一；其他的是插入缓冲和删除缓冲。

参见 `change buffer`, `change buffering`, `delete buffering`, `insert buffer`, `insert buffering`。

**purge lag**

InnoDB 历史列表的另一种名称。与 `innodb_max_purge_lag` 配置选项相关。

参见 `history list`, `purge`。

**purge thread**

InnoDB 进程内专用于执行周期性清除操作的线程。在 MySQL 5.6 及更高版本中，通过 `innodb_purge_threads` 配置选项启用多个清除线程。

参见 `purge`, `thread`。

**Python**

一种广泛应用于多个领域的编程语言，从 Unix 脚本到大规模应用程序。包括运行时类型、高级数据类型、面向对象的功能和广泛的标准库。通常用作其他语言编写的组件之间的“胶水”语言。MySQL Python API 是开源的 `MySQLdb` 模块。

参见 `MySQLdb`, `Python API`。

**Python API**

参见 `API`, `Python`。

## Q

**query**

在 SQL 中，指从一个或多个表中读取信息的操作。根据数据的组织方式和查询的参数，可以通过查阅索引来优化查找。如果涉及多个表，则查询称为联接（join）。

由于历史原因，有时在讨论语句的内部处理时，“查询”一词被广泛使用，包括其他类型的 MySQL 语句，如 DDL 和 DML 语句。

参见 `DDL`, `DML`, `index`, `join`, `SQL`, `table`。

**query execution plan**

由优化器关于如何最有效地执行查询所做的一系列决策，包括使用哪个或哪些索引以及连接表的顺序。计划稳定性（plan stability）意味着对于给定查询，优化器始终做出相同的选择。

参见 `index`, `join`, `plan stability`, `query`。

**query log**

参见 `general query log`。

**quiesce**

减少数据库活动的量，通常是为执行诸如 ALTER TABLE、备份或关闭等操作做准备。可能涉及尽可能多地刷新数据，以便 InnoDB 不再继续进行后台 I/O 操作。

在 MySQL 5.6 及更高版本中，语法 `FLUSH TABLES ... FOR EXPORT` 会将一些数据写入 InnoDB 表的磁盘，这使得通过复制数据文件来备份这些表变得更加简单。

参见 `backup`, `flush`, `InnoDB`, `shutdown`。

## R

**R-tree**

一种用于空间索引的树形数据结构，适用于多维数据如地理坐标、矩形或多边形。

参见 `B-tree`。

**RAID**

“Redundant Array of Inexpensive Drives”的缩写。通过将 I/O 操作分散到多个驱动器上，实现硬件层面的更高并发性，并提高低级写操作的效率，否则这些操作将按顺序执行。

参见 `concurrency`。

**random dive**

一种快速估算列中不同值数量（列的基数）的技术。InnoDB 随机从索引中采样页面，并使用这些数据来估算不同值的数量。

参见 `cardinality`。

**raw backup**

由 MySQL Enterprise Backup 产品生成的初始备份文件集，此时还未应用二进制日志和任何增量备份中反映的更改。在此阶段，文件尚未准备好恢复。在应用这些更改后，这些文件被称为已准备备份（prepared backup）。

参见 `binary log`, `hot backup`, `ibbackup_logfile`, `incremental backup`, `MySQL Enterprise Backup`, `prepared backup`, `restore`。

**READ COMMITTED**

一种隔离级别，它使用放宽的锁定策略，在事务之间保护性能。事务不能看到其他事务未提交的数据，但可以看到其他事务在当前事务启动后提交的数据。因此，事务不会看到错误数据，但它看到的数据在某种程度上可能取决于其他事务的时间安排。

当具有此隔离级别的事务执行 `UPDATE ... WHERE` 或 `DELETE ... WHERE` 操作时，其他事务可能需要等待。事务可以执行 `SELECT ... FOR UPDATE` 和 `LOCK IN SHARE MODE` 操作而不会让其他事务等待。

在 MySQL 8.0.1 中，`SELECT ... FOR SHARE` 替代了 `SELECT ... LOCK IN SHARE MODE`，但 `LOCK IN SHARE MODE` 仍可用于向后兼容。

参见 `ACID`, `isolation level`, `locking`, `REPEATABLE READ`, `SERIALIZABLE`, `transaction`。

**read phenomena**

在事务读取数据时，另一个事务已修改了这些数据，因此可能会发生的现象，如脏读、不可重复读和幻读。

参见 `dirty read`, `non-repeatable read`, `phantom`。

**READ UNCOMMITTED**

提供事务之间最少保护的隔离级别。查询采用一种锁定策略，使其在通常情况下需要等待其他事务时能够继续执行。然而，这种额外的性能提升是以减少结果的可靠性为代价的，包括数据已被其他事务更改但尚未提交（即脏读）。请谨慎使用此隔离级别，注意到结果可能不一致或不可重现，具体取决于同时进行的其他事务。通常，具有此隔离级别的事务仅执行查询，而不执行插入、更新或删除操作。

参见 `ACID`, `dirty read`, `isolation level`, `locking`, `transaction`。

**read view**

InnoDB 的 MVCC 机制使用的内部快照。某些事务根据其隔离级别，看到的数据值与事务（或在某些情况下，语句）开始时的数据一致。使用读取视图的隔离级别包括 `REPEATABLE READ`, `READ COMMITTED` 和 `READ UNCOMMITTED`。

参见 `isolation level`, `MVCC`, `READ COMMITTED`, `READ UNCOMMITTED`, `REPEATABLE READ`, `transaction`。

**read-ahead**

一种 I/O 请求类型，异步预取一组页面（整个区间）到缓冲池中，以防这些页面很快会被需要。线性预读技术根据前一个区间页面的访问模式，预取一个区间的所有页面。随机预读技术一旦某个区间的某些页面进入缓冲池，就预取该区间的所有页面。随机预读在 MySQL 5.5 中不包含，但在 MySQL 5.6 中重新引入，并由配置选项 `innodb_random_read_ahead` 控制。

参见 `buffer pool`, `extent`, `page`。

**read-only transaction**

一种针对 InnoDB 表的事务优化，通过消除为每个事务创建读取视图所涉及的一些记录管理。只能执行非锁定的读取查询。可以通过 `START TRANSACTION READ ONLY` 语法显式启动，或在某些条件下自动启动。详情请参阅[优化 InnoDB 只读事务](https://dev.mysql.com/doc/refman/8.0/en/innodb-performance-ro-tx.html)。

参见 `non-locking read`, `read view`, `transaction`。

**record lock**

一种对索引记录的锁。例如，`SELECT c1 FROM t WHERE c1 = 10 FOR UPDATE;` 防止其他任何事务插入、更新或删除 t.c1 值为 10 的行。与 `gap lock` 和 `next-key lock` 对比。

参见 `gap lock`, `lock`, `next-key lock`。

**redo**

在 DML 语句对 InnoDB 表进行更改时，记录在重做日志中的数据（以记录为单位）。在崩溃恢复期间，它用于修复由未完成的事务写入的数据。不断增加的 LSN 值表示已通过重做日志的数据的累积量。

参见 `crash recovery`, `DML`, `LSN`, `redo log`, `transaction`。

**redo log**

一种基于磁盘的数据结构，在崩溃恢复期间用于修复未完成事务写入的数据。在正常操作期间，它编码请求以更改 InnoDB 表数据，这些请求由 SQL 语句或低级 API 调用产生。在意外关闭前未完成的数据文件更新会被自动重放。

重做日志在磁盘上的物理表现形式为一组重做日志文件。重做日志数据按受影响的记录编码；这些数据统称为 `redo`。数据通过重做日志的传递由不断增加的 LSN 值表示。

详情参见[重做日志](https://dev.mysql.com/doc/refman/8.0/en/innodb-redo-log.html)。

参见 `crash recovery`, `data files`, `ib_logfile`, `log buffer`, `LSN`, `redo`, `shutdown`, `transaction`。

**redo log archiving**

当启用时，InnoDB 特性会将重做日志记录顺序写入存档文件，以避免备份工具在备份操作进行时未能跟上重做日志生成速度而导致的潜在数据丢失。详情请参见[重做日志归档](https://dev.mysql.com/doc/refman/8.0/en/innodb-redo-log-archiving.html)。

参见 `redo log`。

**redundant row format**

InnoDB 最早的行格式。在 MySQL 5.0.3 之前，这是 InnoDB 唯一可用的行格式。从 MySQL 5.0.3 到 MySQL 5.7.8，默认行格式为 `COMPACT`。从 MySQL 5.7.9 起，默认行格式由 `innodb_default_row_format` 配置选项定义，默认设置为 `DYNAMIC`。为了与旧的 InnoDB 表兼容，仍然可以指定 `REDUNDANT` 行格式。

详情参见[InnoDB 行格式](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-formats.html)。

参见 `compact row format`, `dynamic row format`, `row format`。

**referential integrity**

维护数据始终保持一致格式的技术，属于 ACID 哲学的一部分。特别是，通过使用外键约束来保持不同表中的数据一致，这可以防止更改发生或将这些更改自动传播到所有相关表。相关机制包括防止重复值插入的唯一约束和防止错误插入空值的 `NOT NULL` 约束。

参见 `ACID`, `FOREIGN KEY constraint`, `NOT NULL constraint`, `unique constraint`。

**relational**

现代数据库系统的重要方面。数据库服务器编码并执行关系，如一对一、一对多、多对一和唯一性。例如，在一个地址数据库中，一个人可能有零个、一个或多个电话号码；一个电话号码可能与几个家庭成员相关联。在金融数据库中，一个人可能需要恰好一个纳税人 ID，并且任何纳税人 ID 只能与一个人相关联。

数据库服务器可以使用这些关系来防止插入错误数据，并找到查找信息的有效方法。例如，如果一个值被声明为唯一的，服务器可以在找到第一个匹配项时停止搜索，并且它可以拒绝尝试插入该值的第二个副本。

在数据库级别，这些关系通过 SQL 特性来表示，如表中的列、唯一性和 `NOT NULL` 约束、外键以及不同类型的联接操作。复杂的关系通常涉及在多个表之间拆分数据。通常，数据被规范化，以便在一对多关系中只存储一次重复值。

在数学上下文中，数据库中的关系源自集合论。例如，`WHERE` 子句中的 `OR` 和 `AND` 运算符表示并集和交集的概念。

参见 `ACID`, `column`, `constraint`, `foreign key`, `normalized`。

**relevance**

在全文检索功能中，表示搜索字符串与 `FULLTEXT` 索引中数据相似性的数字。例如，当你搜索一个单词时，该单词在文本中出现多次的行通常比仅出现一次的行更相关。

参见 `full-text search`, `FULLTEXT index`。

**REPEATABLE READ**

InnoDB 的默认隔离级别。它防止被查询的行被其他事务更改，从而阻止不可重复读，但不阻止幻读。它使用中等严格的锁定策略，使事务中的所有查询看到相同的快照，即事务开始时的数据。

当具有此隔离级别的事务执行 `UPDATE ... WHERE`, `DELETE ... WHERE`, `SELECT ... FOR UPDATE` 和 `LOCK IN SHARE MODE` 操作时，其他事务可能需要等待。

在 MySQL 8.0.1 中，`SELECT ... FOR SHARE` 替代了 `SELECT ... LOCK IN SHARE MODE`，但 `LOCK IN SHARE MODE` 仍可用于向后兼容。

参见 `ACID`, `consistent read`, `isolation level`, `locking`, `phantom`, `transaction`。

**repertoire**

适用于字符集的术语。字符集的 Repertoire 是该集合中的字符集。参见[字符集 Repertoire](https://dev.mysql.com/doc/refman/8.0/en/charset-repertoire.html)。

**replica**

在复制拓扑中接收来自另一台服务器（源）的更改并应用这些相同更改的数据库服务器机器。因此，它与源保持相同的内容，尽管可能稍有滞后。

在 MySQL 中，副本通常用于灾难恢复，以取代发生故障的源。它们还常用于测试软件升级和新设置，以确保数据库配置更改不会导致性能或可靠性问题。

副本通常具有高工作负载，因为它们处理从源转发的所有 DML（写入）操作以及用户查询。为了确保副本能够足够快地应用来自源的更改，它们通常具有快速的 I/O 设备以及足够的 CPU 和内存，以在同一服务器上运行多个数据库实例。例如，源可能使用硬盘存储，而副本使用 SSD。

参见 `DML`, `replication`, `server`, `source`, `SSD`。

**replication**

将更改从源发送到一个或多个副本，以便所有数据库具有相同的数据。这种技术有广泛的用途，例如负载平衡以提高可扩展性、灾难恢复以及测试软件升级和配置更改。可以通过称为行级复制和语句级复制的方法在数据库之间发送更改。

参见 `replica`, `row-based replication`, `source`, `statement-based replication`。

**restore**

将 MySQL Enterprise Backup 产品生成的备份文件集放置到 MySQL 中以供使用的过程。此操作可以用于修复损坏的数据库、恢复到某个较早的时间点，或在复制上下文中设置新的副本。在 MySQL Enterprise Backup 产品中，此操作由 `mysqlbackup` 命令的 `copy-back` 选项执行。

参见 `hot backup`, `MySQL Enterprise Backup`, `mysqlbackup command`, `prepared backup`, `replica`, `replication`。

**rollback**

一种 SQL 语句，用于结束事务并撤消该事务所做的任何更改。它与 `commit` 相反，`commit` 使事务中的任何更改永久生效。

默认情况下，MySQL 使用自动提交设置，该设置在每个 SQL 语句后自动发出 `commit`。你必须更改此设置才能使用回滚技术。

参见 `ACID`, `autocommit`, `commit`, `SQL`, `transaction`。

**rollback segment**

包含 `undo` 日志的存储区域。回滚段传统上位于系统表空间中。从 MySQL 5.6 开始，回滚段可以位于 `undo` 表空间中。从 MySQL 5.7 开始，回滚段也分配给全局临时表空间。

参见 `global temporary tablespace`, `system tablespace`, `undo log`, `undo tablespace`。

**row**

由一组列定义的逻辑数据结构。一组行构成一个表。在 InnoDB 数据文件中，每个页面可以包含一行或多行。

尽管 InnoDB 使用“行格式”一词与 MySQL 语法保持一致，但行格式是每个表的属性，适用于该表中的所有行。

参见 `column`, `data files`, `page`, `row format`, `table`。

**row format**

InnoDB 表的行的磁盘存储格式。随着 InnoDB 获得新的功能（例如压缩），引入了新的行格式以支持由此带来的存储效率和性能改进。

InnoDB 表的行格式由 `ROW_FORMAT` 选项或 `innodb_default_row_format` 配置选项（在 MySQL 5.7.9 中引入）指定。行格式包括 `REDUNDANT`, `COMPACT`, `COMPRESSED` 和 `DYNAMIC`。要查看 InnoDB 表的行格式，请发出 `SHOW TABLE STATUS` 语句或查询 INFORMATION_SCHEMA 中的 InnoDB 表元数据。

参见 `compact row format`, `compressed row format`, `compression`, `dynamic row format`, `redundant row format`, `row`, `table`。

**row lock**

防止其他事务以不兼容的方式访问某行的锁。同一表中的其他行可以由其他事务自由写入。这是对 InnoDB 表执行 DML 操作时的锁定类型。

与 MyISAM 使用的表锁或在线 DDL 无法完成的 InnoDB 表 DDL 操作期间使用的表锁对比；这些锁会阻止并发访问表。

参见 `DDL`, `DML`, `InnoDB`, `lock`, `locking`, `online DDL`, `table lock`, `transaction`。

**row-based replication**

一种复制形式，其中事件从源传播，指定如何更改副本上的各个行。对于所有设置的 `innodb_autoinc_lock_mode` 选项都是安全的。

参见 `auto-increment locking`, `innodb_autoinc_lock_mode`, `replica`, `replication`, `source`, `statement-based replication`。

**row-level locking**

InnoDB 表使用的锁定机制，依赖于行锁而不是表锁。多个事务可以同时修改同一个表。只有当两个事务试图修改同一行时，其中一个事务才会等待另一个事务完成（并释放其行锁）。

参见 `InnoDB`, `locking`, `row lock`, `table lock`, `transaction`。

**Ruby**

一种强调动态类型和面向对象编程的编程语言。一些语法对 Perl 开发人员来说很熟悉。

参见 `API`, `Perl`, `Ruby API`。

**Ruby API**

基于 `libmysqlclient` API 库的 `mysql2` 可用于为 Ruby 程序员开发 MySQL 应用程序。详情参见[MySQL Ruby API](https://dev.mysql.com/doc/refman/8.0/en/apis-ruby.html)。

参见 `libmysql`, `Ruby`。

**rw-lock**

InnoDB 用于表示和执行对内部内存数据结构的共享访问锁的低级对象，与表示和执行对内部内存数据结构的独占访问锁的互斥量对比。互斥量和 rw-lock 统称为闩锁（latches）。

rw-lock 类型包括 s-lock（共享锁）, x-lock（独占锁）和 sx-lock（共享-独占锁）。

s-lock 允许对公共资源进行读访问。

x-lock 允许对公共资源进行写访问，同时不允许其他线程进行不一致的读取。

sx-lock 允许对公共资源进行写访问，同时允许其他线程进行不一致的读取。sx-lock 在 MySQL 5.7 中引入，以优化并发性并提高读写工作负载的可扩展性。

以下矩阵总结了 rw-lock 类型的兼容性。

| | S | SX | X |
|||||
| **S**| Compatible | Compatible | Conflict |
| **SX** | Compatible | Conflict | Conflict |
| **X**| Conflict | Conflict | Conflict |

参见 `latch`, `lock`, `mutex`, `Performance Schema`。

## S

**savepoint**

保存点有助于实现嵌套事务。它们可以为属于较大事务的表操作提供范围。例如，在预订系统中安排一次旅行可能涉及预订多个不同的航班；如果某个航班无法预订，您可以回滚涉及预订该航段的更改，而无需回滚之前成功预订的航班。

参见：`rollback`，`transaction`。

**scalability**

可扩展性指的是在不因系统容量限制而导致性能突然下降的情况下，能够增加更多工作并发出更多同时请求的能力。软件架构、硬件配置、应用程序编码和工作负载类型都影响可扩展性。当系统达到其最大容量时，提高可扩展性的常见技术包括纵向扩展（增加现有硬件或软件的容量）和横向扩展（增加新服务器和更多 MySQL 实例）。通常与可用性一起被视为大规模部署的关键方面。

参见：`availability`，`scale out`，`scale up`。

**scale out**

通过增加新服务器和更多 MySQL 实例来提高可扩展性的一种技术。例如，设置复制、NDB Cluster、连接池或其他将工作分散到一组服务器上的功能。与纵向扩展相对。

参见：`scalability`，`scale up`。

**scale up**

通过增加现有硬件或软件的容量来提高可扩展性的一种技术。例如，增加服务器上的内存并调整与内存相关的参数，如 `innodb_buffer_pool_size` 和 `innodb_buffer_pool_instances`。与横向扩展相对。

参见：`scalability`，`scale out`。

**schema**

概念上，模式是一个相互关联的数据库对象集合，例如表、表列、列的数据类型、索引、外键等。这些对象通过 SQL 语法连接在一起，因为列组成表，外键引用表和列等。理想情况下，它们在逻辑上也是连接在一起的，作为统一应用程序或灵活框架的一部分共同工作。例如，`INFORMATION_SCHEMA` 和 `performance_schema` 数据库在其名称中使用“schema”以强调它们包含的表和列之间的紧密关系。

在 MySQL 中，物理上，模式与数据库同义。您可以在 MySQL SQL 语法中使用 `SCHEMA` 关键字代替 `DATABASE`，例如使用 `CREATE SCHEMA` 代替 `CREATE DATABASE`。

其他数据库产品可能会区分这两个术语。例如，在 Oracle 数据库产品中，模式仅表示数据库的一部分：单个用户拥有的表和其他对象。

参见：`database`，`INFORMATION_SCHEMA`，`Performance Schema`。

**SDI**

“序列化字典信息”的缩写。

参见：`serialized dictionary information (SDI)`。

**search index**

在 MySQL 中，全文搜索查询使用一种特殊类型的索引，即 `FULLTEXT` 索引。从 MySQL 5.6.4 开始，`InnoDB` 和 `MyISAM` 表都支持 `FULLTEXT` 索引；以前，这些索引仅适用于 `MyISAM` 表。

参见：`full-text search`，`FULLTEXT index`。

**secondary index**

一种 InnoDB 索引，表示表列的子集。一个 InnoDB 表可以有零个、一个或多个二级索引。（与每个 InnoDB 表必需的、存储所有表列数据的聚簇索引形成对比。）

二级索引可用于满足仅需要从索引列获取值的查询。对于更复杂的查询，它可以用于识别表中的相关行，然后通过使用聚簇索引进行查找来检索这些行。

创建和删除二级索引传统上涉及大量的 InnoDB 表数据复制开销。快速索引创建功能使 InnoDB 二级索引的 `CREATE INDEX` 和 `DROP INDEX` 语句的执行速度大大提高。

参见：`clustered index`，`Fast Index Creation`，`index`。

**segment**

InnoDB 表空间内的一个分区。如果表空间类似于目录，则段类似于该目录中的文件。段可以增长。可以创建新的段。

例如，在一个 `file-per-table` 表空间内，表数据位于一个段中，每个关联的索引位于自己的段中。系统表空间包含许多不同的段，因为它可以容纳许多表及其关联的索引。在 MySQL 8.0 之前，系统表空间还包括用于撤消日志的一个或多个回滚段。

随着数据的插入和删除，段会增长和收缩。当一个段需要更多空间时，它会每次扩展一个区（1 兆字节）。同样，当一个区中的所有数据都不再需要时，段将释放一个区的空间。

参见：`extent`，`file-per-table`，`rollback segment`，`system tablespace`，`tablespace`，`undo log`。

**selectivity**

数据分布的一个属性，即列中不同值的数量（其基数）除以表中的记录数。高选择性意味着列值相对唯一，可以通过索引有效地检索。如果您（或查询优化器）可以预测 `WHERE` 子句中的测试仅匹配表中少量（或比例）行，则总体查询在首先使用索引评估该测试时往往效率更高。

参见：`cardinality`，`query`。

**semi-consistent read**

用于 `UPDATE` 语句的一种读取操作，是 `READ COMMITTED` 和 `consistent read` 的组合。当 `UPDATE` 语句检查已锁定的行时，InnoDB 将最新的已提交版本返回给 MySQL，以便 MySQL 可以确定该行是否符合 `UPDATE` 的 `WHERE` 条件。如果该行匹配（必须更新），MySQL 将再次读取该行，这次 InnoDB 要么锁定它，要么等待锁定它。当事务具有 `READ COMMITTED` 隔离级别时，只能发生这种读取操作。

参见：`consistent read`，`isolation level`，`READ COMMITTED`。

**SERIALIZABLE**

使用最保守锁定策略的隔离级别，以防止任何其他事务插入或更改此事务读取的数据，直到该事务完成为止。这样一来，事务内可以反复运行相同的查询，并确保每次检索到相同的结果集。任何尝试更改自当前事务开始以来由其他事务提交的数据的操作，都会导致当前事务等待。

这是 SQL 标准规定的默认隔离级别。实际上，通常不需要这种严格的程度，因此 InnoDB 的默认隔离级别是下一个最严格的 `REPEATABLE READ`。

参见：`ACID`，`consistent read`，`isolation level`，`locking`，`REPEATABLE READ`，`transaction`。

**serialized dictionary information (SDI)**

序列化形式的字典对象元数据。SDI 以 JSON 格式存储。

从 MySQL 8.0.3 开始，SDI 存在于除临时表空间和撤消表空间文件以外的所有 InnoDB 表空间文件中。表空间文件中存在 SDI 提供了元数据冗余。例如，如果数据字典不可用，可以使用 `ibd2sdi` 工具从表空间文件中提取字典对象元数据。

对于 `MyISAM` 表，SDI 存储在架构目录中的 .sdi 元数据文件中。执行 `IMPORT TABLE` 操作时需要 `SDI` 元数据文件。

参见：`file-per-table`，`general tablespace`，`system tablespace`，`tablespace`。

**server**

一种程序，持续运行，等待接收并执行来自另一个程序（客户端）的请求。因为通常整个计算机都用于运行一个或多个服务器程序（如数据库服务器、Web 服务器、应用服务器或这些的组合），所以术语“服务器”也可以指运行服务器软件的计算机。

参见：`client`，`mysqld`。

**server-side prepared statement**

由 MySQL 服务器管理的预处理语句。历史上，由于服务器端预处理语句的问题，`Connector/J` 和 `Connector/PHP` 开发人员有时会使用客户端预处理语句。使用现代 MySQL 服务器版本，推荐使用服务器端预处理语句以提高性能、可扩展性和内存效率。

参见：`client-side prepared statement`，`Connector/J`，`Connector/PHP`，`prepared statement`。

**service principal name**

表示服务的 Kerberos 命名实体名称。

参见：`principal`。

**service ticket**

提供对应用服务（如 Web 或数据库服务器提供的服务）访问权限的 Kerberos 票证。

**servlet**

参见：`Connector/J`。

**session temporary tablespace**

存储用户创建的临时表和由优化器创建的内部临时表的临时表空间，当 InnoDB 被配置为内部临时表的磁盘存储引擎时使用。

参见：`optimizer`，`temporary table`，`temporary tablespace`。

**shared lock**

一种锁，允许其他事务读取被锁定的对象，并且还可以获取其他共享锁，但不能对其进行写操作。与独占锁相对。

参见：`exclusive lock`，`lock`，`transaction`。

**shared tablespace**

另一种指代系统表空间或通用表空间的方式。通用表空间在 MySQL 5.7 中引入。多个表可以位于共享表空间中。每个 `file-per-table` 表空间只能包含一个表。

参见：`general tablespace`，`system tablespace`。

**sharp checkpoint**

将包含在 `redo log` 的某个部分中的所有脏页刷新到磁盘的过程。发生在 InnoDB 重新使用日志文件的一部分之前；日志文件以循环方式使用。通常发生在写密集型工作负载下。

参见：`dirty page`，`flush`，`redo log`，`workload`。

**shutdown**

停止 MySQL 服务器的过程。默认情况下，此过程会清理 InnoDB 表的操作，因此 InnoDB 关闭速度较慢，但随后启动速度较快。如果跳过清理操作，则关闭速度较快，但在下次重启时必须执行清理操作。

InnoDB 的关闭模式由 `innodb_fast_shutdown` 选项控制。

参见：`fast shutdown`，`InnoDB`，`slow shutdown`，`startup`。

**slave**

参见：`replica`。

**slow query log**

一种日志类型，用于对 MySQL 服务器处理的 SQL 语句进行性能调优。日志信息存储在文件中。必须启用此功能才能使用它。您可以控制哪些类别的“慢” SQL 语句会记录下来。更多信息，请参见《第 7.4.5 节，慢查询日志》。

参见：`general query log`，`log`。

**slow shutdown**

一种关闭类型，在完成之前执行额外的 InnoDB 刷新操作。也称为“干净关闭”。通过配置参数 `innodb_fast_shutdown=0` 或命令 `SET GLOBAL innodb_fast_shutdown=0;` 指定。尽管关闭本身可能需要更长时间，但这种时间应在随后的启动时节省。

参见：`clean shutdown`，`fast shutdown`，`shutdown`。

**snapshot**

特定时间点的数据表示，即使其他事务提交更改后，该表示也保持不变。某些隔离级别使用快照来允许一致读取。

参见：`commit`，`consistent read`，`isolation level`，`transaction`。

**sort buffer**

在创建 InnoDB 索引期间用于排序数据的缓冲区。排序缓冲区大小通过 `innodb_sort_buffer_size` 配置选项进行配置。

**source**

在复制场景中处理数据的初始插入、更新和删除请求的数据库服务器。这些更改传播到其他称为副本的服务器上，并在这些服务器上重复。

参见：`replica`，`replication`。

**space ID**

用于唯一标识 MySQL 实例中 InnoDB 表空间的标识符。系统表空间的 `space ID` 始终为 0；此 ID 适用于系统表空间或通用表空间内的所有表。每个 `file-per-table` 表空间和通用表空间都有自己的空间 ID。

在 MySQL 5.6 之前，此硬编码值在 InnoDB 表空间文件在 MySQL 实例之间移动时会引发困难。从 MySQL 5.6 开始，您可以通过使用 `FLUSH TABLES ... FOR EXPORT`，`ALTER TABLE ... DISCARD TABLESPACE` 和 `ALTER TABLE ... IMPORT TABLESPACE` 等语句进行传输表空间功能，在实例之间复制表空间文件。调整空间 ID 所需的信息在与表空间一起复制的 `.cfg` 文件中传达。有关详细信息，请参见《第 17.6.1.3 节，导入 InnoDB 表》。

参见：`.cfg file`，`file-per-table`，`general tablespace`，`.ibd file`，`system tablespace`，`tablespace`，`transportable tablespace`。

**sparse file**

一种文件类型，通过将表示空块的元数据写入磁盘而不是写入实际的空白空间来更有效地使用文件系统空间。InnoDB 的透明页压缩功能依赖于稀疏文件支持。更多信息，请参见《第 17.9.2 节，InnoDB 页压缩》。

参见：`hole punching`，`transparent page compression`。

**spin**

一种等待操作，持续测试资源是否可用。此技术用于通常仅保持短时间的资源，其中在“忙循环”中等待比将线程置于休眠状态并执行上下文切换更有效。如果资源在短时间内未变得可用，旋转循环将停止，并使用其他等待技术。

参见：`latch`，`lock`，`mutex`，`wait`。

**SPN**

参见：`service principal name`。

**Spring**

一种基于 Java 的应用程序框架，旨在通过提供配置组件的方式帮助应用程序设计。

参见：`J2EE`。

**SQL**

标准化的结构化查询语言，用于执行数据库操作。通常分为 `DDL`、`DML` 和查询等类别。MySQL 包含一些额外的语句类别，例如复制。有关 SQL 语法的构建块，MySQL 表列的数据类型，SQL 语句的详细信息及其相关类别，以及查询中使用的标准和 MySQL 特定函数的详细信息，请参见《第 11 章，语言结构》，《第 13 章，数据类型》，《第 15 章，SQL 语句》，以及《第 14 章，函数和运算符》。

参见：`DDL`，`DML`，`query`，`replication`。

**SQLState**

由 `JDBC` 标准定义的错误代码，用于使用 `Connector/J` 的应用程序中的异常处理。

参见：`Connector/J`，`JDBC`。

**SSD**

“固态硬盘”的缩写。与传统的硬盘驱动器（HDD）相比，这种存储设备具有不同的性能特征：存储容量较小，随机读取速度较快，没有移动部件，并且有许多影响写性能的考虑因素。其性能特征会影响磁盘绑定工作负载的吞吐量。

参见：`disk-bound`，`HDD`。

**SSL**

“安全套接字层”的缩写。为应用程序与 MySQL 数据库服务器之间的网络通信提供加密层。

参见：`keystore`，`truststore`。

**ST**

参见：`service ticket`。

**startup**

启动 MySQL 服务器的过程。通常由《第 6.3 节，服务器和服务器启动程序》中列出的程序之一完成。与关闭相对。

参见：`shutdown`。

**statement interceptor**

一种用于跟踪、调试或增强数据库应用程序发出的 SQL 语句的拦截器类型。有时也称为命令拦截器。

在使用 `Connector/J` 的 Java 应用程序中，设置这种类型的拦截器涉及实现 `com.mysql.jdbc.StatementInterceptorV2` 接口，并将 `statementInterceptors` 属性添加到连接字符串中。

在使用 `Connector/NET` 的 Visual Studio 应用程序中，设置这种类型的拦截器涉及定义一个从 `BaseCommandInterceptor` 类继承的类，并将该类名称指定为连接字符串的一部分。

参见：`command interceptor`，`connection string`，`Connector/J`，`Connector/NET`，`interceptor`，`Java`，`Visual Studio`。

**statement-based replication**

一种复制形式，其中 SQL 语句从源发送并在副本上重放。需要对 `innodb_autoinc_lock_mode` 选项的设置格外注意，以避免自动增量锁定的潜在时序问题。

参见：`auto-increment locking`，`innodb_autoinc_lock_mode`，`replica`，`replication`，`row-based replication`，`source`。

**statistics**

与每个 InnoDB 表和索引相关的估计值，用于构造有效的查询执行计划。主要值包括基数（不同值的数量）和表行或索引条目的总数。表的统计信息表示其主键索引中的数据。二级索引的统计信息表示该索引涵盖的行。

这些值是估计的而不是精确计数的，因为在任何时候，不同的事务都可能在同一表中插入和删除行。为了防止这些值频繁重新计算，您可以启用持久化统计信息，其中值存储在 InnoDB 系统表中，并仅在您发出 `ANALYZE TABLE` 语句时刷新。

您可以通过 `innodb_stats_method` 配置选项控制计算统计信息时如何处理 `NULL` 值。

通过 `INFORMATION_SCHEMA` 和 `PERFORMANCE_SCHEMA` 表，还可以获得数据库对象和数据库活动的其他类型统计信息。

参见：`cardinality`，`index`，`INFORMATION_SCHEMA`，`NULL`，`Performance Schema`，`persistent statistics`，`primary key`，`query execution plan`，`secondary index`，`table`，`transaction`。

**stemming**

根据共同的词根搜索不同词形变体的能力，例如单数和复数，或过去、现在和将来时态。目前仅在 `MyISAM` 全文搜索功能中支持此功能，而 InnoDB 表的 `FULLTEXT` 索引中不支持。

参见：`full-text search`，`FULLTEXT index`。

**stopword**

在 `FULLTEXT` 索引中，被视为常见或琐碎到不需要包含在搜索索引中且在搜索查询中被忽略的词。不同的配置设置控制 InnoDB 和 MyISAM 表的停用词处理。更多信息，请参见《第 14.9.4 节，全文停用词》。

参见：`FULLTEXT index`，`search index`。

**storage engine**

MySQL 数据库的一个组件，负责执行存储、更新和查询数据的底层工作。在 MySQL 5.5 及更高版本中，`InnoDB` 是新表的默认存储引擎，取代了 `MyISAM`。不同的存储引擎在内存使用与磁盘使用、读取速度与写入速度、速度与健壮性等因素之间进行不同的权衡。每个存储引擎管理特定的表，因此我们会提到 `InnoDB` 表、`MyISAM` 表等。

MySQL Enterprise Backup 产品针对 InnoDB 表的备份进行了优化。它也可以备份由 MyISAM 和其他存储引擎处理的表。

参见：`InnoDB`，`MySQL Enterprise Backup`，`table type`。

**stored generated column**

值从列定义中包含的表达式计算得出的列。在插入或更新行时评估和存储列值。存储生成列需要存储空间并且可以被索引。

与虚拟生成列形成对比。

参见：`base column`，`generated column`，`virtual generated column`。

**stored object**

存储程序或视图。

**stored program**

存储例程（过程或函数）、触发器或事件调度程序事件。

**stored routine**

存储过程或函数。

**strict mode**

由 `innodb_strict_mode` 选项控制的设置的通用名称。启用此设置后，某些通常被视为警告的条件将被视为错误（并且底层语句失败）。例如，某些与文件格式和行格式相关的无效选项组合，通常会生成警告并继续使用默认值，现在会导致 `CREATE TABLE` 操作失败。`innodb_strict_mode` 在 MySQL 5.7 中默认启用。

MySQL 还具有所谓的严格模式。参见《第 7.1.11 节，服务器 SQL 模式》。

参见：`file format`，`innodb_strict_mode`，`row format`。

**sublist**

在表示缓冲池的列表结构中，较旧和较新的页面由列表的不同部分表示。一组参数控制这些部分的大小以及新旧页面之间的分界点。

参见：`buffer pool`，`eviction`，`list`，`LRU`。

**supremum record**

索引中的伪记录，表示大于该索引中最大值的间隙。如果事务具有诸如 `SELECT ... FROM ... WHERE col > 10 FOR UPDATE;` 之类的语句，并且列中的最大值为 20，则对 `supremum` 记录的锁定将防止其他事务插入更大的值，例如 50、100 等。

参见：`gap`，`infimum record`，`pseudo-record`。

**surrogate key**

`synthetic key` 的同义词。

参见：`synthetic key`。

**synthetic key**

索引列，通常是主键，其值是任意分配的。通常使用自增列完成。通过将值视为完全任意的，可以避免过于严格的规则和错误的应用假设。例如，如果某个员工被批准雇佣但从未真正加入公司，表示员工编号的数字序列可能会有空缺。或者，如果员工离开公司后重新加入，员工编号 100 的入职日期可能比员工编号 500 的晚。数值也会产生可预测长度的较短值。例如，存储代表“Road”、“Boulevard”、“Expressway”等的数字代码比反复存储这些字符串更节省空间。

也称为代理键。与自然键形成对比。

参见：`auto-increment`，`natural key`，`primary key`，`surrogate key`。

**system tablespace**

包含 InnoDB 相关对象的元数据、`change buffer` 的存储区和 `doublewrite buffer` 的一个或多个数据文件（ibdata 文件）。如果表是在系统表空间而不是 `file-per-table` 或通用表空间中创建的，系统表空间还可能包含 InnoDB 表的表和索引数据。系统表空间中的数据和元数据适用于 MySQL 实例中的所有数据库。

在 MySQL 5.6.7 之前，默认是将所有 InnoDB 表和索引保留在系统表空间内，这通常会导致该文件变得非常大。由于系统表空间从不缩小，如果加载并删除了大量临时数据，可能会出现存储问题。在 MySQL 8.0 中，默认设置为 `file-per-table` 模式，其中每个表及其关联的索引存储在一个单独的 .ibd 文件中。此默认设置使得使用依赖于 `DYNAMIC` 和 `COMPRESSED` 行格式的 InnoDB 功能（例如表压缩、离页列的有效存储以及大索引键前缀）变得更加容易。

将所有表数据保留在系统表空间或单独的 .ibd 文件中对存储管理有一定影响。MySQL Enterprise Backup 产品可能会备份少量的大文件，或者是许多较小的文件。在包含数千个表的系统上，处理数千个 .ibd 文件的文件系统操作可能会导致瓶颈。

InnoDB 在 MySQL 5.7.6 中引入了通用表空间，这些表空间也由 .ibd 文件表示。通用表空间是使用 `CREATE TABLESPACE` 语法创建的共享表空间。它们可以在数据目录之外创建，能够容纳多个表，并支持所有行格式的表。

参见：`change buffer`，`compression`，`data dictionary`，`database`，`doublewrite buffer`，`dynamic row format`，`file-per-table`，`general tablespace`，`.ibd file`，`ibdata file`，`innodb_file_per_table`，`instance`，`MySQL Enterprise Backup`，`off-page column`，`tablespace`，`undo log`。

## T

**table**

每个 MySQL 表都与特定的存储引擎相关联。InnoDB 表具有特定的物理和逻辑特性，这些特性会影响性能、可扩展性、备份、管理和应用程序开发。

在文件存储方面，InnoDB 表属于以下类型之一的表空间：

- 共享的 InnoDB 系统表空间，由一个或多个 `ibdata` 文件组成。
- 每个表一个文件的表空间，由单个 `.ibd` 文件组成。
- 共享的通用表空间，由单个 `.ibd` 文件组成。通用表空间是在 MySQL 5.7.6 中引入的。

`.ibd` 数据文件包含表和索引数据。

在每个表一个文件的表空间中创建的 InnoDB 表可以使用 `DYNAMIC` 或 `COMPRESSED` 行格式。这些行格式使得 InnoDB 能够使用诸如压缩、离页列的有效存储以及大索引键前缀等功能。通用表空间支持所有行格式。

系统表空间支持使用 `REDUNDANT`、`COMPACT` 和 `DYNAMIC` 行格式的表。系统表空间对 `DYNAMIC` 行格式的支持是在 MySQL 5.7.6 中添加的。

InnoDB 表的行被组织成一种称为聚簇索引的索引结构，条目根据表的主键列排序。数据访问针对过滤和排序主键列的查询进行了优化，每个索引都包含每个条目相关的主键列的副本。修改任何主键列的值是一项昂贵的操作。因此，InnoDB 表设计的一个重要方面是选择用于最重要查询的列作为主键，并保持主键短且不常变化。

参见：`backup`，`clustered index`，`compact row format`，`compressed row format`，`compression`，`dynamic row format`，`Fast Index Creation`，`file-per-table`，`.ibd file`，`index`，`off-page column`，`primary key`，`redundant row format`，`row`，`system tablespace`，`tablespace`。

**table lock**

一种锁定机制，防止任何其他事务访问表。InnoDB 通过使用诸如在线 DDL、行锁和一致读取等技术来处理 DML 语句和查询，尽量避免这种锁定的必要性。可以通过使用 `LOCK TABLE` 语句在 SQL 中创建这样的锁；从其他数据库系统或 MySQL 存储引擎迁移时，尽可能去除这些语句。

参见：`consistent read`，`DML`，`lock`，`locking`，`online DDL`，`query`，`row lock`，`table`，`transaction`。

**table scan**

参见：`full table scan`。

**table statistics**

参见：`statistics`。

**table type**

存储引擎的过时同义词。我们提到 InnoDB 表、MyISAM 表等。

参见：`InnoDB`，`storage engine`。

**tablespace**

一个可以容纳一个或多个 InnoDB 表及相关索引的数据文件。

系统表空间包含 InnoDB 数据字典，并且在 MySQL 5.6 之前默认保存所有其他 InnoDB 表。

`innodb_file_per_table` 选项在 MySQL 5.6 及更高版本中默认启用，允许表在各自的表空间中创建。每个表一个文件的表空间支持诸如离页列的有效存储、表压缩和可传输表空间等功能。详细信息请参见《第 17.6.3.2 节，每个表一个文件的表空间》。

InnoDB 在 MySQL 5.7.6 中引入了通用表空间。通用表空间是使用 `CREATE TABLESPACE` 语法创建的共享表空间。它们可以在 MySQL 数据目录之外创建，能够容纳多个表，并支持所有行格式的表。

MySQL NDB Cluster 还将其表分组到表空间中。详细信息请参见《第 25.6.11.1 节，NDB Cluster 磁盘数据对象》。

参见：`compressed row format`，`data dictionary`，`data files`，`file-per-table`，`general tablespace`，`index`，`innodb_file_per_table`，`system tablespace`，`table`。

**Tcl**

一种编程语言，起源于 Unix 脚本领域。有时由用 C、C++ 或 Java 编写的代码扩展。有关 MySQL 的开源 Tcl API，请参见《第 31.12 节，MySQL Tcl API》。

参见：`API`。

**temporary table**

一种数据不需要真正永久存储的表。例如，临时表可能被用作复杂计算或转换中的中间结果的存储区域；这些中间数据在崩溃后不需要恢复。数据库产品可以采取各种快捷方式来提高对临时表的操作性能，例如减少将数据写入磁盘的频率以及保护数据跨重启的其他措施。

有时，数据本身会在设定时间自动删除，例如在事务结束或会话结束时删除。在某些数据库产品中，表本身也会自动删除。

参见：`table`。

**temporary tablespace**

InnoDB 使用两种类型的临时表空间。会话临时表空间存储用户创建的临时表和优化器创建的内部临时表。全局临时表空间存储对用户创建的临时表进行更改的回滚段。

参见：`global temporary tablespace`，`session temporary tablespace`，`temporary table`。

**text collection**

包含在 `FULLTEXT` 索引中的列集合。

参见：`FULLTEXT index`。

**TGS**

Kerberos 中的票据授予服务器（TGS）。TGS 也可以指由票据授予服务器提供的票据授予服务。

参见：`ticket-granting server`。

**TGT**

参见：`ticket-granting ticket`。

**thread**

一个处理单元，通常比进程更轻量化，允许更高的并发性。

参见：`concurrency`，`master thread`，`process`，`Pthreads`。

**ticket-granting server**

在 Kerberos 中，提供票据的服务器。票据授予服务器（TGS）与认证服务器（AS）一起构成密钥分发中心（KDC）。

TGS 也可以指由票据授予服务器提供的票据授予服务。

参见：`authentication server`，`key distribution center`。

**ticket-granting ticket**

在 Kerberos 中，票据授予票据用于向票据授予服务器（TGS）获取服务访问的服务票据。

参见：`ticket-granting server`。

**Tomcat**

一个开源 J2EE 应用服务器，支持 Java Servlet 和 JavaServer Pages 编程技术。由一个 Web 服务器和 Java servlet 容器组成。通常与 MySQL 配合使用 `Connector/J`。

参见：`J2EE`。

**torn page**

由于 I/O 设备配置和硬件故障的组合而可能发生的一种错误情况。如果数据以小于 InnoDB 页大小（默认 16KB）的块写出，写入时的硬件故障可能会导致仅部分页被存储到磁盘。InnoDB 的双写缓冲区可以防止这种情况发生。

参见：`doublewrite buffer`。

**TPS**

“每秒事务数”的缩写，有时在基准测试中使用的测量单位。其值取决于特定基准测试表示的工作负载，以及您控制的因素，例如硬件容量和数据库配置。

参见：`transaction`，`workload`。

**transaction**

事务是可以提交或回滚的原子工作单元。当事务对数据库进行多次更改时，要么在提交事务时所有更改都成功，要么在回滚事务时所有更改都被撤消。

由 InnoDB 实现的数据库事务具有被统称为 `ACID` 的属性，代表原子性、一致性、隔离性和持久性。

参见：`ACID`，`commit`，`isolation level`，`lock`，`rollback`。

**transaction ID**

与每一行相关联的内部字段。该字段通过插入、更新和删除操作来记录哪个事务锁定了该行。

参见：`implicit row lock`，`row`，`transaction`。

**transparent page compression**

MySQL 5.7.8 中添加的一项功能，允许在文件逐个表的表空间中的 InnoDB 表执行页级压缩。通过在 `CREATE TABLE` 或 `ALTER TABLE` 中指定 `COMPRESSION` 属性来启用页面压缩。更多信息，请参

见《第 17.9.2 节，InnoDB 页面压缩》。

参见：`file-per-table`，`hole punching`，`sparse file`。

**transportable tablespace**

允许将表空间从一个实例移动到另一个实例的功能。传统上，InnoDB 表空间无法实现这一点，因为所有表数据都是系统表空间的一部分。在 MySQL 5.6 及更高版本中，`FLUSH TABLES ... FOR EXPORT` 语法准备 InnoDB 表以便复制到另一台服务器；在另一台服务器上运行 `ALTER TABLE ... DISCARD TABLESPACE` 和 `ALTER TABLE ... IMPORT TABLESPACE` 可以将复制的数据文件引入到另一实例中。 `.cfg` 文件与 `.ibd` 文件一起复制时，用于在导入表空间时更新表元数据（例如空间 ID）。有关用法信息，请参见《第 17.6.1.3 节，导入 InnoDB 表》。

参见：`.cfg file`，`.ibd file`，`space ID`，`system tablespace`，`tablespace`。

**troubleshooting**

确定问题根源的过程。一些排除 MySQL 问题的资源包括：

- 《第 2.9.2.1 节，排除 MySQL 服务器启动问题》
- 《第 8.2.22 节，排除 MySQL 连接问题》
- 《附录 B.3.3.2，如何重置 root 密码》
- 《附录 B.3.2，使用 MySQL 程序时的常见错误》
- 《第 17.21 节，InnoDB 故障排除》。

**truncate**

一种 DDL 操作，删除表的所有内容，同时保留表和相关索引。与删除形成对比。尽管概念上它与不带 `WHERE` 子句的 `DELETE` 语句的结果相同，但它在后台操作不同：InnoDB 创建一个新的空表，删除旧表，然后重命名新表以代替旧表。由于这是一个 DDL 操作，不能回滚。

如果要截断的表包含引用另一个表的外键，截断操作会使用一种较慢的操作方法，一次删除一行，以便根据 `ON DELETE CASCADE` 子句的需要删除引用表中的对应行。（MySQL 5.5 及更高版本不允许这种较慢形式的截断操作，如果涉及外键，则返回错误。在这种情况下，请改用 `DELETE` 语句。）

参见：`DDL`，`drop`，`foreign key`，`rollback`。

**truststore**

参见：`SSL`。

**tuple**

表示有序元素集合的技术术语。这是一个抽象概念，用于数据库理论的正式讨论中。在数据库领域，元组通常由表行的列表示。它们也可以由查询的结果集表示，例如，仅检索表的某些列或联接表的列的查询。

参见：`cursor`。

**two-phase commit**

在 XA 规范下的分布式事务的一部分操作。（有时缩写为 2PC。）当多个数据库参与事务时，所有数据库要么提交更改，要么所有数据库回滚更改。

参见：`commit`，`rollback`，`transaction`，`XA`。

## U

**undo**

事务生命周期中维护的数据，记录所有更改，以便在回滚操作中可以撤销这些更改。它存储在 `undo logs` 中，这些日志位于系统表空间（MySQL 5.7 及以前）或单独的 `undo tablespaces` 中。从 MySQL 8.0 开始，`undo logs` 默认位于 `undo tablespaces` 中。

参见：`rollback`，`rollback segment`，`system tablespace`，`transaction`，`undo log`，`undo tablespace`。

**undo buffer**

参见：`undo log`。

**undo log**

存储区，用于保存由活动事务修改的数据的副本。如果另一个事务需要查看原始数据（作为一致性读取操作的一部分），则从该存储区检索未修改的数据。

在 MySQL 5.6 和 MySQL 5.7 中，可以使用 `innodb_undo_tablespaces` 变量将 `undo logs` 存放在 `undo tablespaces` 中，这些表空间可以放置在另一个存储设备上，如 SSD 中。在 MySQL 8.0 中，`undo logs` 存放在 MySQL 初始化时创建的两个默认 `undo tablespaces` 中，可以使用 `CREATE UNDO TABLESPACE` 语法创建其他 `undo tablespaces`。

`undo log` 分为两个部分：插入 `undo buffer` 和更新 `undo buffer`。

参见：`consistent read`，`rollback segment`，`SSD`，`system tablespace`，`transaction`，`undo tablespace`。

**undo log segment**

`undo logs` 的集合。`undo log segments` 存在于 `rollback segments` 中。一个 `undo log segment` 可能包含来自多个事务的 `undo logs`。一个 `undo log segment` 一次只能被一个事务使用，但在事务提交或回滚后可以重复使用。也可能被称为“`undo segment`”。

参见：`commit`，`rollback`，`rollback segment`，`undo log`。

**undo tablespace**

`undo tablespace` 包含 `undo logs`。`undo logs` 存在于 `undo log segments` 中，而这些 `undo log segments` 存在于 `rollback segments` 中。传统上，`rollback segments` 位于系统表空间中。从 MySQL 5.6 开始，`rollback segments` 可以位于 `undo tablespaces` 中。在 MySQL 5.6 和 MySQL 5.7 中，`undo tablespaces` 的数量由 `innodb_undo_tablespaces` 配置选项控制。在 MySQL 8.0 中，MySQL 实例初始化时创建了两个默认的 `undo tablespaces`，并且可以使用 `CREATE UNDO TABLESPACE` 语法创建其他 `undo tablespaces`。

有关更多信息，请参见《第 17.6.3.4 节，Undo Tablespaces》。

参见：`rollback segment`，`system tablespace`，`undo log`，`undo log segment`。

**Unicode**

一种系统，支持国家字符、字符集、代码页和其他国际化方面，以灵活和标准化的方式实现。

Unicode 支持是 ODBC 标准的重要方面。`Connector/ODBC 5.1` 是一个 Unicode 驱动程序，而 `Connector/ODBC 3.51` 是一个 ANSI 驱动程序。

参见：`ANSI`，`Connector/ODBC`，`ODBC`。

**unique constraint**

一种约束，断言列中不能包含任何重复值。在关系代数中，它用于指定一对一的关系。为了有效检查值是否可以插入（即该值是否已存在于列中），`unique constraint` 由一个底层的 `unique index` 支持。

参见：`constraint`，`relational`，`unique index`。

**unique index**

在具有 `unique constraint` 的列或列集上的索引。由于已知该索引不包含任何重复值，因此某些类型的查找和计数操作比常规索引更高效。对这种类型索引的大多数查找只是为了确定某个值是否存在。索引中的值数量与表中的行数相同，或者至少与相关列中非空值的行数相同。

更改缓冲优化不适用于唯一索引。作为一种解决方法，可以在向 InnoDB 表批量加载数据时临时设置 `unique_checks=0`。

参见：`cardinality`，`change buffering`，`unique constraint`，`unique key`。

**unique key**

构成 `unique index` 的列集（一个或多个）。当您可以定义一个 `WHERE` 条件匹配确切的一行时，并且查询可以使用相关的 `unique index`，那么查找和错误处理可以非常高效地执行。

参见：`cardinality`，`unique constraint`，`unique index`。

**UPN**

参见：`user principal name`。

**user principal name**

Kerberos 中代表用户的命名实体的名称。

参见：`principal`。

## V

**variable-length type**

一种可变长度的数据类型。`VARCHAR`、`VARBINARY` 以及 `BLOB` 和 `TEXT` 类型都是可变长度类型。

InnoDB 将长度大于或等于 768 字节的定长字段视为可变长度字段，这些字段可以存储在页外。例如，如果字符集的最大字节长度大于 3，像 `CHAR(255)` 列这样的字段可能会超过 768 字节，如使用 `utf8mb4` 字符集时。

参见：`off-page column`，`overflow page`。

**victim**

在检测到死锁时自动选择的事务，被选择的事务将被回滚。InnoDB 会回滚更新行数最少的事务。

可以使用 `innodb_deadlock_detect` 配置选项禁用死锁检测。

参见：`deadlock`，`deadlock detection`，`innodb_lock_wait_timeout`，`transaction`。

**view**

一种存储的查询，当调用时会生成一个结果集。视图充当虚拟表。

**virtual column**

参见：`virtual generated column`。

**virtual generated column**

一种列，其值由列定义中包含的表达式计算得出。列值不存储，但在读取行时计算，并在任何 `BEFORE` 触发器之后立即计算。虚拟生成列不占用存储空间。InnoDB 支持在虚拟生成列上创建二级索引。

与存储生成列（`stored generated column`）相比，虚拟生成列不占用存储空间。

参见：`base column`，`generated column`，`stored generated column`。

**virtual index**

虚拟索引是一个或多个虚拟生成列或虚拟生成列与常规列或存储生成列的组合上的二级索引。有关详细信息，请参见《第 15.1.20.9 节，Secondary Indexes and Generated Columns》。

参见：`secondary index`，`stored generated column`，`virtual generated column`。

**Visual Studio**

有关 Visual Studio 受支持版本的参考，请参见以下内容：

- Connector/NET: Connector/NET 版本支持
- Connector/C++ 8.0: 平台支持和先决条件

参见：`Connector/C++`，`Connector/NET`。

## W

**wait**

当某个操作（如获取`锁`、`互斥锁（mutex）`或`闩锁（latch）`）无法立即完成时，InnoDB 会暂停并再次尝试。这种暂停机制足够复杂，以至于这种操作有一个专有名称，称为“等待（wait）”。单个线程的暂停是通过 InnoDB 内部调度、操作系统的 `wait()` 调用以及短时间的自旋循环组合来实现的。

在负载较重、事务较多的系统中，你可以使用 `SHOW INNODB STATUS` 命令或 `Performance Schema` 的输出来确定线程是否花费了太多时间在等待上，以及如何提高并发性。

参见：`concurrency`，`latch`，`lock`，`mutex`，`Performance Schema`，`spin`。

**warm backup**

在数据库运行时进行的备份，但在备份过程中限制了一些数据库操作。例如，表可能变为只读状态。对于繁忙的应用程序和网站，您可能更倾向于使用热备份。

参见：`backup`，`cold backup`，`hot backup`。

**warm up**

在系统启动后，在典型工作负载下运行一段时间，以便填充缓冲池和其他内存区域，使其达到正常条件下的状态。这一过程在 MySQL 服务器重启或受到新工作负载时会自然发生。

通常，你会在性能测试前运行一段时间的工作负载，以便在多次运行中确保一致的测试结果；否则，在第一次运行时，性能可能会因初始加载较低。

在 MySQL 5.6 中，你可以通过启用 `innodb_buffer_pool_dump_at_shutdown` 和 `innodb_buffer_pool_load_at_startup` 配置选项来加速热身过程，以便在重启后将缓冲池的内容重新加载到内存中。在 MySQL 5.7 中，这些选项默认已启用。参见《第 17.8.3.6 节，Saving and Restoring the Buffer Pool State》。

参见：`buffer pool`，`workload`。

**workload**

SQL 和其他数据库操作的组合和量级，由数据库应用程序在典型或峰值使用期间执行。在性能测试期间，你可以让数据库承受特定的工作负载，以识别瓶颈，或在容量规划期间使用。

参见：`bottleneck`，`CPU-bound`，`disk-bound`，`SQL`。

**write combining**

一种优化技术，当从 InnoDB 缓冲池中刷新脏页时减少写操作。如果页面中的某一行被多次更新，或者同一页面中的多行被更新，则所有这些更改都会在单个写操作中存储到数据文件中，而不是为每个更改执行一次写操作。

参见：`buffer pool`，`dirty page`，`flush`。

**XA**

一种用于协调分布式事务的标准接口，允许多个数据库参与同一个事务，同时保持 `ACID` 合规性。详情参见《第 15.3.8 节，XA Transactions》。

默认启用 `XA` 分布式事务支持。

参见：`ACID`，`binary log`，`commit`，`transaction`，`two-phase commit`。

## Y

**young**

InnoDB 缓冲池中页的一个特征，表示它最近已被访问，并因此在缓冲池的数据结构中移动，以免因 `LRU` 算法而过早刷新。该术语在与缓冲池相关的某些 `INFORMATION_SCHEMA` 列名中使用。

参见：`buffer pool`，`flush`，`INFORMATION_SCHEMA`，`LRU`，`page`。