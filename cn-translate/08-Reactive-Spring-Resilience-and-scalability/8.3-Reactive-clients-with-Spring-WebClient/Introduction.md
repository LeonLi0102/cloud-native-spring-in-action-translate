## 8.3 使用 Spring WebClient 构建响应式客户端

在云原生系统中，应用程序可以以不同方式交互。本节重点介绍你将在 Order Service 和 Catalog Service 之间建立的基于 HTTP 的请求/响应交互。在这种交互中，发出请求的客户端期望收到响应。在命令式应用程序中，这将转化为线程阻塞直到返回响应。相反，在响应式应用程序中，我们可以更有效地使用资源，这样没有线程会等待响应，释放资源来处理其他处理。

Spring Framework 捆绑了两个执行 HTTP 请求的客户端：RestTemplate 和 WebClient。RestTemplate 是原始的 Spring REST 客户端，允许基于模板方法 API 的阻塞 HTTP 请求/响应交互。自 Spring Framework 5.0 以来，它处于维护模式，实际上已弃用。它仍然被广泛使用，但在未来版本中不会获得任何新功能。

WebClient 是 RestTemplate 的现代替代品。它提供阻塞和非阻塞 I/O，使其成为命令式和响应式应用程序的完美候选者。它可以通过函数式风格的流畅 API 操作，让你配置 HTTP 交互的任何方面。

本节将教你如何使用 WebClient 建立非阻塞请求/响应交互。我还将解释如何通过使用 Reactor 运算符 timeout()、retryWhen() 和 onError() 采用超时、重试和故障转移等模式使你的应用程序更具弹性。
