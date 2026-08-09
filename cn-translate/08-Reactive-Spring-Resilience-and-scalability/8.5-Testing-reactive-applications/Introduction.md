## 8.5 使用 Spring、Reactor 和 Testcontainers 测试响应式应用程序

测试是软件开发的关键部分，响应式应用程序也不例外。在本节中，你将学习如何测试 Order Service 的不同组件，包括仓库、服务和控制器。你还将看到如何使用 Testcontainers 在集成测试中运行真实的 PostgreSQL 数据库。

响应式应用程序的测试与命令式应用程序略有不同，因为你需要处理异步和非阻塞操作。Spring Boot 和 Project Reactor 提供了专门用于测试响应式应用程序的工具。
