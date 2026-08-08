# 第 11 章 安全：认证和 SPA

本章内容：

* 使用 Spring Security 进行身份验证
* 实现 OAuth 2.0 和 OpenID Connect
* 保护单页应用程序（SPA）
* 实现 JWT 令牌认证

安全性是任何应用程序的关键方面。在云原生环境中，我们需要在多个层面保护应用程序：身份验证（验证用户身份）、授权（控制访问权限）和数据保护（加密敏感数据）。

Spring Security 是 Spring 生态系统中提供全面安全功能的框架。它支持多种认证机制，包括表单登录、HTTP Basic、OAuth 2.0 和 OpenID Connect。

对于单页应用程序（SPA），我们需要实现令牌认证机制，通常使用 JSON Web Tokens (JWT)。

> 注意：本章示例的源代码在 Chapter11/11-begin 和 Chapter11/11-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
