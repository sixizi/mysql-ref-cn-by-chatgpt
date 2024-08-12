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

### BLOB  
一种SQL数据类型（`TINYBLOB`、`BLOB`、`MEDIUMBLOB`和`LONGBLOB`），用于包含任意大小的二进制数据对象。用于存储文档、图像、声音文件和其他不能轻易分解为MySQL表中的行和列的各种信息。在MySQL应用程序中处理BLOB的技术因每个`Connector`和`API`而异。`MySQL Connector/ODBC`将BLOB值定义为`LONGVARBINARY`。对于大型自由格式的字符数据集合，业界术语是`CLOB`，由MySQL的`TEXT`数据类型表示。

参见 `API`, `CLOB`, `connector`, `Connector/ODBC`。

### bottleneck  
系统中尺寸或容量受限的部分，限制整体吞吐量的部分。例如，内存区域可能小于所需大小；对单一必需资源的访问可能会阻止多个CPU内核同时运行；或等待磁盘I/O完成可能会阻止CPU充分运转。消除瓶颈往往可以提高并发性。例如，能够拥有多个`InnoDB`缓冲池实例可以减少多个会话同时读取和写入缓冲池时的竞争。

参见 `buffer pool`, `concurrency`。

### bounce  
关闭操作后立即重新启动。理想情况下，经过相对较短的预热期后，性能和吞吐量迅速恢复到较高水平。

参见 `shutdown`。

### buddy allocator  
一种用于管理`InnoDB`缓冲池中不同大小页面的机制。

参见 `buffer pool`, `page`, `page size`。

### buffer  
用于临时存储的内存或磁盘区域。数据缓存在内存中，以便可以通过少量大型I/O操作而不是许多小型I/O操作高效地写入磁盘。数据缓存在磁盘上，以提高可靠性，即使在最糟糕的时间点发生崩溃或其他故障时，数据也可以恢复。`InnoDB`使用的主要缓冲区类型是缓冲池、双写缓冲区和更改缓冲区。

参见 `buffer pool`, `change buffer`, `crash`, `doublewrite buffer`。

### buffer pool  
一个保存`InnoDB`表和索引缓存数据的内存区域。为了提高大容量读取操作的效率，缓冲池被分为可以容纳多行的页面。为了提高缓存管理的效率，缓冲池实现为一个页面链表；使用`LRU`算法的变体将很少使用的数据从缓存中逐出。在具有大内存的系统上，您可以通过将缓冲池分为多个缓冲池实例来提高并发性。

几个`InnoDB`状态变量、`INFORMATION_SCHEMA`表和`performance_schema`表有助于监控缓冲池的内部工作。从MySQL 5.6开始，您可以通过在服务器关闭时保存缓冲池状态，并在服务器启动时将缓冲池恢复到相同状态，来避免在重启服务器后经历较长的预热期，特别是对于具有大缓冲池的实例。参见[17.8.3.6节 “Saving and Restoring the Buffer Pool State”](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html#innodb-buffer-pool-saving)。

参见 `buffer pool instance`, `LRU`, `page`, `warm up`。

### buffer pool instance  
缓冲池可以分为的多个区域中的任意一个，由`innodb_buffer_pool_instances`配置选项控制。`innodb_buffer_pool_size`指定