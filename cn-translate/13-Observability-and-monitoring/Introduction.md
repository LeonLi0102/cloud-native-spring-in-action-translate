# 第 13 章 可观测性和监控

本章内容：

* 实现分布式追踪
* 使用 Micrometer 收集指标
* 集成 Prometheus 和 Grafana
* 使用 Spring Boot Actuator 监控应用

可观测性是系统能够从外部输出推断其内部状态的程度。在云原生环境中，可观测性由三个支柱组成：日志（Logs）、指标（Metrics）和追踪（Traces）。

* **日志** — 记录应用程序中发生的事件
* **指标** — 随时间测量的数值数据
* **追踪** — 请求在分布式系统中传播的路径

Spring Boot Actuator 提供了生产就绪的功能来监控和管理应用程序。Micrometer 是一个指标收集库，可以与 Prometheus、Grafana 等系统集成。

> 注意：本章示例的源代码在 Chapter13/13-begin 和 Chapter13/13-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
