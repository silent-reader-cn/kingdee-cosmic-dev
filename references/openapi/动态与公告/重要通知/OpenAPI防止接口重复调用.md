---
title: "OpenAPI防止接口重复调用"
entityId: "341958917577817856"
category: "动态与公告 / 重要通知"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/341958917577817856?productLineId=29&lang=zh-CN"
createdAt: "2022-08-01 15:02:39"
updatedAt: "2024-08-22 09:52:12"
views: 6804
---

# OpenAPI防止接口重复调用

## 变更记录

| 产品版本 | 更新内容 | 更新日期 |
| --- | --- | --- |
| V5.0.005 | 初始版本 | 2022年6月 |
| V6.0.12 | 允许自定义防重复参数的校验时间 | 2024年4月 |

---

1 简介

1.1 功能介绍

为防止API重复请求及网络问题导致网关重复发送请求包问题，可通过请求头参数控制：

- Idempotency-Key: 请求ID，客户端可指定随机数或业务单号；
- Idempotency-Timeout：超时时间（秒）- V6.0.12以上。

一定时间内同一API携带相同请求头参数的调用，只有第一次请求执行，其余请求皆不执行，接口返回604-重复请求。

* 限制：超时时间最大只支持90天，过期的数据会被清理，超过90天的数据不会再校验重复，在并发极高时，建议在数据库建立唯一索引。

1.2 应用场景

接口安全性要求较高，涉及到付款等操作，必须要进行重复调用校验。

1.3 系统路径

【开发服务云】→【开放平台】→【API管理】

2 主要操作

2.1 调用API服务

操作步骤

步骤1： 请求头增加防止重复调用参数： Idempotency-Key ，并传一个唯一值，通过POSTMAN调用接口。

![](https://vip.kingdee.com/download/0109c226cf9aa1a24b7da5c0fc3017b47663.png)

步骤2： 再次调用接口，触发重复调用校验。

![](https://vip.kingdee.com/download/01093c6214965c724b8eb5c378dfeaf6433d.png)

# 3. 更多资讯

请关注[开放平台新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072)的最新特性。
OpenAPI幂等性（API防止重复请求）使用说明.pdf
