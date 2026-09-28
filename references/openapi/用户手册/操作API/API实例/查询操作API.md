---
title: "查询操作API"
entityId: "264032313997444096"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/264032313997444096?productLineId=29&lang=zh-CN"
createdAt: "2021-12-29 14:10:09"
updatedAt: "2026-01-21 17:09:03"
views: 21956
---

# 查询操作API

## 1 接口介绍

查询操作API是通过在系统中维护接口基本信息、配置请求参数、查询条件及返回参数来定义查询接口具体的功能。

## 2 注意事项

- 无论是GET请求还是POST请求，查询接口必须携带分页参数。
- 系统已预置Content-Type、accesstoken等请求头参数，用户无需维护。
- 查询操作API无需代码开发，支持配置快速生成，注意请求参数和返回参数不要泄露敏感信息。
- 若要在调用API时，调用方不传请求参数时忽略参数对应的过滤条件，可以将参数设为非必填，同时默认值为“*”。
- 若API要进行分录过滤时，分录中的物料必须选分录最内层的物料属性，否则返回的物料信息为null（若保存时则相反，因为物料采购信息可能会有组织信息，此时应选择不带masterid的物料编码）；
- 查询API的排序仅针对主单排序，分录不排序。若排序条件字段只选择分录字段时，会比较各单据内所有分录中该字段的最大/最小值，对主单进行排序。

另外，关于提升查询接口性能，有以下优化建议：

- 请确保每条查询条件都有索引，建议使用日期范围、单号、ID作为查询条件。如果有多个查询条件，建议建立联合索引，能有效提升查询性能。
- 不建议将子表属性作为查询条件，会导致全面关联查询；如果是基础资料，还可能涉及跨库连接，性能极差。
- 避免在名称上使用 "like" 查询条件，否则，也会触发全表扫描，影响查询性能。
- 针对业务单据的查询，建议将日期范围作为必要的查询条件之一，并建立日期字段索引，这样可以帮助过滤掉大量无用数据，提升查询性能。

## 3 接口示例

### 3.1根据工号查询人员信息

路径：【开放服务云】→【OpenAPI】→【API管理】→【API开发】，列表点击“新增”按钮，进入“零代码开发”模式。

![](https://vip.kingdee.com/download/0109f3578bc01b4a4aaa9f3dc03fac4fd2fc.png)

依次维护API编码、名称、请求方式等信息，如业务对象选择“人员”，操作方式选择“查询”。然后维护请求参数，通过“添加属性”按钮可以快速添加参数，也可以点击“增行”按钮，手工录入参数，参数名称支持完全自定义。

![](https://vip.kingdee.com/download/0109a0eff7c819d940d599b31c9554877484.png)

维护请求参数后，接着维护查询条件和返回参数，比较业务字段和请求参数，常见的比较方式有等于、不等于、包含...等等。

备注：当查询条件比较方式为“在...中”或“不在...中”时，对应比较变量的参数类型必须为Array数组。此时可以选择Array<Integer>、Array<String>、Array<Long>、Array<Date>这四种数组类型。

![](https://vip.kingdee.com/download/0109dd54aed10c7a41e5b0f33dba295df770.png)

维护完返回参数后，接口就开发完毕了，接下来点击“API测试”，开始调试你的接口吧！

![](https://vip.kingdee.com/download/0109223ffe1990a449fbb8d575aec4f7480a.png)

### 3.2 自由组合查询条件，查询人员信息

在上个场景中， 用户通过“添加属性”返回外部系统需要的字段，并且配置非常灵活。那么如果想要更加灵活的请求参数组合，应该怎么做呢？

您只需要在定义查询条件时，配置多组不同的查询条件即可。例如，根据人员状态、创建时间和性别来查询人员信息。

![](https://vip.kingdee.com/download/01096ce8715a56904242a3ef357bead1afc0.png)

若需要在调用API时，调用方不传请求参数时忽略参数对应的过滤条件，按其他条件过滤，只需要将参数设为非必填，并且设置默认值为“*”，当然也可以给其他有具体含义的默认值。

![](https://vip.kingdee.com/download/0109efed0f2d2b91495eac133c05bac06bcb.png)

若在此时调试API，调用方只传入了必填参数，接口会忽略默认值为*的参数对应的查询条件，并组合默认值为其他值的查询条件。

![](https://vip.kingdee.com/download/010943162a8220ea4532b958a71c941443b5.png)

### 3.3 指定固定常量或脚本查询人员信息

在实际应用中，可能还有一个场景，比如A系统对B系统开放查询接口，但出于数据安全考虑，只允许对方查到A组织或来源于B供应商的采购订单，那么可以通过添加常量查询条件来达到这个目的。

![](https://vip.kingdee.com/download/01094458429d3d23431bba61d73e988ad974.png)

只需要在查询条件中配置常量过滤条件，无需维护任何请求参数，如果我们测试API，那么接口会根据固定查询条件返回对应的数据。

![](https://vip.kingdee.com/download/010949019a50665f40fc9f3b869a998df12e.png)

**3.4 分录过滤，根据物料编码**查询**采购订单**

**维护API基本信息，**如API编码、API名称、业务对象、操作方式、详细描述等，系统自动生成API请求地址。

![](https://vip.kingdee.com/download/0109140a25aa153f4f0cab652965e93ff62e.png)

**维护请求参数和查询条件，**配置查询条件时注意，采购订单分录中的物料编码比较特殊，必须用主物料编码和请求参数进行比较，参数标识为：billentry.material.masterid.number。

![](https://vip.kingdee.com/download/0109d5755737955b4b188059a3cdfdaea337.png)

**定义返回参数，**点击“添加属性”按钮，勾选需要返回的参数，若要返回物料编码字段，必须勾选分录最里层的物料编码和名称。确认后点击“保存”按钮，API维护完成。

![](https://vip.kingdee.com/download/01097a589987297e4cfd9e730e30516f9bf4.png)

![](https://vip.kingdee.com/download/0109db886ad81af040c5acfb5a6327a69b0f.png)

如果我们测试API，就可以根据物料编码查询到对应的采购订单信息了。

![](https://vip.kingdee.com/download/010923c814981daf4d58b6c37d60e4e5e038.png)

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)以及[金蝶AI苍穹OpenAPI接口规范](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=386536775126291968&id=448792125560557568&productLineId=29)。
