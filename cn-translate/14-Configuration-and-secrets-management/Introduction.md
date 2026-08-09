# 第 14 章 配置和密钥管理

本章内容：

* 在 Kubernetes 上配置应用
* 使用 Spring Cloud Config 管理密钥和刷新运行时配置
* 使用 ConfigMaps 和 Secrets（秘密）在 Kubernetes 中管理配置和敏感信息
* 使用 Kustomize 管理多个 Kubernetes 清单并根据环境定制部署

配置是指一切随部署环境而变化的东西。在之前的章节中，你已经了解了如何通过属性文件、环境变量和配置服务（Spring Cloud Config）来外部化应用配置。本章将扩展这一主题，重点介绍在 Kubernetes 环境中管理配置和密钥的机制。

首先，你会看到如何把第 4 章构建的 Config Service 投入到生产级使用：通过 Spring Security 进行保护、在运行时刷新配置、安全地管理密钥，以及在需要时把它从应用中移除。

然后，你会了解 Kubernetes 原生提供的两个配置策略：ConfigMaps 用于保存非敏感配置数据，Secrets 用于保存敏感信息。你会学会如何把它们作为卷挂载到 Pod 中，让 Spring Boot 直接消费，以及如何在运行时刷新这些配置。

最后，你会看到 Kustomize——一个声明式工具，可让你把多个 Kubernetes 清单作为一个整体来处理，并根据部署环境（例如开发、staging、生产）对配置进行定制。

> 注意：本章示例的源代码在 Chapter14/14-begin 和 Chapter14/14-end 文件夹中（[https://github.com/ThomasVitale/cloud-native-spring-in-action](https://github.com/ThomasVitale/cloud-native-spring-in-action)）。