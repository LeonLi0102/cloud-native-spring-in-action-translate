# 云原生 Spring 实战

**使用 Spring Boot 和 Kubernetes**

**Thomas Vitale**

**序言作者：Josh Long**

---

## 序言

这些年来我写过几十篇序言和前言，但这可能是我第一次不得不写序言时感到恼火。为什么？我是一个输不起的人！我因为我没有写这本书而感到恼火。我因为我甚至怀疑自己能否写出来而感到恼火。

这本书太棒了。书页中充满了宝贵的思想，这些思想都源自作者明显而深刻的实践经验。我一直希望看到所有这些概念被汇集到一处，在可预见的未来，我会向人们推荐这本书。

构建生产级应用程序——如今生产环境大多是 Kubernetes——以及构建生产本身？这是一项艰巨的任务，就像这本书一样，它超过了 600 页！但不要因为我喋喋不休地谈论篇幅而放弃购买这本书。这是一本关于一个更大主题的大书。

本书涵盖了常见的主题：如何构建服务和微服务、如何处理持久化、消息传递、为可观测性进行检测、配置和安全。此外，还有专门针对其中一些概念的完整章节。

您的 Spring Boot 应用程序是本书雄心壮志的璀璨明珠（一个商店系统，很明显），但它绝不是本书关注的唯一焦点。这本书既有深度又有广度——这是一个令人瞩目的成就！我想我应该列出一些具体内容，以便您开始了解本书涵盖内容的细微差别。在列出之前，请记住，您必须阅读这本书。以下列表绝不是详尽无遗的，但它包括了我发现自己读到时感到震惊的内容。这些内容应该出现在一本关于 Spring Boot 和 Spring Cloud 的书中，但不幸的是，很少出现。

* 有一篇关于使用 Loki、FluentBit 和 Grafana 进行日志记录的精彩论述。
* 本书将带您远不止"启动并运行" Kubernetes。到本书结束时，您将轻松掌握 Kubernetes 部署。您将使用 Knative 和 Spring Cloud Function 实现无服务器。接下来，您将使用 GitHub Actions、Kustomize 和 Kubeval 等工具构建管道。最后，您将使用 Tilt 和 Docker Compose 等工具进行本地开发。
* 在单页应用程序（SPA）上下文中讨论安全问题本身就可以成为一本优秀的书。它内容丰富、循序渐进、节奏快速且面向生产。不要错过这一章。
* 一切都考虑到了测试。Spring 为各种项目提供了互补的测试模块，这些模块在这里得到了优雅的展示。
* 本书介绍了 GraalVM 的原生镜像编译器和 Spring Native 项目。Spring Native 是生态系统中相对较新的补充，因此没有人会责怪 Thomas 没有包含它。但他确实包含了。真是个传奇！
* Thomas 介绍了我们为什么要做本书中描述的许多事情，与新的技术概念保持一致。我特别喜欢对敏捷和 GitOps 的处理。

Spring Boot 改变了世界，Thomas 的书是这个勇敢的、"美好的"新世界的最佳指南。购买它。阅读它。按照它行动。构建一些令人惊叹的东西，享受您通往生产环境的旅程！

**—— Josh Long**
Spring 开发者布道师
VMware Tanzu @starbuxman

---

## 前言

我清楚地记得第一次实地考察，去看护士和从业者如何在日常工作中使用我所在公司开发的软件。见证我们的应用程序如何改善他们照顾患者的方式，这是一个令人难以置信的时刻。软件可以产生影响。这就是我们构建它的原因。我们通过技术解决问题，目标是为用户、客户和业务本身提供价值。

另一个我无法忘记的时刻是我了解 Spring Boot 的时候。在那之前，我非常喜欢使用核心 Spring Framework。我特别喜欢我编写的代码，用于管理安全、数据持久性、HTTP 通信和集成等方面。这是很多艰苦的工作，但它是值得的，特别是考虑到当时 Java 领域的替代方案。Spring Boot 改变了一切。突然间，平台本身为我处理了所有这些方面。所有处理基础设施关注点和集成的代码都不再需要了。

但后来我想到：所有处理基础设施关注点和集成的代码都不再需要了！当我开始删除所有这些代码时，我意识到与应用程序的业务逻辑（产生价值的部分）相比，我花了多少时间在上面。我意识到与所有样板代码相比，实际属于业务逻辑的代码有多少。这是一个关键时刻！

多年后，Spring Boot 仍然是 Java 领域构建企业级软件产品的领先平台，其受欢迎的原因之一是它专注于开发人员的生产力。使每个应用程序与众不同的是其业务逻辑，而不是它如何公开数据或连接数据库。正是这种业务逻辑最终为用户、客户和企业提供价值。利用广泛的框架、库和集成生态系统，Spring Boot 使开发人员能够专注于业务逻辑，同时处理管道和样板代码。

云计算是我们领域的另一个颠覆者，Kubernetes 迅速成为云的"操作系统"。利用云计算模型的功能，我们可以构建云原生应用程序，并为我们的项目实现更好的可扩展性、弹性、速度和成本优化。最终，我们有机会增加通过软件产生的价值，并以以前不可能的方式解决新型问题。

本书的想法源于我希望帮助软件工程师在交付价值的旅程中。我很高兴您决定加入我这次从代码到生产环境的冒险。Spring Boot，以及整个 Spring 生态系统，代表了这段旅程的支柱。云原生原则和模式将指导我们实现各种应用程序。持续交付实践将支持我们安全、快速、可靠地交付高质量软件。Kubernetes 及其生态系统将为向用户部署和发布应用程序提供平台。

在构建和编写本书时，我的指导原则是提供相关的、现实世界的示例，您可以立即将其应用到日常工作中。书中涵盖的所有技术和模式都旨在在生产环境中交付高质量的软件，在有限空间的书籍可以包含的范围内。我希望我成功地实现了这一目标。

再次感谢您加入我这次从代码到生产环境的云原生之旅。我希望您在阅读本书时获得愉快且有教育意义的体验，并希望它能帮助您用软件创造更多价值并产生影响。

---

## 致谢

写书很难，如果没有许多人在整个开发过程中提供的支持，这是不可能的。首先，我要感谢我的家人和朋友，他们一直鼓励和支持我。特别感谢我的父母 Sabrina 和 Plinio、我的姐妹 Alissa 和我的祖父 Antonio，感谢他们的持续支持和对我的信任。

我要感谢我的朋友和同事 Filippo、Luciano、Luca 和 Marco，他们从最初的提案就一直支持我，并随时提供反馈和建议来改进这本书。我要感谢 Systematic 的同事和朋友，他们在这段时间里一直鼓励我。我很幸运能与你们一起工作。

我要感谢都灵理工大学的 Giovanni Malnati 教授，是他首先向我介绍了 Spring 生态系统，并改变了我的职业生涯轨迹。非常感谢 Spring 团队创建了如此高效和有价值的生态系统。特别感谢 Josh Long 的出色工作，他教会了我很多，并为本书撰写了序言。这对我意义重大！

我要感谢整个 Manning 团队在使本书成为宝贵资源方面提供的巨大帮助。我特别要感谢 Michael Stephens（选题编辑）、Susan Ethridge（开发编辑）、Jennifer Stout（开发编辑）、Nickie Buckner（技术开发编辑）和 Niek Palm（技术校对）。他们的反馈、建议和鼓励为本书带来了巨大价值。还要感谢 Mihaela Batinic（审阅编辑）、Andy Marinkovich（制作编辑）、Andy Carroll（文字编辑）、Keri Hales（校对员）和 Paul Wells（制作经理）。

感谢所有审阅者：Aaron Makin、Alexandros Dallas、Andres Sacco、Conor Redmond、Domingo Sebastian、Edd Melendez Gonzales、Fatih Mehmet Ucar、Francois-David Lessard、George Thomas、Gilberto Taccari、Gustavo Gomes、Harinath Kuntamukkala、Javid Asgarov、Joao Miguel、Pires Dias、John Guthrie、Kerry E. Koitzsch、Michal Rutka、Mladen Knezic、Mohamed Sanaulla、Najeeb Arif、Nathan B. Crocker、Neil Croll、Ozay Duman、Raffaella Ventaglio、Sani Sudhakaran Subhadra、Simeon Leyzerzon、Steve Rogers、Tan Wee、Tony Sweets、Yogesh Shetty 和 Zorodzayi Mukuya，您的建议帮助使这本书变得更好。

最后，我要感谢 Java 社区以及这些年来我遇到的所有优秀的人：开源贡献者、同行演讲者、会议组织者，以及所有为这个社区做出贡献的人。

---

## 关于本书

《Cloud Native Spring in Action》旨在帮助您使用 Spring Boot 和 Kubernetes 设计、构建和部署云原生应用程序。它定义了一条通往生产环境的精选路径，并教授您可以立即应用于企业级应用程序的有效技术。它还逐步引导您从最初的想法到生产环境，展示云原生开发如何在软件开发生命周期的每个阶段增加业务价值。当您开发在线书店系统时，您将学习如何使用 Spring 和 Java 生态系统中可用的强大库来构建和测试云原生应用程序。一章接一章，您将使用 REST API、数据持久化、响应式编程、API 网关、函数、事件驱动架构、弹性、安全、测试和可观测性。然后本书扩展介绍了如何将应用程序打包为云中的容器镜像、如何为 Kubernetes 等云环境配置部署、如何使应用程序准备好投入生产，以及如何使用持续交付和持续部署设计从代码到生产的路径。

本书提供了一个实践性的、项目驱动的指南，帮助您驾驭日益复杂的云环境，并学习如何将模式和技术结合在一起构建真正的云原生系统并将其投入生产。

### 谁应该读这本书？

本书面向希望了解更多关于使用 Spring Boot 和 Kubernetes 设计、构建和部署生产级云原生应用程序的开发人员和架构师。

要从本书中获得最大收益，您需要具备扎实的 Java 编程技能、构建 Web 应用程序的经验，以及对 Spring 核心功能的基本了解。我假设您熟悉 Git、面向对象编程、分布式系统、数据库和测试。不需要 Docker 和 Kubernetes 的经验。

### 本书的组织结构：路线图

本书分为 4 个部分，涵盖 16 章。第 1 部分为您的云原生之旅从代码到生产奠定了基础，并帮助您更好地理解本书其余部分涵盖的主题，并将其正确地放在整体云原生图景中。

* **第 1 章** 是对云原生领域的介绍。它定义了云原生的含义、云原生应用程序的基本属性以及支持它们的流程。
* **第 2 章** 涵盖了云原生开发的原则，并指导您完成第一次动手体验，构建一个最小的 Spring Boot 应用程序并将其作为容器部署到 Kubernetes。

第 2 部分向您介绍了使用 Spring Boot 和 Kubernetes 构建生产级云原生应用程序的主要实践和模式。

* **第 3 章** 涵盖了启动新云原生项目的基础知识，包括组织代码库、管理依赖项和定义部署管道提交阶段的策略。您将学习如何使用 Spring MVC 和 Spring Boot Test 实现和测试 REST API。
* **第 4 章** 讨论了外部化配置的重要性，并介绍了 Spring Boot 应用程序可用的一些选项，包括属性文件、环境变量和使用 Spring Cloud Config 的配置服务。
* **第 5 章** 介绍了云中数据服务的主要方面，并向您展示如何使用 Spring Data JDBC 向 Spring Boot 应用程序添加数据持久化。您将学习使用 Flyway 管理数据的生产选项和使用 Testcontainers 进行测试的策略。
* **第 6 章** 关于容器；您将了解更多关于 Docker 以及如何使用 Dockerfile 和 Cloud Native Buildpacks 将 Spring Boot 应用程序打包为容器镜像。
* **第 7 章** 讨论了 Kubernetes，涵盖了服务发现、负载均衡、可扩展性和本地开发工作流程。您还将了解更多关于如何将 Spring Boot 应用程序部署到 Kubernetes 集群的信息。

第 3 部分涵盖了云中分布式系统的基本属性和模式，包括弹性、安全、可扩展性和 API 网关。它还描述了响应式编程和事件驱动架构。

* **第 8 章** 介绍了响应式编程和 Spring 响应式技术栈的主要功能，包括 Spring WebFlux 和 Spring Data R2DBC。它还教您如何使用 Project Reactor 使应用程序更具弹性。
* **第 9 章** 涵盖了 API 网关模式以及如何使用 Spring Cloud Gateway 构建边缘服务。您将学习如何使用 Spring Cloud 和 Resilience4J 构建弹性应用程序，使用重试、超时、回退、断路器和速率限制器等模式。
* **第 10 章** 描述了事件驱动架构，并教您如何使用 Spring Cloud Function、Spring Cloud Stream 和 RabbitMQ 实现它们。
* **第 11 章** 全部关于安全，向您展示如何使用 Spring Security、OAuth2、OpenID Connect 和 Keycloak 在云原生系统中实现身份验证。它还描述了当单页应用程序是系统的一部分时，如何解决 CORS 和 CSRF 等安全问题。
* **第 12 章** 继续安全之旅，介绍如何使用 OAuth2 和 Spring Security 在分布式系统中委托访问、保护 API 和数据，以及根据用户角色授权用户。

第 4 部分将引导您完成使云原生应用程序准备好投入生产的最后几个步骤，解决可观测性、配置管理、密钥管理和部署策略等问题。它还涵盖了无服务器和原生镜像。

* **第 13 章** 介绍如何使用 Spring Boot Actuator、OpenTelemetry 和 Grafana 可观测性技术栈使云原生应用程序可观察。您将学习如何配置 Spring Boot 应用程序以生成相关的遥测数据，如日志、健康状况、指标、跟踪等。
* **第 14 章** 涵盖了高级配置和密钥管理策略，包括 Kubernetes 原生选项，如 ConfigMaps、Secrets 和 Kustomize。
* **第 15 章** 将引导您完成云原生之旅的最后步骤，并教您如何为生产配置 Spring Boot。然后，您将为应用程序设置持续部署，并使用 GitOps 策略将其部署到公共云中的 Kubernetes 集群。
* **第 16 章** 涵盖了使用 Spring Native 和 Spring Cloud Function 的无服务器架构和函数。您还将了解 Knative 及其强大功能，这些功能在 Kubernetes 之上提供了卓越的开发人员体验。

总的来说，我建议从第 1 章开始，按顺序阅读每一章。如果您更喜欢根据自己的特定兴趣以不同的顺序阅读章节，请确保首先阅读第 1 到 3 章，以便更好地理解全书中使用的术语、模式和策略。即便如此，每一章都建立在前一章的基础上，因此如果您决定这样做，可能会缺少一些上下文。

### 关于代码

本书提供了一个实践性和项目驱动的体验。从第 2 章开始，您将构建一个由多个云原生应用程序组成的系统，用于一个虚构的在线书店。

您可以从本书的 liveBook（在线）版本 [https://livebook.manning.com/book/cloud-native-spring-in-action](https://livebook.manning.com/book/cloud-native-spring-in-action) 获取可执行的代码片段。本书中开发的所有项目的源代码都在 GitHub 上，根据 Apache License 2.0 许可（[https://github.com/ThomasVitale/cloud-native-spring-in-action](https://github.com/ThomasVitale/cloud-native-spring-in-action)）。对于每一章，您都会找到一个"begin"和一个"end"文件夹。每一章都建立在前一章的基础上，但即使您没有跟随前几章，您也可以始终使用给定章节的"begin"文件夹作为起点。"end"文件夹包含完成该章步骤后的最终结果，您可以将其与自己的解决方案进行比较。例如，您可以在 Chapter03 文件夹中找到第 3 章的源代码，其中包含 03-begin 和 03-end 文件夹。

本书中开发的所有应用程序都基于 Java 17 和 Spring Boot 2.7，并使用 Gradle 构建。这些项目可以导入到任何支持 Java、Gradle 和 Spring Boot 的 IDE 中，例如 Visual Studio Code、IntelliJ IDEA 或 Eclipse。您还需要安装 Docker。第 2 章和附录 A 将提供更多信息来帮助您设置本地环境。

这些示例已在 macOS、Ubuntu 和 Windows 上进行了测试。在 Windows 上，我建议使用 Windows Subsystem for Linux 来完成本书中描述的部署和配置任务。在 macOS 上，如果您使用 Apple Silicon 计算机，您可以运行所有示例，但在撰写本文时，某些不提供 ARM64 架构本机支持的工具可能会出现性能问题。相关章节将包含其他上下文信息。

前面提到的 GitHub 仓库（[https://github.com/ThomasVitale/cloud-native-spring-in-action](https://github.com/ThomasVitale/cloud-native-spring-in-action)）包含本书所有源代码的主分支。除此之外，我计划维护一个 sb-2-main 分支，在其中我会让源代码与 Spring Boot 2.x 的未来版本保持同步，以及一个 sb-3-main 分支，在其中我会根据 Spring Boot 3.x 的未来版本来演进源代码。

本书包含许多源代码示例，既在编号清单中，也在普通文本中内联。在这两种情况下，源代码都使用等宽字体格式化，如 this，以将其与普通文本区分开来。有时代码也以粗体显示，以突出显示与本章前面步骤相比已更改的代码，例如当新功能添加到现有代码行时。

在许多情况下，原始源代码已被重新格式化；我们添加了换行符并重新调整了缩进，以适应书中可用的页面空间。在极少数情况下，这仍然不够，清单包括行继续标记（）。此外，当在文本中描述代码时，源代码中的注释通常已从清单中删除。代码注释伴随许多清单，突出显示重要概念。

### liveBook 讨论论坛

购买《Cloud Native Spring in Action》可免费访问 liveBook，Manning 的在线阅读平台。使用 liveBook 的独家讨论功能，您可以将评论附加到本书的全局或特定部分或段落。为自己做笔记、回答技术问题以及从作者和其他用户那里获得帮助非常简单。要访问论坛，请转到 [https://livebook.manning.com/book/cloud-native-spring-in-action/discussion](https://livebook.manning.com/book/cloud-native-spring-in-action/discussion)。您还可以在 [https://livebook.manning.com/discussion](https://livebook.manning.com/discussion) 了解更多关于 Manning 论坛和行为准则的信息。

Manning 对我们的读者的承诺是提供一个场所，让个人读者之间以及读者与作者之间可以进行有意义的对话。这不是对作者任何特定参与程度的承诺，作者对论坛的贡献仍然是自愿的（且无报酬）。我们建议您尝试向作者提出一些具有挑战性的问题，以免他的兴趣偏离！只要本书仍在印刷中，论坛和先前讨论的存档就可以从出版商的网站访问。

### 其他在线资源

您可以通过 Twitter（@vitalethomas）、LinkedIn（[www.linkedin.com/in/vitalethomas](http://www.linkedin.com/in/vitalethomas)）或我的博客 [https://thomasvitale.com](https://thomasvitale.com) 在网上找到我。

如果您想了解更多关于 Spring 生态系统的知识，我在 [https://github.com/ThomasVitale/awesome-spring](https://github.com/ThomasVitale/awesome-spring) 维护了一个教育资源列表，包括书籍、视频、播客、课程和活动。
