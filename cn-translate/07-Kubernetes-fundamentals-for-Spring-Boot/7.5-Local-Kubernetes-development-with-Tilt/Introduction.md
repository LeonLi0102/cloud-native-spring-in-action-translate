## 7.5 使用 Tilt 进行本地 Kubernetes 开发

在前面的章节中，您学习了 Kubernetes 的基本概念，并使用了将应用程序部署到集群的基本对象：Pod、ReplicaSet、Deployment 和 Service。在定义了 Deployment 和 Service 清单后，您可能不想在每次更改时都手动重建容器镜像并使用 kubectl 客户端更新 Pod。幸运的是，您不必这样做。

本节将向您展示如何设置本地 Kubernetes 开发工作流，以自动化构建镜像和将清单应用到 Kubernetes 集群等步骤。这是实现 Kubernetes 平台内部开发循环的一部分。Tilt 负责许多基础设施关注点，让您可以更专注于应用程序的业务逻辑。我还将介绍 Octant，它将帮助您通过便捷的 GUI 可视化和管理 Kubernetes 对象。
