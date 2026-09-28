---
title: "审核操作API
"
entityId: "264352025188367872"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/264352025188367872?productLineId=29&lang=zh-CN"
createdAt: "2021-12-30 11:20:34"
updatedAt: "2025-12-19 10:08:04"
views: 3835
---

# 审核操作API

## 1 接口介绍

审核操作API是通过在系统中维护接口基本信息、配置请求参数、查询条件来定义接口具体的功能。

## 2 注意事项

由于可以通过查询条件批量审核数据，开发人员新增接口时一定要谨慎定义查询条件，充分测试，避免因数据误审核对业务产生影响。

## 3 接口示例

### 3.1 维护API基本信息

录入API编码、API名称、业务对象、操作方式、详细描述等信息，请求方式为“POST”，系统自动生成API请求地址。

![](https://vip.kingdee.com/download/01091f8bd1898ca1445f8306577afedbe59f.png)

### 3.2 维护请求头参数

系统预置了content_type和accesstoken等参数，用户无需维护。

### 3.3 维护请求体参数

点击“增行”或“添加属性”按钮，快速添加请求参数，后续调用方须遵循界面配置传入请求参数。

![](https://vip.kingdee.com/download/01092235189941494fce9960c2275b870228.png)

### 3.4 定义查询条件

维护查询条件，将业务字段和请求参数进行比较生成查询条件。查询条件还支持常量过滤，方便接口定向处理数据。

备注：当查询条件比较方式为“在...中”或“不在...中”时，对应比较变量的参数类型必须为Array数组。此时可以选择Array<Integer>、Array<String>、Array<Long>、Array<Date>这四种数组类型。

![](https://vip.kingdee.com/download/0109898f66beb97b4373a6126b1779bb7dbe.png)

### 3.5 定义返回参数

审核操作服务的返回参数目前不允许用户自定义，统一按平台规范返回。

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

### 3.6 API测试

点击“API测试”按钮，开始调试API。若测试结果符合功能需求，接口就可以正式发布了。

![](https://vip.kingdee.com/download/0109cbd44957d7674ffa9a6175899f81db1c.png)

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
