# 总结

本章涵盖了以下内容：

* **可观测性（Observability）是云原生应用的一个属性** — 衡量我们能从应用输出推断其内部状态的程度。
* **监控（Monitoring）是控制已知故障状态** — 可观测性超越监控，允许我们对未知提出问题。
* **日志（Log）是软件应用中随时间发生的离散记录** — Spring Boot 通过 SLF4J 支持日志，SLF4J 为最常见日志库提供门面（Facade）。
* **默认情况下日志通过标准输出打印** — 符合 15-Factor 方法论的建议。
* **使用 Grafana 可观测性栈** — Fluent Bit 收集所有应用产生的日志并转发给 Loki 存储，然后使用 Grafana 导航日志。
* **应用应暴露健康端点以检查其状态** — Spring Boot Actuator 暴露总体健康端点，显示应用及其可能使用的所有组件或服务的状态。
* **Spring Boot Actuator 提供专用端点作为 Kubernetes 的存活探针（Liveness Probe）和就绪探针（Readiness Probe）** — 存活探针宕机意味着应用进入不可恢复的故障状态，Kubernetes 会尝试重启；就绪探针宕机时应用未准备好处理请求，Kubernetes 会停止流向该实例的流量。
* **指标（Metric）是按固定时间间隔测量的应用数值数据** — Spring Boot Actuator 利用 Micrometer 门面检测 Java 代码、生成指标并通过专用端点暴露。
* **当 classpath 中有 Prometheus 客户端时** — Spring Boot 可暴露 Prometheus 或 OpenMetrics 格式的指标。
* **使用 Grafana 可观测性栈** — Prometheus 聚合并存储所有应用的指标，使用 Grafana 查询指标、设计仪表盘和设置告警。
* **分布式追踪（Distributed Tracing）是一种跟踪请求在分布式系统中流动的技术** — 让我们定位分布式系统中错误发生的位置并排查性能问题。
* **追踪（Trace）以 Trace ID 为特征，由多个跨度（Span）组成** — 表示事务中的步骤。
* **OpenTelemetry 项目包含为最常见 Java 库生成追踪和跨度的 API 和插桩** — OpenTelemetry Java Agent 是一个 JAR 制品，可附加到任何 Java 应用，动态注入必要的字节码以捕获追踪和跨度。
* **使用 Grafana 可观测性栈** — Tempo 聚合并存储所有应用的指标，使用 Grafana 查询追踪并将其与日志关联。
* **Spring Boot Actuator 提供管理和监控端点** — 满足对应用进行管理和监控的任何需求。
