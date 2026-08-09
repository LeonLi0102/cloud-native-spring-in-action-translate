# 总结

本章涵盖了以下内容：

* **响应式范式可以提升应用的可扩展性、弹性和成本效益** — 当预期高流量和高并发且计算资源较少时尤为有效，代价是较陡峭的初始学习曲线。
* **根据需求在非响应式和响应式栈之间做选择** — 没有银弹，需权衡利弊。
* **Spring WebFlux 基于 Project Reactor** — 是 Spring 响应式栈的核心，支持异步、非阻塞 I/O。
* **响应式 RESTful 服务可通过 @RestController 类或路由函数（Router Function）实现** — 两种方式都支持声明式路由。
* **Spring WebFlux 切片可通过 @WebFluxTest 注解进行测试** — 与 Spring MVC 的 @WebMvcTest 类似。
* **Spring Data R2DBC 提供基于 R2DBC 驱动的响应式数据持久化支持** — 方法与任何 Spring Data 项目相同：数据库驱动、实体和仓库。
* **数据库模式可通过 Flyway 管理** — 响应式应用的持久化切片可通过 @DataR2dbcTest 注解和 Testcontainers 进行测试。
* **系统的弹性（Resilience）体现在面对故障时仍能持续提供服务** — 有时无法完全做到，至少确保服务优雅降级。
* **WebClient 基于 Project Reactor** — 使用 Mono 和 Flux 发布者。
* **通过 Reactor 操作符配置超时、重试、降级和错误处理** — 使交互对下游服务故障或网络问题更具弹性。
