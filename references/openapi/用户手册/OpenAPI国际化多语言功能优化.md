---
title: "OpenAPI国际化多语言功能优化"
entityId: "453557180935869184"
category: "用户手册"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/453557180935869184?productLineId=29&lang=zh-CN"
createdAt: "2023-06-05 13:54:19"
updatedAt: "2025-12-19 10:12:23"
views: 4591
---

# OpenAPI国际化多语言功能优化

优化了OpenAPI对多语言文本的支持，更加灵活易用。

发布版本：苍穹V5.0

上线日期：2023-05-21

补丁号：V5.0.021（BOS）

 特性效果展示

## 1 功能介绍

苍穹平台OpenAPI支持国际化多语言，当通过OpenAPI执行查询或保存操作时，系统会获取访问令牌（access_token）上下文中的语言（language），自动处理多语言文本。旧版本中API仅返回或保存当前语言的数据；新版本优化了对多语言文本的支持，具体优化如下：

1. 查询操作API，通过开关配置，支持一次返回字段的所有语言数据；
2. 保存操作API，支持使用map形式传入多语言字段，保存字段所有语言数据；
3. 调用接口时支持自定义语言环境，在请求头中传入Accept-Language（仅v2接口），优先级高于访问令牌上下文。

## 2 应用场景

在金蝶AI苍穹单据或基础资料中，多语言文本是比较特殊的字段，OpenAPI支持查询单据或基础资料中的多语言文本字段。同时，用户可以通过接口保存当前语言或所有语言的数据。

## 3 操作示例

### 3.1 查询接口，返回所有语言的供应商名称

当企业有部分供应商为跨国公司时，因此，在进行供应商管理时，需要启用多语言字段，分别维护供应商的英语名称与简称。

![](https://vip.kingdee.com/download/010900a90e30e6e4444d8074f65c2b12474a.png)

第三方系统通过接口查询供应商信息时，首先需要获取access_token，此时需要传入默认系统语言作为参数，不同语言的标识如下：

- 简体中文：zh_CN
- 繁体中文：zh_TW
- 英文：en_US

![](https://vip.kingdee.com/download/01098e962e67944d41c3a5e531b57255b438.png)

在请求头中携带accesstoken并调用查询接口，默认返回对应语言的数据，即，如传入英文语言标识，那么查询供应商名称和简称时，会返回对应的英文名称。

![](https://vip.kingdee.com/download/0109aa72f7d0f9984fa5916fb8a7d6a58ef6.png)

若第三方系统需要一次返回所有语言的供应商名称信息，可以通过打开API配置中的‘返回多语言’选项实现路径：【开放服务云】 → 【OpenAPI】→ 【API管理】→ 【API开发】

![](https://vip.kingdee.com/download/01091293735d437a435e9fb578bc2ab6bd7a.png)

第三方系统若再次调用接口，此时会返回所有语言的供应商名称信息。

![](https://vip.kingdee.com/download/0109ddfc1b72ee514fc6b051823d0f9da3dc.png)

### 3.2 保存接口，保存所有语言的供应商名称

以供应商基础资料为例，通过接口保存不同语言的供应商名称。

当只需要保存某种语言数据时，同样在获取accesstoken的请求参数中，定义language，将系统语言定义为英文。

![](https://vip.kingdee.com/download/010953df3da47e30409a8e336ce262c57a50.png)

在请求头中携带accesstoken并调用保存接口，就能成功将英文数据保存成功。

![](https://vip.kingdee.com/download/01094a1c58808cf948fc848a008d54301d4d.png)

当需要一次保存所以语言的供应商名称时，在请求参数中传入如下map样式：

"name":

{

"zh_CN": "这是简体",

"zh_TW": "这是繁体",

"en_US": "this is e"

}

![](https://vip.kingdee.com/download/01093098f756596046918991cbcf8f38b53e.png)

![](https://vip.kingdee.com/download/0109b4203c42c8da482f824d7e84ae007aed.png)

### 3.3 请求头自定义语言环境

**使用场景：**当使用基本认证等方式，无法定义访问令牌的语言环境上下文，或使用accesstoken认证时，不想在上下文中固定环境language，而是在接口调用时定义语言环境，OpenAPI也支持在请求头中自定义Accept-Language，定义后的效果如下：

- 接口查询多语言字段（不打开返回多语言开关），会返回Accept-Language中的多语言数据；
- 接口保存多语言字段（不传入map），会保存Accept-Language中定义的语言数据。

![](https://vip.kingdee.com/download/0109ec1acfccf78842558b6ad9c8f9beb8b2.png)

![](https://vip.kingdee.com/download/01098adbcc9490484ab385489f2d30c0ac08.png)

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
