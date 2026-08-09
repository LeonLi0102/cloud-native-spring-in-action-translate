# 第 11 章 安全：身份验证和 SPA

**本章内容**

* 理解 Spring Security 基础知识
* 使用 Keycloak 管理用户帐户
* 使用 OpenID Connect、JWT 和 Keycloak
* 使用 Spring Security 和 OpenID Connect 进行用户身份验证
* 测试 Spring Security 和 OpenID Connect

安全是 Web 应用程序最关键的方面之一，可能是出错时影响最灾难性的方面。出于教育目的，我现在才介绍这个主题。在现实世界中，我建议从每个新项目或功能的一开始就考虑安全，直到应用程序退役为止。

访问控制系统仅在用户身份得到证明且具有所需权限时才允许用户访问资源。为此，我们需要遵循三个关键步骤：识别、身份验证和授权。

1. **识别（Identification）** 发生在用户（人或机器）声称身份时。在现实世界中，当我通过说出自己的名字来介绍自己时，就会发生这种情况。在数字世界中，我会通过提供用户名或电子邮件地址来做到这一点。

2. **身份验证（Authentication）** 是关于通过护照、驾照、密码、证书或令牌等因素验证用户声称的身份。当使用多个因素来验证用户身份时，我们称之为多因素身份验证。

3. **授权（Authorization）** 总是在身份验证之后发生，它检查用户在给定上下文中被允许做什么。

本章和下一章将介绍在云原生应用程序中实现访问控制系统。您将了解如何向 Polar Bookshop 等系统添加身份验证，以及如何使用 Keycloak 等专用身份和访问管理解决方案。我将向您展示如何使用 Spring Security 来保护应用程序的安全，并采用 JWT、OAuth2 和 OpenID Connect 等标准。在此过程中，您还将向系统添加 Angular 前端，并了解涉及单页应用程序（SPA）时的安全最佳实践。

> **注意** 本章示例的源代码可在 Chapter11/11-begin 和 Chapter11/11-end 文件夹中找到，分别包含项目的初始和最终状态（[https://github.com/ThomasVitale/cloud-native-spring-in-action](https://github.com/ThomasVitale/cloud-native-spring-in-action)）。
