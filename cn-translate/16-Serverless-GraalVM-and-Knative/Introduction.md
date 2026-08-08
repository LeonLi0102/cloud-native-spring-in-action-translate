# 第 16 章 Serverless、GraalVM 和 Knative

本章内容：

* 理解原生镜像（native images）和 GraalVM
* 在 Spring Boot 应用中使用 Spring Native
* 使用 Spring Cloud Function 实现 Serverless 应用
* 使用 Knative 在 Kubernetes 上部署 Serverless 应用

云原生应用对启动速度和资源占用的要求越来越高，尤其是 Serverless 场景。你可能还记得第 1 章讲过：Serverless 让您可以把更多职责交给平台，让开发人员专注于应用本身。有些应用天生是事件驱动的，并不是时刻都在忙于处理请求；或者它们会有突然的高峰，需要更多计算资源。Serverless 平台提供完全托管的自动伸缩能力，可以把应用实例缩到零，这样在没有需要处理的内容时，您就不用支付任何费用。本章您将学习更多关于 Serverless 模型的细节，并用 Spring Native 和 Spring Cloud Function 构建一个 Serverless 应用。最后，您将看到如何使用 Knative（一个基于 Kubernetes 的 Serverless 平台）来部署应用。

> 注意：本章示例的源代码可以在 Chapter16/16-begin 和 Chapter16/16-end 文件夹中找到，分别包含项目的初始和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。