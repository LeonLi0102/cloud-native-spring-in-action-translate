## 总结

* Spring Environment 抽象提供了一个统一接口来访问属性和 profiles。
* 属性是用于存储配置的键/值对。
* Profiles 是仅在特定 profile 激活时才注册的逻辑 bean 组。
* Spring Boot 根据优先级规则从不同来源收集属性。从最高到最低优先级，属性可以定义在命令行参数、JVM 系统变量、操作系统环境变量、特定 profile 的属性文件和通用属性文件中。
* Spring bean 可以通过使用 `@Value` 注解注入值，或通过映射到一组属性的 `@ConfigurationProperties` bean，从 Environment 对象访问属性。
* 活动 profile 可以通过 `spring.profiles.active` 属性定义。
* `@Profile` 注解标记仅在指定 profile 激活时才被考虑的 bean 或配置类。
* Spring Boot 管理的属性提供了 15 要素方法论定义的外部化配置，但这还不够。
* 配置服务器处理密钥加密、配置可追溯性、版本控制和运行时无需重启的上下文刷新等方面。
* 可以使用 Spring Cloud Config Server 库设置配置服务器。
* 配置本身可以根据不同策略存储，例如在专用 Git 仓库中。
* 配置服务器使用应用程序名称、活动 profile 和 Git 特定标签来标识应向哪个应用程序提供哪个配置。
* Spring Boot 应用程序可以使用 Spring Cloud Config Client 库通过配置服务器进行配置。
* `@ConfigurationProperties` bean 被配置为监听 `RefreshScopeRefreshedEvent` 事件。
* 当新更改推送到配置仓库后可以触发 `RefreshScopeRefreshedEvent` 事件，使客户端应用程序使用最新配置数据重新加载上下文。
* Spring Boot Actuator 定义了一个 `/actuator/refresh` 端点，可用于手动触发该事件。
