> # Preface and Legal Notices
>

# 前言和法律声明

> This is the Reference Manual for the MySQL Database System, version 8.0, through release 8.0.32. Differences between minor versions of MySQL 8.0 are noted in the present text with reference to release numbers (8.0.*`x`*). For license information, see the [Legal Notices](https://dev.mysql.com/doc/refman/8.0/en/preface.html#legalnotice).
>

这是MySQL数据库系统的参考手册，版本号为8.0，适用于8.0.32版本及以下。本文所提到的MySQL 8.0各个小版本之间的差异以版本号（8.0.*`x`*）的形式进行说明。有关许可信息，请参阅[法律声明](#法律声明)。

> This manual is not intended for use with older versions of the MySQL software due to the many functional and other differences between MySQL 8.0 and previous versions. If you are using an earlier release of the MySQL software, please refer to the appropriate manual. For example, [*MySQL 5.7 Reference Manual*][mysql57ref] covers the 5.7 series of MySQL software releases.
>

本手册不适用于较旧版本的MySQL软件，因为MySQL 8.0与以前版本之间存在许多功能和其他差异。如果您正在使用MySQL软件的早期版本，请参考相应的手册。例如，[*MySQL 5.7参考手册*][mysql57ref]涵盖了MySQL软件5.7系列的发布版本。

[mysql57ref]: https://dev.mysql.com/doc/refman/5.7/en/

> **Licensing information—MySQL 8.0.** This product may include third-party software, used under license. If you are using a *Commercial* release of MySQL 8.0, see the [MySQL 8.0 Commercial Release License Information User Manual](https://downloads.mysql.com/docs/licenses/mysqld-8.0-com-en.pdf) for licensing information, including licensing information relating to third-party software that may be included in this Commercial release. If you are using a *Community* release of MySQL 8.0, see the [MySQL 8.0 Community Release License Information User Manual](https://downloads.mysql.com/docs/licenses/mysqld-8.0-gpl-en.pdf) for licensing information, including licensing information relating to third-party software that may be included in this Community release.

**许可信息 - MySQL 8.0。**本产品可能包括经许可使用的第三方软件。如果您使用的是MySQL 8.0的商业版本，请参阅[MySQL 8.0商业版许可信息用户手册](https://downloads.mysql.com/docs/licenses/mysqld-8.0-com-en.pdf)，了解许可信息，包括可能包含在此商业版本中的第三方软件的许可信息。如果您使用的是MySQL 8.0社区版，请参阅MySQL 8.0社区版许可信息用户手册，了解许可信息，包括可能包含在此社区版本中的第三方软件的许可信息。

> **Licensing information—MySQL NDB Cluster 8.0.** If you are using a *Commercial* release of MySQL NDB Cluster 8.0, see the[MySQL NDB Cluster 8.0 Commercial Release License Information User Manual][cluster-8.0-com-en] for licensing information, including licensing information relating to third-party software that may be included in this Commercial release. If you are using a *Community* release of MySQL NDB Cluster 8.0, see the [MySQL NDB Cluster 8.0 Community Release License Information User Manual][cluster-8.0-gpl-en] for licensing information, including licensing information relating to third-party software that may be included in this Community release.

**许可信息 - MySQL NDB Cluster 8.0。**如果您使用的是MySQL NDB Cluster 8.0的商业版本，请参阅[MySQL NDB Cluster 8.0商业版许可信息用户手册][cluster-8.0-com-en]，了解许可信息，包括可能包含在此商业版本中的第三方软件的许可信息。如果您使用的是MySQL NDB Cluster 8.0社区版，请参阅[MySQL NDB Cluster 8.0社区版许可信息用户手册][cluster-8.0-gpl-en]，了解许可信息，包括可能包含在此社区版本中的第三方软件的许可信息。

[cluster-8.0-com-en]: https://downloads.mysql.com/docs/licenses/cluster-8.0-com-en.pdf
[cluster-8.0-gpl-en]: https://downloads.mysql.com/docs/licenses/cluster-8.0-gpl-en.pdf

> ## Legal Notices

## 法律声明

> Copyright © 1997, 2023, Oracle and/or its affiliates.

版权所有 © 1997、2023 Oracle 及其附属公司。

> This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

本软件及相关文档受许可协议限制使用和披露，并受知识产权法保护。除非在您的许可协议明确允许或法律许可的情况下，您不得以任何形式或任何方式使用、复制、重制、翻译、广播、修改、授权、传输、分发、展示、执行、发布或显示任何部分。禁止对本软件进行逆向工程、反汇编或反编译，除非在法律上需要进行互操作性的情况下。

> The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

本文所包含的信息如有更改，恕不另行通知，并且不保证无误。如果您发现任何错误，请以书面形式向我们报告。

> If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, then the following notice is applicable:

如果本软件或相关文档交付给美国政府或代表美国政府许可使用，那么以下通知适用：

> U.S. GOVERNMENT END USERS: Oracle programs (including any operating system, integrated software, any programs embedded, installed or activated on delivered hardware, and modifications of such programs) and Oracle computer documentation or other Oracle data delivered to or accessed by U.S. Government end users are "commercial computer software" or "commercial computer software documentation" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, the use, reproduction, duplication, release, display, disclosure, modification, preparation of derivative works, and/or adaptation of i) Oracle programs (including any operating system, integrated software, any programs embedded, installed or activated on delivered hardware, and modifications of such programs), ii) Oracle computer documentation and/or iii) other Oracle data, is subject to the rights and limitations specified in the license contained in the applicable contract. The terms governing the U.S. Government's use of Oracle cloud services are defined by the applicable contract for such services. No other rights are granted to the U.S. Government.

美国政府最终用户：Oracle程序（包括任何操作系统、集成软件、任何嵌入、安装或激活在交付的硬件上的程序以及这些程序的修改）和Oracle计算机文档或其他Oracle数据，适用于适用的联邦采购条例和机构特定的补充规定的“商业计算机软件”或“商业计算机软件文档”。因此，i) Oracle程序（包括任何操作系统、集成软件、任何嵌入、安装或激活在交付的硬件上的程序以及这些程序的修改）、ii）Oracle计算机文档和/或iii）其他Oracle数据的使用、复制、复制、发布、显示、披露、修改、派生作品的准备和/或调整，受限于适用合同中包含的许可权利和限制。美国政府使用Oracle云服务的条款由适用该服务的合同定义。未授予美国政府其他权利。

> This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.
>

本软件或硬件是为各种信息管理应用程序的通用使用而开发的。它没有为任何本质上危险的应用程序开发或意图，包括可能产生个人受伤风险的应用程序。如果您在危险的应用程序中使用此软件或硬件，则应负责采取所有适当的故障保护、备份、冗余和其他措施，以确保其安全使用。Oracle公司及其附属公司不对因在危险的应用程序中使用此软件或硬件而导致的任何损害负责。

> Oracle, Java, and MySQL are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Oracle、Java和MySQL是Oracle及/或其附属公司的注册商标。其他名称可能是其各自所有者的商标。

> Intel and Intel Inside are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Epyc, and the AMD logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

Intel和Intel Inside是Intel Corporation的商标或注册商标。所有SPARC商标均在许可下使用，是SPARC International，Inc.的商标或注册商标。AMD、Epyc和AMD徽标是Advanced Micro Devices的商标或注册商标。UNIX是The Open Group的注册商标。

> This software or hardware and documentation may provide access to or information about content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services unless otherwise set forth in an applicable agreement between you and Oracle. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services, except as set forth in an applicable agreement between you and Oracle.

该软件或硬件及文档可能提供第三方内容、产品和服务的访问或信息。Oracle公司及其附属公司不对第三方内容、产品和服务的任何种类的担保负责，除非您与Oracle之间的适用协议另有规定。Oracle公司及其附属公司不会对因您访问或使用第三方内容、产品或服务而产生的任何损失、费用或损害负责，除非您与Oracle之间的适用协议另有规定。

> This documentation is NOT distributed under a GPL license. Use of this documentation is subject to the following terms:

此文档不是在GPL许可下发布的。使用此文档需要遵守以下条款：

> You may create a printed copy of this documentation solely for your own personal use. Conversion to other formats is allowed as long as the actual content is not altered or edited in any way. You shall not publish or distribute this documentation in any form or on any media, except if you distribute the documentation in a manner similar to how Oracle disseminates it (that is, electronically for download on a Web site with the software) or on a CD-ROM or similar medium, provided however that the documentation is disseminated together with the software on the same medium. Any other use, such as any dissemination of printed copies or use of this documentation, in whole or in part, in another publication, requires the prior written consent from an authorized representative of Oracle. Oracle and/or its affiliates reserve any and all rights to this documentation not expressly granted above.

您可以创建此文档的打印副本，仅供个人使用。只要实际内容未经修改或编辑，可以将其转换为其他格式。除非您以类似Oracle发布软件的方式（即通过软件的网站电子下载）或在CD-ROM或类似介质上分发文档（但是必须与软件一起在同一媒介上分发文档），否则您不得以任何形式或媒介发布或分发此文档。任何其他用途，如在另一出版物中全部或部分地传播打印副本或使用此文档，都需要得到Oracle授权代表的事先书面同意。Oracle和/或其附属公司保留此文档未明示授权的所有权利。

> ## Documentation Accessibility

## 本文档无障碍性信息

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website athttps://www.oracle.com/corporate/accessibility/.

关于 Oracle 对无障碍性的承诺的信息，请访问 Oracle 无障碍性计划网站 <https://www.oracle.com/corporate/accessibility/>。

> ## Access to Oracle Support for Accessibility
>

## 获取支持的无障碍性访问

> Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab.
>

已购买支持的 Oracle 客户可以通过我的 Oracle 支持访问电子支持。有关详细信息，请访问 <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>。





