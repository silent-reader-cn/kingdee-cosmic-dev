---
title: "RESTful API 文档&测试"
entityId: "755465871337911040"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/755465871337911040?productLineId=29&lang=zh-CN"
createdAt: "2025-09-15 16:31:40"
updatedAt: "2026-09-18 17:18:34"
views: 1533
---

# RESTful API 文档&测试

# 1 简介

## 1.1 功能介绍

RESTful API 文档是基于 Swagger 格式生成的标准化接口说明文档，核心功能包括：

- 接口信息展示：完整呈现 API 的基本信息（名称、编码、所属应用）、请求配置（请求方法、资源路径、参数说明）、响应配置（HTTP 状态码、返回字段、示例值）及错误码说明，确保开发者清晰了解接口用法；文档与 API 模型实时同步，API 配置变更后文档自动更新，确保开发者获取最新接口信息。
- 在线测试支持：集成 Swagger 在线测试功能，开发者可直接在文档页面输入参数、发起模拟请求，查看实时响应结果，无需额外工具。

## 1.2 应用场景

为开发者提供清晰的接口说明（如 ERP 系统开发者对接采购 API 时，通过文档了解参数格式与响应逻辑），并快速完成接口调试。

## 1.3 系统路径

【开放服务云】→【OpenAPI】→【RESTful API】→【RESTful API文档】；

关联路径：在 RESTful API 管理列表，选中目标 API 后点击 “API 测试” 按钮，自动跳转至该 API 的 Swagger 文档页面。

## 1.4 按钮说明

【Authorize】：点击按钮，打开鉴权弹窗，在弹窗中输入获取的accesstoken值和x-acgw-identity（网关认证参数），方便在swagger文档页面快速进行API测试。

【try it out】：点击按钮，进入API调试模式，支持传入请求参数直接执行API。

# 2 主要操作

## 2.1 查看RESTful API文档

开发者需了解 API 的参数格式、响应逻辑或进行快速调试时，通过查看文档获取必要信息，确保接口对接效率与正确性。

- 单 API 文档：在 RESTful API 管理列表中，找到目标 API（如 “查询采购订单详情”），点击操作列的 “API 测试” 按钮，自动跳转至该 API 的 Swagger 文档页面；
- 全量文档：通过路径【开放服务云】→【OpenAPI】→【RESTful API】→【API 文档中心】，进入全量 API 文档页面，默认展示所有 “启用” 状态的 API。

首先筛选目标 API，若进入全量文档页面，通过顶部 “Select a definition” 下拉选择分组（如 “采购管理”），或在 “Filter by tag” 输入框中输入 API 名称 / 编码（如 “查询采购订单详情”），快速定位目标 API。点击 API 名称（如 “GET /pm_purorder/{id}”），展开查看详细文档内容。

核心信息：

- 基本信息：确认 API 的名称、所属应用及详细描述，判断是否为所需接口；
- 请求参数：查看 “Parameters” 区域，明确参数类型（Path/Query/Request body）、必填性及示例值；
- 响应参数：查看 “Responses” 区域，了解不同状态码下的返回字段。

![上传图片](https://vip.kingdee.com/download/0100ec3e29d433c54e1898bf197fd894193e.png)

## 2.2 在线测试

**1）维护Authorize认证相关参数**

点击 “Authorize” 按钮，在弹窗中输入有效的 access_token，点击 “Authorize” 维护认证参数。（若有接入网关，还需维护x-acgw-identity）。

![上传图片](https://vip.kingdee.com/download/0100f88df5145c464726938fdbcd315676e9.png)

**2）快速获取access_token和x-acgw-identity**

**路径：OpenAPI - 安全策略 - 第三方应用，**打开第三方应用清单，在列表勾选测试用的第三方应用，然后点击按钮【获取token】，维护第三方应用的Accesstoken认证密钥（即appSecret）,即可快速获取access_token。

![上传图片](https://vip.kingdee.com/download/0100485de5cd85f94cf780edc2dca5bceaa8.png)

同时可以**进入第三方应用详情**中，查看具体的网关认证参数：**x-acgw-identity的详细值**。

**3）测试RESTful API**

点击 “Try it out” 按钮，激活参数输入框，录入测试参数（如 Path 参数id输入 “2184074116397546496”）；

点击 “Execute” 按钮发起请求，查看 “Responses” 区域的实时响应结果（如响应状态码 200、返回采购订单的billno“org” 等数据），验证接口可用性。

![上传图片](https://vip.kingdee.com/download/0100b2d0a44b85404e3f80215d5be6d1d867.png)

# 3 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
