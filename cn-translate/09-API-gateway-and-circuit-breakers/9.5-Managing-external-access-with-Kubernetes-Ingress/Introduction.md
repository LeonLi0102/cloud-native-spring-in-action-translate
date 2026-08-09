## 9.5 使用 Kubernetes Ingress 管理外部访问

Spring Cloud Gateway 帮助你定义一个边缘服务，你可以在系统的入口点实现多种模式和跨切面关注点。在前面的几节中，你看到了如何将其用作 API 网关、实现限流和断路器等弹性模式，以及定义分布式会话。在第 11 章和第 12 章中，我们还将为 Edge Service 添加认证和授权功能。

Edge Service 代表 Polar Bookshop 系统的入口点。然而，当它部署在 Kubernetes 集群中时，只能从集群内部访问。在第 7 章中，我们使用了 port-forward 功能将 minikube 集群中定义的 Kubernetes Service 暴露到本地计算机。这是开发期间有用的策略，但不适合生产环境。

本节将介绍如何使用 Ingress API 管理对 Kubernetes 集群中运行的应用程序的外部访问。

> **注意：** 本节假设你已经完成了前面"Polar Labs"边栏中列出的任务，并为在 Kubernetes 上部署 Edge Service 做好了准备。
