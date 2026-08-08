# 第 8 章 响应式 Spring：韧性和可扩展性

本章内容：

* 使用 Reactor 和 Spring 的异步非阻塞架构
* 使用 Spring WebFlux 构建响应式 REST API
* 使用 Spring Data R2DBC 进行响应式数据持久化
* 使用 resilience4j 实现弹性模式

另一个重要的系统功能是购买图书的可能性。在本章中，您将开始处理 Order Service 应用程序。这个新组件不仅与数据库交互，还与 Catalog Service 交互。当您的应用程序大量依赖 I/O 操作（如数据库调用或与 HTTP 请求/响应通信等其他服务的交互）时，Catalog Service 中使用的每请求一线程模型开始暴露其技术限制。

响应式应用程序以异步和非阻塞方式运行，这意味着计算资源被更有效地使用。这在云中是一个巨大的优势，因为您按使用付费。当线程向后端服务发送调用时，它不会空闲等待，而是继续执行其他操作。这消除了线程数和并发请求数之间的线性依赖关系，导致更具可扩展性的应用程序。

本章将重点介绍使用响应式范式为云构建有韧性、可扩展和高效的应用程序。首先，我将介绍事件循环模型以及 Reactive Streams、Project Reactor 和 Spring 响应式栈的主要特性。然后您将使用 Spring WebFlux 和 Spring Data R2DBC 构建响应式 Order Service 应用程序。

> 注意：本章示例的源代码在 Chapter08/08-begin 和 Chapter08/08-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
