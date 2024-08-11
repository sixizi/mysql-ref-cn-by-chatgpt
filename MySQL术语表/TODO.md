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