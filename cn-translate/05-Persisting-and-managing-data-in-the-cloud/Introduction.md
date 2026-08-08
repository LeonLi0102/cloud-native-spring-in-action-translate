# 第 5 章 云中的数据持久化和管理

本章内容：

* 云原生系统的数据库
* 使用 Spring Data JDBC 进行数据持久化
* 使用 Spring 和 Testcontainers 测试数据持久化
* 使用 Flyway 管理生产环境中的数据库

在前面的章节中，我们构建了一个 RESTful 应用程序来管理图书目录。作为实现的一部分，我们定义了一些数据来配置应用程序的某些方面。现在，我们需要将这些数据持久化到数据库中。

在本章中，我们将为 Catalog Service 应用程序添加数据持久化功能。首先了解云原生环境中的数据服务，然后使用 Spring Data JDBC 和 PostgreSQL 实现数据持久化，最后使用 Testcontainers 进行测试，使用 Flyway 管理数据库迁移。
