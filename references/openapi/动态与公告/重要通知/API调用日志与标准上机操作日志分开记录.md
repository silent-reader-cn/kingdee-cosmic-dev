---
title: "API调用日志与标准上机操作日志分开记录"
entityId: "262227934248092672"
category: "动态与公告 / 重要通知"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/262227934248092672?productLineId=29&lang=zh-CN"
createdAt: "2021-12-24 14:40:11"
updatedAt: "2023-10-27 17:57:57"
views: 5797
---

# API调用日志与标准上机操作日志分开记录

发布说明

发布版本：苍穹V4.0

适用范围：苍穹开放平台所有用户

上线日期：2021-12-09

补丁号：V4.0.013（BOS）

 更多内容

 1. 简介

金蝶AI苍穹BOS_V4.0.013版本最新特性，开放平台的API接口调用的所有日志单独记录到了开放平台的API调用日志中。使用了新的日志模型，可以存储到 ES 中，并与上机操作日志分开记录，提升效果及性能。

备注：若用户仍需要将API接口方式调用的操作日志，记录到上机操作日志里面，在BOS_V4.0.014版本中提供了一个控制是否同时需要记录到标准的上机操作日志的开关。在BOS_V4.0.018版本中开关失效。

2. 日志查看方式

a）若客户使用的金蝶AI苍穹版本低于BOS_V4.0.013，通过上机操作日志查看，路径：系统服务云→系统管理→监控管理→操作日志。

![](https://vip.kingdee.com/download/0100d526f429b2174bcd8c5e98ab7f6af1bb.png)

b）当金蝶AI苍穹版本升级为BOS_V4.0.013 后，上机操作日志中不再记录上图红框内具体的API操作日志，而是默认记录在**开放平台的API调用日志**中。路径：开发服务云→开放平台→API新版体验→API调用日志2.0。

![](https://vip.kingdee.com/download/0100716195e1b2f14ae19ba4c644c8cf91a2.png)

点击API编码，打开API日志详情界面。

![](https://vip.kingdee.com/download/0100f9f34dbfdc6e49c3869adc59dcd2e4c9.png)

![](https://vip.kingdee.com/download/01003bb6c48576c642f1baafef0dacbd292d.png)
