---
title: "接口DobboServiceLookup，表单插件中AfterCreateNewData报空指针"
entityId: "652870812092969472"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/652870812092969472?productLineId=29&lang=zh-CN"
createdAt: "2024-12-06 13:55:31"
updatedAt: "2024-12-06 14:17:59"
views: 886
---

# 接口DobboServiceLookup，表单插件中AfterCreateNewData报空指针

## 问题描述

当调用保存操作API时，接口请求报错，提示errorCode：DobboServiceLookup，打开详细错误信息，发现是业务对象的表单插件报空指针，并且指向表单插件中的AfterCreateNewData方法。

![](https://vip.kingdee.com/download/01092c27f298af564a8f85d2aa3a7539f22a.png)

## 问题分析

由于保存操作API默认会触发表单插件中的fireAfterCreateNewData方法，可能会导致该方法中的逻辑校验与传入的请求参数不匹配发生报错。

## 解决办法

在保存操作API上，维护自定义操作参数：fireAfterCreateNewData，将该值设为false，即不触发该方法，接口正常按请求参数传值，就可以正常执行。

![](https://vip.kingdee.com/download/01099e086b2adfac43659e36e32c6ce1d21c.png)
