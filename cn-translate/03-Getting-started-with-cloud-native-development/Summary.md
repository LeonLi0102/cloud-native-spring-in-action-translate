# 3.6 总结

* 每个云原生应用都应在其自己的代码库中跟踪，其所有依赖都应使用 Gradle 或 Maven 等工具在清单中声明。
* 云原生应用不依赖于环境中注入的服务器。相反，它们使用内嵌服务器并且是自包含的。
* Tomcat 是 Spring Boot 应用的默认内嵌服务器，可以通过属性进行配置，以自定义其监听的端口、连接、超时和线程。
* 像 Tomcat 这样的 Servlet 容器提供的请求/响应交互既是同步的也是阻塞的。每个线程处理一个 HTTP 请求直到返回响应。
* API 优先原则建议在实现业务逻辑之前先设计 API 以建立契约。这样，其他团队可以基于契约本身开发他们的服务来消费您的应用，而无需等待应用完成。
* 在 Spring MVC 中，REST API 在 `@RestController` 类中实现。
* 每个 REST 控制器方法处理具有特定方法（GET、POST、PUT、DELETE）和端点（如 `/books`）的传入请求。
* 控制器方法可以通过 `@GetMapping`、`@PostMapping`、`@PutMapping`、`@DeleteMapping` 和 `@RequestMapping` 注解声明它们处理的端点和操作。
* `@RestController` 类的方法可以通过应用 `@Valid` 注解在处理之前校验 HTTP 请求体。
* 给定 Java 对象的校验约束通过在字段上使用 Java Bean Validation API 的注解定义（例如 `@NotBlank`、`@Pattern`、`@Positive`）。
* HTTP 请求处理期间抛出的 Java 异常可以在集中的 `@RestControllerAdvice` 类中映射到 HTTP 状态码和响应体，将 REST API 的异常处理与抛出异常的代码解耦。
* 单元测试不感知 Spring 配置，但可以使用熟悉的工具（如 JUnit、Mockito 和 AssertJ）作为标准 Java 测试编写。
* 集成测试需要 Spring 应用上下文才能运行。可以使用 `@SpringBootTest` 注解初始化完整的应用上下文（包括可选的内嵌服务器）进行测试。
* 当测试仅专注于应用的一个"切片"且只需要部分配置时，Spring Boot 提供了几种注解用于更有针对性的集成测试。使用这些注解时，会初始化 Spring 应用上下文，但仅加载特定功能切片使用的组件和配置部分。
* `@WebMvcTest` 用于测试 Spring MVC 组件。
* `@JsonTest` 用于测试 JSON 序列化和反序列化。
* GitHub Actions 是 GitHub 提供的工具，用于声明流水线（或工作流）以自动化任务。它可以用于构建部署流水线。
