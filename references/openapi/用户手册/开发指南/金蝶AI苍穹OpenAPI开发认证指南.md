---
title: "金蝶AI苍穹OpenAPI开发认证指南"
entityId: "218694224487485696"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/218694224487485696?productLineId=29&lang=zh-CN"
createdAt: "2021-08-26 11:32:46"
updatedAt: "2026-04-02 16:23:52"
views: 115610
---

# 金蝶AI苍穹OpenAPI开发认证指南

## 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V5.0.011 | 初始版本 | 2022年6月 |
| V6.0.1 | 开放平台更名为OpenAPI，迁移至开放服务云；第三方应用支持增强型Token认证，合并AccessToken认证和JWT认证策略 | 2023年10月 |
| V7.0.13 | 增强型Token认证、摘要认证、签名认证支持多时区，时间戳传入零时区 | 2025年6月 |
| V7.0.13 | 摘要认证POST请求优化Content-Type校验逻辑，不再强校验application/json格式，兼容application/json;Charset=utf-8等常见json格式标识 | 2025年6月 |

---

## 1. 简介

本文档适用于外部系统与金蝶AI苍穹间的系统集成场景。当外部系统调用金蝶AI苍穹OpenAPI时，金蝶AI苍穹会对每个API进行身份鉴权，判断其请求合法性，最后响应API请求。

**2 认证方式**

路径：【开放服务云】→【OpenAPI】→【第三方应用】，在第三方应用中为外部系统选择合适的认证方式。

![](https://vip-admin.kingdee.com/download/01096ecf298a08074fb6bd14d687cb418766.png)

金蝶AI苍穹OpenAPI共支持五种认证方式，分别是：

- AccessToken 认证
- JWT认证
- 摘要认证
- 基本认证
- 签名认证

其中，AccessToken认证应用最广泛，基本认证则最方便。从安全和易用性的角度进行分析，不同的认证方式各有特点，用户可以根据具体需求，选择合适的认证方式。

| 特点 | 强弱分析 |
| --- | --- |
| 安全性 | 签名认证 > 摘要认证 > JWT > AccessToken认证 > 基本认证 |
| 便捷性 | 基本认证 >JWT > AccessToken认证 > 摘要认证 > 签名认证 |

### 2.1 AccessToken认证/JWT认证

**功能描述**

Token（令牌）是第三方应用调用OpenAPI的身份凭证，每次请求时，客户端都需要通过请求头发送token，服务端以此来控制身份，当token过期后，服务端会销毁token，客户端需要重新请求才能获得token。

JWT(全称是JSON WEB TOKEN)是一种用于双方之间传递安全信息表述性声明规范，和access_token一样，都是访问资源的令牌。access_token需要查库验证access_token是否有效，而JWT不用查库，直接在服务端进行校验，用户可按需选择。

若access_token调用失败，但accesstoken调用成功，可能是Nginx版本较低的原因，需手动将Nginx中的underscores_in_headers 设为on，详见[access_token报错合集](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337785987048960&id=473850934762799616&productLineId=29&lang=zh-CN) 。

- **请求 URL**：http://{{localhost}}/kapi/oauth2/getToken
- **调用方式**：HTTP调用
- **请求方式**：POST
- **请求类型**：Content-Type:application/json
- **调用频率**：1分钟30次
- **token有效期**：2小时

![](https://vip.kingdee.com/download/01099c04c0d9854941e6a0a784ddf4cc3af5.png)

**注意事项：**

- 令牌的获取是有限制的，每个令牌的有效期为 2 小时，用户需要做好令牌的管理，在令牌快过期时，重新调用接口获取请求令牌或调用刷新令牌接口，延长请求令牌的有效期。
- 获取Token请求，同时支持在Header和Body中传输数据中心accountId。
- 获取access_token前需注册第三方应用，详见[第三方应用介绍](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337544983020032&id=225286231527892224&productLineId=29)、[金蝶AI苍穹OpenAPI增强型Token认证](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=218694224487485696&productLineId=29)。
- 若金蝶AI苍穹版本低于V6.0，获取token参考[API认证方式-AccessToken认证/JWT认证](https://vip.kingdee.com/article/491614364106171648)。

![](https://vip.kingdee.com/download/010955fc57d262724669b21fcf071e747bb2.png)

**请求Body参数**

| **请求参数** | **类型** | **必传** | **说明** |
| --- | --- | --- | --- |
| client_id | String | 是 | 第三方应用系统编码，即appId |
| client_secret | String | 是 | 第三方应用AccessToken认证密钥，即appSecret |
| username | String | 是 | 第三方应用代理用户的用户名 |
| accountId | String | 是 | 数据中心id |
| language | String | 否 | 语言字串： zh_CN，zh_TW、en_US等。 默认系统默认语言，查询接口会返回对应的多语言文本字段 |
| nonce | String | 是 | 随机数 |
| timestamp | String | 是 | 时间戳（兼容零时区格式，如：2025-06-12T00:00:10.009Z），当前时间前后5分钟 |

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
| - refresh_token | String | 刷新令牌，使用refresh_token 去刷新获得新的access_token，只能使用1次 |
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
    "id_token": "OPE1MGFXMWxJam9pTWpBeU15MHdPQzB5T1NBd01Eb3dNRG93TUM0d0lpd2labVZ1WVdKc1pTSTZJakVpTENKbWRXbGtJam9pTVRNME5qWTNNemtpTENKMWMyVnlWSGx3WlNJNklqRWlMQ0psZUhBaU9qRTJPVFEyTURReU1UZ3NJbWxoZENJNk1UFYTjBaV1FpT2lJeElpd2labkJ6ZDNOMGNtRjBaV2Q1YVdRaU9pSTNOakk1TnpjM09UVTNOekl3TURVek56WWlMQ0oxYzJWeWIzQmxibWxrSWpvaU5XRXlaR1ZtWTJKbE5HSXdPVFUzWm1Fd09HWTRZemN5SWl3aWRYTmxjbTVoYldVaU9pSkpSVkpRSW4wLi1ZZEd1cWhIX25Mcm5ibURnQTlfU2FvQkZsTGJWTTJEUmp2cnR4NXZwckk=",
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

通过getToken接口获取的JWT，也可用于调用OpenAPI服务，接口示例如下：

**请求头参数**

| **请求参数** | **类型** | **必传** | **说明** |
| --- | --- | --- | --- |
| client_id | String | 是 | 第三方应用系统编码，即appId |
| accountId | String | 是 | 数据中心id |
| JWT | String | 是 | Json Web Token，即通过getToken接口获取的id_token |

```
URL：http://{{localhost}}/kapi/v2/kdtest/basedata/bd_supplier/save

请求Header参数：
Content-Type=application/json
client_id={第三方应用编码}
accountId={数据中心Id}
JWT={上面获取的id_token}

请求Body参数：

{
    "data":[
        {
            "number":"Sup-001012",
            "name":"金蝶瑞杰汽车有限公司",
            "createorg_number":"00"
                }
           ]
}

请求结果：
{
    "data": {
        "failCount": "0",
        "result": [
            {
                "billIndex": 0,
                "billStatus": true,
                "errors": [],
                "id": "1698490236113273856",
                "keys": {
                    "number": "Sup-001012"
                },
                "number": "Sup-001012",
                "type": "Update"
            }
        ],
        "successCount": "1"
    },
    "errorCode": "0",
    "message": null,
    "status": true
}
```

### 2.2 摘要认证

摘要认证使用摘要代替token的传输，并采用MD5、SHA等不可逆哈希算法对参数摘要。首先，客户端通过指定的加密算法将随机数、时间戳等信息生成摘要。然后，调用请求时，将摘要放在请求头中发送给服务器；最后，服务器拿到摘要后，使用同样的算法和数据库密钥进行摘要并对比，匹配则身份验证通过。

![](https://vip.kingdee.com/download/0109e3c714eb5cde46949ab60e5fec6aaf0c.png)

**金蝶AI苍穹摘要认证流程：**

1. 生成第三方appId和第三方app的摘要认证加密秘钥；

2. API调用过程中加入验证信息。

摘要签名可以通过java工具类指定默认算法（如sha-256）直接生成签名。

- POST方式请求的API，验证内容都在请求体中；
- GET方式请求的API，验证内容都在url的参数中。

生成摘要后，后续只需要在请求的参数中带上签名信息就可以完成API调用。**摘要认证详细方法和demo见附件**。

**请求示例（GET）**

```
URL：http://{{localhost}}/kapi/v2/kdtest/basedata/bd_supplier/getNumber?name=Kingdeecar&pageSize=10&pageNo=1&appId=TEST&timestamp=2021-08-18 14:19:08&signatureNonce=iksiertoidkwek;oitdwudysletwsuej&signature=32beeebfc277817a80bb9371ff367f8b487a5&parameters=name,pageSize,pageNo&user=17299999999&usertype=Mobile&accountId=1173910536060928000

请求Header参数：
Content-Type=application/json

请求结果：
{
    "data": {
        "filter": "[name = 'kingdeecar']",
        "lastPage": true,
        "pageNo": 1,
        "pageSize": 10,
        "rows": [
            {
                "id": "968563370657601536",
                "number": "KDC"
            }
        ],
        "totalCount": 1
    },
    "errorCode": "0",
    "message": null,
    "status": true
}
```

**URL请求参数说明**

| **请求参数** | **类型** | **必传** | **字段说明** |
| --- | --- | --- | --- |
| name | string | 是 | 请求参数，供应商名称 |
| pageSize | int | 是 | 请求参数，分页数量 |
| PageNo | int | 是 | 请求参数，查询页码 |
| appId | string | 是 | 第三方appId |
| timestamp | string | 是 | 当前时间，和服务器时间相差10分钟就为无效请求，目前格式为yyyy-MM-dd HH:mm:ss |
| signatureNonce | string | 是 | 访问随机数，最好32位uuid，如果随机数已经访问过，则再次访问无效 |
| signature | string | 是 | 用SHA-256算法和摘要加密认证密钥key对query的拼接参数。公式：HMACSHA256（query的拼接参数+timestamp+signatureNonce，key） |
| parameters | string | 是 | 参与摘要的参数列表，多个参数用“,”隔开 |
| user | string | 是 | 金蝶云或云之家的用户名 |
| accountId | string | 是 | 数据中心id |
| usertype | string | 是 | 用户类型：Mobile： 标识为手机，默认为手机Email：标识为emailUserName：标识为用户名 |

**请求示例（POST）**

```
URL：http://{{localhost}}/kapi/v2/kdtest/basedata/bd_supplier/save

请求Header参数：
appId=test
signature=32beeebfc277817a80b01d5787242c51ca5295f5edcf2eb9371ff367f8b487a5
timestamp=2023-08-19 15:31:59
signatureNonce=iksiertoidkwek;oitdwudysletwsues
user=130****2580
usertype= Mobile
accountId=1173910536060920000

请求BODY参数：
{
    "data": {
        "number": "kingdeeCuS",
        "name": "供应商测试001",
        "alias_name": "供应商001"
    }
}

请求结果：
{
    "data": {
        "failCount": "0",
        "result": [
            {
                "billIndex": 0,
                "billStatus": true,
                "errors": [],
                "id": "1908634934143101952",
                "keys": {
                    "number": "kingdeeCuS"
                },
                "number": "kingdeeCuS",
                "type": "add"
            }
        ],
        "successCount": "1"
    },
    "errorCode": "0",
    "message": null,
    "status": true
}
```

**请求头参数说明**

| **参数名** | **类型** | **必传** | **字段说明** |
| --- | --- | --- | --- |
| appId | string | 是 | 第三方appId |
| timestamp | string | 是 | 当前时间，和服务器时间相差10分钟就为无效请求，格式为yyyy-mm-dd hh:mm:ss（兼容零时区格式，如：2025-06-12T00:00:10.009Z） |
| signatureNonce | string | 是 | 访问随机数，最好32位uuid，如果随机数已经访问过，则再次访问无效 |
| signature | string | 是 | 用SHA-256算法和对称加密key对body+timestamp+ signatureNonce进行摘要后的结果。公式：HMACSHA256（body+timestamp+signatureNonce，key） |
| user | string | 是 | 用户手机号 |
| usertype | string | 是 | 用户类型：Mobile： 标识为手机，默认为手机Email：标识为emailUserName：标识为用户名 |

如果报文内容为空，则在body中输入固定值，如：

| *{**"testName": "test"**}* |
| --- |

### 2.3 基本认证

苍穹OpenAPI基本认证，是结合了HTTPS Basic Authentication 的一种认证方式，通过基本认证调用接口时，需要在URL参数或请求头中携带openApiSign凭证，格式如下： {{localhost}}/{apiuri}?openApiSign=xxx，该凭证是由第三方应用、代理用户和当前数据中心ID组合加密生成的base64编码，可以作为访问OpenAPI 的固定认证密钥。作为接口匿名访问的一种更安全和方便的替代方案，基本认证可以广泛应用于接口回调的场景。

注意：

- 第三方应用启用基本认证后，由于基本认证密钥是长期有效的，必须配合API授权清单来保证系统整体安全。
- 另外如果是多数据中心环境，必须请求头或URL参数携带上accountId数据中心，否则会默认路由到MC里配置的默认数据中心。

![](https://vip.kingdee.com/download/010960695f5007ba4c6e92e68a6dee7f7d94.png)

**请求示例**

```
URL：http://{{localhost}}/kapi/v2/kdtest/gl/gl_voucher/gl_voucher?billno=cugyi5&pageSize=10&pageno=1&openApiSign=Slh4bFF3Mnh0LXZLUE9fRUtzRnItc2JTblgyM0RtNk9RN2V5ODR2WU13QT06MTMzMTIwNDQ0NTk5NTc5NDQzbg==&accountId=1393492185164283904

请求Header参数：
Content-Type=application/json

请求结果：

{
    "data": {
        "lastPage": true,
        "pageNo": 1,
        "pageSize": 10,
        "rows": [
            {
                "id": "1393492185164283904",
                "billno": "cugyi5",
                "entries": [
                    {
                        "id": "1393492186380632064",
                        "assgrp": {
                            "id": "1393492186061865984",
                            "供应商": {
                                "name": "唐山金属材料有限公司",
                                "number": "SUP000001",
                                "id": "346159251409862656"
                            },
                            "文本弹性域": "其他"
                        }
                    }
                ]
            }
        ],
        "totalCount": 1
    },
    "errorCode": "0",
    "message": "",
    "status": true
}
```

当苍穹与外围系统对接时，若存在某个接口回调场景，对方系统接口协议规定：访问路径需要为固定接口且不可以添加参数，或在接口访问路径中不允许有“?”，苍穹开放平台回调接口可使用如下格式：http://{{localhost}}/$/openApiSign/xxx/billno/cugyi5/pageSize/10/pageno/1。

注意：URL中openApiSign必须在特殊符号“$”后，在其他URL参数前。

### 2.4 签名认证

苍穹OpenAPI签名认证采用双向签名和加解密的模式，解决第三方系统和金蝶AI苍穹安全高效的数据交互问题，不仅有效防止数据被篡改，还保障了数据完整性和隐私安全性，支持金融交易，HR集成等高安全性应用场景。

**1）金蝶AI苍穹签名加密过程：**

1. 第三方系统产生随机会话密钥randomKey, 通过randomKey和加密策略将请求body参数加密，放在字段encryptData中，同时将会话密钥randomKey通过平台公钥RSA加密，放入字段dgtlEnvlp中；
2. 第三方系统通过SHA256将随机数，时间戳及请求body报文加签后发送给金蝶AI苍穹OpenAPI；
3. 金蝶AI苍穹OpenAPI通过openApiSign(SecretKey)验证后，获取代理用户，第三方应用ID及数据中心，再验证签名，此时会检查随机数、时间戳以及请求参数的合法性和有效性；
4. 签名验证通过后，解密并还原数据，进行下一步业务处理，如查询或保存数据；
5. 金蝶AI苍穹OpenAPI产生随机数，加密返回结果数据；
6. 金蝶AI苍穹OpenAPI对返回结果数据进行SHA256签名；
7. 第三方系统接收到返回结果进行验证签名；
8. 第三方系统解密返回的结果，进行相关业务处理。

**2）操作指引**

路径：【开放服务云】 → 【OpenAPI】 → 【安全策略】 → 【第三方应用】。在第三方应用中添加签名认证策略，维护认证密钥（key）和代理用户，同时获取Secret key。另外还需要添加加密策略，并配置需要加密的API，下载平台公钥证书。

![](https://vip.kingdee.com/download/010981f84dea8e544abf9a5189933ffe08b2.png)

![](https://vip.kingdee.com/download/01099889860347cd4a4b90cb40d98a0c7ac8.png)

注意：接口只支持POST请求

**3）请求示例**

```
URL: http://{{localhost}}/kapi/v2/kdtest/open/openapi_unittest/findOrders

请求方式：POST

请求Header参数：
Content-Type=application/json
OpenApiAuth=5
openApiSign=UlZqZWxjZWZJRk5BbjZnMGF1jYWZZeFNPOUxwND06MTMzMTIwNDQ0NTk5NTc5NDQzMg==

请求Body参数：

{
    "dgtlEnvlp": "6F56001A8479097414D4F3137C25D0A72EA7D3D9D089AF0498CC1CF9CD90C8D583C0135049B64764AEE26C30DA1C1295F5F21C80F3DC901293A8C64624B66399B95255E8932C3D8F9E65F1FE6AD091948DB8BED453E80B8A4CF2E32E0227E9AEC96B3BE5B57C457589B7578EBADC6EBB4F5ABDD98B6614E3C741AA691FF0259D",
    "encryptData": "AAAADKPWJMKRjHiwR67fLSUUfkwcZo0XJQeSEGExBDp1jDCqGl+FB8GNLUQXzLsIdP6kbkyCNTPpYLdu4x5f7EJgPbzJ7fLWN+Cs44OJMKeHapFOgKM=",
    "signature": "712f5d468ecb13c8b8fc24118d23bc541a93d2f3d6b5f998af8952bbc862387c",
    "signatureNonce": "0f8cf008-9095-4ce7-9600-e28e564aaae7",
    "timestamp": "2022-10-19 15:26:33"
}

请求结果：

{
    "accountId": "1355633519610561536",
    "authType": "5",
    "data": {
        "data": null,
        "errorCode": "0",
        "message": null,
        "status": true
    },
    "dgtlEnvlp": "0EEFE62AA75CF03638568D30AC5CC165637529632E0E2A9CB1C77E28645D8DD7555DBB52EA78758798A366D375E1E46D314C5B7D41F461757793FCECEE948D41428F69D1A304110FE469DCA6BA032DA599F244F11408915BB76EE7275CE3595578E1FA6E4CF0A96FE3B6642631D2B0DCD5090F9C762D16032138AD4C198271AF",
    "encryptData": "AAAADIULnyBUVP/qDzgdateRk6LdD7puKpNdXSNYEHtnsYxZUwucf5Jc8MrbEMDvqV8dIr/uKH3jTvsfQXMZuzI88JaX+s9KfxMYgL5382dDPigkaASyCbtRJkm4LTyIkd96JmJAzeZQYOSsk9OFfJFfpT0rFbpNRHcs5t5sPfB7iI91UtjRCg==",
    "signature": "1af6b267b0c74801996cb7a6b621eb44a6a95fc496128373ed3f8bfd5d2dca00",
    "signatureNonce": "5bfb355d-6966-4289-935a-17d64fa86994",
    "thirdId": "1520516744903424000",
    "timestamp": "2022-10-19 15:26:34",
    "url": "/kapi/v2/kdtest/open/openapi_unittest/findOrders"
}
```

**请求Header参数**

| **参数名** | **类型** | **必传** | **字段说明** |
| --- | --- | --- | --- |
| Content-Type | string | 是 | application/json |
| OpenApiAuth | string | 是 | 认证类型，1：AccessToken认证，2：摘要认证，3：JWT认证，4：基本认证，5：签名认证 |
| openApiSign | string | 是 | 签名认证策略卡片中的SecretKey |

**请求Body参数**

| **参数名** | **类型** | **必传** | **字段说明** |
| --- | --- | --- | --- |
| dgtlEnvlp | string | 是 | 随机会话密钥，通过平台公钥加密后的字符串 |
| encryptData | string | 是 | 采用加密策略加密后的请求参数 |
| signatureNonce | string | 是 | 访问随机数，建议使用32位uuid |
| timestamp | string | 是 | 当前时间，和服务器时间相差10分钟就为无效请求，目前格式为yyyy-MM-dd HH:mm:ss（兼容零时区格式，如：2025-06-12T00:00:10.009Z） |
| signature | string | 是 | 用SHA-256算法和认证密钥（key）对请求body参数、timestamp、signatureNonce进行摘要后的结果。公式：HMACSHA256（body参数+timestamp+signatureNonce，key） |

**返回参数**

| **参数名** | **类型** | **字段说明** |
| --- | --- | --- |
| accountId | string | 数据中心ID |
| thirdId | string | 第三方应用ID |
| dgtlEnvlp | string | 随机会话密钥，通过平台私钥加密后的字符串 |
| encryptData | string | 采用加密策略加密后的返回参数 |
| signatureNonce | string | 访问随机数，建议使用32位uuid |
| timestamp | string | 当前时间，和服务器时间相差10分钟就为无效请求，目前格式为yyyy-MM-dd HH:mm:ss，以后为时间戳 |
| signature | string | 用SHA-256算法和认证密钥key对body参数和timestamp， signatureNonce进行摘要后的结果。公式：HMACSHA256（body参数+timestamp+signatureNonce，key） |
| url | string | 请求地址 |

## 3 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
