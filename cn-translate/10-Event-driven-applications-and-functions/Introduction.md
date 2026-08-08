# 第 10 章 事件驱动应用和函数

本章内容：

* 使用 Spring Cloud Stream 实现事件驱动架构
* 使用 Spring Cloud Function 构建函数式应用
* 与 Apache Kafka 和 RabbitMQ 集成
* 实现事件溯源模式

事件驱动架构是一种软件设计模式，其中系统的组件通过产生、消费和响应事件来进行通信。这种解耦的通信方式使系统更具可扩展性、弹性和可维护性。

Spring Cloud Stream 是一个构建事件驱动微服务的框架，它简化了与消息代理（如 Apache Kafka 和 RabbitMQ）的集成。

Spring Cloud Function 允许您以函数式风格编写业务逻辑，并将其部署到各种平台。

> 注意：本章示例的源代码在 Chapter10/10-begin 和 Chapter10/10-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
