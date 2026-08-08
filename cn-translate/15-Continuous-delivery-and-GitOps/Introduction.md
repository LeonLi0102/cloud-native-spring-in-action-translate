# 第 15 章 持续交付和 GitOps

本章内容：

* 用 Git commit hash 标识发布候选
* 使用 GitHub Actions 实现部署流水线的验收阶段和生产阶段
* 使用 Kustomize 为生产环境配置 Spring Boot 应用
* 使用 Argo CD 实现 GitOps 工作流

在本章中，你将把前 14 章所学的一切整合起来，把 Polar Bookshop 系统部署到生产环境的 Kubernetes 集群中，并实现一条完整的持续交付（Continuous Delivery）流水线。

持续交付是一种软件开发实践，代码的每次变更都会被自动构建、测试并准备发布到生产环境。部署流水线（Delivery Pipeline）自动化了从代码提交到可发布软件的全部过程，而 GitOps 则以 Git 仓库作为基础设施和应用配置的单一真相来源。

在生产环境中运行云原生应用，还需要根据环境定制配置。你将学习如何使用 Kustomize 为生产环境定义配置 overlay（覆盖层），包括环境变量、Secret、ConfigMap、资源请求与限制等。

GitOps 是一种运维模型，把 Git 作为声明式基础设施和应用程序的中心枢纽。它提供了版本控制、协作和审计跟踪等优势。Argo CD 是一个声明式的、基于 GitOps 的持续交付工具，可用于保持 Kubernetes 集群中的实际状态与 Git 仓库中的期望状态同步。

> 注意：本章示例的源代码在 Chapter15/15-begin 和 Chapter15/15-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。