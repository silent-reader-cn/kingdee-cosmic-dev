---
title: "匿名访问guest用户权限问题"
entityId: "376072785895906560"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/376072785895906560?productLineId=29&lang=zh-CN"
createdAt: "2022-11-03 18:18:59"
updatedAt: "2023-10-27 17:44:58"
views: 2545
---

# 匿名访问guest用户权限问题

# 问题分析

外部系统匿名访问苍穹服务，若不控制权限存在安全风险，第三方在获取到苍穹接口请求地址后，可以匿名的方式随意对数据进行增删改查，所以必须对匿名访问的代理用户guest进行权限管控。

# 问题描述

匿名访问调用POST请求，为什么提示error:oAuth认证失败，guest用户没有访问权限？

# 解决方法

匿名按照白名单和元数据配置限制guest用户能访问的元数据范围（公共基础资料如币别不会限制匿名访问）。

方法一：设计器修改相关元数据的属性，勾选匿名访问；

![](https://vip.kingdee.com/download/0109d383cd1446804fc48e0472dde89669d8.png)

方法二：mc增加租户级参数：security.meta.guestwhitelist，值为表单编码(小写逗号，分隔）。

# 适用版本

- BOS_V4.0.014

# 注意事项

- 2种方法都有被非法访问的风险，不建议接口使用匿名访问
