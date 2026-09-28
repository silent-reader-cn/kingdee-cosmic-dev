---
title: "API测试"
entityId: "626005170010472192"
category: "用户手册"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/626005170010472192?productLineId=29&lang=zh-CN"
createdAt: "2024-09-23 10:41:03"
updatedAt: "2025-12-19 14:08:21"
views: 7719
---

# API测试

## 变更记录

| 产品版本 | 更新内容 | 更新日期 |
| --- | --- | --- |
| V4.0.013 | 初始版本 | 2021年12月 |
| V7.0.1 | 增加Mock业务数据功能，支持将业务数据填充到参数示例 | 2024年10月 |

---

## 1 功能介绍

OpenAPI支持在线测试，模拟真实数据调用API服务。无需填写参数、URL，实动构造测试数据，一键进行测试，实时调试，方便快捷。

## 2 应用场景

开发人员在除生产外的环境使用在线API测试来快速测试和调试正在开发的API，帮助发现并修复代码中的错误和问题。当API出现问题或故障时，在线API测试工具可用于重现问题，帮助开发团队更快地找到问题的根本原因。

## 3 系统路径

【开放服务云】 → 【OpenAPI】 → 【API管理】 → 【API开发】

## 4 关键按钮说明

| 按钮名称 | 详细解释 |
| --- | --- |
| API测试 | 点击按钮，弹出API测试弹窗，只有测试环境展示该按钮（MC管理中集群类型为测试环境），生产环境不允许进行在线测试。 |
| 填充示例数据 | 点击按钮，弹出弹框，选择手工录入参数实例数据或选单填充参数示例数据 |

## 5 主要操作

### 5.1 在线测试

创建API服务，维护API基本信息、请求参数等信息后保存，点击“API测试”按钮，即可打开在线测试弹窗。点击“Send”按钮，即可实时调试API，支持JSON、XML、SOAP1.1、SOAP1.2四种报文格式。

![](https://vip.kingdee.com/download/0109befc16aad45649aeae4510216f1eb0a7.png)

若请求方式为Get，此时会将请求参数自动拼接在URL中。

![](https://vip.kingdee.com/download/010944b98cd3aa854bb590f709d54a24b989.png)

### 5.2 Mock数据

用于测试的请求参数数据，需要用户进行手工维护，但是当参数数量较多时，维护工作量较大，如保存操作API，动则近百个请求参数，此时可以使用填充示例数据，方便快速进入调试并生成准确的API文档。

点击“填充示例数据”按钮，点击“手工录单”。

![](https://vip.kingdee.com/download/01094845bd39fd3d4847985cc1c9b69b8357.png)

即可打开实体录入界面，快速录入数据，并将页面录入的数据，通过“返回数据”按钮，填充到接口的参数示例中。

![](https://vip.kingdee.com/download/010979cdad646c6a4fa29330b8bf802f52eb.png)

同时，也可直接勾选“选单”按钮，从已存在的业务数据中，选择一条，进行填充。

![](https://vip.kingdee.com/download/0109e52c1c8751f649e3afdc4909026c6fe6.png)

![](https://vip.kingdee.com/download/01098d01f05edb6c4b28bf89165d9cb9abc5.png)

### 5.3 参数控制

由于API在线测试会对环境中数据造成影响，所以不允许用户在生产环境进行在线测试。用户可在MC管理中心的集群管理中，维护集群的类型，若为测试环境和开发环境，可以直接进行在线测试。

![](https://vip.kingdee.com/download/01093b0227b07e1443baa2d6b790fc241085.png)

同时API测试支持模态和分屏两种模式，管理员可通过参数配置进行设置。路径：【基础服务云】 → 【公共设置】 → 【参数配置】 → 【系统参数】。

![](https://vip.kingdee.com/download/01093d18798e2c374b77a2d4d56e7406a10f.png)

## 6 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
