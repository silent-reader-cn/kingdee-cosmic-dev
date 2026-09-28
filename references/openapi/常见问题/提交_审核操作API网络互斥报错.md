---
title: "提交/审核操作API网络互斥报错"
entityId: "697535079416788736"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/697535079416788736?productLineId=29&lang=zh-CN"
createdAt: "2025-04-08 19:55:23"
updatedAt: "2025-04-08 19:56:13"
views: 1772
---

# 提交/审核操作API网络互斥报错

## 1 问题描述

使用零代码配置的提交或审核操作API，提示报错：“当前单据已在其他页签中打开，如需继续操作，请关闭单据后重试，或重新登录后，再次尝试。”

即标准的提交或审核操作API，如何忽略网络互斥？

## 2 解决方案

若遇到上述场景，有以下方案：

方案一：用户手工删除网络互斥，路径：系统服务云 - 日志管理 - 网络互斥。

方案二：OpenAPI自定义参数解决方案，通过调用方传入参数，忽略网络互斥，若接口以编码作为入参进行审核单据，下面是请求报文示例：

```
{
    "data": {
        "billno": "unittest-00002049"
    },
    "optionvariables": {
        "mutex_ignoremodify": "true"
    }
}
```

![](https://vip.kingdee.com/download/0109c061a660e7f244b88d755e1ffac0ff3a.png)
