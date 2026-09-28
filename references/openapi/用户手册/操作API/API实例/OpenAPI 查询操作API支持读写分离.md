---
title: "OpenAPI 查询操作API支持读写分离"
entityId: "815251507280459008"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/815251507280459008?productLineId=29&lang=zh-CN"
createdAt: "2026-02-27 15:58:26"
updatedAt: "2026-02-27 16:30:13"
views: 621
---

# OpenAPI 查询操作API支持读写分离

## 变更记录

| **产品版本** | **更新内容** | **更新时间** |
| --- | --- | --- |
| **V8.0.2** | OpenAPI 查询操作API支持读写分离 | 2025年11月 |

#### 1. 简介

大部分中小客户通常只部署写库，查询和写入均在同一数据库上进行，当查询数据量过大，查询并发增大时，数据库会成为系统的性能瓶颈。在实际场景中，可能某个单据的查询所占用的资源就会拖垮数据库，造成严重的系统性能问题。当出现这种情况时，可以采用读写分离的方案，把查询的负载分担到读库（从库），减轻主库的负载压力，提升系统的性能及稳定性。

#### 2. 主要操作

参考 [**读写分离整体介绍**](https://vip.kingdee.com/knowledge/626770489779829760?productLineId=29&isKnowledge=2&lang=zh-CN)

**OpenAPI读写分离配置**

“系统服务云” >> “分布式管理” >> “读写分离” >> “读写分离配置”

![上传图片](https://vip.kingdee.com/download/01004914e5bdf21b4b73ac8ac9908c949c49.png)

所属场景选择openapi

编码选择需要进行读写分离查询的业务对象

配置: “从库优先”代表优先从读库进行查询，“主库优先”优先从主库进行查询。
