---
title: "下推操作API"
entityId: "439503562712934144"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/439503562712934144?productLineId=29&lang=zh-CN"
createdAt: "2023-04-27 19:10:15"
updatedAt: "2025-12-19 10:12:08"
views: 6064
---

# 下推操作API

## 1 接口介绍

下推操作API是通过在系统中维护接口基本信息、配置请求参数、查询条件来定义接口具体的功能。

## 2 注意事项

由于可以通过查询条件批量下推数据，开发人员新增接口时一定要谨慎定义查询条件，充分测试，避免因数据误下推对业务产生影响。

注意：下推操作API暂时只支持整单下推，如需要按分录下推以及合并下推，请使用自定义API。

## 3 接口示例

### 3.1 维护API基本信息

录入API编码、API名称、业务对象、操作方式、详细描述等信息，请求方式为“POST”，系统自动生成API请求地址。

![](https://vip.kingdee.com/download/01098e796302579c4dc7a47ccb631f555b3c.png)

### 3.2 维护请求体参数/查询条件

请求头无需维护，点击“增行”或“添加属性”按钮，快速添加请求参数。通过参数控制，将单据字段和请求参数进行比较，生成查询条件。

备注：当查询条件比较方式为“在...中”或“不在...中”时，对应比较变量的参数类型必须为Array数组。此时可以选择Array<Integer>、Array<String>、Array<Long>、Array<Date>这四种数组类型。

![](https://vip.kingdee.com/download/01092f57ac5c21ce40d0b1d7dccdf4e60395.png)

下推操作服务的返回参数目前不允许用户自定义，统一按平台规范返回。

API Response契约统一为:

{

“data”: {                                  //结果数据

" filter":"",                            //过滤条件

"result": [],                          //返回结果详细信息

"totalCount":"",                   //总数

“failcount”: “”,                   //操作失败数量

“successcount”: “”             //操作成功数量

}

“errorCode”: “”,                     //错误码
       “message”: null,                     //失败时的提示信息

“status”: true/false                //是否成功

}

### 3.3 API测试

点击“API测试”按钮，开始调试API。若测试结果符合功能需求，接口就可以正式发布了。

![](https://vip.kingdee.com/download/01098082b017430e45d78b46ac3ff231ef20.png)

接口调用成功后，可以打开费用报销单列表，路径：【财务云】→ 【费用核算】→【单据中心】→ 【费用报销单】，点击列表中的【下查】按钮，能联查到接口下推生成的付款单。

![](https://vip.kingdee.com/download/01097240603ea6bd4dcdaba14a0510cb47b1.png)

![](https://vip.kingdee.com/download/0109962278a4c6894ce8856f2f970bb67631.png)

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
