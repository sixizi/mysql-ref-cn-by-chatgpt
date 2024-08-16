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
一种涉及硬件相关方面（如磁盘块、内存页、文件、位、磁盘读取等）的操作类型。通常