## 7.3 服务发现和负载均衡

我们已经讨论了 Pod 和 Deployment，接下来深入了解一下 Service。您已将 Catalog Service 应用程序作为 Pod 在本地 Kubernetes 集群中运行，但仍有一些问题没有解决。它如何与集群中运行的 PostgreSQL Pod 交互？它如何知道在哪里找到 PostgreSQL？如何将 Spring Boot 应用程序暴露给集群中的其他 Pod 使用？如何将其暴露到集群外部？

本节将通过介绍云原生系统的两个重要方面来回答这些问题：服务发现和负载均衡。我将介绍在 Spring 应用程序中实现它们的两种主要模式：客户端和服务器端。然后您将应用后者——Kubernetes 通过 Service 对象便捷地原生提供的方式，这意味着您无需更改代码中的任何内容即可支持它（与客户端选项不同）。最后，您将了解 Catalog Service Pod 和 PostgreSQL Pod 之间的通信是如何实现的，并将 Catalog Service 应用程序暴露为网络服务。
