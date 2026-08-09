# 第 5 章 云中的数据持久化和管理

本章内容：

* 理解云原生系统中的数据库
* 使用 Spring Data JDBC 实现数据持久化
* 使用 Spring Boot 和 Testcontainers 测试数据持久化
* 使用 Flyway 管理生产环境中的数据库

在第 1 章中，我区分了云原生系统中的应用程序服务和数据服务。到目前为止，我们一直在处理应用程序服务，它们应该是无状态的，以便在云环境中良好运行。然而，如果不在某处存储状态或数据，大多数应用程序都没有意义。例如，我们在第 3 章构建的 Catalog Service 应用程序没有持久化存储机制，因此您无法真正用它来管理图书目录。一旦关闭它，您添加到目录中的所有图书都会消失。作为有状态的后果，您甚至无法水平扩展该应用程序。

状态是在您关闭服务并启动新实例时应保留的一切。数据服务是系统中有状态的组件。例如，它们可以是像 PostgreSQL、Cassandra 和 Redis 这样的数据存储，也可以是像 RabbitMQ 和 Apache Kafka 这样的消息系统。

本章将介绍云原生系统的数据库以及在云中持久化数据的主要方面。我们将依赖 Docker 在本地环境中运行 PostgreSQL，但在生产环境中，我们将用云平台提供的托管服务来替换它。然后，我们将使用 Spring Data JDBC 为 Catalog Service 添加数据持久化层。最后，我将介绍使用 Flyway 在生产环境中管理和演进数据库的一些常见问题。

> 注意：本章示例的源代码可在 GitHub 上的 Chapter05/05-begin、Chapter05/05-intermediate 和 Chapter05/05-end 文件夹中找到，包含项目的初始、中间和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
