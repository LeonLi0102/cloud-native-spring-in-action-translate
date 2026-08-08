## 4.3 使用 Spring Cloud Config Server 进行集中化配置管理

通过环境变量，您可以外部化应用程序的配置并遵循 15 要素方法论。然而，有一些问题它们无法处理：

* 配置数据与应用程序代码同样重要，应该以同样的细心和关注来处理。您应该在哪里存储配置数据？
* 环境变量不提供细粒度的访问控制功能。如何控制对配置数据的访问？
* 配置数据会演进并需要更改，就像应用程序代码一样。如何跟踪配置数据的修订？如何审核发布中使用的配置？
* 更改配置数据后，如何让应用程序在运行时读取它而无需完全重启？
* 当应用程序实例数量增加时，以分布式方式为每个实例处理配置可能具有挑战性。如何克服这些挑战？
* Spring Boot 属性和环境变量都不支持配置加密，因此您无法安全地存储密码。如何管理密钥？

Spring 生态系统提供了许多选项来解决这些问题。我们可以将它们分为三组：

### 配置服务

Spring Cloud 项目提供了可用于运行自己的配置服务并配置 Spring Boot 应用程序的模块：

* **Spring Cloud Config** — 提供由可插拔数据源支持的配置服务，如 Git 仓库、数据存储或 HashiCorp Vault
* **Spring Cloud Consul** — 使用 HashiCorp Consul 作为数据存储的配置服务
* **Spring Cloud Vault** — 使用 HashiCorp Vault 作为数据存储的配置服务

Spring Cloud Config Server 是一个集中式配置服务器，可以从 Git、SVN 或文件系统等后端存储中获取配置数据。

### 4.3.1 使用 Git 存储配置数据

Git 是 Spring Cloud Config 最常用的后端存储。它提供了配置数据的版本控制，可以跟踪更改并回滚到以前的版本。

配置 Config Server 使用 Git 仓库：

```yaml
# application.yml
server:
  port: 8888

spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/your-username/config-repo
          default-label: main
          clone-on-start: true
          search-paths:
            - '{application}'
```

### 4.3.2 设置 Config Server

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}
```

### 4.3.3 使 Config Server 更有韧性

Config Server 可能成为单点故障。为了提高可用性，可以：

1. 运行多个 Config Server 实例
2. 使用负载均衡器分发请求
3. 启用本地缓存

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/your-username/config-repo
          clone-on-start: true
        fail-on-access-error: false
```

### 4.3.4 理解 Config Server 的 REST API

Config Server 暴露了几个 REST 端点来获取配置数据：

* `/{application}/{profile}` — 获取指定应用和环境的配置
* `/{application}-{profile}.properties` — 获取属性文件格式的配置
* `/{application}-{profile}.yml` — 获取 YAML 格式的配置

```bash
$ http :8888/catalog-service/development
{
    "name": "catalog-service",
    "profiles": ["development"],
    "label": "main",
    "version": "abc123",
    "propertySources": [...]
}
```
