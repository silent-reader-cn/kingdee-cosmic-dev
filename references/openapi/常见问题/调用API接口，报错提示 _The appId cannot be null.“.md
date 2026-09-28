---
title: "调用API接口，报错提示 \"The appId cannot be null.“"
entityId: "754033420287437056"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/754033420287437056?productLineId=29&lang=zh-CN"
createdAt: "2025-09-11 17:39:37"
updatedAt: "2025-09-11 17:48:31"
views: 691
---

# 调用API接口，报错提示 "The appId cannot be null.“

## 1 问题描述

当第三方系统请求OpenAPI时，请求报错提示：The appId cannot be null.。

![上传图片](https://vip.kingdee.com/download/0100422cec744759448f931db704bed95cb9.png)

## 2 问题分析

该错误的触发原因：

**API 所属应用已被删除**：当前调用的 API 对应的原始应用已不存在，导致系统无法识别其归属。同时，第三方应用的 API 授权清单中，**存在 “所属应用” 字段为空的接口。**

当系统验证第三方应用的接口权限时，会检测到异常 API，因无法获取有效的 appId（应用标识），最终触发 “appId 不能为空” 的错误提示。

## 3 解决方法

1. 登录系统，路径：【开放服务云】-【OpenAPI】-【安全策略】-【第三方应用】。进入第三方应用的 “API 授权清单” 。
2. 筛选并找到 “所属应用” 字段为空的异常 API ，直接删除后保存，再次重新调用即可。

![上传图片](https://vip.kingdee.com/download/0100154650cc18be41a18db9c8c96f1c4b84.png)
