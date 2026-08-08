# 第 6 章 Spring Boot 容器化

本章内容：

* 使用 Docker 处理容器镜像
* 将 Spring Boot 应用程序打包为容器镜像
* 使用 Docker Compose 管理 Spring Boot 容器
* 部署流水线：打包和发布

到目前为止，我们已经开发了一个 Catalog Service 应用程序，它暴露 REST API 并通过运行在容器中的 PostgreSQL 数据库持久化数据。我们即将把 Polar Bookshop 系统的第一个组件部署到 Kubernetes 集群。但在此之前，您需要学习如何将 Spring Boot 应用程序打包为容器镜像并管理其生命周期。

本章将教您容器镜像的基本特征以及如何构建一个。我们将使用 Docker 来处理容器，但您也可以使用任何其他兼容开放容器倡议（OCI）标准的容器运行时。在本书的剩余部分中，当我提到容器镜像或 Docker 镜像时，我指的是兼容 OCI 镜像规范的镜像。

在学习过程中，我将与您分享关于为生产构建容器镜像的几个注意事项，例如安全性和性能。我们将探索两种可能性：Dockerfile 和 Cloud Native Buildpacks。

当我们开始处理多个容器时，Docker CLI 效率不高。相反，我们将使用 Docker Compose 来管理多个容器及其生命周期。

最后，我们将继续第 3 章开始的部署流水线工作。我将向您展示如何向提交阶段添加新步骤，以自动将容器镜像打包和发布到 GitHub Container Registry。

> 注意：本章示例的源代码在 Chapter06/06-begin 和 Chapter06/06-end 文件夹中，包含项目的初始和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
