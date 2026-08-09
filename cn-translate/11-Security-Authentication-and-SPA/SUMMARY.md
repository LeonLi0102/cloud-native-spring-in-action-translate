# 总结

本章涵盖了以下内容：

* **访问控制系统需要身份识别（您是谁？）、认证（能证明是您吗？）和授权（您被允许做什么？）** — 三个关键步骤缺一不可。
* **云原生应用实现认证和授权的常见策略** — 基于 JWT 作为数据格式、OAuth2 作为授权框架、OpenID Connect 作为认证协议。
* **使用 OIDC 认证时，Client 应用发起流程并委托授权服务器（Authorization Server）进行实际认证** — 授权服务器随后向 Client 颁发 ID Token。
* **ID Token 包含用户认证信息** — Keycloak 是支持 OAuth2 和 OpenID Connect 的身份和访问管理解决方案，可用作授权服务器。
* **Spring Security 原生支持 OAuth2 和 OpenID Connect** — 可将 Spring Boot 应用转变为 OAuth2 Client。
* **在 Spring Security 中，可通过 SecurityWebFilterChain Bean 配置认证和授权** — 使用 oauth2Login() DSL 启用 OIDC 认证流程。
* **默认情况下 Spring Security 暴露 /logout 端点用于登出** — 在 OIDC/OAuth2 上下文中还需将登出请求传播到授权服务器（如 Keycloak），通过 OidcClientInitiatedServerLogoutSuccessHandler 类支持的 RP-Initiated Logout 流程实现。
* **当安全的 Spring Boot 应用作为 SPA 后端时** — 需通过 Cookie 配置 CSRF 保护，并实现返回 HTTP 401 响应（而非默认 HTTP 302 重定向）的认证入口点。
* **Spring Security Test 依赖提供多种便捷的安全测试工具** — WebTestClient Bean 可通过特定 OIDC 登录和 CSRF 保护配置修改其请求上下文。
