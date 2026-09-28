---
title: "MCP服务介绍"
entityId: "783706444222381056"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/783706444222381056?productLineId=29&lang=zh-CN"
createdAt: "2025-12-02 14:49:37"
updatedAt: "2026-05-26 10:00:53"
views: 1017
---

# MCP服务介绍

## 1 功能介绍

苍穹MCP服务支持将苍穹REST API一键打包发布为MCP工具包，苍穹Agent或第三方AI工具通过标准协议实现标准接口的智能调用。

## 2 应用场景

通过该功能，企业能够使用AI自主调用苍穹标准接口，实现业务流程自动化运行。

## 3 系统路径

开放服务云>OpenAPI >MCP服务

## 4 关键字段/按钮说明

### 4.1 关键按钮说明

| 按钮名称 | 详细解释 |
| --- | --- |
| 获取URL | 获取MCP服务包的SSE服务地址 |

## 5 主要操作

MCP服务主要分为内部与外部两种：

- 外部MCP服务是将OpenAPI的RESTful API包装为MCP工具给第三方AI客户端进行调用。
- 内部MCP服务通过代码注解的方式将JAVA方法包装为MCP工具给苍穹AI Agent进行调用。

![上传图片](https://vip.kingdee.com/download/01002efc0e4d34d6499b8d20a99e7c8c097b.png)

### 5.1 创建外部MCP服务包

- **前提条件**

已经创建好了RESTful API

- **操作步骤**

*注：外部MCP服务需要依赖领域模型提供的MCP服务实例，可联系领域模型部门的曹勇老师提供镜像。*

-步骤1： 将领域模型提供的MCP服务实例镜像安装到服务器上，确保该服务器能被AI客户端和苍穹所访问。

-步骤2：将部署好的MCP服务实例地址配置到公共参数中，配置路径：公共设置>系统参数>OpenAPI参数>MCP服务地址。

![上传图片](https://vip.kingdee.com/download/01001637bca0ee5d45389bf1d874953e2749.png)

-步骤3：在MCP服务页面创建MCP服务包，可以选择多个相关业务领域的REST API包装为MCP工具。

![上传图片](https://vip.kingdee.com/download/0100720919d2d6b1421fb66aea6d15da64bb.png)

-步骤4：由于AI客户端调用MCP工具最后会透传到OpenAPI，所以鉴权机制还是沿用OpenAPI的。可以创建一个第三方应用，配置好访问策略，AI客户端也配置响应的ID与秘钥。此处以基本认证为例，需要将对应的秘钥配置到AI客户端的请求头中。

![上传图片](https://vip.kingdee.com/download/010095a3ece5a9a04ef39b6f0b771bd82b0f.png)

![上传图片](https://vip.kingdee.com/download/010000fd74c417fe4a62b58717357fa24afb.png)

- **后续操作**测试连接正常后可以同步拉取MCP工具，将MCP工具添加到智能体中便可进行自主调用。

### 5.2 创建内部MCP服务

- **操作步骤**

-步骤1： 内部MCP服务需要统一放到kd.bos.mcp.tools包名下才能扫描到，MCP注解方式参考下图：

![上传图片](https://vip.kingdee.com/download/01009fe06fb1e4804de4af91cce90fabac4d.png)

*注：服务编码格式为**isv_cloud_app_serviceCode，如果是标品的，默认isv为kingdee，然后是云，应用，服务编码。*

-步骤2：在苍穹Agent开发平台中新增内部MCP工具。

![上传图片](https://vip.kingdee.com/download/0100722e92ad505e43e7a985c336fee25931.png)

可以选择当前环境中已扫描到的内部MCP服务，系统将自动拉取该服务下的所有MCP工具。

![上传图片](https://vip.kingdee.com/download/0100a1c3cf63801d49149d926130e81d1b74.png)

![上传图片](https://vip.kingdee.com/download/01006ae3f2d17d804e1ba5d9c4996bc3a53a.png)

- **后续操作**在测试与启用工具后，便可以将工具添加到智能体中进行调用。

## 6 注意事项

AI调用工具存在一定安全风险，请勿将关键操作发布为MCP工具。

---

## 变更记录

| **产品版本** | **更新内容** | **更新时间** |
| --- | --- | --- |
| **V8.0.1** | 初始版本 | 2025年11月 |
| **V8.0.4** | 支持嵌入式MCP | 2025年12月 |
