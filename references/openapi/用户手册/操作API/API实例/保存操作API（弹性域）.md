---
title: "保存操作API（弹性域）"
entityId: "305337130916664064"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/305337130916664064?productLineId=29&lang=zh-CN"
createdAt: "2022-04-22 13:40:45"
updatedAt: "2025-12-19 10:09:09"
views: 7805
---

# 保存操作API（弹性域）

## 1 接口介绍

保存操作API是通过在系统中维护接口基本信息、配置请求参数来定义接口具体的功能。

弹性域：金蝶AI苍穹表单中的特殊字段，包括核算维度和辅助属性。

## 2 接口示例

### 2.1 零代码配置API

以凭证为例，维护API基本信息及请求参数，点击“添加属性”可快速添加请求参数，其中核算维度为弹性域字段。

![](https://vip.kingdee.com/download/01095ac22b9a54ac41688efa97e0c6d4caee.png)

返回参数目前不允许用户自定义，统一按平台规范返回。点击“保存”按钮，接口创建完成。

![](https://vip.kingdee.com/download/01093305be232c2147e699f7b67c66ff1a86.png)

### 2.2 API测试

用户可以点击“参数示例”按钮，查看数据结构示例，如某科目核算维度为供应商（基础资料）、地址类型（辅助资料）和手工输入维度（其他类型），入参如下：

| "assgrp": {"id": 8445228273874472960, //核算维度id，若传参，则以下所有核算维度可不填"供应商": { //核算维度名称-基础资料类型（支持id或number）"number": "SUP000001",},"地址类型": { //核算维度名称-辅助资料类型,（支持id或number）"number": "Address01",},"手工输入维度": "自定义文本" //核算维度名称-其他类型 |
| --- |

点击“API测试”按钮，开始调试API。按规范传入弹性域并构造请求参数，调用API批量保存凭证。

![](https://vip.kingdee.com/download/0109bfdef3d7f4764a92a09f75c1c526f497.png)

当第三方系统不支持传入核算维度的中文名称时（如使用ABAP开发语言），金蝶AI苍穹OpenAPI也支持按核算维度编码赋值，此时入参格式如下：

| "assgrp":{"flextype":"number","103":{"number":"00"}} |
| --- |

![](https://vip.kingdee.com/download/01099dfe1f41ed934af2aac9ff3431d2d340.png)

![](https://vip.kingdee.com/download/01095bc632ca6f834fb19f6147f4edba1cf0.png)

**保存操作API同时支持维护默认值（两种格式），当弹性域不传值或传空值时，自动按默认值保存凭证。**

![](https://vip.kingdee.com/download/010986981231c50146909d3259c92bebf7e0.png)

## 3 注意事项

- 核算维度若同时传入了基础资料id、number和name时，保存优先级是id > number > name。
- 若弹性域需要按编码保存，assgrp参数中需传入**"flextype":"number"**。

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
