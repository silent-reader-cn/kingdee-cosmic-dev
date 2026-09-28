---
title: "API接口允许匿名访问"
entityId: "119023921520783104"
category: "用户手册 / API1.0 / API服务管理"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/119023921520783104?productLineId=29&lang=zh-CN"
createdAt: "2020-11-24 10:38:34"
updatedAt: "2024-11-04 17:15:33"
views: 8738
---

# API接口允许匿名访问

### 1 适用范围

本文档适用于所有金蝶AI苍穹开放平台用户，介绍如何设置接口匿名访问。

2 业务场景

外部系统访问金蝶AI苍穹API服务时，正常流程一般是先在开放平台经过注册，生成第三方应用的appid和appsecret，然后通过接口获取应用令牌（app_token）和访问令牌(access_token)，后续每次请求中，带上访问令牌进行接口调用。

特殊场景下，当企业对某些API服务的安全性管控要求较低，有部分API接口，允许用户在未登录的情况下进行访问，如客户定义了某个接口，让匿名用户也能直接调用，查询某些基础资料或单据信息，此时，可以在开放平台开启API匿名功能，在接口层面进行设置。

### 3功能实现

3.1 开启MC开关

系统路径：苍穹管理中心 → 基础数据维护 → 环境公共配置项，目录：/root/config/common/prop/api.properties，开关名称：**“login_api_support_anonymous”**，该开关为公共配置，默认为false，此时MC租户的API接口不允许匿名访问。将该开关值设置为true，则允许匿名访问。

**特别注意**：在MC修改配置后，需要点击发布，否则苍穹无法读取到最新参数。

![](https://vip.kingdee.com/download/0100788b2e2023964c50a8fccdb2aa2692de.png)

3.2 设置API服务，允许匿名访问

当MC开关开启后，进入金蝶AI苍穹开放平台的API服务定义界面，系统路径：开发服务云 → 开放平台 → API服务管理，找到需要开启匿名访问的API服务，点击API名称进入到编辑界面。

![](https://vip.kingdee.com/download/0100f6fcdb3892154b69a09eab2b89f29a4c.png)

在API基本信息中，打开匿名访问开关，点击“保存”按钮，此时API服务已允许匿名用户访问。

![](https://vip.kingdee.com/download/0100202a94e3da424837bbb39329fc4854ab.png)

3.3 API服务调用

当API服务接口允许【匿名访问】后，在请求头或URL参数中不带上访问令牌（access_token），此时调用结果返回消息推送成功。

![](https://vip.kingdee.com/download/0100755499b482c74ad9a786fdb1cab5e8ac.png)

反之，当API服务接口不允许【匿名访问】，API调用结果返回未经授权的访问。

![](https://vip.kingdee.com/download/01007b488bd1fed4431a9b892945e00c4aad.png)

![](https://vip.kingdee.com/download/010034166f23e5344a7080ae959f7f2d0fdb.png)

### 4 注意事项

1）若设置API接口匿名访问后，匿名调用仍不生效，可能是由于该租户存在多个数据中心，且当前设置匿名API的数据中心和默认数据中心不一致。此时，**必须在请求header中添加参数accountId**，指定数据中心的API服务，匿名访问才能生效。

2）匿名访问，请求方式为POST时，必须在请求头中添加accountId 。在URL参数中添加accountId无意义，接口会自动路由到默认数据中心（MC配置）。

3）匿名访问，GET请求，查询为例，需要在请求头或URL中添加accountId，(URL中必须大写，传accountId），才能正常调用。

4）API匿名使用的是guest身份，在操作单据时平台会[**有权限限制**](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337340351087360&id=329557236689250560&productLineId=29)，一般用于查询操作，无法更新数据。

**5）启用匿名****访问，该API接口无需登录即可以访问，请谨慎选择。由于匿名访问导致数据泄露的风险，请您自行承担。**
