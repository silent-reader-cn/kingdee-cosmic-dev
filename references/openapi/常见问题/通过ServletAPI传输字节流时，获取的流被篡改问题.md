---
title: "通过ServletAPI传输字节流时，获取的流被篡改问题"
entityId: "742800435701891072"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/742800435701891072?productLineId=29&lang=zh-CN"
createdAt: "2025-08-11 17:43:44"
updatedAt: "2025-08-11 17:50:50"
views: 444
---

# 通过ServletAPI传输字节流时，获取的流被篡改问题

**1 问题描述**

当第三方系统需要通过 OpenAPI 的 ServletAPI 传输字节流并保存原始字节流时，若在请求头中设置`Content-Type: application/octet-stream`或其他类似的流式类型，会出现异常情况：在 OpenAPI 的入口处通过`HttpServletRequest`获取到的流已被篡改（具体现象可参考附图）。

![上传图片](https://vip.kingdee.com/download/01006c74eaf8ef354568a974aa6388d27c6c.png)

## 2 原因分析

平台基础服务存在默认处理机制：会将 API 请求默认按文本方式处理，此时会替换原始的`HttpServletRequest`对象，并对其进行字符集转换。这一过程会导致两个问题：

- 经过字符集转换后，获取到的流已不再是原始字节流；
- 流已被提前读取过一次，后续无法再次读取。

## 3 解决方法

可通过以下两种方式（二选一）设置请求头，确保传输原始字节流：

- 设置`Content-Type: multipart/XXXXX;`（XXXXX 为具体子类型）；
- 传递`kd-transfer-encoding: original`。

![上传图片](https://vip.kingdee.com/download/010068cf315c03ac472b94cbd2568fe5029e.png)

## 4 相关文档

[自定义ServletAPI开发API](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=358247193897143040&id=407938727974135040&type=Knowledge&productLineId=29&lang=zh-CN)
