# 总结

本章涵盖了以下内容：

* **事件驱动架构是分布式系统通过产生和消费事件进行交互的架构** — 事件是系统中发生的相关的状态变更。
* **在发布/订阅（pub/sub）模型中** — 生产者发布事件，事件被发送给所有订阅者进行消费。
* **事件处理平台（如 RabbitMQ 和 Kafka）负责从生产者收集事件** — 进行路由并分发给感兴趣的消费者。
* **在 AMQP 协议中，生产者向 Broker 中的 Exchange 发送消息** — Exchange 根据特定路由算法将消息转发到队列。
* **在 AMQP 协议中，消费者从 Broker 中的队列接收消息** — 消息是由键/值属性和二进制负载组成的数据结构。
* **RabbitMQ 是基于 AMQP 协议的消息代理** — 可用于实现基于 pub/sub 模型的事件驱动架构，提供高可用性、弹性和数据复制。
* **Spring Cloud Function 允许使用标准 Java Function、Supplier 和 Consumer 接口实现业务逻辑** — 提供透明类型转换和函数组合等特性。
* **Spring Cloud Function 中的函数可通过多种方式暴露和与外部系统集成** — 作为 REST 端点、打包部署到 FaaS 平台（Knative、AWS Lambda、Azure Function、Google Cloud Functions）或绑定到消息通道。
* **Spring Cloud Stream 构建在 Spring Cloud Function 之上** — 提供将函数与外部消息系统（如 RabbitMQ 或 Kafka）集成所需的所有管道工作。
* **实现函数后无需修改代码** — 只需添加 Spring Cloud Stream 依赖并配置即可。
* **在 Spring Cloud Stream 中，目标绑定器（Destination Binder）提供与外部消息系统的集成** — 目标绑定（Destination Binding，输入和输出）将应用中的生产者和消费者与消息代理中的 Exchange 和队列桥接。
* **函数和消费者在新消息到达时自动激活** — 供应商（Supplier）需要显式激活，例如通过向目标绑定显式发送消息。
