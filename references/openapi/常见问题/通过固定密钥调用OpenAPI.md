---
title: "通过固定密钥调用OpenAPI"
entityId: "376375102336315904"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/376375102336315904?productLineId=29&lang=zh-CN"
createdAt: "2022-11-04 14:20:17"
updatedAt: "2023-10-27 17:43:13"
views: 3779
---

# 通过固定密钥调用OpenAPI

**问题描述**

场景一：企业同一个局域网内，其他系统调用苍穹接口时，不想通过access token认证反复获取令牌，而是想要有个固定密钥作为认证标识，就能调用苍穹api接口，如何实现？

场景二：系统对接时，调用苍穹接口成功后，需要传给外部系统一个无需认证的网址用于对方回调，如何实现？

# 解决方法

开放平台第三方应用基本认证是一种更安全、方便的方案，可以广泛应用于接口回调的场景。只需要在请求的URL参数或请求header中带上固定的openApiSign凭证，形式如下： {host}?openApiSign=xxx

![](https://vip.kingdee.com/download/01096a4b1f35194f454192ba5751c03f2ce0.png)

也可通过在API接口（2.0）上配置回调地址的方式，查看具体的接口回调地址。

参考文档：[API支持配置自动生成接口回调地址](https://vip.kingdee.com/article/352773265946763776)

# 适用版本

V5.0.002

# 注意事项

- 当第三方应用启用基本认证后，由于基本认证密钥是长期有效的，必须配合API授权清单来保证系统整体安全。
- 当苍穹与外围系统对接时，若存在某个接口回调场景，对方系统接口协议规定：访问路径需要为固定接口且不可以添加参数，或在接口访问路径中不允许有“?”，苍穹开放平台回调接口可使用如下格式： {host}/$/openApiSign/xxx/billno/cugyi5/pageSize/10/pageno/1。URL中openApiSign必须在特殊符号“$”后，在其他URL参数前。
