---
title: "OpenAPI新特性汇总"
entityId: "226708319996323072"
category: "动态与公告 / 新特性公告"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/226708319996323072?productLineId=29&lang=zh-CN"
createdAt: "2021-09-17 14:17:56"
updatedAt: "2026-07-02 14:22:07"
views: 14505
---

# OpenAPI新特性汇总

**本文章用于OpenAPI（开放平台）的新特性发布通知，请大家定期关注**

**苍穹补丁下载路径：**[https://download.kdcloud.com/](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fdownload.kdcloud.com%2F)

## 2026-06-23 BOS_V8.0.11

1. 【性能优化】优化了批量保存接口单头单候选键场景下的查询逻辑，支持按批量**IN**方式查询候选键，提升数据保存性能
2. 【新功能】支持了 OpenAPI 配置“按任一应用鉴权”能力，查询API通过参数**currbizappid** 可按指定应用校验单据查询权限
3. 【功能优化】优化了 OpenAPI API 数据及第三方应用接入软删除机制，删除后接口不可调用，并支持回收站恢复

## 2026-04-28 BOS_V8.0.9

1. 【功能优化】优化了提交、审核等状态变更类 Restful API 在无编码字段业务对象场景下的返回逻辑，支持接口正常执行并返回结果
2. 【功能优化】优化了 1.0 API 防重复请求功能与 API 日志的兼容性，支持正常记录请求体

## 2026-03-08 BOS_V8.0.8

1. 【新功能】支持了Restful API列表查询操作在请求参数传入 * 或设为默认值时，忽略对应过滤条件
2. 【新功能】新增了防重复调用处理 application/x-www-form-urlencoded 格式的请求
3. 【新功能】新增了自定义API中相同Model的属性可配置不同名称和示例值的能力

## 2025-12-22 BOS_V8.0.4

1. 【新功能】新增查询操作API支持安全权限校验能力[https://developer.kingdee.com/knowledge/788778229871437568](https://developer.kingdee.com/knowledge/788778229871437568?productLineId=29&isKnowledge=2&lang=zh-CN)
2. 【新功能】新增RESTful API通过操作参数 strictvalidation 控制返回结果部分成功部分失败或一条失败整批失败
3. 【新功能】新增v2保存操作API解析报文时，通过手工添加操作参数 isInOrderFieldOfReq 为 true 保证原报文字段顺序,避免触发值更新时有顺序问题

## 2025-11-25 BOS_V8.0.2

1. 【新功能】新增查询操作API读写分离能力[https://developer.kingdee.com/knowledge/815251507280459008](https://developer.kingdee.com/knowledge/815251507280459008?productLineId=29&isKnowledge=2&lang=zh-CN)

## 2025-10-28 BOS_V8.0.1

1. 【新功能】新增RESTful API开发引擎，支持GET、POST、PUT、DELETE等请求方式，确保设计的API符合RESTful设计规范，降低海外客户接入门槛，为企业产品出海提供支持。[https://developer.kingdee.com/knowledge/742777899320623104](https://developer.kingdee.com/knowledge/742777899320623104)
2. 【新功能】新增RESTful API文档功能，支持查看Swagger 格式的标准化接口说明文档，支持展示接口信息、在线测试等功能。[https://developer.kingdee.com/knowledge/755465871337911040](https://developer.kingdee.com/knowledge/755465871337911040)
3. 【新功能】新增RESTful API日志功能，支持记录RESTful API 的调用日志信息，方便开发与运维人员查询实时日志，对接口调用进行故障定位和日志审计等操作。[https://developer.kingdee.com/knowledge/755467282905756672](https://developer.kingdee.com/knowledge/755467282905756672)
4. 【新功能】新增RESTful API 监控看板，支持实时查看调用量、失败数、成功率、平均响应时间等核心指标，帮助用户快速发现异常与性能问题。[https://developer.kingdee.com/knowledge/755468720763499520](https://developer.kingdee.com/knowledge/755468720763499520)
5. 【新功能】新增 RESTful API 升级工具，可帮助用户快速将系统内存量 V2 版本接口升级至 RESTful API 标准，解决手动改造中效率低下、规范不统一、参数迁移易出错等痛点，加速完成接口标准化改造。
6. 【新功能】新增MCP服务功能，支持将 RESFful API 一键打包为 MCP 服务，可通过苍穹 Agent 或外部 Agent 调用，提升流程自动化效率和业务创新能力。
7. 【功能优化】优化 API 日志记录功能，支持“全局 + API 级别” 双重配置维度。用户可根据实际需求灵活选择日志记录范围，提升日志记录的灵活性。
8. 【功能优化】下架第三方应用的 “授权全部 API” 功能，改为强制要求用户维护精细化的 API 授权清单。从源头规避潜在越权风险，进一步提升系统安全防护等级。

1. 【功能优化】优化了接口保存数据时的值更新触发机制，支持通过维护操作参数firePropChangedOnAdd，在新增数据时触发值更新事件并填充数据。

## 2025-07-23 BOS_V7.0.15

1. 【功能优化】优化OpenAPI日志清理调度机制，采用 “分批查询 + 批量删除” 策略提升执行效率与系统稳定性。
2. 【功能优化】优化了自定义 API 权限管控机制，新创建的接口不再支持【匿名访问】，建议统一通过[基本认证](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=218694224487485696&type=Knowledge&productLineId=29&lang=zh-CN)实现接口回调；当关闭 “第三方应用授权” 开关后，强制关联业务对象及权限项，第三方系统调用接口时，系统会自动校验上下文用户是否拥有该权限项，防范潜在的越权访问风险。

## 2025-06-12 BOS_V7.0.13

1. 【功能优化】优化了API调用日志记录机制，大文本日志统一截取请求参数和返回参数的前10000字符，私有云租户可通过MC参数配置：api_fullPayloadLog，值设为true后，可记录完整大文本日志，以满足特定场景下的详细日志需求。

[https://developer.kingdee.com/knowledge/263990262375226880](https://developer.kingdee.com/knowledge/263990262375226880)

2. 【功能优化】优化了增强型认证接口和摘要认证的多时区支持，请求参数中时间戳字段支持零时区格式，如2025-06-12T00:00:10.009Z，服务端能够准确识别并校验调用方传入的时间戳准确性，提升接口可用性和易用性。

[https://developer.kingdee.com/knowledge/218694224487485696](https://developer.kingdee.com/knowledge/218694224487485696)

## 2025-02-25 BOS_V7.0.6

1. 【功能优化】增强保存操作API 的灵活性，通过操作参数自由组合保存、提交、审核 等操作，提升集成效率与开发体验。

[https://developer.kingdee.com/knowledge/264036069979704064](https://developer.kingdee.com/knowledge/264036069979704064)

2. 【新功能】：增加了dts文件转换工具，支持忽略接口中的多语言信息，实现高版本API向低版本环境的快速迁移。

[https://developer.kingdee.com/knowledge/679319664643729152](https://developer.kingdee.com/knowledge/679319664643729152)

3. 【功能优化】优化了自定义API对文件类型的处理能力，支持通过单个参数接收多个文件，提升集成效率。

[https://developer.kingdee.com/knowledge/644193911996299264](https://developer.kingdee.com/knowledge/644193911996299264)

4. 【功能优化】优化了操作API在XML及SOAP报文格式下的多值处理能力，支持调用方一次性传入多值或多条分录，提升数据交互效率。

5. 【功能优化】优化了API批量导出功能，导出API时不再限制100条数据上限，后台自动分批处理，提升备份效率。

## 2024-10-17 BOS_V7.0.1

1. 【新功能】：OpenAPI新增异步API功能，接口调用方无需等待API执行结果，可继续执行其他任务，适用于大数据同步或高并发场景。

[https://vip.kingdee.com/article/614851837958827520](https://vip.kingdee.com/article/614851837958827520)

2. 【新功能】：OpenAPI新增开放事件功能，通过事件消息，实时向外传输苍穹平台业务数据变更情况，实现高效的事件驱动集成。

[https://vip.kingdee.com/article/535180376516381952](https://vip.kingdee.com/article/535180376516381952)

3. 【功能优化】：OpenAPI新增Mock业务数据功能，支持将业务数据快速填充到请求参数示例，准确生成API测试报文和文档，提升调试和对接效率。

[https://vip.kingdee.com/article/626005169960140544](https://vip.kingdee.com/article/626005169960140544)

4. 【功能优化】：自定义Servlet API支持流式模式。

[https://vip.kingdee.com/article/407938727957357824](https://vip.kingdee.com/article/407938727957357824)

5. 【功能优化】：OpenAPI支持跨境数据脱敏，用户可以对敏感返回参数，维护数据标签，平台自动脱敏。

6. 【功能优化】：本地缓存LocalCacheUtil从Idle策略改为TTL策略，即10~20分钟强制过期，避免因MQ组件异常，导致本地缓存清除失败。

7. 【功能优化】：操作API支持用户自定义请求参数默认值，如Content-Type、accesstoken等。

8. 【功能优化】：支持用户自定义导出API的信息（dts文件），通过公共配置OpenAPI系统级参数，可定义需忽略导出的字段。

9. 【功能优化】：OpenAPI配置信息多语言适配，即API名称、参数名称、说明、示例等字段，支持维护多语言信息。

10. 【问题修复】：修复了当单据保存操作维护了服务端服务如自动下推等，保存操作API接口无法触发服务导致报错的问题。

## 2024-06-13 BOS_V6.0.13

1. 【功能优化】：OpenAPI请求报文出入参最大长度限制20M(文件流50M)，防止因报文过长而导致请求超时。

## 2024-05-30 BOS_V6.0.12

1. 【功能优化】：保存操作API支持用户定义请求参数默认值。

2. 【功能优化】：OpenAPI防重复请求优化，增加数据库防重控制机制。

3. 【问题修复】：解决统计看板中折线图，在切换数据中心时的数据残留问题。

## 2024-05-16 BOS_V6.0.11

1. 【新功能】：OpenAPI新增摘要认证调试界面，方便用户使用摘要认证时生成和校验签名。

## 2024-04-25 BOS_V6.0.10

1. 【功能优化】：OpenAPI详情界面和API文档展示完整URL地址（智能拼接），提升用户体验 2. 功能优化：优化API文档导出功能，支持批量导出到1个PDF文件。

2. 【功能优化】：优化API文档导出功能，支持将多个API文档合并导出到1个PDF文件中。

## 2024-03-28 BOS_V6.0.8

1. 【新功能】：新增慢接口统计功能，默认统计前一天响应时间超过10s的慢接口记录，帮助用户实时监控整体接口性能。

[https://vip.kingdee.com/article/561129544887976960](https://vip.kingdee.com/article/561129544887976960)

2. 【新功能】：新增预警配置功能，支持配置消息渠道和消息模板，当出现慢接口等异常情况时，及时进行消息预警。

[https://vip.kingdee.com/article/561135209848877312](https://vip.kingdee.com/article/561135209848877312)

3. 【新功能】：新增预警日志功能，记录API消息预警日志，帮助用户查看预警消息的推送情况。

[https://vip.kingdee.com/article/561139114830087168](https://vip.kingdee.com/article/561139114830087168)

4. 【新功能】：API列表左树新增自定义分组模式，支持按不同的分组维度，个性化管理不同云、应用下的API。

[https://vip.kingdee.com/article/558285650663628544](https://vip.kingdee.com/article/558285650663628544)

5. 【功能优化】：保存操作API支持自动提交并审核。

[https://vip.kingdee.com/article/563359453035097856](https://vip.kingdee.com/article/563359453035097856)

6.【功能优化】：API请求头示例参数允许用户自定义，并自动同步到API文档。

7.【功能优化】：扩展插件功能优化，序列化插件提供新的方法获取全部参数。

[https://vip.kingdee.com/article/512929770493846784](https://vip.kingdee.com/article/512929770493846784)

8.【功能优化】：扩展插件功能优化，查询操作API插件新增自定义排序功能。

[https://vip.kingdee.com/article/512935531689404928](https://vip.kingdee.com/article/512935531689404928)

9. 【功能优化】：增强API日志打印安全性，默认脱敏access_token、jwt、openApiSign等令牌字段。

10. 【功能优化】：API日志优化，记录接口限流时的monitor日志，方便用户定位问题。

11. 【功能优化】：API 防重复请求功能优化，通过接口保存数据时锁定业务对象，避免高并发场景下接口重复保存数据。

12.【功能优化】：请求参数协议支持优化，增加报文格式text/xml的内容检测，并进行正确的报文处理。

13.【功能优化】：当使用基本认证时，请求URL中的openApiSign值支持使用转义符，如=转%3D。

14.【问题修复】：修复了特殊场景下，当弹性域中的基础资料没有名称属性时，使用查询操作API查询弹性域报错的问题。

15. 【问题修复】：修复了点击云更新同步标准接口时，系统提示“认证不通过”的问题。

## 2023-10-24 BOS_V6.0.1

1.  云迁移：【开放平台】改名为【OpenAPI】，菜单迁移到【开放服务云】。

2. 新增功能：新增【增强型Token认证】模式，管理Token的全生命周期，支持获取、刷新、验证及失效请求令牌。

[https://vip.kingdee.com/article/489812471528707840?productLineId=29&isKnowledge=2](https://vip.kingdee.com/article/489812471528707840?productLineId=29&isKnowledge=2)

3. 功能优化：操作API 适配开发平台【单据】字段类型。

4. 功能优化：导出PDF文档中请求地址由URI改为完整URL，自动拼接当前环境地址和kapi段。

5. 功能优化：保存操作API新增自定义操作参数：“rmStatusControl”，是否移除单据状态控制，手工新增，当值为true时，可跳过已审核单据和基础资料不允许修改的校验，直接更新已审核的单据或基础资料。

6. 功能优化：保存操作API新增操作参数：“is_importinit”，是否触发引入方法。

7. 功能优化：保存操作API新增操作参数："mutex_ignore_validation"，保存时是否忽略网络互斥。

8. 功能优化：第三方应用列表增加【更多】按钮，支持查看当前账套信息。

9. 功能优化：第三方应用增加【应用联系人】字段，可维护外部系统的对接人信息。

10. 功能优化：第三方应用增加【获取Token示例】按钮，可快速查看获取Token报文示例。

11. 问题修复：操作API优化日期字段合规性校验，不允许超出数据库存储范围，如日期小于1900-01-01。

## 2023-08-20 BOS_V5.0.026

1. 问题修复：修复了操作API如批量提交、删除审核等接口，请求参数的Array字段示例错误问题。

2. 问题修复：优化了查询操作API使用体验，当检查到PageSize查询页码过大时，提示报错；当检查到PageNo超过int 最大值时，提示报错。

3. 体验优化：增强查询权限控制，操作API新增时，若操作方式为查询，默认打开开关“启用查询权限控制”。

## 2023-06-30 BOS_V5.0.023

1. 体验优化：优化了第三方应用页面交互，将认证方式、访问控制和加密策略展示成卡片形式，提升用户体验。

[https://vip.kingdee.com/article/464754959607876608](https://vip.kingdee.com/article/464754959607876608)

2. 体验优化：优化了查询操作API文档的展示效果，在返回参数中增加公共返回参数，提升文档可用性。

3. 功能优化：优化了第三方应用访问控制，允许用户配置IP黑名单，提升系统安全性。

4. 功能优化：自定义API支持将参数值以路径变量形式直接拼接到请求url。

5. 功能优化：新增操作API支持的表单模型，支持日志表单和余额模型，降低API开发门槛。

[https://vip.kingdee.com/article/464748428388700416](https://vip.kingdee.com/article/464748428388700416)

6. 问题修复：修正API文档中公共返回参数示例，调用成功时错误码返回"0"。

7. 问题修复：非简体中文语言环境下，API管理列表和API文档左树节点支持展示默认语言。

## 2023-05-21 BOS_V5.0.021

1. 新增功能：API列表支持导出Swagger文档，遵循最新的Swagger3.0规范。

[https://vip.kingdee.com/article/454600313165665024](https://vip.kingdee.com/article/454600313165665024)

2. 功能优化：API 国际化多语言功能优化。

[https://vip.kingdee.com/article/453557180919091968](https://vip.kingdee.com/article/453557180919091968)

## 2023-04-27 BOS_V5.0.020

1. 功能优化：操作API支持更新业务对象分录时，不校验分录id。保存操作API增加操作参数：is_checkentryid，默认为true，若设为false，则更新数据时，不强制校验分录id在系统中是否存在。

2. 体验优化：第三方应用维护页面，不强制禁用状态才允许保存，增加弹窗提示。

3. 问题修复：解决脚本API，在导出PDF时，请求参数出现乱序和丢失参数问题。

4. 问题修复：解决ALL方式的SevletAPI，请求文档中的请求方式错误问题。

## 2023-03-31 BOS_V5.0.018

1. 新增功能： 操作API支持扩展插件，对请求出入参进行序列化处理。

[https://vip.kingdee.com/article/512929770493846784](https://vip.kingdee.com/article/512929770493846784)

[https://vip.kingdee.com/article/512935531689404928](https://vip.kingdee.com/article/512935531689404928)

2. 新增功能： API配置页面，新增配置项【防止重复请求】，相同请求参数的请求在10秒内只能调用一次。

3. 功能优化：API日志过期自动清理，保留时间改为默认30天，最长90天。

[https://vip.kingdee.com/article/418791066016674816](https://vip.kingdee.com/article/418791066016674816)

4. 功能优化：Webservice接口支持一键生成WSDL文件。

5. 体验优化：API配置界面，不强制禁用状态才允许保存，增加弹窗提示。

6. 体验优化：测试弹窗可以改为分屏模式，支持放大缩小。

7. 问题修复：解决部分自定义API返回参数示例与实际返回不符问题。

## 2022-12-15 BOS_V5.0.014

1. 新增功能：API Servlet扩展，支持自定义处理Servlet，解决复杂业务场景。

[https://vip.kingdee.com/article/407938727957357824](https://vip.kingdee.com/article/407938727957357824)

2. 新增功能：查询、保存操作API接入隐私中心，支持对敏感字段和日志脱敏。

[https://vip.kingdee.com/article/408204299592721152](https://vip.kingdee.com/article/408204299592721152)

3. 功能优化：OpenAPI报文格式context-type支持text/xml。

4. 问题修复：解决保存操作接口，特殊基础资料（如业务员、银行账户等）编码传空值时报错问题。

## 2022-12-15 BOS_V5.0.012

1. 新增功能：支持用户配置查询操作API时，查询条件中常量参数支持函数脚本。

2. 功能优化：新增保存操作API参数，可配置是否执行引入方法。

[https://vip.kingdee.com/article/376380062704500992](https://vip.kingdee.com/article/376380062704500992)

3. 功能优化：新增配置项，在API详情界面，用户可配置调用API接口是否需第三方应用授权、匿名访问等。

4. 功能优化：支持为保存操作API配置最大处理数据行，避免接口超时问题。

5. 功能优化：限流策略支持匿名访问维度。

6. 功能优化：支持开发操作API时，请求参数和返回参数中选到分录的关联关系实体。

7.  新增接口：新增开放平台标准单据示例接口，作为用户开发操作API时参考模板。

## 2022-11-17 BOS_V5.0.011

1.  交互优化：开放平台菜单目录调整。

2. 交互优化：开放平台第三方应用详情UE交互优化。

3. 新增功能：API管理列表增加【云更新】按钮，支持从云端同步最新的API资源。

4. API&SDK：新增 500+ 标准OpenAPI接口和SDK文档，覆盖财务、供应链、制造、HR、流程等领域接口使用场景。

[开放门户：https://dev.kingdee.com/index/open](https://dev.kingdee.com/index/open)

5. API安全：第三方应用新增认证方式：签名认证，对接口数据加签，有效防篡改。

[https://vip.kingdee.com/article/383567026112739840](https://vip.kingdee.com/article/383567026112739840)

6. API安全：第三方应用新增加密策略，调用接口时对数据加密。

7. 问题修复：修复通过操作API更新数据时，基础资料id或编码传空时，未清除单据中基础资料字段且接口报错的问题。

8. 问题修复：修复通过操作API保存数据时，若long类型字段如ID为一位数，则保存报错的问题。

9. 问题修复：修复通过操作API保存数据时，若单据中某个基础资料存在多个分组中时（如销售员与销售组），保存报错的问题。

10. 问题修复：修复通过操作API保存数据时，请求体中若存在long类型字段，且为一位数，则保存报错的问题。

## 2022-09-22 BOS_V5.0.009

1.  新增功能：API管理列表支持导出并导入，帮助用户快速完成不同环境间的API数据的备份和迁移。

[https://vip.kingdee.com/article/347769782810858496](https://vip.kingdee.com/article/347769782810858496)

2.  新增功能：开放平台API管理列表支持导出sql脚本。

3. 新增功能：API文档样式优化，展示更清晰简洁的markdown文档。

4. 新增功能：自定义API支持匿名访问，当MC参数 login_api_support_anonymous为true 时，自定义API详情界面展示匿名开关。

5. 新增功能：API查询操作API 支持校验接口代理用户组织权限及数据规则，防止出现数据越权。

6. 功能优化：操作API支持选择业务对象所有操作方式。

7. 功能优化：API详情新增版本苍穹版本字段，默认展示当前接口适用的版本号。

8. 功能优化：保存操作API，参数控制增加默认参数：完全覆盖分录OverrideEntry，当值为true时，更新保存会将原分录完全删除后再新增分录。

9. 功能优化：查询操作API，当查询参数新增一行后，默认生成对应的查询条件。

10. 功能优化：自定义API出参允许修改根节点，支持将root节点变更为其它如名称如response。

11. 功能优化：自定义API支持model属性直接传参、通过注解声明请求头和错误代码。

[https://vip.kingdee.com/article/294499338318073088](https://vip.kingdee.com/article/294499338318073088)

12. 功能优化：脚本API支持在脚步里面获取获取全部请求参数。

13. 功能优化：脚本API资源引用资源优化，避免API资源间接循环引用。

14. 问题修复：解决保存操作API，自定义操作参数无法直接保存的问题。

15. 问题修复：保存操作API，日期字段格式缺陷处理，解决部分错误格式传入后依然可以传入成功的问题。

16. 问题修复：解决查询操作API，当请求参数默认值为"*"时，导致的左括号与右括号不匹配问题。

17. 问题修复：查询操作API查询条件中状态字段(status）比较方式支持“不等于”。

18. 问题修复：解决部分场景下删除操作API调用失败后，返回参数外层message为null的问题。

19. 问题修复：解决导出PDF接口文档时，API接口请求体示例结构缺少data域的问题。

20. 问题修复：优化API日志记录，GET方式的查询接口的请求参数，展示请求地址中拼接的query参数。

21. 问题修复：解决由于NGINX转发后字符集问题，导致中文参数在接收时出现乱码的问题。

## 2022-08-25 BOS_V5.0.007

1. 新增功能：API支持基于基本认证模式，一键生成接口回调地址。

[https://vip.kingdee.com/article/352773265946763776](https://vip.kingdee.com/article/352773265946763776)

2. 功能优化：优化弹性域保存入参样式，支持按核算维度编码作为入参标识。

[https://vip.kingdee.com/article/352775732332438016](https://vip.kingdee.com/article/352775732332438016)

3. 功能优化：优化PG库兼容问题，查询操作API支持按基础资料的内码进行过滤查询。

4. 新增接口：提供API日志的API查询接口，用户可以分页导出大量日志以做审计。

5. 新增接口：提供API查询接口，允许用户查询API列表。

6. 新增接口：提供第三方应用查询接口，允许用户查询第三方应用列表和详情。

## 2022-08-11 BOS_V5.0.006

1. 问题修复：修复了API2.0保存接口，入参中long类型字段为空时，系统默认赋值 '0' 的问题。

3. 问题修复：修复了日志取日志接口频繁调用微服务的问题。

4. 问题修复：修复了API2.0分容器多节点部署时，调用接口提示 kd.bos.ext 相关问题。

5. 功能优化：优化了API2.0接口返回错误message的展示。

## 2022-07-28 BOS_V5.0.005

1. 新增功能：API2.0维护界面添加字段，支持接口出参仅返回Data域内参数。[https://vip.kingdee.com/article/342000610100428544](https://vip.kingdee.com/article/342000610100428544)
2. 新增功能：OpenAPI接口防止重复调用参数。

[https://vip.kingdee.com/article/341958917544263424](https://vip.kingdee.com/article/341958917544263424)

3. 功能下架： API服务管理列表1.0 下架新增按钮，建议优先使用API2.0版本进行接口开发。

[https://vip.kingdee.com/article/341987772477117184](https://vip.kingdee.com/article/341987772477117184)

4. 功能优化： 新增API1.0接口【升级】按钮，支持跳转到API2.0接口配置界面。

5. 功能优化：API2.0接口、第三方应用在修改前必须先禁用，保障数据安全。

6. 功能优化：API管理查询/保存/提交等操作API返回参数样式调整。

7. 功能优化：API查询接口最大返回数量条数限制修改为100000(增加提示)。

8. 功能优化：API日志当出入参超过2000字符时，支持导出大文本日志（详细日志）。

## 2022-06-30 BOS_V5.0.003

1. 功能优化：统一开放平台API的错误message；
2. 问题修复：解决接口保存凭证时，弹性域中的核算维度若都为辅助类型，当编码一致时接口报错问题；

3. 问题修复：解决API2.0标准查询接口部分基础资料如部门，查询条件界面配置与实际预览效果不一致问题；

4. 问题修复：解决API2.0标准查询接口，当请求参数设为必填，但当参数传入空value时未校验问题。

## 2022-06-18 BOS_V5.0.002

1. 菜单重构：优先展示API2.0功能菜单，【API管理】、【API文档】仅展示API2.0的接口数据，原版本接口菜单路径转移至【其他】-【API1.0】下；[https://vip.kingdee.com/article/321672729236116992](https://vip.kingdee.com/article/321672729236116992?productLineId=29&isKnowledge=2)
2. 新增功能：操作API2.0支持启用/禁用操作；
3. 新增功能：自定义API2.0支持脚本开发模式；[https://vip.kingdee.com/article/322686880653270784](https://vip.kingdee.com/article/322686880653270784?productLineId=29&isKnowledge=2)
4. 新增功能：新增代码片段管理功能，开发者可保存代码片段，在开发自定义API2.0时快速引用；[https://vip.kingdee.com/article/322432991026765568](https://vip.kingdee.com/article/322432991026765568?productLineId=29&isKnowledge=2)
5. 新增功能：开放平台提供预置的增删改查数据库脚本函数；
6. 新增功能：开放平台提供自定义API2.0开发脚本、工具的帮助手册；[https://vip.kingdee.com/article/322440885663733248](https://vip.kingdee.com/article/322440885663733248?productLineId=29&isKnowledge=2)
7. 功能优化：API统计看板过滤维度支持第三方应用维度；
8. 新增功能：第三方应用和API支持配置限流策略；[https://vip.kingdee.com/article/322444102576922368](https://vip.kingdee.com/article/322444102576922368?productLineId=29&isKnowledge=2)
9. 新增功能：新增第三方应用登录认证方式：基本认证。适用接口回调场景，使用固定的登录认证密钥，无需多次获取；[https://vip.kingdee.com/article/218694224386822400](https://vip.kingdee.com/article/218694224386822400?productLineId=29&isKnowledge=2)
10. 功能优化：操作API2.0，请求体参数的添加属性面板，支持选择基础资料的引用属性；

11. 功能优化：统一API接口调用结果返回样式。

## 2022-04-28 BOS_V4.0.020

1. 功能优化：优化API服务管理列表的标准引入引出模板，在不同环境能够正常迁移数据，且不会丢失参数的层级节点（参数仍有上下层级关系）。
2. 功能优化：优化了API操作接口外层message，当对多条业务数据进行操作，遇到了业务抛错且不统一时，外层message统一返回：操作失败。
3. 功能优化：优化API文档，API2.0增加错误码区域，供开发者维护接口相关的错误码和错误说明。
4. 功能优化：AI服务请求方式默认为POST，且不允许修改。

## 2022-04-14 BOS_V4.0.019

1. 功能优化：API2.0保存接口弹性域解析优化

[https://vip.kingdee.com/article/305337130849555200](https://vip.kingdee.com/article/305337130849555200)

2. 功能优化：API2.0保存接口多选基础资料解析优化

[https://vip.kingdee.com/article/305343720336171008](https://vip.kingdee.com/article/305343720336171008?productLineId=29&isKnowledge=2)

3. 新增功能：API2.0操作服务支持撤销（unsubmit）操作

[https://vip.kingdee.com/article/304982138011667200](https://vip.kingdee.com/article/304982138011667200)

4. 功能优化：API2.0的接口调用日志会按实际调用的格式展示。

5. 功能优化：API服务管理列表引入引出模板优化，方便用户在不同环境进行API服务数据初始化。

6. 功能下架：系统参数控制，删除上机操作日志字段：API操作日志不再记录在上级操作日志中，统一记录在API调用日志中。

## 2022-03-24 BOS_V4.0.018

1. 功能优化：API1.0操作服务插件逻辑优化，保存操作接口，优化前插件是需要配置在界面元数据的位置才有作用，用户需要对单据做扩展，使用起来不方便。现在改动为插件仅需要在开放平台配置后，直接生效。
2. 功能优化：在开放平台系统参数中打开限流开关后，用户可在第三方应用中配置限流策略，从而限制第三方对苍穹系统的接口调用频率。
3. 功能优化：API2.0操作服务支持生成WSDL，发布为Webservice接口。

## 2022-03-10 BOS_V4.0.017

1. 新增功能：开放平台自定义服务2.0新版体验。

[https://vip.kingdee.com/article/291996579606116096](https://vip.kingdee.com/article/291996579606116096)

2.新增功能： 自定义服务2.0 支持发布成webservice接口。

[https://vip.kingdee.com/article/292625960623314176](https://vip.kingdee.com/article/292625960623314176)

## 2021-12-23 BOS_V4.0.014

1. 功能优化：开放平台首页提供接入引导、产品动态和统计看板，帮助用户实时掌控OpenAPI最新动态。

[https://vip.kingdee.com/article/264025376299785728](https://vip.kingdee.com/article/264025376299785728)

2. 新增功能：增加API统计监控菜单，统计API服务的调用次数、平均响应时间等信息，监控目标偏离情况。

[https://vip.kingdee.com/article/263991453675078656](https://vip.kingdee.com/article/263991453675078656)

## 2021-12-09 BOS_V4.0.013

1. 新增功能：API2.0接口（新版体验），增删改查等操作API，增加页面约束，按界面配置参数进行逻辑处理

[https://vip.kingdee.com/article/263964194020967424](https://vip.kingdee.com/article/263964194020967424)

2. 新增功能：API在线测试（新版体验），通过界面配置操作服务，自动生成URL和参数示例，支持一键测试

[https://vip.kingdee.com/article/264387370336526592](https://vip.kingdee.com/article/264387370336526592)

3. 新增功能：API状态转换（新版体验） ，设置内测、发布、维护、禁用共四种API状态，用于管理API生命周期

4. 新增功能：API日志（新版体验），在开放平台中记录API调用日志

[https://vip.kingdee.com/article/263990262291340800](https://vip.kingdee.com/article/263990262291340800)

5. 新增功能：API清单2.0（新版体验），更加扁平化的参数记录文档，展示json和xml报文示例，简洁易读

[https://vip.kingdee.com/article/263976322287191040](https://vip.kingdee.com/article/263976322287191040)

6. 新增功能：第三方应用支持IP白名单管理

[https://vip.kingdee.com/article/264403098557467392](https://vip.kingdee.com/article/264403098557467392)

7. 新增功能：第三方应用支持限流

[https://vip.kingdee.com/article/264401528076026880](https://vip.kingdee.com/article/264401528076026880)

8. 新增功能：增加API参数设置面板，统一管理Open API系统级参数，如记录API日志级别、是否显示异常stack等

[https://vip.kingdee.com/article/264031111892565504](https://vip.kingdee.com/article/264031111892565504)

9. 功能优化：API2.0入参支持XML格式

## 2021-10-14 BOS_V4.0.009

1. 功能优化：允许用户配置API结果序列化是否包含NULL值的字段，MC配置开关： api.jsonFormatIncludeNull 为 true 时允许，否则默认是不输出NULL值的字段[https://club.kdcloud.com/article/258974043687531008](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fclub.kdcloud.com%2Farticle%2F258974043687531008)

2. 功能优化：第三方应用增加启用/禁用按钮，用来管理第三方应用的状态

3. 功能优化：API查询接口支持返回多选基础资料编码和名称：在URL参数中增加 api.resulttype=json

## 2021-09-23 BOS_V4.0.008

1. 功能优化：第三方应用列表界面增加 创建人、创建时间、更新人、更新时间字段

## 2021-09-09 BOS_V4.0.007

1. 新增功能：开放平台标准API服务新增分录删除接口

[https://vip.kingdee.com/article/230330085126444032](https://vip.kingdee.com/article/230330085126444032)

2. 功能优化：自定义API不需多次定义请求头，可以通过 (Map) params.get("requestHeaders")获取请求头

[https://club.kdcloud.com/article/258975175914914560](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fclub.kdcloud.com%2Farticle%2F258975175914914560)

3.  功能优化：开放平台接口屏蔽异常堆栈信息

[https://vip.kingdee.com/article/262145430811822848](https://vip.kingdee.com/article/262145430811822848)

## 2021-08-26 BOS_V4.0.006

1.  新增功能：API服务支持导出生成PDF文档

2. 功能优化：Content-type返回类型统一格式

3. 功能优化：支持配置API日志记录级别，客户可在MC添加开关： "api.writelog.level"支持选择保存的日志信息级别，默认为detail1，只记录请求头及返回头内容，也可选择detail2，此时记录请求头及请求体、返回头及返回体全部内容

[https://vip.kingdee.com/article/261944995475868416](https://vip.kingdee.com/article/261944995475868416)

4. 功能优化：优化API日志处理，记录上机日志、日志敏感信息处理

5. 功能优化：查询接口支持按不同时间类型过滤：如支持按YYYY/MM/DD，YYYY/MM/DD HH:MM:SS 过滤

6. 功能优化：API接口异常提示处理优化，默认隐藏堆栈信息：客户可在mc添加开关exception_showstacktrace=true，会按照之前的方式把错误堆栈抛出来

7. 功能优化：接口请求方式检查限制，用户可限制接口调用方式必须和开放平台发布的API服务保持一致。在MC管理中心的集群下，增加参数api.httpmethod.match，当值为true时，会强制校验接口调用方式和开放平台配置的请求方式。

8. 功能优化：API多级路由

[https://vip.kingdee.com/article/262143039940722176](https://vip.kingdee.com/article/262143039940722176)

9. 功能优化：API接口跨域限制

[https://vip.kingdee.com/article/262144553967600640](https://vip.kingdee.com/article/262144553967600640)

10. 功能优化：redis及本地缓存处理优化

11. 功能优化：第三方应用认证方式和API服务授权

[https://vip.kingdee.com/article/220628918863785216](https://vip.kingdee.com/article/220628918863785216)

12. 功能优化：应用密匙加密存储优化

## 2020-08-27 BOS_V2.0.035

1.  功能优化：增加了开放平台query接口分页查询功能

[https://club.kdcloud.com/article/88944267246091777](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fclub.kdcloud.com%2Farticle%2F88944267246091777)

2.  功能优化：优化了开放平台query接口in查询功能

[https://club.kdcloud.com/article/88946348577177088](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fclub.kdcloud.com%2Farticle%2F88946348577177088)

## 2019-07-08 BIZ_V1.5.001

1. 新增功能：API列表以组织层次分类左树右表展示

2. 功能优化：API录入向导交互方式进行了优化，引导性得到了提升

3. 功能优化：API录入即审核，无需提交审核即可访问

4. 功能优化：API加入权限管控，安全性得到了提升
