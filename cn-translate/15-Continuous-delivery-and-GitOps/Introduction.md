# 第 15 章 持续交付和 GitOps

本章内容：

* 实现 CI/CD 流水线
* 使用 GitHub Actions 自动化部署
* 实现 GitOps 工作流
* 使用 Argo CD 进行持续部署

持续交付是一种软件开发实践，其中代码更改自动构建、测试并准备好发布到生产环境。部署流水线自动化了从代码提交到可发布软件的整个过程。

GitOps 是一种操作模型，其中 Git 仓库作为基础设施和应用程序配置的单一真相来源。通过将 Git 作为声明式基础设施和应用程序的中心枢纽，GitOps 提供了版本控制、协作和审计跟踪等优势。

Argo CD 是一个声明式的、基于 GitOps 的持续交付工具，用于 Kubernetes。它监控 Git 仓库中的应用程序定义和目标环境中的实际状态，并自动同步它们。

> 注意：本章示例的源代码在 Chapter15/15-begin 和 Chapter15/15-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
