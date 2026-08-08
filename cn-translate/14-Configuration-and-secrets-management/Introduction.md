# 第 14 章 配置和密钥管理

本章内容：

* 使用 Kubernetes ConfigMaps 管理配置
* 使用 Kubernetes Secrets 管理敏感信息
* 实现配置热更新
* 使用 Spring Cloud Config Server

在云原生环境中，配置管理是一个关键挑战。应用程序需要能够适应不同的环境（开发、测试、预发、生产），而不需要重新构建。

Kubernetes 提供了 ConfigMaps 和 Secrets 来管理配置数据和敏感信息。Spring Cloud Config Server 提供了集中化的配置管理解决方案。

配置热更新允许在不重启应用程序的情况下更新配置，这对于生产环境非常重要。

> 注意：本章示例的源代码在 Chapter14/14-begin 和 Chapter14/14-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
