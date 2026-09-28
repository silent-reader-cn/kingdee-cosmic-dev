---
title: "脚本API报错：\"未发现类xxx的方法xxx\""
entityId: "648940431903962368"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/648940431903962368?productLineId=29&lang=zh-CN"
createdAt: "2024-11-25 17:37:36"
updatedAt: "2024-11-26 16:28:33"
views: 923
---

# 脚本API报错："未发现类xxx的方法xxx"

## 问题描述

当使用脚本API中的脚本调用微服务时，提示未发现类xxx的方法xxx，是什么原因？报错如下：

{

"data":null,

"errorCode":"###",

"message":"未发现类fxy.manufacture.mplan.plugin.AssignServiceImp的方法saveUrlFile,traceId：cb8000df11142426",

"status":false

}

## 解决办法

使用脚本调用二开微服务，若出现未发现类xxx的方法等问题，解决办法如下：

1. 首先需要确认类和方法名是否正确；

2. 请参考OpenAPI脚本帮助手册进行微服务调用，并检查参数类型是否和文档中参数说明保持一致，若类型错误，则调用接口时也会提示未发现类xxx的方法xxx。

![](https://vip.kingdee.com/download/0109ba88f363a25e4e139387effe01a42663.png)
