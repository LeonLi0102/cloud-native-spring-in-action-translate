# 第 7 章 Kubernetes 基础

本章内容：

* 从 Docker 过渡到 Kubernetes
* Spring Boot 的 Kubernetes Deployment
* 服务发现和负载均衡
* 部署 Polar Bookshop 到 Kubernetes

本章将 Kubernetes 引入您的工作流程，以解决仅 Docker 无法解决的问题。

作为开发人员，配置和管理 Kubernetes 集群不是您的工作。您可能会使用云提供商（如 Amazon、Microsoft 或 Google）提供的托管服务，或由组织内专业团队（通常称为平台团队）管理的本地服务。目前，您将使用 minikube 提供的本地 Kubernetes 集群。在本书后面，您将使用云提供商提供的托管 Kubernetes 服务。

在我们的日常开发工作中，我们不希望花太多时间在基础设施问题上，但了解基础知识至关重要。Kubernetes 已成为事实上的编排工具和讨论容器化部署的通用语言。

本章将带您了解 Kubernetes 的主要功能，并教您如何为 Spring Boot 应用程序创建和管理 Pod、Deployment 和 Service。在此过程中，您将为应用程序启用优雅关闭，学习如何扩展它们，以及如何使用 Kubernetes 提供的服务发现和负载均衡功能。

> 注意：本章示例的源代码在 Chapter07/07-begin 和 Chapter07/07-end 文件夹中，包含项目的初始和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
