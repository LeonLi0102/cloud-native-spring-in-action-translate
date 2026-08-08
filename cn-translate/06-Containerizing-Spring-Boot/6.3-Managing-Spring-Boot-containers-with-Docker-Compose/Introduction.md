## 6.3 使用 Docker Compose 管理 Spring Boot 容器

当您处理多个容器时，Docker CLI 命令会变得冗长且难以管理。Docker Compose 是一个工具，可以使用 YAML 文件定义和运行多容器应用程序。

使用 Docker Compose，您可以：

* 使用单个命令定义多个服务
* 管理容器的生命周期（启动、停止、重启）
* 配置网络和卷
* 简化开发环境的设置

### 6.3.1 使用 Docker Compose 管理容器生命周期

创建一个 docker-compose.yml 文件：

```yaml
version: '3.8'

services:
  catalog-service:
    build: .
    ports:
      - "9001:9001"
    environment:
      - SPRING_DATASOURCE_URL=jdbc:postgresql://polar-postgres:5432/polardb_catalog
      - SPRING_PROFILES_ACTIVE=testdata
    networks:
      - catalog-network
    depends_on:
      - polar-postgres

  polar-postgres:
    image: postgres:14.4
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=polardb_catalog
    ports:
      - "5432:5432"
    networks:
      - catalog-network

networks:
  catalog-network:
```

启动所有服务：

```bash
$ docker-compose up -d
```

停止并移除所有服务：

```bash
$ docker-compose down
```

### 6.3.2 调试 Spring Boot 容器

使用 Docker Compose，您可以轻松地调试容器化应用程序。在 docker-compose.yml 中添加远程调试配置：

```yaml
services:
  catalog-service:
    build: .
    ports:
      - "9001:9001"
      - "5005:5005"
    environment:
      - JAVA_TOOL_OPTIONS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005
```

然后您可以使用 IDE 连接到容器中的应用程序进行调试。
