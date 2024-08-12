# MySQL 术语表

这些术语常用于MySQL数据库服务器的信息中。

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