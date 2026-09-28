---
title: "金蝶AI苍穹OpenAPI接口规范"
entityId: "448792125560557568"
category: "接口规范"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/448792125560557568?productLineId=29&lang=zh-CN"
createdAt: "2023-05-23 10:19:41"
updatedAt: "2025-08-26 10:59:36"
views: 19356
---

# 金蝶AI苍穹OpenAPI接口规范

## 1. 接口规范

传输协议支持 HTTPS /HTTP 协议，主要采用 JSON 格式作为传输规范，报文格式由具体服务接口定义。

苍穹平台OpenAPI接口规范.pdf

### 1.1 协议标准

1）数据传输支持 HTTPS/HTTP 协议标准。

2）基于 GET、POST标准通过OpenAPI进行数据请求交互，支持JSON、XML、文件流等报文格式。

3）主要采用Token认证方式进行权限校验，同时也支持其他认证方式，如摘要认证、基本认证等。

### 1.2 报文限制

- OpenAPI报文出入参报文最大限制为20M ，同时文件流限制为50M。 - 适用于苍穹V6.0.14以上。

备注：苍穹V7.0版本统一调整为30M。

- 私有云租户可通过MC参数调整报文限制（公有云不支持调整）：OpenApi.MaxBodySize       修改默认最大请求报文大小（单位：字节），若调整为40M，则参数value为 41943040OpenApi.MaxOutBodySize  修改默认最大返回报文大小（单位：字节）- 苍穹V7.0版本以上OpenApi.FileItem.MaxSize  修改默认文件流最大报文大小（单位：字节）

特别注意：私有云用户遇到报文超过限制问题，建议优先通过**分批处理**的方式解决；若需调整 MC 参数，务必严格控制调整幅度，避免设置过高，否则在高并发场景下，可能引发内存占用异常飙升，进而导致进程内存溢出（OOM）故障，影响系统稳定性。

### 1.3 公共请求参数

公共参数是每个接口都要携带的参数，描述每个接口的基本信息，用于统计或其他用途，放在header或url参数中。

**Query参数** url?后面的参数，存放请求接口的参数数据。

**请求Header** 请求头，存放以下公共参数、APP端公共参数等，也可以存放一些特殊加密字段。

**请求Body** Body体，存放请求接口的参数数据。

**请求头**

| 参数名称 | 参数类型 | 必填 | 描述 | 详细说明 |
| --- | --- | --- | --- | --- |
| Content-Type | string | 是 | 内容格式 | 请求报文的入参格式，如application/json、application/xml 等 |
| accesstoken | string | 是 | 请求令牌 | 获取的accesstoken值，用于接口访问鉴权 |
| Idempotency-Key | long | 否 | 非必传参数，防止接口被重复调用 | 唯一的requestId，有效时间30分钟。当调用接口时，系统识别到重复的 Idempotency-Key，会拒绝请求 |

**分页查询请求参数**

| 参数名称 | 参数类型 | 必填 | 描述 | 详细说明 |
| --- | --- | --- | --- | --- |
| pageNo | Integer | 否 | 分页参数，查询页码 | 查询接口分页时填写，如查第1页，则传入1 |
| pageSize | Integer | 是 | 分页参数，分页数量 | 查询接口分页时填写，如每页返回10条数据，则传入10 |

### 1.4 公共返回参数

为了方便给客户端响应，响应数据会包含四个属性，结果数据（data）、错误码（errorCode）、信息描述（message）和状态（Status）。客户端根据status和信息描述可快速知道接口是否调用成功以及具体的错误信息。

**通用返回数据结构**

| 参数名称 | 参数类型 | 描述 | 详细说明 |
| --- | --- | --- | --- |
| data | Object | 结果数据 | {} |
| errorCode | String | 错误码 | 成功时为0，失败时会返回错误码如400 |
| message | String | 接口调用错误信息 | 成功时为空，失败时会返回错误信息如“操作失败” |
| status | Boolean | 接口访问是否成功 | true/false |

**分页对象**

| 参数名称 | 参数类型 | 描述 | 详细说明 |
| --- | --- | --- | --- |
| rows | List | 结果数据列表 | [] |
| pageNo | Integer | 分页参数，查询页码 | 若为1，则查询的是第1页 |
| pageSize | Integer | 分页参数，分页数量 | 若为10，则每页返回10条数据 |
| filter | string | 过滤条件 | 查询接口的过滤条件，既执行逻辑 |
| lastPage | Boolean | 是否最后一页 | true/false |
| totalCount | Integer | 总记录数 | 接口查询总条数 |

**错误码说明**

| 错误码 | 描述 | 详细说明 |
| --- | --- | --- |
| 0 | OK | 请求成功 |
| 999 | 未知错误 | 发生业务异常但未指定错误码 |
| 400 | 参数无效 | 客户端请求中的参数无效或语法错误 |
| 401 | 未授权访问（Token无效） | 身份验证失败、token错误或已失效 |
| 403 | 禁止访问（IP限制或该API没有授权） | 无法访问未授权的服务，请联系管理员授权 |
| 404 | API不存在 | 请求路径有误或地址无法找到任何资源 |
| 405 | Http方法不允许 | 请求方法(GET, POST)对某些特定的资源不适用，请确认接口的请求方法是否有误 |
| 406 | API无法解晰或处理数据 | 客户端无法解析服务端返回的内容 |
| 415 | 不能支持的MediaType | 服务器无法处理请求附带的媒体格式, 解决方法就是在请求头中加入Content-Type指定内容格式 |
| 429 | API被限流 | 请求频率超过了所请求的服务设置频率 控制条件，请降频请求或联系管理员提高请求频率 |
| 500 | 服务异常，服务内部错误 | 未知异常，需联系系统管理员排查确认 |
| 601 | 数据重复 | 请求数据重复，可能由于网络波动或高并发生成重复数据 |
| 602 | 找不到数据 | 数据不存在，比如更新数据时找不到相应的分录 |
| 603 | 数据无效 | 必填字段数据为空/数据校验无效/请求数据量超出最大限制 |
| 604 | 不允许重复执行 | 幂等性控制时不允许重复请求，防止数据重复 |
| 611 | 更新数据失败 | 数据更新失败（逻辑校验没通过或数据不合法） |
| 612 | 没有数据操作权限 | 没有相应的数据获取权限 |
| 701 | 脚本执行错误 | 接口脚本执行时发生错误，请联系管理员检查脚本 |
| 702 | 插件执行时发生异常 | 执行Java插件时发生错误 |

### 1.5 调用示例

调用接口分为以下几步:

1）带上参数请求具体的接口地址，开放平台注册的接口地址为URI，拼接域名/kapi 组成完整请求地址；

2）在请求头加入认证信息如accesstoken；

3）如http状态码为 200 且返回参数中errorCode 为 0，表示请求成功，可读取公共返回结果数据。

**POSTMAN****调用示例**

**![](https://vip.kingdee.com/download/0109ee95559c2dc84a02988a8525c683d480.png)**

**分页查询**

公共返回参数说明详见分页查询

详细返回示例

| *{**"data": {**"filter": "[biztime >= '2023-04-24 00:00:00' AND biztime < '2023-05-23 00:00:00']",**"lastPage": true,**"pageNo": 1,**"pageSize": 10,**"rows": [**{**"billno": "2023041801",**"billentry": [**{**"qty": 2.0000000000,**"material_masterid_name": "采购单测（一次性）",**"material_masterid_number": "unitMatpm-002"**},**{**"qty": 3.0000000000,**"material_masterid_name": "采购单测（一次性）",**"material_masterid_number": "unitMatpm-002"**}**],**"biztime": "2023-04-26 00:00:00",**"org_name": "环宇国际集团有限公司",**"org_number": "00"**},**{**"billno": "2023041802",**"billentry": [**{**"qty": 3.0000000000,**"material_masterid_name": "采购单测（一次性）",**"material_masterid_number": "unitMatpm-002"**},**{**"qty": 3.0000000000,**"material_masterid_name": "采购单测（一次性）",**"material_masterid_number": "unitMatpm-002"**}**],**"biztime": "2023-04-26 00:00:00",**"org_name": "环宇国际集团有限公司",**"org_number": "00"**},**{**"billno": "20230508001",**"billentry": [**{**"qty": 10.0000000000,**"material_masterid_name": "采购单测（一次性）",**"material_masterid_number": "unitMatpm-002"**}**],**"biztime": "2023-05-08 00:00:00",**"org_name": "环宇国际集团有限公司",**"org_number": "00"**}**],**"totalCount": 3**},**"errorCode": "0",**"message": null,**"status": true**}* |
| --- |

## 2. 更多资讯

[金蝶AI苍穹开放平台OpenAPI调用流程](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=213309216805890816&productLineId=29)

[金蝶AI苍穹开放平台OpenAPI开发认证指南](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=218694224487485696&productLineId=29)
