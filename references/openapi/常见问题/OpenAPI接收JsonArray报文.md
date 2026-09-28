---
title: "OpenAPI接收JsonArray报文"
entityId: "399138577717794816"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/399138577717794816?productLineId=29&lang=zh-CN"
createdAt: "2023-01-06 09:54:13"
updatedAt: "2023-10-27 17:44:38"
views: 3131
---

# OpenAPI接收JsonArray报文

问题描述

场景：由于对接多套系统，导致企业外部系统无法调整报文格式，只能对外传递JSONArray 报文，那么在对接金蝶AI苍穹时，如何通过OpenAPI 实现请求入参时，接收JSONArray报文呢？

![](https://vip.kingdee.com/download/01090f81c2a1ea9d4806b2c19190ad102940.png)

# 解决方法

可以通过开放平台自定义API实现

- 方法一：使用自定义API-Servlet开发，接口开发者在代码中解晰报文（适用版本：V5.0.014）
- 方法二：使用自定义API-Java插件开发，使用String作为参数，在自定义API插件中反序列化String，然后解晰报文（适用版本：V5.0.002）

自定义Servlet开发API接口.pdf
