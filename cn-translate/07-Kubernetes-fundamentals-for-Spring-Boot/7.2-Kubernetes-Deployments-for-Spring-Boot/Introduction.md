## 7.2 Spring Boot 的 Kubernetes Deployment

本节将带您了解作为开发人员将使用的 Kubernetes 对象，以及与平台团队有效沟通并将应用程序部署到集群所需的词汇。

您已经完成了 Spring Boot 应用程序的容器化。Kubernetes 上的 Spring Boot 应用程序仍然打包为容器，但它运行在由 Deployment 对象控制的 Pod 中。

Pod 和 Deployment 是使用 Kubernetes 时需要理解的核心概念。

### 7.2.1 从容器到 Pod

Pod 是 Kubernetes 中最小的可部署单元。它封装了一个或多个容器，这些容器共享存储和网络资源。Pod 中的容器始终一起调度在同一个节点上。

Pod 的主要特点：

* **共享网络** — Pod 中的所有容器共享相同的网络命名空间，可以使用 localhost 互相通信
* **共享存储** — 可以使用卷在容器之间共享数据
* **生命周期绑定** — Pod 中的容器同时启动和停止
* **最小部署单元** — 不能单独部署容器，只能部署 Pod

### 7.2.2 使用 Deployment 控制 Pod

Deployment 是 Kubernetes 中用于管理 Pod 的核心对象。它提供：

* **声明式更新** — 定义所需状态，Kubernetes 会自动达到
* **滚动更新** — 逐步更新 Pod，确保零停机
* **回滚** — 如果更新有问题，可以回滚到之前的版本
* **扩展** — 轻松增加或减少 Pod 副本数

Deployment YAML 示例：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: catalog-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: catalog-service
  template:
    metadata:
      labels:
        app: catalog-service
    spec:
      containers:
      - name: catalog-service
        image: ghcr.io/your-username/catalog-service:latest
        ports:
        - containerPort: 9001
        env:
        - name: SPRING_DATASOURCE_URL
          value: jdbc:postgresql://polar-postgres:5432/polardb_catalog
```

### 7.2.3 为 Spring Boot 应用程序创建 Deployment

使用 kubectl 创建 Deployment：

```bash
$ kubectl apply -f catalog-service-deployment.yaml
```

查看 Deployment 状态：

```bash
$ kubectl get deployments
$ kubectl get pods
```

查看 Pod 日志：

```bash
$ kubectl logs -l app=catalog-service
```

### 7.2.4 在 Kubernetes 上运行 Spring 应用程序

将应用程序部署到 Kubernetes 后，您需要访问它。默认情况下，Pod 只能从集群内部访问。要从外部访问，您需要创建 Service。
