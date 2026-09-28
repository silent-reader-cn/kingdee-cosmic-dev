---
title: "持续更新 | 【OpenAPI】重大新特性发布汇总"
entityId: "457115890811666944"
category: "动态与公告 / 新特性公告"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/457115890811666944?productLineId=29&lang=zh-CN"
createdAt: "2023-06-15 09:35:21"
updatedAt: "2024-06-27 16:50:09"
views: 1164
---

# 持续更新 | 【OpenAPI】重大新特性发布汇总

想知道OpenAPI的最新功能特性有哪些？

想了解新功能是否能满足你的场景需求？

那就不要错过本帖子！汇总OpenAPI每月重大新特性，带你第一时间获取产品最新特性资讯~

![](https://vipfront.obs.cn-north-4.myhuaweicloud.com/emotion/define/86.gif) 帖子持续更新，推荐收藏，回看干货不迷路！

附：OpenAPI完整特性帖：[金蝶AI苍穹开发平台补丁新特性汇总](https://developer.kingdee.com/knowledge/specialDetail/174931520225092096?category=181160777515051776&id=447460388506859520&productLineId=29)

苍穹补丁下载路径：[http://download.kdcloud.com/login#/download](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fdownload.kdcloud.com%2Flogin%23%2Fdownload)

---

## 2023.06 重大新特性

1、支持“操作API”零代码配置余额模型和日志表单的查询接口，降低API开发门槛

为提升用户接口开发效率，降低集成工作量，新版本开放平台**支持零代码配置日志表单和余额模型的查询接口**，本次支持了**“操作API”**零代码配置余额模型和日志表单的查询接口。

同样的操作方法，也可以**零代码配置日志表单**的查询接口。

**发布版本：***BOS V5.0.023*更多功能细节，点击 [操作API支持余额模型和日志表单](https://vip.kingdee.com/article/464748428388700416?productLineId=29&isKnowledge=2)了解。

![](https://vip.kingdee.com/download/01091f8215a5ff5648518fceb26cc1b4825f.png)

*打开API管理列表 - 新增操作API*

## ![](https://vip.kingdee.com/download/010964139f747eef4722b8fb32506e9da00a.png)

*新增操作API - 业务对象选择余额模型*

**2、优化第三方应用交互，以卡片形式提升用户体验**

进一步优化了第三方应用交互，将**认证方式、访问控制和加密策略展示成卡片形式**，提升用户体验。

**发布版本：***BOS V5.0.023*更多功能细节，点击 [第三方应用新版交互体验](https://vip.kingdee.com/article/464754959607876608?productLineId=29&isKnowledge=2)了解。

![](https://vip.kingdee.com/download/010975b1eaa38ca646ddbc7f1bf4126f6b2f.png)

*卡片形式*

## 2023.05 重大新特性

1、开发必备！苍穹开放平台一键导出Swagger API文档！

API列表支持导出Swagger文档，遵循最新的Swagger3.0规范，提供更友好的统一交互体验。Swagger是一种广泛使用的API文档规范，它具有清晰的结构和交互式的界面，帮助开发人员更直观地了解和调试API。

**发布版本：***BOS V5.0.021*更多功能细节，点击 [开放平台新特性：导出Swagger](https://vip.kingdee.com/article/454600313165665024?productLineId=29&isKnowledge=2)了解。

![](https://vip.kingdee.com/download/010941c6f2fd3afa48aba729a3f5ad61913e.png)

*“导出swagger”按钮操作界面*

![](https://vip.kingdee.com/download/0109b71711ae51c240e987874e2d32b1ff90.png)

*Swagger样式的API文档*

2、提升API多语言支持，实现一次获取所有语言数据

在旧版本中，API只会把当前语言的返回或保存。**该版本优化了对多语言文本的支持**，更加灵活，具体优化如下：

1) 查询操作API，通过开关配置，支持**一次返回字段所有语言数据**；

2) 保存操作API，使用map形式传入多语言字段，支持保存字段所有语言数据；

3) 支持调用接口时自定义语言环境，在请求头传入Accept-Language（仅v2接口），优先级比访问令牌中language更高。

**发布版本：***BOS V5.0.021*更多功能细节，点击[OpenAPI 国际化多语言功能优化](https://vip.kingdee.com/article/453557180919091968?productLineId=29&isKnowledge=2)了解。

![](https://vip.kingdee.com/download/01096db4db702df2446fa1b5cd224520b6a0.png)

*示例：接口保存的供应商名称所有多语言信息*
