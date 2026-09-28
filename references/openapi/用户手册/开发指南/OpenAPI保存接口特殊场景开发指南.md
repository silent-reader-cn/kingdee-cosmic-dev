---
title: "OpenAPI保存接口特殊场景开发指南"
entityId: "376385674566087168"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/376385674566087168?productLineId=29&lang=zh-CN"
createdAt: "2022-11-04 15:02:18"
updatedAt: "2025-12-19 10:11:12"
views: 13489
---

# OpenAPI保存接口特殊场景开发指南

## 1. 简介

本文档主要介绍OpenAPI零代码配置的保存接口，在保存数据过程中的特殊逻辑，以方便开发者快速定位接口问题。

## 2. 保存接口开发指南

### 2.1 表单插件中的值更新事件

路径：【开放服务云】→ 【OpenAPI】→ 【API管理】→ 【API开发】，在API管理列表点击“新增”按钮，并维护API信息，在操作参数中选择默认参数“firePropChanged”，并将值设置为true。

此时调用该接口，且出现更新数据的场景，那么将会触发表单所有插件执行propertyChanged方法。

注意事项：

- 当保存的数据中有属性值发生变化时，才会触发propertyChanged 方法，**新增数据时不会触发；**
- 表单的“业务规则”同样与该参数有关，当参数“firePropChanged”为true时，才会在更新数据时触发业务规则。

![image.png](https://vip.kingdee.com/download/010951981382984f43d68898e35c42a97a17.png)

### 2.2 表单插件中的引入方法

保存接口默认触发表单插件中的以下引入方法：

- afterImportData 方法
- beforeImportData 方法
- initImportData 方法

注意事项：

- 通过接口传入的数据类型为Map，调用方需要严格区分页面与接口传递的数据类型区别；
- 从苍穹V5.0.012 版本开始，新增了操作参数 "is_importinit"，可配置是否触发引入方法。若值设为false，将不触发引入方法，有效提升接口性能。
- **保存操作API永远不会触发引入操作中绑定的插件**。

![image.png](https://vip.kingdee.com/download/0109bdf93ac35f184aacb793c0fa024ef61d.png)

## 3. 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
