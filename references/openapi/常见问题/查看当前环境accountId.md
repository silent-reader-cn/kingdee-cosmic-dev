---
title: "查看当前环境accountId"
entityId: "376304364442380800"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/376304364442380800?productLineId=29&lang=zh-CN"
createdAt: "2022-11-04 09:39:12"
updatedAt: "2024-04-28 11:10:18"
views: 6284
---

# 查看当前环境accountId

**问题描述**

如何快速获取金蝶AI苍穹当前环境租户id和数据中心id？

# 解决方法

- 方法一：在金蝶AI苍穹MC租户管理中心，即可查看租户和数据中心信息。

- 方法二：路径：开放服务云 - OpenAPI - 安全策略 - 第三方应用，点击【当前账套信息】按钮查看。

![](https://vip.kingdee.com/download/01095e510aee6dfe4e289d0cd46a4150d701.png)

- 方法三：进入第三方应用详情页面，点击【获取Token示例】按钮。

![](https://vip.kingdee.com/download/01099b8ce1b49c8045ef974f895e64c2b2fe.png)

- 方法四：以谷歌为例，按F12进入浏览器开发者模式，点击浏览器刷新按钮，见下图，Network - Fetch/XHR下，在第二行getconfig的Preview信息中，能看到当前的数据中心和租户信息。

![](https://vip.kingdee.com/download/0100b2868d0b12bd4b95952fc6cf3a641760.png)

# 注意事项

- 数据中心id属于敏感信息，避免泄漏。
