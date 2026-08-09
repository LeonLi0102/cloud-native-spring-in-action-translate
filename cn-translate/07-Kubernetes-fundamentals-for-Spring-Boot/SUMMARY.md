# 总结

本章涵盖了以下内容：

* **当系统需要可扩展性和弹性时，可使用 Kubernetes** — Docker 适用于单机单实例容器运行，但 Kubernetes 提供跨机器集群扩展容器的能力。
* **Kubernetes 提供在容器故障和机器宕机时确保弹性的所有功能** — Pod 是 Kubernetes 中最小的可部署单元。
* **通过 Deployment 对象声明应用的期望状态** — Kubernetes 会确保实际状态匹配期望状态，包括保持所需数量的副本始终运行。
* **服务发现（Service Discovery）和负载均衡允许动态建立服务间交互** — 可在客户端（如 Spring Cloud Netflix Eureka）或服务器端（如 Kubernetes）管理。
* **Kubernetes 通过 Service 对象提供原生的服务发现和负载均衡功能** — 每个 Service 名称可用作 DNS 名称，Kubernetes 会将名称解析为 Service IP 地址并最终转发到可用实例之一。
* **可通过定义两个 YAML 清单将 Spring Boot 应用部署到 Kubernetes 集群** — 一个用于 Deployment 对象，一个用于 Service 对象。
* **使用 kubectl apply -f <文件名> 命令从文件创建对象** — kubectl 客户端是与 Kubernetes 集群交互的主要工具。
* **云原生应用应具备可丢弃性（快速启动和优雅关闭）和无状态性** — 依赖数据服务存储状态。
* **优雅关闭（Graceful Shutdown）由 Spring Boot 和 Kubernetes 共同支持** — 是可扩展应用的重要方面。
* **Kubernetes 使用 ReplicaSet 控制器复制应用 Pod** — 保持它们持续运行。
* **Tilt 是自动化本地开发工作流的工具** — 您编写应用代码，Tilt 负责构建镜像、部署到本地 Kubernetes 集群并在代码变更时保持更新，通过 tilt up 启动。
* **Octant 仪表盘可视化 Kubernetes 工作负载** — 不仅适用于本地集群检查和故障排除，也适用于远程集群。
* **Kubeval 是验证 Kubernetes 清单的便捷工具** — 包含在部署管道中时尤为有用。
