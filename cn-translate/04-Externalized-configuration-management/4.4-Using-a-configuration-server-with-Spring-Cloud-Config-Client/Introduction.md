## 4.4 通过 Spring Cloud Config Client 使用配置服务器

在上一节中构建的 Config Service 应用程序是一个通过 REST API 暴露配置的服务器。通常，应用程序会与此 API 交互，但您可以使用 Spring Cloud Config Client 来处理 Spring 应用程序。

本节将教您如何使用 Spring Cloud Config Client 并将 Catalog Service 与配置服务器集成。您将看到如何使交互更加健壮，以及当新更改推送到配置仓库时如何刷新客户端的配置。
