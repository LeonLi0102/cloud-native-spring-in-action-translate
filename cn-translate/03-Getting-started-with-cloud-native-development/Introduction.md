# 第 3 章 进行云原生应用开发

本章内容：

* 创建云原生项目
* 使用内嵌服务器和 Tomcat
* 使用 Spring MVC 构建 RESTful 应用
* 使用 Spring Test 测试 RESTful 应用
* 使用 GitHub Actions 自动化构建和测试

云原生的技术版图如此广阔，以至于入门阶段可能令人感到不知所措。在本书第 1 部分中，您已经获得了云原生应用及其支持流程的理论介绍，并第一次亲手实践了构建一个最小的 Spring Boot 应用并将其作为容器部署到 Kubernetes 的全过程。这些都将帮助您更好地理解整体云原生图景，并正确定位我将在本书剩余部分涵盖的主题。

云计算为我们能够实现的目标开启了无尽的可能性。在本章中，我将从最常见的应用类型开始：一种通过 HTTP 以 REST API 的方式暴露其功能的 Web 应用。我将引导您完成将在所有后续章节中遵循的开发流程，阐述传统 Web 应用与云原生 Web 应用之间的重大差异，巩固 Spring Boot 和 Spring MVC 的一些必要知识，并强调关键的测试和生产环境考量。我还会解释 15-Factor 方法论推荐的一些指导原则，包括依赖管理、并发和 API 优先。

在此过程中，您将实现在上一章中初始化的 Catalog Service（目录服务）应用。它将负责管理 Polar Bookshop（极地书店）系统中的图书目录。

> **注意** 本章示例的源代码可在 `Chapter03/03-begin` 和 `Chapter03/03-end` 文件夹中找到，分别包含项目的初始状态和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
