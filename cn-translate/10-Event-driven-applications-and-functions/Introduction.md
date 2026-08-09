# 第 10 章 事件驱动应用和函数

**本章内容**

* 理解事件驱动架构
* 使用 RabbitMQ 作为消息代理
* 使用 Spring Cloud Function 实现函数
* 使用 Spring Cloud Stream 处理事件
* 使用 Spring Cloud Stream 产生和消费事件

在前面的章节中，我们构建了一个分布式应用系统，这些应用按照请求/响应模式进行交互，这是一种同步通信方式。您已经看到了如何以命令式和响应式两种方式来设计这种交互。在第一种情况下，处理线程会阻塞，等待 I/O 操作的响应。在第二种情况下，线程不会等待，一旦收到响应，任何可用的线程都会异步处理它。

即使响应式编程范式允许您订阅生产者并异步处理传入的数据，两个应用之间的交互仍然是同步的。第一个应用（客户端）向第二个应用（服务器）发送请求，并期望在短时间内收到响应。客户端如何处理响应（命令式或响应式）是一个实现细节，不会影响交互本身。无论如何，都期望收到响应。

云原生应用程序应该是松散耦合的。微服务专家 Sam Newman 识别了几种不同类型的耦合，包括实现耦合、部署耦合和时间耦合¹。让我们考虑一下到目前为止一直在处理的 Polar Bookshop 系统。

> ¹ 参见 Sam Newman，《Monolith to Microservices》（O'Reilly，2019）。

我们可以更改任何应用程序的实现，而无需更改其他应用程序。例如，我们可以使用响应式范式重新实现 Catalog Service，而不会影响 Order Service。通过使用像 REST API 这样的服务接口，我们隐藏了实现细节，提高了松散耦合性。所有应用程序都可以独立部署，它们没有耦合，从而降低了风险并提高了敏捷性。

然而，如果您思考一下我们迄今为止构建的应用程序如何交互，您会注意到它们需要系统的其他组件可用。Order Service 需要 Catalog Service 来确保用户能够成功订购一本书。我们知道故障随时可能发生，因此我们采用了多种策略来确保在逆境中保持弹性，或者至少确保功能优雅降级。这是时间耦合的后果：Order Service 和 Catalog Service 需要同时可用才能满足系统需求。

事件驱动架构描述了通过产生和消费事件进行交互的分布式系统。交互是异步的，解决了时间耦合的问题。本章将介绍事件驱动架构和事件代理的基础知识。然后，您将学习如何使用函数式编程范式和 Spring Cloud Function 实现业务逻辑。最后，您将使用 Spring Cloud Stream 通过 RabbitMQ 将函数暴露为消息通道，通过发布/订阅（pub/sub）模型构建事件驱动应用程序。

> **注意** 本章示例的源代码可在 Chapter10/10-begin、Chapter10/10-intermediate 和 Chapter10/10-end 文件夹中找到，分别包含项目的初始、中间和最终状态（[https://github.com/ThomasVitale/cloud-native-spring-in-action](https://github.com/ThomasVitale/cloud-native-spring-in-action)）。
