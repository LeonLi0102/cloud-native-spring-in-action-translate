## 4.4 通过 Spring Cloud Config Client 使用配置服务

在上一节中，您设置了 Config Server 来集中管理配置数据。在本节中，您将学习如何配置 Spring Boot 应用程序作为 Config Client，从 Config Server 获取配置。

### 4.4.1 设置 Config Client

首先，在应用程序的 `bootstrap.yml`（或 `bootstrap.properties`）文件中添加 Config Client 依赖和配置：

```yaml
# bootstrap.yml
spring:
  application:
    name: catalog-service
  cloud:
    config:
      uri: http://localhost:8888
      fail-fast: true
      retry:
        max-attempts: 5
        initial-interval: 1000
```

添加 Config Client 依赖：

```groovy
dependencies {
    implementation 'org.springframework.cloud:spring-cloud-starter-config'
}
```

### 4.4.2 使 Config Client 更有韧性

Config Server 可能暂时不可用。为了提高韧性，可以配置重试机制：

```yaml
# bootstrap.yml
spring:
  cloud:
    config:
      uri: http://localhost:8888
      fail-fast: true
      retry:
        max-attempts: 6
        initial-interval: 1000
        max-interval: 2000
        multiplier: 1.1
```

添加重试依赖：

```groovy
dependencies {
    implementation 'org.springframework.retry:spring-retry'
    implementation 'org.springframework.boot:spring-boot-starter-aop'
}
```

### 4.4.3 运行时刷新配置

Spring Cloud Config 提供了几种方式在运行时刷新配置而无需重启应用程序：

#### 使用 @RefreshScope

```java
@RestController
@RefreshScope
public class ConfigController {
    
    @Value("${app.feature.enabled:false}")
    private boolean featureEnabled;
    
    @GetMapping("/config")
    public Map<String, Object> getConfig() {
        Map<String, Object> config = new HashMap<>();
        config.put("featureEnabled", featureEnabled);
        return config;
    }
}
```

#### 手动刷新

```bash
$ curl -X POST http://localhost:9001/actuator/refresh
```

#### 使用 Spring Cloud Bus 自动刷新

```yaml
# application.yml
spring:
  cloud:
    bus:
      enabled: true
      refresh:
        enabled: true
```

通过 Spring Cloud Bus，当配置仓库中的配置发生变化时，可以自动通知所有连接的客户端刷新配置。

### 4.4.4 使用 Config Server 的加密功能

Config Server 支持加密敏感配置数据：

```bash
# 加密属性值
$ curl http://localhost:8888/encrypt -d 'my-secret-password'

# 在配置文件中使用加密值
spring:
  datasource:
    password: '{cipher}加密后的值'
```

Config Server 还支持使用 HashiCorp Vault 来安全管理密钥。

通过 Spring Cloud Config，您可以实现配置的集中管理、版本控制和动态更新，同时保持应用程序的可移植性和可维护性。
