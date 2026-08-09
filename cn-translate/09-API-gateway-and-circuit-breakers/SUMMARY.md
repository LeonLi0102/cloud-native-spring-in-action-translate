# 总结

本章涵盖了以下内容：

* **API 网关在分布式架构中提供多种好处** — 包括将内部服务与外部 API 解耦，提供集中处理安全、监控和弹性等横切关注点的便捷场所。
* **Spring Cloud Gateway 基于 Spring 响应式栈** — 提供 API 网关实现，并与 Spring Security、Spring Cloud Circuit Breaker、Spring Session 等 Spring 项目集成。
* **路由（Route）是 Spring Cloud Gateway 的核心** — 由唯一 ID、一组谓词（Predicate）、转发 URI 和一组过滤器（Filter）组成。
* **Retry 过滤器用于为特定路由配置重试尝试** — 提高对瞬时故障的容错能力。
* **RequestRateLimiter 过滤器集成 Spring Data Redis Reactive** — 限制在特定时间窗口内可接受的请求数量。
* **CircuitBreaker 过滤器基于 Spring Cloud Circuit Breaker 和 Resilience4J** — 定义断路器、时间限制器和针对特定路由的降级处理。
* **云原生应用应是无状态的** — 数据服务用于存储状态，如 PostgreSQL 用于持久化存储、Redis 用于缓存和会话数据。
* **Kubernetes Ingress 资源允许管理对集群内运行应用的外部访问** — 路由规则由 ingress controller（同样运行在集群中的应用）执行。
