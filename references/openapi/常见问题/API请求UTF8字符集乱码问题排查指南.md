---
title: " API请求UTF8字符集乱码问题排查指南"
entityId: "568740319093390592"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/568740319093390592?productLineId=29&lang=zh-CN"
createdAt: "2024-04-18 10:10:59"
updatedAt: "2024-04-18 13:45:18"
views: 1976
---

# API请求UTF8字符集乱码问题排查指南

## 1 问题描述

当第三方系统请求OpenAPI时，请求参数和返回参数中文字段出现乱码问题。

![](https://vip.kingdee.com/download/01091e248ca76ca443c58ba5a02696ec45ef.png)

## 2 问题分析

乱码发生原因，一般是因为发送方与接收方编码不一致。比如发送方是GB2312，而苍穹接收统一要求为UTF-8。

## 3 解决方法

那么如何才能保证不会乱码？

- 【可选】请求头中声明UTF-8编码 httpPost.setContentType("application/json;charset="UTF-8")；如果没设置则默认UTF-8。
- 【可选】如果没指定请求头则可以设置：httpPost.addHeader("Accept-Charset", "UTF-8");
- 【必须】确保http请求中的报文body，传送的是真UTF-8编码报文。如果不是UTF-8编码，可以通过以下语句进行转换：

StringEntity entity = new StringEntity(jsonData, "UTF-8");//解决中文乱码问题

entity.setContentType("application/json;charset="UTF-8");

httpPost.setEntity(entity);

注意事项：如果仅仅声明请求头中的utf-8编码，而正文body传送的编码不是UTF-8时不进行转换，还是会乱码。请求头只是声明编码格式，而真正传送的数据必须转换成相应的utf-8编码。

## 4 测试步骤

1）示例代码见附件TestUTF8Java.zip，resource下的gb2312json.txt是示例json报文，由gb2312进行编码。可以通过vscode或notepad++查看编码格式。

2）测试时请更改静态变量URL环境地址以及token。

3）打开开放平台的日志，路径：开放服务云 → OpenAPI → 监控统计 → API调用日志，看下入参是不是乱码。可以看到最近2条日志，一个是正常，一个是乱码。乱码的原因是：只是声明了请求头，报文body没有进行转码。

![](https://vip.kingdee.com/download/0109e7148b53ab3e4692b1238c144c127f5d.png)

![](https://vip.kingdee.com/download/0109126470f46ece407199f2cd6d2cb8ec76.png)
