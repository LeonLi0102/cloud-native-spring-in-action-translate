# 第 12 章 安全：授权和审计

**本章内容**

* 使用 Spring Cloud Gateway 和 OAuth2 进行授权和角色管理
* 使用 Spring Security 和 OAuth2 保护 API（命令式）
* 使用 Spring Security 和 OAuth2 保护 API（响应式）
* 使用 Spring Security 和 Spring Data 保护和审计数据

在上一章中，我介绍了云原生应用程序的访问控制系统。您了解了如何使用 Spring Security 和 OpenID Connect 向 Edge Service 添加身份验证，管理用户会话生命周期，以及在将 Angular 前端与 Spring Boot 集成时解决 CORS 和 CSRF 问题。

通过将身份验证步骤委托给 Keycloak，Edge Service 不受特定身份验证策略的影响。例如，我们使用了 Keycloak 提供的登录表单功能，但我们也可以启用通过 GitHub 的社交登录或依赖现有的 Active Directory 对用户进行身份验证。Edge Service 只需要支持 OIDC 来验证身份验证是否正确，并通过 ID Token 获取有关用户的信息。

仍然有一些我们尚未解决的问题。Polar Bookshop 是一个分布式系统，用户成功通过 Keycloak 身份验证后，Edge Service 应该代表用户与 Catalog Service 和 Order Service 交互。我们如何安全地将身份验证上下文传播到其他系统应用程序？本章将帮助您使用 OAuth2 和 Access Token 解决该问题。

在处理身份验证之后，我们将解决授权步骤。目前，Polar Bookshop 的客户和员工都可以在系统上执行任何操作。本章将引导您完成使用 OAuth2、Spring Security 和 Spring Data 处理的几种授权场景：

* 我们将使用基于角色的访问控制（RBAC）策略来保护 Spring Boot 暴露的 REST 端点，具体取决于用户是书店的客户还是员工。
* 我们将配置数据审计以跟踪哪个用户进行了哪些更改。
* 我们将强制执行数据保护规则，以便只有其所有者才能访问它。

最后，您将探索如何使用 Spring Boot、Spring Security 和 Testcontainers 测试这些更改。

> **注意** 本章示例的源代码可在 Chapter12/12-begin 和 Chapter12/12-end 文件夹中找到，分别包含项目的初始和最终状态（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
