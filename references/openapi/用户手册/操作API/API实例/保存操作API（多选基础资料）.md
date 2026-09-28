---
title: "保存操作API（多选基础资料）"
entityId: "305343720352948224"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/305343720352948224?productLineId=29&lang=zh-CN"
createdAt: "2022-04-22 14:06:56"
updatedAt: "2025-12-19 10:09:22"
views: 6935
---

# 保存操作API（多选基础资料）

## 1 接口介绍

保存操作API是通过在系统中维护接口基本信息、配置请求参数来定义接口具体的功能。若保存操作API存在多选基础资料字段，可参考本文档配置。

## 2 接口示例

### 2.1零代码配置API

以高等院校（hbss_college）为例，维护API基本信息及请求参数，其中院校特性字段（collegecharact）是**多选基础资料**，通过点击“添加属性”按钮，可定义多选基础资料的入参：如id、number、name等，建议勾选一个参数即可，推荐使用number。

![](https://vip.kingdee.com/download/01097e5973ea36f8495e8cd63313639c0b77.jpg)

维护完请求参数后，点击“保存”按钮，接口创建完成。

![](https://vip.kingdee.com/download/0109fb4a18b16158456f8b636527efd867fb.png)

### 2.2 API测试

点击“API测试”按钮，开始调试API。在Request body 中传入正确格式的请求参数调用接口，新增数据成功。

![](https://vip.kingdee.com/download/01096358a4620e0544bc935b5e547bc4e0e5.png)

## 3 注意事项

- 当多选基础资料同时勾选了id、number和name时，系统执行保存的优先级是id > number > name。即这三个参数若代表不同基础资料，系统会优先按id去保存。
- 当多选基础资料的编码字段，使用的是非标准number字段，如银行账户（bd_accountbanks）、资产清单（tdm_asset_data），此时基础资料无法按number字段引入，建议使用id字段。或通过扩展插件，传入非标准编码字段后，在插件中转为id写入。参考[扩展插件：序列化出入参](https://developer.kingdee.com/knowledge/512929770527401216?specialId=226337046514476288&productLineId=29&isKnowledge=2&lang=zh-CN)。

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
