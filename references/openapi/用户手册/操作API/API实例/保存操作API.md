---
title: "保存操作API"
entityId: "264036069979704064"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/264036069979704064?productLineId=29&lang=zh-CN"
createdAt: "2021-12-29 14:25:05"
updatedAt: "2026-07-21 10:35:55"
views: 20630
---

# 保存操作API

**变更记录**

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V5.0.011 | 初始版本 | 2022年06月 |
| V7.0.6 | 保存操作API增加操作参数multiOps，支持组合保存、提交、审核操作 | 2025年02月 |
| V7.0.7 | 保存操作API增加自定义操作参数judgeKeyRepeatCheck，支持批量保存数据时，在内存中校验候选键 | 2025年03月 |
| V8.0.1 | 保存操作API增加操作参数firePropChangedOnAdd，支持新增时触发值更新事件 | 2025年11月 |

---

## 1 接口介绍

保存操作API是通过在系统中维护接口基本信息、配置请求参数来定义接口具体的功能。

## 2 注意事项

- 保存操作接口根据入参的不同，可同时执行保存、更新、批量保存和批量更新四种操作。
- 候选键作为接口执行更新逻辑的唯一主键，需要谨慎选择，一般选id或number/billno为候选键，也可选择不同字段组合作为候选键。
- 若接口只用于更新数据，此时可以将候选键字段设为必填。

## 3 接口示例

### 3.1 维护API基本信息

录入API编码、API名称、业务对象、操作方式、详细描述等信息，请求方式为“POST”，系统自动生成API请求地址。

![](https://vip.kingdee.com/download/01099b2f27ecdbd34291b5fa87ad10a4efc2.png)

### 3.2 维护请求头参数

系统已预置Content-Type、accesstoken等参数，用户无需维护。

![](https://vip.kingdee.com/download/0109d6ac59a76dc2455bb46465cb380f0916.png)

### 3.3 维护请求体参数

点击“添加属性”按钮快速添加请求参数，业务对象每个层级必须设有候选键，若在系统中查到相同候选键的数据，会执行更新操作，若未传入则执行新增操作。用户还可以点击“参数示例”按钮，查看JSON、XML、SOAP1.1、SOAP1.2 四种格式的数据示例。

注意：保存采购订单时，物料采购信息可能会有组织信息，此时应选择不带masterid的物料编码。

![](https://vip.kingdee.com/download/01098cea691be9e94c60aca1175e2216329f.png)

### 3.4 维护操作参数（可选）

操作参数分为系统保存参数和自定义参数，都支持在保存时对数据进行特殊处理。

1）系统保存参数：

- importType ：保存类型，new - 新增，override - 覆盖，overridenew - 覆盖新增，接口默认执行覆盖新增逻辑；
- firePropChanged ：更新时触发值更新事件，true - 触发，false - 不触发，接口默认不触发，该参数非常影响性能，不建议开启后进行大数据量更新；
- firePropChangedOnAdd：新增时触发值更新事件，true - 触发，false - 不触发，接口默认不触发，注意，开启后性能影响极大，单次请求分录上限为200条(可通过MC参数配置行数 OpenApi.EntryRowsForPropChanged)
- forcedSubmit：强制提交（注意，若单据的save插件中有复杂计算逻辑，配置后无法触发），submit - 提交，空 - 不提交，接口默认不自动提交；
- OverrideEntry ：更新时完整覆盖分录，会将原表单分录数据清除后追加分录， true - 覆盖，false - 不覆盖，接口默认不覆盖；
- mutex_ignoremodify：保存时忽略网络互斥，true - 忽略，false - 不忽略，接口默认不忽略；
- is_importinit：是否触发引入方法，true - 触发，false - 不触发，接口默认触发。
- multiOps：组合操作参数，支持将保存、提交和审核操作组合执行。save,submit - 保存后提交；save,submit,audit - 保存后提交并审核，接口默认只执行保存。注意：批量保存时，若提交或审核失败，会出现不同状态的数据，需用户手工补偿。
- checkApiImportBasedataRule true 保存基础资料字段时，会对基础资料的过滤条件、启用禁用设置和基础资料数据规则进行校验，校验会对性能造成一定影响。 true - 校验，false - 不校验
- isReturnEntryIds true 是否返回分录ID。注意：不支持返回子分录ID。 true - 返回，false - 不返回，接口默认不返回

2）自定义参数：

- rmStatusControl：是否移除单据状态控制，默认为false，当值为true时，可跳过已审核单据和基础资料不允许修改的校验，直接更新已审核的单据或基础资料。
- is_checkentryid，默认为true，默认为true，若设为false，则更新数据时，不强制校验分录id在系统中是否存在，适用于接口更新单据时，同时新增单据分录（带id）的场景。
- forcedAudit：强制提交并审核，默认为false，当值为 true 时，新增数据时会自动提交并审核单据（注意，由于不会触发保存操作，所以不适用于更新场景）。
- WF：该参数配合forcedAudit参数使用，可控制OpenAPI提交审核的单据是否进入工作流，默认为true，将该值设为false后，即可跳过工作流，直接审核成功。
- updateEntrySummaryEnable：更新时汇总分录金额到单据头，默认为false，当值为true时，当API不传入单据头汇总金额字段时，会将分录金额自动汇总至单据头。
- fireAfterCreateNewData：是否触发表单插件中的fireAfterCreateNewData方法，默认为true，当值为false时，不触发该方法。
- fireFieldControlRule：保存时是否触发实体中的字段权限方案（字段不可读写），默认为true，当值为false时，不触发该权限校验。
- judgeKeyRepeatCheck：保存时是否在内存中检查候选键，默认为false，将请求候选键和数据库已存在的数据，进行唯一性校验；当值为true时，在内存中检查候选键是否唯一。
- isInOrderFieldOfReq 为 true 时会保证原报文字段顺序,避免触发值更新时有顺序问题

**3.5 定义返回参数**

保存操作服务的返回参数目前不允许用户自定义，统一按平台规范返回。

API Response契约统一为:

{

“data”: {                                  //结果数据

"result": [],                          //返回结果详细信息

“failcount”: “”,                   //操作失败数量

“successcount”: “”             //操作成功数量

}

“errorCode”: “”,                     //错误码        “message”: null,                     //失败时的提示信息

“status”: true/false                //是否成功

}

### 3.6 API测试

点击“API测试”按钮，开始调试API。当传入候选键字段时，执行更新操作，不传入候选键字段，则执行新增操作。

![](https://vip.kingdee.com/download/0109351d7010edc14b78890c740b9958c5a7.png)

![](https://vip.kingdee.com/download/010907215bb5200b4eea89acdfe95045b072.png)

## 4 注意事项

- 多类别基础资料支持按id、number和name引入，但若选择其他属性引入（不推荐），系统会根据这个属性按第一个基础资料类别去找id，若找到也能正常引入。
- 若多选基础资料的编码字段，使用的是非标准number字段，如银行账户（bd_accountbanks）、资产清单（tdm_asset_data），此时基础资料无法按number字段引入，建议使用id字段。或通过扩展插件，传入非标准编码字段后，在插件中转为id写入。参考[扩展插件：序列化出入参](https://developer.kingdee.com/knowledge/512929770527401216?specialId=226337046514476288&productLineId=29&isKnowledge=2&lang=zh-CN)。

## 5 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
