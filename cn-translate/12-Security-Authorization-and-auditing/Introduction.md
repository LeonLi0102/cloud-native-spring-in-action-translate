# 第 12 章 安全：授权和审计

本章内容：

* 实现基于角色的访问控制（RBAC）
* 使用 Spring Security 的方法级安全
* 实现审计日志
* 使用 Spring Data 的审计功能

授权是确定经过身份验证的用户是否有权执行特定操作的过程。在微服务架构中，授权可以在多个层面实现：API 网关层面、服务层面和方法层面。

Spring Security 提供了灵活的授权机制，支持基于角色、基于权限和基于表达式的访问控制。

审计是跟踪系统中发生的重要事件的过程，对于安全合规和问题排查非常重要。

> 注意：本章示例的源代码在 Chapter12/12-begin 和 Chapter12/12-end 文件夹中（https://github.com/ThomasVitale/cloud-native-spring-in-action）。
