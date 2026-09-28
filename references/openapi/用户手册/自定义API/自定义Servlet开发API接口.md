---
title: "自定义Servlet开发API接口"
entityId: "407938727974135040"
category: "用户手册 / 自定义API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/407938727974135040?productLineId=29&lang=zh-CN"
createdAt: "2023-01-30 16:42:52"
updatedAt: "2025-12-19 10:11:39"
views: 9708
---

# 自定义Servlet开发API接口

发布版本：苍穹V7.0

上线日期：2024-10-17

补丁号：V5.0.014（BOS）、V7.0.1（BOS）

 新特性介绍

- 自定义API支持Servlet开发
- 自定义Servlet API支持流式模式

 操作指引

 1路径：【开发服务云】 → 【开放平台】→ 【参数配置】，打开开关“自定义servlet功能”

2开发者自行开发一个插件，测试此API功能是否符合预期

 特性效果展示

## 1. 概述

OpenAPI2.0引擎 （>=5.0.014版本）允许客户开发自定义的Servlet来开发接口，用来处理复杂场景。例如：

1. 处理流的断点续传；

2. 与异构系统对接，第三方系统做了很多参数限制。如限制了特殊的URL、请求方式、特殊的Content-Type；

3. 特殊的数据加密、证书处理API（标准引擎目前支持 AES/SM4数据加密，以及SHA256签名）；

4. 自行处理入参的反序列化、出参结果的序列化操作；

5. 需要自行处理HttpServletRequest或HttpServletResponse对象的特殊需求；

6. 其他的复杂场景需求。

具体接口开发demo，参考自定义Servlet开发API接口.pdf

Servlet接口流式处理开发案例，参考Stream流式API开发案例.pdf

## 2. 操作示例

### 2.1 打开参数开关

路径：【开发服务云】 → 【开放平台】→ 【参数配置】，打开“自定义servlet功能” 开关。打开后新增API时可以选择Servlet开发选项。

![](https://vip.kingdee.com/download/01091d4b7b8958854d1fb1c6e9e0914b49d4.png)

### 2.2 Servlet开发自定义API

路径：【开发服务云】 → 【开放平台】→ 【API管理】→ 【API开发】，进入API列表界面，点击“新增”按钮，选择自定义API（Servlet开发）。

![](https://vip.kingdee.com/download/01097136054b0dca48dd9818570519e038b3.png)

开发者事先实现ICustomApiServlet接口，并将类名正确填写在接口基本信息中，根据实际场景，维护API编码、API名称、请求地址、请求参数和返回参数等信息。点击“保存”按钮，接口开发完成。

![](https://vip.kingdee.com/download/010994530610b64d4b9a8f0a66303ebe8e96.png)

可以点击“API测试”按钮，来测试接口是否满足实际需求。

![](https://vip.kingdee.com/download/010973b1df8a05944a978c457a33f03bb481.png)

## 3. 注意事项

1. 自行开发的Servlet-API接口仍然受认证鉴权、API安全、IP策略、限流策略等统一控制；

2. 只允许处理当前数据中心的上下文（当前数据中心的RequestContext），不能创建新的线程；

3. 会统一记录请求日志、执行API统计监控；

4. 自定义的Servlet-API实现类必须部署在Web节点，其内部逻辑仍然可以调用微服务操作。建议对HttpServletRequest或HttpServletResponse对象的操作部署在Web节点，但具体的业务逻辑处理，代码仍部署在二开业务JAR包及对应的业务容器中，实现更清晰的逻辑分离；

5. 在处理HttpServletResponse等操作时，注意及时释放、关闭Stream流，以避免资源泄露。
