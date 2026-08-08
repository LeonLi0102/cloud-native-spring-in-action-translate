# 第 16 章 Serverless、GraalVM 和 Knative

本章内容：

* 理解 Serverless 架构
* 使用 GraalVM 原生镜像
* 使用 Knative 部署 Serverless 应用
* 实现函数即服务（FaaS）

Serverless 是一种云原生开发模型，允许开发人员构建和运行应用程序，而无需管理服务器。虽然服务器仍然存在，但它们对开发人员是抽象的。

GraalVM 是一个高性能的多语言虚拟机，可以将 Java 应用程序编译为原生镜像，显著减少启动时间和内存占用。

Knative 是一个基于 Kubernetes 的平台，提供了一组组件来部署和管理 Serverless 工作负载。它支持自动缩放到零、流量分割和事件驱动架构。

这些技术共同帮助开发人员构建更高效、更经济的云原生应用程序。

> 注意：本章示例的源代码在 Chapter16/16-begin 和 Chapter16/16-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
