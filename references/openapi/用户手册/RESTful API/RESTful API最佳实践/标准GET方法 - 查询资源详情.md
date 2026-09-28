---
title: "标准GET方法 - 查询资源详情"
entityId: "754643845081672448"
category: "用户手册 / RESTful API / RESTful API最佳实践"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/754643845081672448?productLineId=29&lang=zh-CN"
createdAt: "2025-09-13 10:05:13"
updatedAt: "2025-12-18 09:50:18"
views: 944
---

# 标准GET方法 - 查询资源详情

## 1 接口介绍

将业务对象（如采购订单、客户）的单条资源查询操作发布为RESTful API，通过资源唯一标识（如 ID）查询详情，支撑外部系统获取单条业务数据需求（如电商平台查询单个订单详情）。

## 2 接口示例

点击“快速创建”或“新增”按钮，新增详情查询操作的RESTful API，在详情页面维护API信息。

- **实体信息：**业务对象、操作类型和操作会根据创建向导中的配置自动带出，
- **维护基本信息：**名称：录入“查询采购订单详情”（需体现业务语义）；编码：系统自动生成，支持手工修改；所属应用：按业务对象关联自动带出；日志级别：默认记录基本日志，可选择 “详细日志”（记录出入参，便于故障排查）；详细描述：录入 “根据采购订单 ID 查询详情，包含单据编号、采购组织、物料明细等字段”。
- **请求端点配置：**方法：GET；资源路径：系统自动生成，支持修改；路由唯一标识：系统自动拼接；完整请求地址：系统自动拼接（如“[https://feature.kingdee.com:1026/deviai/kapi/v3/pm/pm_purorder/{id}”）。](https://feature.kingdee.com:1026/deviai/kapi/v3/pm/pm_purorder/{id}”）。)
- **维护请求参数：**仅需 Path 参数，默认为资源的唯一标识，也就是主键“id”，字段类型为 “long”，系统自动生成示例值。
- **维护响应参数：**选择 HTTP 状态码 “200-OK”，点击 “添加字段”按钮，勾选需返回的字段（如 “id”“billno”（单据编号）、“org”（采购组织）、“billentry”（物料明细））；补充示例值（如 “billno” 示例 “CGDD-250601-001”）。

![上传图片](https://vip.kingdee.com/download/0100f8aad1422b3b4f6894373bca122960f5.png)

![上传图片](https://vip.kingdee.com/download/0100cbc1e87fc1a2428bbe5a5d1345219e1f.png)

配置完成后，点击 “保存”并“启用”，API 可对外调用；用户在获取到请求令牌后，可通过完整请求地址，查询指定订单详情。
