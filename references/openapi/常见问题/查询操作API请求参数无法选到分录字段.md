---
title: "查询操作API请求参数无法选到分录字段"
entityId: "724273430630919424"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/724273430630919424?productLineId=29&lang=zh-CN"
createdAt: "2025-06-21 14:44:02"
updatedAt: "2025-06-21 15:03:54"
views: 874
---

# 查询操作API请求参数无法选到分录字段

## 问题描述

通过开放平台OpenAPI新增查询操作接口，请求参数添加属性时，为什么选不到分录字段？

![](https://vip.kingdee.com/download/01096073ef7b4d1e40f7970281645e2c0559.png)

## 原因分析

在系统中，查询操作API 与保存操作 API 在数据处理逻辑上存在差异，所以用户在配置请求参数时需采用不同的方式。具体如下：

-
  保存操作 API 在写入数据时，用户要在请求参数中明确指定单据头和分录字段，系统会自动将这些参数与对应对象属性建立关联。
-
  而查询操作 API 则通过参数控制中的查询条件，将实体的单据头和分录字段与传入的请求头参数进行动态关联。因此，用户在配置查询请求参数时，无需直接选择分录字段，只需将查询条件中的条件字段，与请求参数进行逻辑关联即可。

具体操作建议：

1. 对于单据头字段：可通过 "添加属性" 功能快速完成配置
2. 对于单据体或子单据体字段：
  - 点击【增行】按钮自定义参数（用户可随意命名，如aa或customkey）
  - 在查询条件配置中将该自定义参数与目标分录字段建立比较关系

这种查询操作更加灵活高效，用户可以根据实际需求动态组合查询条件，而无需预先定义固定的字段映射关系。

![](https://vip.kingdee.com/download/0109f875b6d320424248ae4ac9d33d60aa92.png)
