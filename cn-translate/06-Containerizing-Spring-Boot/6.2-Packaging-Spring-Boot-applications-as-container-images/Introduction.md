## 6.2 将 Spring Boot 应用程序打包为容器镜像

在前面的章节中，我们构建了 Catalog Service 应用程序，具有 REST API 和数据库集成功能。在本节中，作为部署到 Kubernetes 之前的中间步骤，我们将构建一个镜像，在 Docker 上以容器方式运行 Catalog Service。

首先，我将回顾将 Spring Boot 应用程序打包为容器镜像时应考虑的一些方面。然后我将向您展示如何使用 Dockerfile 和 Cloud Native Buildpacks 来完成。
