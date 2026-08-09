## 8.4 使用响应式 Spring 构建弹性应用程序

弹性是关于保持系统可用并提供其服务，即使发生故障也是如此。由于故障将会发生，并且无法预防所有故障，因此设计容错应用程序至关重要。目标是保持系统可用，而用户不会注意到任何故障。在最坏的情况下，系统可能具有降级的功能（优雅降级），但它仍然应该可用。

实现弹性（或容错）的关键点是将故障组件隔离，直到故障修复。通过这样做，你将防止 Michael T. Nygard 所说的裂缝传播。考虑 Polar Bookshop。如果 Catalog Service 进入故障状态并变得无响应，你不希望 Order Service 也受到影响。应用程序服务之间的集成点应仔细保护，以抵御影响对方的故障。

有几种构建弹性应用程序的模式。在 Java 生态系统中，Netflix 开发的用于实现此类模式的流行库是 Hystrix，但截至 2018 年，它已进入维护模式，不会进一步开发。Resilience4J 获得了极大的普及，填补了 Hystrix 留下的空白。Project Reactor（响应式 Spring 技术栈的基础）也提供了一些有用的弹性功能。

在本节中，你将使 Order Service 和 Catalog Service 之间的集成点更加健壮，使用响应式 Spring 配置超时、重试和回退。在下一章中，你将了解更多关于使用 Resilience4J 和 Spring Cloud Circuit Breaker 构建弹性应用程序的内容。
