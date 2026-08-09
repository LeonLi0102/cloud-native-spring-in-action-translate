## 7.2 Spring Boot 的 Kubernetes Deployment

本节将带您了解作为开发人员将使用的 Kubernetes 对象，以及与平台团队高效沟通并将应用程序部署到集群所需的词汇。

您已经完成了 Spring Boot 应用程序的容器化。Kubernetes 上的 Spring Boot 应用程序仍然打包为容器，但它运行在由 Deployment 对象控制的 Pod 中。

Pod 和 Deployment 是使用 Kubernetes 时需要理解的核心概念。让我们先了解它们的一些主要特征，然后实践声明和创建 Kubernetes 资源来部署 Catalog Service 应用程序。
