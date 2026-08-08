## 7.1 从 Docker 过渡到 Kubernetes

使用 Docker Compose，您可以同时管理多个容器的部署，包括网络和存储的配置。这非常强大，但它仅限于单台机器。

使用 Docker CLI 和 Docker Compose，交互与单个 Docker 守护进程发生，该守护进程管理单台机器（称为 Docker 主机）上的 Docker 资源。此外，无法扩展容器。当您需要可扩展性和韧性等云原生属性时，所有这些都受到了限制。

在第 2 章中，您了解到当从 Docker 等容器运行时过渡到 Kubernetes 等编排平台时，我们会改变观点。使用 Docker，我们将容器部署到单个机器。使用 Kubernetes，我们将容器部署到机器集群，实现可扩展性和韧性。

Kubernetes 客户端使用 API 与 Kubernetes Control Plane 交互，Control Plane 负责在 Kubernetes 集群中创建和管理对象。在新场景中，我们仍然向单个实体发送命令，但它作用于多台机器而不是仅一台。

图 7.2 中显示的主要组件：

* **集群（Cluster）** — 运行容器化应用程序的一组节点。它托管 Control Plane 并包含一个或多个工作节点。
* **Control Plane** — 暴露 API 和接口以定义、部署和管理 Pod 生命周期的集群组件。它包含实现编排器典型功能的所有基本元素，如集群管理、调度和健康监控。
* **工作节点（Worker nodes）** — 提供 CPU、内存、网络和存储等容量的物理或虚拟机，以便容器可以运行并连接到网络。
* **Pod** — 包装应用程序容器的最小可部署单元。
