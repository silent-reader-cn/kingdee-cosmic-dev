---
title: "OpenAPI新特性：操作API敏感数据脱敏"
entityId: "408204299626275584"
category: "用户手册 / 操作API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/408204299626275584?productLineId=29&lang=zh-CN"
createdAt: "2023-01-31 10:18:09"
updatedAt: "2025-12-19 10:11:55"
views: 7986
---

# OpenAPI新特性：操作API敏感数据脱敏

为保护苍穹平台个人数据的隐私安全，开放平台查询和保存操作API对接隐私中心，支持在调用API接口时，对入参和出参中的敏感数据进行脱敏。

发布版本：苍穹V5.0

上线日期：2023-01-12

补丁号：V5.0.014（BOS）

 操作指引

 1前提条件1：开启租户级参数“privacycenter.enable”，启用隐私中心

2前提条件2：为需要脱敏的业务对象，配置数据安全标签和隐私方案，路径：基础服务云 → 安全管理 → 隐私管理

3前提条件3：在操作API详情界面，打开脱敏开关，路径：开放服务云 → OpenAPI → API管理 → API开发

 特性效果展示

## 1. 应用场景

外部系统调用苍穹操作API时，数据脱敏的需求集中在查询和保存API的使用过程中。OpenAPI可对查询API返回数据中的敏感数据进行脱敏；同时，还可以对保存API请求参数中的敏感数据进行脱敏。最终打印出的API日志也是脱敏后的效果，来保障企业的数据隐私安全。

## 2. 功能介绍

### 2.1 隐私中心配置

路径：系统服务云 → 隐私中心 ，为需要脱敏的业务对象字段，分别配置数据安全标签和脱敏规则，配置完成后发布。

![](https://vip.kingdee.com/download/0109288214e69cbd4de0af299f1a0a62ad39.png)

![](https://vip.kingdee.com/download/010927b33d1638be4617a7ef708e73f2f6c3.png)

### 2.2 打开API脱敏开关

路径：开放服务云 → OpenAPI → API管理 → API开发。打开API管理列表。找到通过零代码配置生成的查询API，并在配置项中勾选上“是否脱敏”。

![](https://vip.kingdee.com/download/0109d89dd48a89cd4d42a0333e18442e2ce6.png)

![](https://vip.kingdee.com/download/0109bfc73a1cc0704ca690e4e2006e988d4d.png)

### 2.3 API在线测试

点击“API测试”按钮，可以在系统中实时调试，查看API脱敏效果。

![](https://vip.kingdee.com/download/01091d41476f86734fad8dd9ceeee775889a.png)

### 2.4 API日志脱敏

无论是调用查询或保存操作API，API调用日志中记录的都是脱敏后的日志信息。

![](https://vip.kingdee.com/download/0109dbe3ab32854e4eb7b9de6f8ae470d698.png)

![](https://vip.kingdee.com/download/010994a63d5a964e4a349c9eb4e13f6443ec.png)

## 3.常见问题

Q：所有表单都能够支持隐私方案配置吗？

A：当前版本仅支持单据和基础资料两种表单类型的隐私配置，动态表单、报表等表单需要二开接口完成特殊类表单的处理。

Q：为什么配置了隐私中心并打开了API脱敏开关后，仍然无法实现数据脱敏？

A：请检查是否满足了API脱敏的前提条件，如租户级MC参数“privacycenter.enable”，值是否为true，以及是够配置了数据安全标签和脱敏规则等。
