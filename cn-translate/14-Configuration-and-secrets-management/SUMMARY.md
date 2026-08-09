# 总结

本章涵盖了以下内容：

* **使用 Spring Security 保护 Spring Cloud Config Server 构建的配置服务器** — 例如可要求客户端使用 HTTP Basic 认证访问服务器暴露的配置端点。
* **Spring Boot 应用中的配置数据可通过调用 `/actuator/refresh` 端点重新加载** — 该端点由 Spring Boot Actuator 暴露。
* **通过 Spring Cloud Bus 将配置刷新操作传播给系统中的其他应用** — 实现配置的自动同步。
* **Spring Cloud Config Server 提供 Monitor 模块** — 暴露 `/monitor` 端点，代码仓库提供者可通过 Webhook 在配置仓库推送新变更时调用。结果是所有受配置变更影响的应用将由 Spring Cloud Bus 触发重新加载配置，整个过程自动完成。
* **管理密钥（Secret）是任何软件系统的关键任务** — 出错时后果严重。
* **Spring Cloud Config 提供加密和解密功能** — 使用对称或非对称密钥安全处理配置仓库中的密钥。
* **也可使用云提供商（Azure、AWS、Google Cloud）提供的密钥管理解决方案** — 通过 Spring Cloud Azure、Spring Cloud AWS 和 Spring Cloud GCP 与 Spring Boot 集成。
* **HashiCorp Vault 是另一种选择** — 可直接通过 Spring Vault 项目配置所有 Spring Boot 应用，或将其作为 Spring Cloud Config Server 的后端。
* **Spring Boot 应用部署到 Kubernetes 集群时** — 可通过 ConfigMap（非敏感配置数据）和 Secret（敏感配置数据）进行配置。
* **可将 ConfigMap 和 Secret 用作环境变量来源或作为卷挂载到容器** — 后者是首选方式，由 Spring Boot 原生支持。
* **Secret 并不保密** — 其中包含的数据默认未加密，不应放入版本控制并包含在仓库中。
* **平台团队负责保护密钥** — 例如使用 Sealed Secrets 项目加密密钥使其可纳入版本控制。
* **Kustomize 提供了便捷的方式来管理、部署、配置和升级 Kubernetes 中的应用** — 提供生成器构建 ConfigMap 和 Secret，以及在它们更新时触发滚动重启的能力。
* **Kustomize 配置定制方法基于基础（Base）和覆盖层（Overlay）的概念** — 覆盖层构建在基础清单之上，任何定制通过补丁（Patch）应用，可定义自定义环境变量、ConfigMap、容器镜像和副本的补丁。
