# 第 9 章 API 网关和断路器

本章内容：

* 边缘服务器和 Spring Cloud Gateway
* 使用 Spring Cloud Gateway 构建 API 网关
* 使用 Resilience4j 实现断路器模式
* 实现重试、超时和限流

由于 API 网关是系统的入口点，它也是处理横切关注点（如安全性、监控和韧性）的绝佳位置。边缘服务器是系统边缘的应用程序，实现 API 网关和横切关注点等方面。

您可以配置断路器以防止调用下游服务时的级联故障。可以为所有对内部服务的调用定义重试和超时。可以控制入口流量并执行配额策略。还可以在边缘实现身份验证和授权，并将令牌传递给下游服务。

Spring Cloud Gateway 大大简化了构建边缘服务的过程，专注于简单性和生产力。由于它基于响应式栈，它可以高效扩展以处理系统边缘自然发生的高工作负载。

> 注意：本章示例的源代码在 Chapter09/09-begin 和 Chapter09/09-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
