# 附录 A 设置开发环境

**本附录内容**

* 设置 Java
* 设置 Docker
* 设置 Kubernetes
* 设置其他工具

在本附录中，您将找到设置开发环境和安装我们在整本书中用于构建、管理和部署云原生应用程序的工具的说明。

## A.1 Java

本书中的所有示例都基于 Java 17，这是撰写本文时 Java 的最新长期支持版本。您可以安装任何 OpenJDK 17 发行版。我将使用 Adoptium 项目（[https://adoptium.net](https://adoptium.net)）的 Eclipse Temurin，以前称为 AdoptOpenJDK，但您可以随意选择其他发行版。

在您的计算机上管理不同的 Java 版本和发行版可能很痛苦。我建议使用像 sdkman（[https://sdkman.io](https://sdkman.io)）这样的工具来轻松安装、更新和切换不同的 JDK。在 macOS 和 Linux 上，您可以按如下方式安装 sdkman：

```bash
$ curl -s "https://get.sdkman.io" | bash
```

有关 Windows 的安装说明，请参考官方文档。安装后，通过运行以下命令检查所有可用的 OpenJDK 发行版和版本：

```bash
$ sdk list java
```

然后选择一个发行版并安装它。例如，我可以按如下方式安装撰写本文时可用的最新 17 版本的 Eclipse Temurin：

```bash
$ sdk install java 17.0.3-tem
```

当您阅读本节时，可能会有更新的版本可用，因此请检查从 list 命令返回的列表以识别最新版本。

在安装过程结束时，sdkman 会询问您是否要将该发行版设为默认发行版。我建议您选择是，以确保您可以从您在整本书中构建的所有项目中访问 Java 17。您始终可以使用以下命令更改默认版本：

```bash
$ sdk default java 17.0.3-tem
```

现在让我们验证 OpenJDK 安装：

```bash
$ java --version
openjdk 17.0.3 2022-04-19
OpenJDK Runtime Environment Temurin-17.0.3+7 (build 17.0.3+7)
OpenJDK 64-Bit Server VM Temurin-17.0.3+7 (build 17.0.3+7, mixed mode)
```

您还可以选择仅在当前 shell 的上下文中更改 Java 版本：

```bash
$ sdk use java 17.0.3-tem
```

最后，如果您想检查当前 shell 中配置的 Java 版本，可以按如下方式进行：

```bash
$ sdk current java
Using java version 17.0.3-tem
```

## A.2 Docker

Open Container Initiative（OCI）是一个 Linux 基金会项目，定义了使用容器的行业标准（[https://opencontainers.org](https://opencontainers.org)）。具体来说，OCI Image Specification 定义了如何构建容器镜像，OCI Runtime Specification 定义了如何运行这些容器镜像，OCI Distribution Specification 定义了如何分发它们。我们在整本书中用于使用容器的工具是 Docker，它符合 OCI 规范。

在 Docker 网站（[www.docker.com](http://www.docker.com)）上，您可以找到在本地环境中设置 Docker 的说明。我将使用撰写本文时可用的最新版本：Docker 20.10 和 Docker Desktop 4.11。

* 在 Linux 上，您可以直接安装 Docker 开源平台。它也称为 Docker Community Edition（Docker CE）。
* 在 macOS 和 Windows 上，您可以选择使用 Docker Desktop，这是一个构建在 Docker 之上的商业产品，使您能够从这些操作系统运行 Linux 容器。在撰写本文时，Docker Desktop 对个人使用、教育、非商业开源项目和小型企业免费。请在安装软件之前仔细阅读 Docker Subscription Service Agreement，并确保您遵守它（[www.docker.com/legal](http://www.docker.com/legal)）。

Docker Desktop 支持 ARM64 和 AMD64 架构，这意味着您可以在配备 Apple Silicon 处理器的新 Apple 计算机上运行本书中的所有示例。

如果您在 Windows 上工作，Docker Desktop 提供两种类型的设置：Hyper-V 或 WSL2。我建议您选择后者，因为它提供更好的性能，并且更稳定。

Docker 预配置为从 Docker Hub 下载 OCI 镜像，Docker Hub 是一个托管许多流行开源项目镜像的容器注册表，如 Ubuntu、PostgreSQL 和 Redis。它是免费使用的，但如果您匿名使用，它会受到严格的速率限制策略。因此，我建议您在 Docker 网站（[www.docker.com](http://www.docker.com)）上创建一个免费帐户。

创建帐户后，打开终端窗口并向 Docker Hub 进行身份验证（确保您的 Docker 引擎正在运行）。由于它是默认容器注册表，因此您无需指定其 URL：

```bash
$ docker login
```

出现提示时，输入您的用户名和密码。使用 Docker CLI，您现在可以与 Docker Hub 交互以下载镜像（pull）或上传您自己的镜像（push）。例如，尝试从 Docker Hub 拉取官方 Ubuntu 镜像：

```bash
$ docker pull ubuntu:22.04
```

在整本书中，您将了解更多关于使用 Docker 的知识。在那之前，如果您想尝试使用容器，我将为您提供一个用于控制容器生命周期的有用命令列表（表 A.1）。

**表 A.1 用于管理镜像和容器的有用 Docker CLI 命令**

| Docker CLI 命令 | 功能 |
|----------------|------|
| `docker images` | 显示所有镜像 |
| `docker ps` | 显示正在运行的容器 |
| `docker ps -a` | 显示所有已创建、已启动和已停止的容器 |
| `docker run <image>` | 从给定镜像运行容器 |
| `docker start <name>` | 启动现有容器 |
| `docker stop <name>` | 停止正在运行的容器 |
| `docker logs <name>` | 显示给定容器的日志 |
| `docker rm <name>` | 删除已停止的容器 |
| `docker rmi <image>` | 删除镜像 |

我们在整本书中构建的所有容器都符合 OCI 规范，将与任何其他 OCI 容器运行时配合使用，例如 Podman（[https://podman.io](https://podman.io)）。如果您决定使用 Docker 以外的平台，请注意，我们用于本地开发和集成测试的一些工具可能需要额外的配置才能正常工作。

## A.3 Kubernetes

有几种方法可以在本地环境中安装 Kubernetes。以下是一些最常用的选项：

* **minikube**（[https://minikube.sigs.k8s.io](https://minikube.sigs.k8s.io)）允许您在任何操作系统上运行本地 Kubernetes 集群。它由 Kubernetes 社区维护。
* **kind**（[https://kind.sigs.k8s.io](https://kind.sigs.k8s.io)）允许您以 Docker 容器的形式运行本地 Kubernetes 集群。它主要是为了测试 Kubernetes 本身而开发的，但您也可以将其用于 Kubernetes 的本地开发。它由 Kubernetes 社区维护。
* **k3d**（[https://k3d.io](https://k3d.io)）允许您基于 k3s 运行本地 Kubernetes 集群，k3s 是由 Rancher Labs 实现的 Kubernetes 最小发行版。它由 Rancher 社区维护。

请随意选择最适合您需求的工具。我将在整本书中使用 minikube，因为它具有稳定性，并且与所有操作系统和架构兼容，包括新的 Apple Silicon 计算机。您应该至少有 2 个 CPU 和 4 GB 可用内存才能使用 minikube 运行书中的所有示例。

您可以在项目网站上找到安装指南（[https://minikube.sigs.k8s.io](https://minikube.sigs.k8s.io)）。我将使用撰写本文时可用的最新版本：Kubernetes 1.24 和 minikube 1.26。在 macOS 上，您可以使用 Homebrew 安装 minikube，如下所示：

```bash
$ brew install minikube
```

使用 minikube 运行本地 Kubernetes 集群需要容器运行时或虚拟机管理器。由于我们已经在使用 Docker，这就是我们将要使用的。在底层，任何 minikube 集群都将作为 Docker 容器运行。

安装 minikube 后，您可以使用 Docker 驱动程序启动新的本地 Kubernetes 集群。第一次运行此命令时，需要几分钟时间来下载运行集群所需的所有组件：

```bash
$ minikube start --driver=docker
```

我建议通过运行以下命令将 Docker 设为 minikube 的默认驱动程序：

```bash
$ minikube config set driver docker
```

要与新创建的 Kubernetes 集群交互，您需要安装 kubectl，即 Kubernetes CLI。安装说明可在官方网站上找到（[https://kubernetes.io/docs/tasks/tools](https://kubernetes.io/docs/tasks/tools)）。在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew install kubectl
```

然后您可以验证 minikube 集群是否正确启动，并检查节点是否在本地集群中运行：

```bash
$ kubectl get nodes
NAME STATUS ROLES AGE VERSION
minikube Ready control-plane,master 2m20s v1.24.3
```

我建议在不需要 minikube 时停止它，以释放本地环境中的资源：

```bash
$ minikube stop
```

在整本书中，您将了解更多关于使用 Kubernetes 和 minikube 的知识。在那之前，如果您想尝试使用 Kubernetes 资源，我将为您提供一些有用的命令（表 A.2）。

**表 A.2 用于管理 Pod、Deployment 和 Service 的有用 Kubernetes CLI 命令**

| Kubernetes CLI 命令 | 功能 |
|-------------------|------|
| `kubectl get deployment` | 显示所有 Deployment |
| `kubectl get pod` | 显示所有 Pod |
| `kubectl get svc` | 显示所有 Service |
| `kubectl logs <pod_id>` | 显示给定 Pod 的日志 |
| `kubectl delete deployment <name>` | 删除给定的 Deployment |
| `kubectl delete pod <name>` | 删除给定的 Pod |
| `kubectl delete svc <service>` | 删除给定的 Service |
| `kubectl port-forward svc <service> <host-port>:<cluster-port>` | 将流量从本地机器转发到集群内 |

## A.4 其他工具

本节将介绍一系列在整本书中用于执行特定任务的有用工具，例如安全漏洞扫描或 HTTP 交互。

### A.4.1 HTTPie

HTTPie 是一个方便的"命令行 HTTP 和 API 测试客户端"（[https://httpie.org](https://httpie.org)）。它专为人类设计，提供卓越的用户体验。请参考官方文档获取安装说明和有关该工具的更多信息。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew install httpie
```

作为安装的一部分，您将获得两个可以从终端窗口使用的工具：http 和 https。例如，您可以按如下方式发送 GET 请求：

```bash
$ http pie.dev/get
```

### A.4.2 Grype

在供应链安全的背景下，我们使用 Grype 扫描 Java 代码库和容器镜像中的漏洞（[https://github.com/anchore/grype](https://github.com/anchore/grype)）。扫描在您运行它的机器上本地进行，这意味着您的文件或工件都不会发送到外部服务。这使其非常适合更受监管的环境或气隔场景。有关更多信息，请参考官方文档。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew tap anchore/grype
$ brew install grype
```

该工具尚不适用于 Windows。如果您是 Windows 用户，我建议利用 Windows Subsystem for Linux 2（WSL2）并在那里安装 Grype。有关 WSL2 的更多信息，您可以参考官方文档（[https://docs.microsoft.com/en-us/windows/wsl/](https://docs.microsoft.com/en-us/windows/wsl/)）。

### A.4.3 Tilt

Tilt（[https://tilt.dev](https://tilt.dev)）旨在在使用 Kubernetes 时提供良好的开发人员体验。它是一个开源工具，提供在本地环境中构建、部署和管理容器化工作负载的功能。有关安装说明，请参考官方文档（[https://docs.tilt.dev/install.html](https://docs.tilt.dev/install.html)）。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew install tilt-dev/tap/tilt
```

### A.4.4 Octant

Octant（[https://octant.dev](https://octant.dev)）是一个"面向开发人员的 Kubernetes 开源 Web 界面，让您可以检查 Kubernetes 集群及其应用程序。"有关安装说明，请参考官方文档（[https://reference.octant.dev](https://reference.octant.dev)）。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew install octant
```

### A.4.5 Kubeval

Kubeval（[www.kubeval.com](http://www.kubeval.com)）是当您需要"验证一个或多个 Kubernetes 配置文件"时的方便工具。我们将在部署管道中使用它来确保所有 Kubernetes 清单格式正确且符合 Kubernetes API。有关安装说明，请参考官方文档（[www.kubeval.com/installation/](http://www.kubeval.com/installation/)）。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew tap instrumenta/instrumenta
$ brew install kubeval
```

### A.4.6 Knative CLI

Knative 是一个"基于 Kubernetes 的平台，用于部署和管理现代无服务器工作负载"（[https://knative.dev](https://knative.dev)）。该项目提供了一个方便的 CLI 工具，您可以使用它与 Kubernetes 集群中的 Knative 资源进行交互。有关安装说明，请参考官方文档（[https://knative.dev/docs/install/quickstart-install](https://knative.dev/docs/install/quickstart-install)）。

在 macOS 和 Linux 上，您可以使用 Homebrew 安装它，如下所示：

```bash
$ brew install kn
```
