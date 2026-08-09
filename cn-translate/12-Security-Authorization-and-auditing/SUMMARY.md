# 总结

本章涵盖了以下内容：

* **在 OIDC/OAuth2 设置中，Client（Edge Service）通过 Access Token 被授予代表用户访问 Resource Server（Catalog Service 和 Order Service）的权限** — Token 由 Keycloak 在 OIDC 认证阶段颁发。
* **Spring Cloud Gateway 提供 TokenRelay 过滤器** — 自动将 Access Token 添加到任何向下路由的请求中。
* **遵循 JWT 格式的 ID Token 和 Access Token 可传播已认证用户的相关信息作为声明（Claim）** — 例如可添加 roles 声明并根据用户角色配置 Spring Security 授权策略。
* **Spring Boot 应用可通过 Spring Security 配置为 OAuth2 Resource Server** — 认证策略完全基于每个请求 Authorization 头中提供的有效 Access Token，称为 JWT 认证。
* **在 OAuth2 Resource Server 中，安全策略仍通过 SecurityFilterChain（命令式）或 SecurityWebFilterChain（响应式）Bean 执行** — 权限、角色和范围由 GrantedAuthority 对象表示。
* **可提供自定义 JwtAuthenticationConverter Bean** — 定义如何从 JWT 中提取授予的权限，例如使用 roles 声明。
* **授予的权限可用于采用 RBAC（基于角色的访问控制）策略** — 根据用户角色保护端点。
* **Spring Data 库支持审计功能以跟踪谁创建和最后更新了实体** — 在 Spring Data JDBC 和 Spring Data R2DBC 中均可通过配置 AuditorAware（或 ReactiveAuditorAware） Bean 启用。
* **启用数据审计后，可使用 @CreatedBy 和 @LastModifiedBy 注解** — 在创建或更新操作时自动注入正确的值。
* **测试安全具有挑战性，但 Spring Security 提供了便捷工具** — 包括修改 HTTP 请求以包含 JWT Access Token（.with(jwt()) 或 .mutateWith(mockJwt())）或在特定安全上下文中运行测试用例（@WithMockUser）的表达式。
* **Testcontainers 可帮助编写完整的集成测试** — 使用实际的 Keycloak 容器验证与 Spring Security 的交互。
