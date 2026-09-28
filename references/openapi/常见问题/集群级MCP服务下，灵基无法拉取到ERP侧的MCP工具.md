---
title: "集群级MCP服务下，灵基无法拉取到ERP侧的MCP工具"
entityId: "882309925832495360"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/882309925832495360?productLineId=29&lang=zh-CN"
createdAt: "2026-08-31 17:04:38"
updatedAt: "2026-09-15 19:32:54"
views: 382
---

# 集群级MCP服务下，灵基无法拉取到ERP侧的MCP工具

## 问题描述

灵基企业配置中心的【连接器配置】中，拉取不到指定的MCP工具，但该服务在AI套件或星翰的**集群级MCP服务**中正常存在。

![气球](https://cdn-vip.kingdee.com/statics/emotion/define/101.gif)误区澄清：集群级MCP服务不能依靠ERP某个数据中心的MCP服务状态，来判断服务是否发布，应以MCP网关扫描的**目标数据中心**的MCP服务状态作为依据（扫描数据中心和MCP注册状态可通过Monitor日志关键字**OpenApiMcpProvider**查询）。

![上传图片](https://vip.kingdee.com/download/01004bf7a6f622ca44f2a1ce67032daf5934.png)

## 解决方法

### 原因一：集群各数据中心的MCP服务不一致

**现象说明：**正常情况下，同一集群下所有数据中心的MCP服务由标品预置，数据应保持一致。但部分私有云环境中，集群内各数据中心升级脚本执行时序不同步，会引发MCP服务数据不一致。

**解决办法：**通过集群级MC参数"**openapi.mcp.accountId**"指定MCP网关扫描的目标数据中心，并确保该数据中心的MCP服务数据为集群内最准确的。注册完毕后，回到灵基后台，再次拉取MCP工具。

注意：参数修改完成后，需要**重启MCP节点**生效。

### 原因二：目标数据中心的MCP服务状态异常

**现象说明：被扫描的ERP数据中心内，MCP服务为待注册或已下架/失败这两种异常状态。**

**解决办法：**

1. 状态为【待注册】：无需手动操作，等待5分钟，由MCP网关完成自动扫描；

2. 状态为【已下架】：执行重置注册状态操作，等待5分钟，MCP网关自动扫描同步。

3. 状态为【失败】：进入 MCP 服务详情页查看失败原因。

- 若原因为 API 在当前系统不存在：该 MCP 服务无法发布；
- 若无失败原因：判定为 MCP 服务异常，执行重置注册状态，等待 5 分钟，由 MCP 网关自动扫描同步。

ERP侧正常注册发布后，回到灵基后台，再次拉取MCP工具。

### 原因三：目标数据中心中标品预置的MCP服务状态异常

**现象说明：**标品预置的MCP服务，脚本内服务状态不是待注册（UNPUBLISH）而是已发布（SUCCESS）。

**解决办法：**网关不会重复扫描已发布的 MCP 服务（除非重启MCP服务节点），因此标品脚本禁止预置已发布状态的MCP服务，需统一配置为待注册（UNPUBLISH）。
