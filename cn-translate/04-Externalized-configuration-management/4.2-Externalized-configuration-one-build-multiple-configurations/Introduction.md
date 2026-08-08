## 4.2 外部化配置：一个构建多个配置

与应用程序源代码打包在一起的属性文件对于定义一些合理的默认值很有用。但是，如果您需要根据环境提供不同的值，则需要其他方式。外部化配置允许您根据部署位置配置应用程序，同时始终使用相同的不可变构建。关键方面是构建和打包应用程序后不再更改它。如果需要任何配置更改（例如，不同的凭据或数据库句柄），则从外部进行。

15 要素方法论提倡在环境中存储配置，Spring Boot 提供了多种方式来实现这一点。在本节中，您将看到如何使用命令行参数、JVM 属性和环境变量来配置云原生应用程序而无需重新构建它。

## 4.2.1 命令行参数配置应用

默认情况下，Spring Boot 将任何命令行参数转换为属性键/值对，并将其包含在 Environment 对象中。在生产应用程序中，这是具有最高优先级的属性源。使用您之前构建的同一个 JAR，您可以指定命令行参数来自定义应用程序配置：

```bash
$ java -jar build/libs/catalog-service-0.0.1-SNAPSHOT.jar \
    --polar.greeting="Welcome to the catalog from CLI"
```

命令行参数与 Spring 属性同名，以熟悉的 `--` 作为 CLI 参数前缀。这次应用程序将使用命令行参数中定义的消息，因为它优先于属性文件：

```bash
$ http :9001/
Welcome to the catalog from CLI
```

## 4.2.2 JVM 系统属性配置应用

JVM 系统属性可以像命令行参数一样覆盖 Spring 属性，但优先级较低。这是外部化配置的一部分，因此您不需要构建新的 JAR 工件——您仍然可以使用之前打包的那个。终止上一个示例中的 Java 进程（Ctrl-C）并运行以下命令：

```bash
$ java -Dpolar.greeting="Welcome to the catalog from JVM" \
    -jar build/libs/catalog-service-0.0.1-SNAPSHOT.jar
```

JVM 系统属性与 Spring 属性同名，以通常的 `-D` 作为 JVM 参数前缀。这次应用程序将使用 JVM 系统属性中定义的消息，因为它优先于属性文件：

```bash
$ http :9001/
Welcome to the catalog from JVM
```

如果同时指定了 JVM 系统属性和 CLI 参数，优先级规则将确保 Spring 使用命令行参数指定的值，因为它优先于 JVM 属性。

## 4.2.3 环境变量配置应用

操作系统中定义的环境变量通常用于外部化配置，根据 15 要素方法论，它们是推荐的选项。环境变量的一个优点是每个操作系统都支持它们，使其在任何环境中都具有可移植性。

在 Spring 中，您不需要显式地从周围系统读取环境变量。Spring 在启动阶段自动读取它们，并将它们添加到 Spring Environment 对象中，使其可以像任何其他属性一样被访问。

您可以将 Spring 属性键转换为环境变量，方法是将所有字母大写，并将任何点或破折号替换为下划线。Spring Boot 会将其正确映射到内部语法。例如，`POLAR_GREETING` 环境变量被识别为 `polar.greeting` 属性。此功能称为宽松绑定。

```bash
$ POLAR_GREETING="Welcome to the catalog from ENV" \
    java -jar build/libs/catalog-service-0.0.1-SNAPSHOT.jar
```

> 提示：在 Windows 上，您可以通过在 PowerShell 控制台中运行 `$env:POLAR_GREETING="Welcome to the catalog from ENV"; java -jar build/libs/catalog-service-0.0.1-SNAPSHOT.jar` 来实现相同的结果。

当您使用环境变量存储配置数据时，无需更改运行应用程序的命令。Spring 会自动从部署环境中读取环境变量。这种方法比使用 CLI 参数或 JVM 系统属性更不容易出错。
