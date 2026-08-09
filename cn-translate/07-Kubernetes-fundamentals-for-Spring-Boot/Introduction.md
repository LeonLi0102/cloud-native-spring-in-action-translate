# 第 7 章 Kubernetes 基础

本章内容：

* 从 Docker 过渡到 Kubernetes
* 在 Kubernetes 上部署 Spring Boot 应用程序
* 理解服务发现和负载均衡
* 构建可扩展和可弃置的应用程序
* 建立本地 Kubernetes 开发工作流
* 使用 GitHub Actions 验证 Kubernetes 清单

在上一章中，您学习了 Docker 以及镜像和容器的主要特征。借助 Buildpacks 和 Spring Boot，您可以用一条命令构建生产就绪的镜像，甚至不需要编写自己的 Dockerfile 或安装额外的工具。借助 Docker Compose，您可以同时控制多个应用程序，这对于微服务架构来说非常方便。但是，如果容器停止工作怎么办？如果运行容器的机器（Docker 主机）崩溃了怎么办？如果您想扩展应用程序怎么办？

本章将把 Kubernetes 引入您的工作流程中，以解决仅凭 Docker 无法解决的问题。

作为开发人员，配置和管理 Kubernetes 集群不是您的工作。您可能会使用云提供商（如 Amazon、Microsoft 或 Google）提供的托管服务，或由组织内专业团队（通常称为平台团队）管理的本地服务。目前，您将使用 minikube 创建的本地 Kubernetes 集群。在本书后面的内容中，您将使用云提供商提供的托管 Kubernetes 服务。

在我们的日常开发工作中，我们不希望花太多时间在基础设施问题上，但了解基础知识至关重要。Kubernetes 已成为事实上的编排工具和讨论容器化部署的通用语言。云供应商一直在 Kubernetes 之上构建平台，为开发者提供更好的体验。一旦您了解了 Kubernetes 的工作原理，使用这些平台就会变得非常简单，因为您已经熟悉了其语言和抽象。

本章将带您了解 Kubernetes 的主要功能，并教您如何为 Spring Boot 应用程序创建和管理 Pod、Deployment 和 Service。在此过程中，您将为应用程序启用优雅关闭，学习如何扩展它们，以及如何使用 Kubernetes 提供的服务发现和负载均衡功能。您还将学习使用 Tilt 自动化本地开发工作流，使用 Octant 可视化工作负载，以及验证 Kubernetes 清单。

> 注意：本章示例的源代码可在 Chapter07/07-begin 和 Chapter07/07-end 文件夹中找到，其中包含项目的初始和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
