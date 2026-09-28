---
title: "API日志介绍"
entityId: "263990262375226880"
category: "用户手册"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/263990262375226880?productLineId=29&lang=zh-CN"
createdAt: "2021-12-29 11:23:03"
updatedAt: "2025-12-19 10:06:17"
views: 14942
---

# API日志介绍

## 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V5.0.001 | 初始版本 | 2022年6月 |
| V6.0.3 | 权限增强控制， 仅管理员有权限在公共设置中维护OpenAPI参数 | 2023年11月 |
| V6.0.4 | API日志记录API名称字段，同时支持自定义日志关键字段（出入参摘要） | 2023年12月 |
| V6.0.5 | 应用场景增加API日志归档 | 2024年1月 |
| V7.0.13 | 私有云租户支持记录完整OpenAPI大文本日志 | 2025年6月 |

---

## 1 简介

### 1.1 功能介绍

- API日志用于记录OpenAPI调用过程中的请求参数、执行过程、响应结果、错误码等信息，便于开发与运维人员查询实时日志，对接口调用进行故障定位和日志审计等操作。用户可以根据实际使用情况，配置API日志记录的详细程度，详见[参数配置](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337544983020032&id=264031111959674368&productLineId=29&lang=zh-CN)。
- 支持单独记录请求出入参中的关键业务字段，方便快速定位API日志。同时还支持ES存储，提升查询效率。

注意：API调用日志仅记录OpenAPI日志，即URL中含kapi标识的接口，不会记录登录接口如api/login.do等的调用日志。

### 1.2 应用场景

- **API日志监控**：当系统参数中“API调用日志”的值为记录详细日志或记录摘要日志时，用户可以在该界面查看具体的调用日志。
- **API日志清理：**若日志量较大，建议定期清理日志。清理指南见附件金蝶AI苍穹V5.0_开放平台-日志清理配置指南-20231130.pdf。
- **API日志归档**：若日志需要定期归档备份留作审计，建议使用苍穹平台数据归档功能，可归档单据分别为 API调用日志（openapi_log_data）和 API调用详细日志（openapi_log_detail），归档指南详见[大表冷热数据分离之数据归档](https://vip.kingdee.com/article/344790275899953920?productLineId=29&isKnowledge=2&lang=zh-CN)。

### 1.3 系统路径

【开放服务云】→【OpenAPI】→【监控统计】→【API日志】

### 1.4 字段说明

| **字段名称** | **详细解释** |
| --- | --- |
| URL | API的url地址 |
| 请求参数 | API请求参数 |
| 响应结果 | API响应结果 |
| 错误信息 | 当请求出现异常返回时，显示的错误信息 |
| ApiId | API的主键ID |
| API编码 | API编码 |
| API名称 | API名称 |
| 调用状态 | API调用状态 |
| 调用时间 | 调用API的时间 |
| 第三方应用 | 调用API的第三方应用 |
| 调用者 | 调用API的用户名称 |
| 调用者ID | 调用API的用户ID |
| 调用客户端IP | 调用API的客户端IP |
| 云 | API所属云 |
| 应用 | API所属应用 |
| 业务对象 | API具体操作的业务对象 |
| API耗时（ms） | API调用耗时 |
| 操作服务耗时(ms) | 操作服务耗时 |
| TraceId | 接口调用的TraceId，日志记录的主键 |
| 入参摘要 | 记录API配置中的请求参数关键字段值 |
| 出参摘要 | 记录API配置中的响应内容关键字段值 |

### 1.5 按钮说明

| **按钮名称** | **详细解释** |
| --- | --- |
| 退出 | 点击退出按钮，退出API日志详情界面 |
| 导出详细日志 | 导出大文本日志 |

## 2 主要操作

### 2.1 自定义API日志级别

管理员可以通过OpenAPI系统参数，来定义记录不同级别的API日志和日志保留天数。

**1）配置API日志级别**

路径：基础服务云 → 公共设置 → 参数配置 → 系统参数，在OpenAPI参数中，可以配置不同的API日志级别，包含基本日志、详细日志和大文本日志等。用户按需勾选需要的日志级别，并维护日志保存天数。

备注：大文本日志默认截取请求参数和返回参数前10000字符，私有云租户可通过MC参数“api_fullPayloadLog”（默认false），将该参数设为true后，即可完整记录日志请求和返回参数。

特别声明：若MC配置了记录全部入参数据参数，可能会导致系统API调用缓慢，并且日志量暴增，极端场景下会有OOM的风险，用户需严格控制相关接口的并发调用。

![](https://vip.kingdee.com/download/01090f4cc64d03354a41a41025a0989aa2d3.png)

**2）查看API调用日志**

路径：开放服务云 → OpenAPI → 监控统计 → API日志，打开API调用日志列表界面，在这里可以看到API日志调用记录，包含API编码、名称、请求参数、错误消息、调用状态、调用时间、traceid等信息。

备注：日志默认保留30天，到期自动清理。

![](https://vip.kingdee.com/download/010930343e8cae374d9d8160e8173148450f.jpg)

![](https://vip.kingdee.com/download/0109ff17daf4cf3340d396ff1290a33cb174.jpg)

**3）查看API大文本日志**

若在OpenAPI参数中，配置了记录“大文本日志”，在调用接口（特别是批量保存或列表查询API）后，用户可以在API日志中点击“导出详细日志”，系统会生成一个txt文件，展示完整的请求参数和响应结果。

![](https://vip.kingdee.com/download/010937efd62460994ac9b2b2eb7680df1d73.jpg)

### 2.2 自定义日志关键字段

用户可以通过简单配置，即可在API日志中单独记录请求出入参中的的关键字段，如单据编码、创建组织等，从而过滤对应的日志记录，快速定位问题或审计日志。

**1）配置日志记录模板**

路径：开放服务云 → OpenAPI → API管理 → API开发，通过零代码配置快速开发一个API，在配置项中维护入参日志记录模板和出参日志记录模板。

![](https://vip.kingdee.com/download/01098c9413851f794be68d721ad033ff78d9.jpg)

紧接着，通过脚本维护关键字段，例如将采购订单编码和分录中物料编码作为入参关键字段，单据id作为出参关键字段。

注意：若接口为操作API同时请求方式为POST，由于请求参数和返回参数默认返回参数“data”，所以在维护脚本时，需要增加一层data参数，例如#{$data.data.billno}。

![](https://vip.kingdee.com/download/0109b336c452add34b42b20c109ddf4312a6.jpg)

![](https://vip.kingdee.com/download/01096e0699615e4647df9e842f45674598eb.jpg)

**2）调用接口生成日志**

在维护完API基本信息、日志记录模板和请求参数后，点击“保存”按钮，接下来就可以调试API了。

![](https://vip.kingdee.com/download/0109cb589676829b427799efac7b31884068.jpg)

点击“API测试”按钮，发送请求，生成调用记录。

![](https://vip.kingdee.com/download/01094241805f580e47749ac62c86ff5b3a22.jpg)

**3）查看API调用日志**

路径：开放服务云 → OpenAPI → 监控统计 → API日志，此时可以看到API日志的入参摘要和出参摘要中，记录了上一步配置的关键字段，若存在多条数据通过逗号分隔。

![](https://vip.kingdee.com/download/0109ba6e64e7972f40ebaf337578e2b7bbaf.jpg)

## 3 注意事项

- 若苍穹版本高于V6.0.3，只能由管理员维护API调用日志记录级别。
- 维护API日志记录模板时，需要注意请求参数和响应参数的层级，否则可能无法记录到正确的数据。

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
