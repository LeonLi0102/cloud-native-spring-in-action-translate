3 Getting started with cloud native development 
3 开始掌握云原生开发

This chapter covers:
本章内容涵盖

* Bootstrapping a cloud native project 
* 云原生引导项目

* Working with embedded servers and Tomcat 
* 如何在嵌入式服务器和 Tomcat 开展开发工作

* Building a RESTful application with Spring MVC
* 如何基于 Spring MVC 工程构建 RESTful 应用

* Testing RESTful applciation with Spring Test 
* 如何基于 Spring Test 框架测试 RESTful 应用

* Automating build and tests with GitHub Actions 
* 如何基于 GitHub Action 来构建自动化测试


The cloud native landscape is so broad that getting started can be overwhelming. In Part1, you got a theoretical introduction to cloud native applications and the processes supporting them, and you had a first hands-on experience building a minimal Spring Boot application and deploing it to Kubernetes as a container. All of that will help you understande better and place correctly in the overall cloud native picture the topics I'll be covering in the rest of the book.

云原生蓝图涵盖知识面如此之广以至于很难一开始就学习其全部技术点. 在本书的第一部分中, 你已经对云原生中的应用以及其运行过程在概念上有了大致的了解, 并且动手实践了如何基于 Spring Boot 框架构建小型的应用并将其作为容器部署在 Kubernetes 中. 这些会帮助你更好的理解书中的概念以及与我将会在本书后续内容中介绍的云原生的概念与技术点一一对应. 


The cloud opened up endless possibilities in what we can achieve with many different types of applications. 
云技术让我们在其上可以部署不同类型的应用提供了无限可能.

In this chapter, I chose to start with one of the most common types: a web application exposiing its functionality over HTTP through a REST API.
在本章节, 我选择最为通用的类型: 基于 HTTP 协议对外暴露 REST API 函数接口 web 应用. 


I'll guide you through the development process you'll be following in all the subsequent chapters, addressing the significant differences between traditional and cloud native web applications, consolidating some necessary aspects about Spring Boot and Spring MVC, and highlighting essential testing and production considerations.
我将会指导你全部开发流程这些开发流程在在后续的章节也会有所涉及, 并且会告诉你传统 Web 应用开发与基于云原生的 Web 应用开发最为重要的不同点的同时也会巩固一些 Spring Boot 和 Spring MVC 中必要的知识点, 以及会对如何测试以及将应用部署至生产环境中需要注意的事项. 

I'll also explain some of the guidelines recommended by the 15-Factor methodology, including dependency management, concurrency, and API first. 
我同样会介绍 15-Factor 方法论中推荐的知道方针其中包括管理依赖, 并发以及 API. 


Along the way, you'll implement the Catalog Service application you initialized in the previous chapter.
同时, 你将会负责完成前几章节中的 Catalog Service 应用的开发工作. 

It will be responsible for managing the catalog of books in the Polar Bookshop system. 
Catalog Service 该服务将负责用于管理 Polar 书店系统中所有书本的目录.


* Note
* 注意事项
The source code for the example in this chapter is available in the /Chater03/03-begin and /Chapter03/03-end folders, 
containing the initial and final state of the project. 
本章节中示例项目源码可以在 /Chapter03/03-begin 以及 /Chapter03/03-end 文件夹中找到, 其中包含项目的初始阶段的文件, 以及项目完成阶段的文件. 
(github.com/ThomasVitale/cloud-native-spring-in-action)

## 3.1 Bootstrapping a cloud native project 
## 3.1 启动云原生项目

Starting a new development project is always exciting. 
开展一个新的开发项目总是令人兴奋的. 

The 15-Factor methodology contains some partical guidelines when bootstratping a cloud native application.
15-Factor 方法论中涵盖了在启动云原生应用时实际可用的指导方案.

















