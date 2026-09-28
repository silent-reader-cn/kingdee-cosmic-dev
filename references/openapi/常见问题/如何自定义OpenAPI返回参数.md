---
title: "如何自定义OpenAPI返回参数"
entityId: "506782654369362688"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/506782654369362688?productLineId=29&lang=zh-CN"
createdAt: "2023-10-30 10:53:20"
updatedAt: "2024-04-28 10:27:46"
views: 4968
---

# 如何自定义OpenAPI返回参数

## 问题描述

如何自定义OpenAPI的返回参数，比如新增返回参数或修改已有的data、errorCode参数

## 解决方法

- 方法一：通过API扩展插件，实现对API的**出参**和**入参**根据具体业务场景**自定义序列化**和**反序列化**类，即按需定义返回参数。适用版本：V5.0.018以上。

![](https://vip.kingdee.com/download/0109970f091348af4d09bd50b282351d0f96.png)

下图代码示例中的response即为API返回值。

![](https://vip.kingdee.com/download/010947951f1bc97c40039227e3d5ba5b5287.png)

代码demo：序列化插件使用文档.pdf

- 方法二：通过自定义API，在插件中自行定义返回参数，同时打开API配置开关：“出参仅返回data域”，接口会默认不返回包括data参数在内的同级参数errorCode、status、message。适用版本：V5.0.005以上。

![](https://vip-admin.kingdee.com/download/0109c0a09460a7a0484b8a5e98dae0aa6550.png)

### 更多资讯

[OpenAPI自定义序列化插件](https://developer.kingdee.com/article/418816108595089920?productLineId=29)
