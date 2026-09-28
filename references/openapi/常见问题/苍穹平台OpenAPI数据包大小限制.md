---
title: "苍穹平台OpenAPI数据包大小限制"
entityId: "789500807736679680"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/789500807736679680?productLineId=29&lang=zh-CN"
createdAt: "2025-12-18 14:34:21"
updatedAt: "2025-12-18 14:39:02"
views: 960
---

# 苍穹平台OpenAPI数据包大小限制

## 1 问题描述

苍穹平台OpenAPI请求参数和返回参数的数据包大小限制是多少？

## 2 问题解答

OpenAPI请求参数和返回参数的最大限制为30M（含文件流）。

## 3 解决方法

私有云租户可通过MC参数调整报文限制（公有云不支持调整），参数如下：

OpenApi.MaxBodySize       修改默认最大请求报文大小（单位：字节），若调整为40M，则参数value为 41943040

OpenApi.MaxOutBodySize  修改默认最大返回报文大小（单位：字节）

OpenApi.FileItem.MaxSize  修改默认文件流最大报文大小（单位：字节）

特别注意：私有云用户遇到报文超过限制问题，建议优先通过**分批处理**的方式解决；若需调整 MC 参数，务必严格控制调整幅度，避免设置过高，否则在高并发场景下，可能引发内存占用异常飙升，进而导致进程内存溢出（OOM）故障，影响系统稳定性。

## 4 适用版本

金蝶AI苍穹V7.0.1及以上。
