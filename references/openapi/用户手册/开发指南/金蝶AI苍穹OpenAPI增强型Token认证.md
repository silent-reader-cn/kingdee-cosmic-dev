---
title: "金蝶AI苍穹OpenAPI增强型Token认证"
entityId: "489812471545485056"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/489812471545485056?productLineId=29&lang=zh-CN"
createdAt: "2023-09-13 14:59:53"
updatedAt: "2025-12-19 10:12:50"
views: 84703
---

# 金蝶AI苍穹OpenAPI增强型Token认证

## 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V6.0.1 | 新增增强型Token认证模式 | 2023年10月 |
| V7.0.8 | 下架refreshToken接口 | 2025年04月 |
| V7.0.13 | 增强型Token接口多时区优化，时间戳参数支持零时区格式 | 2025年06月 |

---

## 1. 简介

### 1.1 背景介绍

为优化产品体验，进一步提升安全性，并进行资源隔离，苍穹V6.0版本新增了增强型Token认证模式，支持通过接口获取、刷新、验证及失效请求令牌，管理请求令牌的的全生命周期。

### 1.2 注意事项

- 新增第三方应用时，默认打开增强型Token认证开关，若用户关闭开关，则仍可通过getAppToken.do和login.do接口获取access_token；
- 若第三方系统需要免登调用附件相关接口（如attachment/preview.do等），此时不建议使用增强型Token认证。

### 1.3 优化内容

- 更规范：接口参考最新Oauth2.0认证方式，参数命名更加规范；
- 更易用：只需一次请求，即可获取请求令牌access_token和JWT，简单易用；
- 更安全：1）请求参数增加随机数和时间戳，有效防止恶意重放攻击，提升整体安全性；            2）增加限流和黑白名单检查功能，并支持密钥错误锁定；

3）认证参数支持加密脱敏，并在打印日志时隐藏敏感信息，防止信息泄露；

4）请求令牌access_token只允许在请求头中传递，不允许通过URL参数传递，避免造成资源权限外泄。

### 1.4 使用场景

在集成项目中，通过API接口进行集成时，需要首先调用getToken接口获取请求令牌，并缓存在调用端；在access_token过期（默认2小时有效）前，调用verifyToken验证access_token的有效性，并获取最新的过期时间。

在access_token即将过期时，支持通过refreshToken接口刷新access_token的有效期，从而在不换access_token的情况下继续访问OpenAPI资源。

### 1.5 接口列表

| **序号** | **接口名称** | **接口地址** | **说明** |
| --- | --- | --- | --- |
| 1 | 获取access_token令牌 | /kapi/oauth2/getToken | 获取请求令牌access_token，在第三方应用中启用JWT token后还会返回id_token，均可用于访问接口 |
| 2 | 检测令牌有效性 | /kapi/oauth2/verifyToken | 检测access_token/refresh_token有效性及过期时间，检测JWT token(id_token)有效性 |
| 3 | 撤回密钥令牌 | /kapi/oauth2/withdrawToken | 撤回access_token |

[开放平台OpenAPI调用流程参考](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=213309216805890816&productLineId=29)

## 2 特性详情

### 2.1 getToken

- **功能描述**：请求令牌（access_token）是第三方应用调用OpenAPI的调用凭证，客户端每次请求都需要在请求头中带上token，服务端以此来控制身份，当token过期后，服务端会销毁token，客户端需要重新请求获取token。

- **请求 URL**：http://{{localhost}}/kapi/oauth2/getToken
- **调用方式**：HTTP调用
- **请求方式**：POST
- **请求类型**：Content-Type:application/json
- **调用频率**：1分钟30次
- **token有效期**：2小时

**注意事项：**

- 获取请求令牌的次数是有限制的，同时，每个令牌的有效期为 2 小时，用户需要做好令牌的管理，在令牌快过期时（通过验证接口获取剩余过期时间比如1小时50分），可重新调用接口获取或调用刷新令牌接口延长有效期。
- 同时支持在Header和Body传输数据中心accountId。
- 注册第三方应用是获取access_token的前提条件，可点击查看[第三方应用介绍](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337544983020032&id=225286231527892224&productLineId=29)。

<https://vip.kingdee.com/tolink?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FopenApi%2FOpenApiDoc%2Fticket-token%2FgetComponentAccessToken.html%23%25E8%25B0%2583%25E7%2594%25A8%25E6%2596%25B9%25E5%25BC%258F>

**请求Body参数**

| **请求参数** | **必传** | **类型** | **说明** |
| --- | --- | --- | --- |
| client_id | 是 | String | 第三方应用系统编码，即appId |
| client_secret | 是 | String | 第三方应用AccessToken认证密钥，即appSecret |
| username | 是 | String | 第三方应用代理用户的用户名 |
| accountId | 是 | String | 数据中心id |
| language | 否 | String | 语言字串： zh_CN，zh_TW、en_US等。 默认系统默认语言，查询接口会返回对应的多语言文本字段 |
| nonce | 是 | String | 随机数 |
| timestamp | 是 | String | 时间戳[（兼容零时区格式，如：2025-06-12T00:00:10.009Z）](（兼容零时区格式，如：2025-06-12T00:00:10.009Z）)，当前时间前后5分钟 |

**请求参数示例**

```
{
    "client_id": "thirdappunittest_003",
    "client_secret": "Abcdrty@1234567890#@2",
    "username":"zhangSan",
    "accountId": "1355633519610561531",
    "language": "zh_CN",
    "nonce": "123",
    "timestamp": "2023-09-08 11:47:00"
}
```

**返回参数**

| 返回参数 | 类型 | 说明 |
| --- | --- | --- |
| data |  |  |
| - access_token | String | 请求令牌，第三方应用调用OpenAPI的凭证 |
| - token_type | String | 令牌类型，默认为Bearer，即任何持有token的用户都可以访问对应的资源 |
| - refresh_token | String | 刷新令牌，暂不支持 |
| - scope | String | 作用域，用户授权给第三方的权限，默认为API |
| - expires_in | Int | access_token的有效期，即距离过期的剩余时长（单位：毫秒） |
| - id_token | String | JWT（Json Web Token） |
| - id_token_expires_in | Int | JWT的有效期，即距离过期的剩余时长（单位：毫秒） |
| - language | String | 浏览器接收语言 |
| errorCode | String | 错误码，成功时为0 |
| message | String | 错误消息 |
| status | Boolean | 请求状态，true/false |

**返回参数示例**

```
{
"data": {
    "access_token":"OPENAPIAUTH_MTMzMTIwNDQ0NTk5NTc5NDQzMl9FZ3h4MXU1Zzd2Qk9kRjR4MzIxQXZKcXU5c2hpbzNCaTRtTGIzbEsyM3JnbmFJUUJEMEltZUt3UURYQmFFdDJIVnc3MWtyaTVUR01ZbTRDUGVETDVSamE2R0F1a2g5SGpVcmwx",
    "token_type": "Bearer",
    "refresh_token": "d367106c-de46-4fc4-9e1a-59cbcfc430d2",
    "scope": "API",
    "expires_in": "7199977",
    "id_token": "OPENAPIAUTH_ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5Sm1hV1FpT2lJeE16UTJOamN6T1NJc0luTjFZaUk2SW10a2FuZDBJaXdpWm5Cb2IyNWxJam9pTVRjeU9UazVPVGs1T1RraUxDSmxhV1FpT2lJeE1UUTNOVFl4TnlJc0ltWjBjblZsYm1GdFpTSTZJa2xGVWxBaUxDSm1iM0puYVdRaU9pSXhJaXdpWm1WdFlXbHNJam9pYVdWeWNFQnJhVzVuWkdWbExtTnZiU0lzSW1semN5STZJbXRrSWl3aWRYTmxjbWxrSWpvaU1UTTBOalkzTXpraUxDSm1ZbWw2Y0dGeWRHNWxjbWxrSWpvaU1DSXNJbVpzWVhOMGJHOW5hVzVwY0NJNklqRTNNaTR5TUM0eE5DNDJOeUlzSW1acGMyRmpkR2wyWldRaU9pSXhJaXdpWm05d1pXNXBaQ0k2SWpWaE1tUmxabU5pWlRSaU1EazFOMlpoTURobU9HTTNNaUlzSW1ac1lYTjBiRzluYVc1MGFXMWxJam9pTWpBeU15MHdPQzB5T1NBd01Eb3dNRG93TUM0d0lpd2labVZ1WVdKc1pTSTZJakVpTENKbWRXbGtJam9pTVRNME5qWTNNemtpTENKMWMyVnlWSGx3WlNJNklqRWlMQ0psZUhBaU9qRTJPVFEyTURReU1UZ3NJbWxoZENJNk1UWTVORFU1TnpBeE9Dd2labWx6Y21WbmFYTjBaV1FpT2lJeElpd2labkJ6ZDNOMGNtRjBaV2Q1YVdRaU9pSTNOakk1TnpjM09UVTNOekl3TURVek56WWlMQ0oxYzJWeWIzQmxibWxrSWpvaU5XRXlaR1ZtWTJKbE5HSXdPVFUzWm1Fd09HWTRZemN5SWl3aWRYTmxjbTVoYldVaU9pSkpSVkpRSW4wLi1ZZEd1cWhIX25Mcm5ibURnQTlfU2FvQkZsTGJWTTJEUmp2cnR4NXZwckk=",
    "id_token_expires_in": "7199977",
    "language": "zh_CN"
        },
    "errorCode": "0",
    "message": "",
    "status": true
}
```

**错误码说明**

| **错误码** | **说明** |
| --- | --- |
| 0 | 请求成功 |
| 401 | 不正确的第三方应用编码client_id或client_secret |
| 603 | 请求参数错误 |

<https://vip.kingdee.com/tolink?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FopenApi%2FOpenApiDoc%2Fticket-token%2FgetComponentAccessToken.html%23%25E8%25AF%25B7%25E6%25B1%2582%25E5%258F%2582%25E6%2595%25B0>

### 2.2 verifyToken

- **功能描述**：检测请求令牌的有效性。

- **请求 URL**：http://{{localhost}}/kapi/oauth2/verifyToken
- **调用方式**：HTTP调用
- **请求方式**：POST
- **请求类型**：Content-Type:application/json
- **调用频率**：1分钟30次
- **token有效期**：2小时

**请求Body参数**

| **请求参数** | **必传** | **类型** | **说明** |
| --- | --- | --- | --- |
| client_id | 是 | String | 第三方应用系统编码，即appId |
| token_type_hint | 是 | String | 令牌类型，access_token/id_token |
| token | 是 | String | 令牌值 |
| accountId | 是 | String | 数据中心id |
| nonce | 是 | String | 随机数 |
| timestamp | 是 | String | 时间戳，当前时间前后5分钟 |

**请求参数示例**

```
{
  "client_id": "thirdappunittest_003",
  "token_type_hint": "access_token",
    "token":"OPENAPIAUTH_MTMzMTIwNDQ0NTk5NTc5NDQzMl9peGdobmxERWluY1FpZDc2R2pjUDcyYlg0UTNwNDhpczZXM01NYTlsTDVhNEU2TFRkT0ZIWTlybUl5SDdvQUJ1ZGFSaGtWU0hGNlNRRTBjMjZ6MkxxQWRjbkNpTzBnd1ZzMW9P",
  "nonce": "1234",
  "timestamp": "2023-09-15 16:14:00",
  "accountId": "1331204445995794432"
}
```

**返回参数**

| 返回参数 | 类型 | 说明 |
| --- | --- | --- |
| data |  |  |
| - expires_in | Int | 令牌的有效期，即距离过期的剩余时长（单位：毫秒） |
| - active | Boolean | 是否有效，true/false |
| - scope | String | 作用域，用户授权给第三方的权限，默认为API |
| errorCode | String | 错误码，成功时为0 |
| message | String | 错误消息 |
| status | Boolean | 请求状态，true/false |

**返回参数示例**

```
{
    "data": {
    "expires_in": "7133040",
    "active": true,
    "scope": "API"
    },
    "errorCode": "0",
    "message": "",
    "status": true
}
```

**错误码说明**

| **错误码** | **说明** |
| --- | --- |
| 0 | 请求成功 |
| 603 | 请求参数错误 |
| 612 | AccessToken verify failed/JWT(id_token) 验证失败：已过期 |

### 2.3 withdrawToken

<https://vip-admin.kingdee.com/tolink?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foplatform%2FopenApi%2FOpenApiDoc%2Fticket-token%2FgetAuthorizerRefreshToken.html%23%25E6%25B3%25A8%25E6%2584%258F%25E4%25BA%258B%25E9%25A1%25B9>

- **功能描述**：撤回请求令牌（暂不支持JWT）。

- **请求 URL**：http://{{localhost}}/kapi/oauth2/withdrawToken
- **调用方式**：HTTP调用
- **请求方式**：POST
- **请求类型**：Content-Type:application/json
- **调用频率**：1分钟30次
- **token有效期**：2小时

**请求Body参数**

| **请求参数** | **必传** | **类型** | **说明** |
| --- | --- | --- | --- |
| client_id | 是 | String | 第三方应用系统编码，即appId |
| client_secret | 是 | String | 第三方应用AccessToken认证密钥，即appSecret |
| token_type_hint | 是 | String | 令牌类型，access_token/refresh_token |
| token | 是 | String | 令牌值 |
| accountId | 是 | String | 数据中心id |
| nonce | 是 | String | 随机数 |
| timestamp | 是 | String | 时间戳，当前时间前后5分钟 |

**请求参数示例**

```
{
    "client_id": "thirdappunittest_003",
    "client_secret": "Abcdrty@1234567890#@2",
    "token_type_hint": "access_token",
    "token":"OPENAPIAUTH_MTMzMTIwNDQ0NTk5NTc5NDQzMl9peGdobmxERWluY1FpZDc2R2pjUDcyYlg0UTNwNDhpczZXM01NYTlsTDVhNEU2TFRkT0ZIWTlybUl5SDdvQUJ1ZGFSaGtWU0hGNlNRRTBjMjZ6MkxxQWRjbkNpTzBnd1ZzMW9P",
    "nonce": "12345",
    "timestamp": "2023-09-15 16:29:00",
    "accountId": "1331204445995794432"
}
```

**返回参数**

| 返回参数 | 类型 | 说明 |
| --- | --- | --- |
| data |  |  |
| errorCode | String | 错误码，成功时为0 |
| message | String | 错误消息 |
| status | Boolean | 请求状态，true/false |

**返回参数示例**

```
{
    "data": true,
    "errorCode": "0",
    "message": "true",
    "status": true
}
```

**错误码说明**

| **错误码** | **说明** |
| --- | --- |
| 0 | 请求成功 |
| 401 | 不正确的第三方应用编码client_id或client_secret |
| 603 | 请求参数错误 |
| 611 | 撤回失败 |

**3 更多资讯**

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。

认证相关信息，请查看[金蝶AI苍穹OpenAPI开发认证指南](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=218694224487485696)
