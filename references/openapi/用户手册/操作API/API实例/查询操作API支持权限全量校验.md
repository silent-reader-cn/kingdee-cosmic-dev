---
title: "查询操作API支持权限全量校验"
entityId: "788778229871437568"
category: "用户手册 / 操作API / API实例"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/788778229871437568?productLineId=29&lang=zh-CN"
createdAt: "2025-12-16 14:43:05"
updatedAt: "2026-07-31 10:38:08"
views: 2303
---

# 查询操作API支持权限全量校验

## 变更记录

| **产品版本** | **更新内容** | **更新时间** |
| --- | --- | --- |
| **V8.0.4** | 提升查询操作API安全权限校验能力，增加受控基础资料权限控制和特殊数据权限 | 2025年12月 |

## 1 功能介绍

当前操作 API 在查询数据时，会默认校验用户的组织权限与数据规则，避免用户查询到权限范围外的数据。

本次我们对API权限控制能力进行了优化升级，使其安全机制更完善。优化后，查询过程可同时校验代理用户的组织权限、数据规则（含受控基础资料）及特殊数据权限。

**注意**：查询受控基础资料时，可通过请求头`X-BD-CTRL-ORGIDS`或请求参数`bos_bdCtrl_useOrgIds`传入使用组织信息。

## 2 应用场景

- 当用户想要OpenAPI具备更严格的实体查询权限控制，同时确保受控基础资料的数据规则可正常生效时，可开启该开关。
- 第三方客户端希望通过 API 查询受控基础资料时，能像前端页面操作一样指定业务组织，接口精准返回该组织下用户有权限查看的业务数据，如客户、供应商等。

## 3 系统路径

基础服务云 >公共设置 >参数设置 >系统参数

## 4 主要操作

### 4.1 打开查询API权限全量校验开关

路径：基础服务云 >公共设置 >参数设置 >系统参数。

在OpenAPI参数中，勾选开关【数据查询权限权利校验】，开关开启后，查询操作API的默认执行新的权限校验规则，将同时校验接口代理用户的组织权限、数据规则（含受控基础资料）及特殊数据权限。

![上传图片](https://vip.kingdee.com/download/010067f5a642c51c49b39093184cf8e1aba4.png)

### 4.2 列表查询受控基础资料

路径：基础服务云 >基础资料 >客户，进入客户列表页面，当前测试用户拥有两个业务组的权限，在不同组织下可查看的客户数据量存在差异。

![上传图片](https://vip.kingdee.com/download/010008d8e01554c742c8a885f559704d195a.png)

![上传图片](https://vip.kingdee.com/download/010013cd368f339a45bcbd56194930f5ef1f.png)

### 4.3 API查询受控基础资料

路径：开放服务云 >OpenAPI >API管理 >API开发。

接下来以客户为例，在OpenAPI应用下，新增一个查询客户列表接口。

![上传图片](https://vip.kingdee.com/download/0100a3d699de841c4f7999aafaa2787d1b92.png)

维护完成后，点击API测试，接口提示：“**使用组织参数[orgIds（bos_bdCtrl_useOrgIds）]为空**”，这是因为前面开启了公共设置的【数据查询权限权利校验】开关，调用方必须传入指定的业务组织。

![上传图片](https://vip.kingdee.com/download/0100faea18541cae46fa84fb57292bc299a9.png)

由于使用组织（业务组织）属于**虚字段**，未在实际业务对象中定义，因此无法在请求参数的【添加属性】面板中直接选中。针对这一情况，系统已做特殊处理，支持用户通过请求头（`X-BD-CTRL-ORGIDS`）、query 参数（`bos_bdCtrl_useOrgIds`）或请求体参数的方式传入该字段。用户也可通过手工新增的方式，在 API 中维护该字段，以便生成完整的 API 文档。

注意：通过POST进行查询时，请求体参数中将`bos_bdCtrl_useOrgIds`参数放在data对象中传入即可。

![上传图片](https://vip.kingdee.com/download/01009d187b2e332f4bcb8785dc064426cbb4.png)

传入后，即可模拟页面查询的方式，分别查看对应组织下的受控基础资料。

![上传图片](https://vip.kingdee.com/download/0100f1f67d27aa474be3977954e089e02dec.png)

![上传图片](https://vip.kingdee.com/download/0100f600c317db124875832b5989a45c6667.png)

### 4.4 获取有基础资料查询权的组织

路径：开放服务云>OpenAPI >RESTful API >RESTful API管理。

标准产品在提供了获取用户有权使用的组织的接口，方便第三方根据用户ID和应用ID，获取该用户对于特定的基础资料，有查询权的组织ID集合。

接口地址为：GET /ctrl_bd/query_perm/org

![上传图片](https://vip.kingdee.com/download/0100238b8e27320841ab959fca0792e488a0.png)

其中userId为接口代理用户的唯一标识id，entityId为业务对象的标识，appId为应用id，当用户传入任意值时，系统会按原始应用处理。

![上传图片](https://vip.kingdee.com/download/0100c0d7a421c9ca45d08ffc62afc7ff780a.png)

### 4.5 API测试特殊数据权限控制

路径：基础服务云 >安全管理 >权限管理 >特殊数据权限。

管理员为客户维护并启用特殊数据规则，仅创建人能查看客户基础资料。

![上传图片](https://vip.kingdee.com/download/010078657761822a4064bb5b8e0dd44c3207.png)

此时通过相同的接口，再次查询指定业务组织的客户，由于当前用户未创建任何客户资料，所以查询结果为空。

![上传图片](https://vip.kingdee.com/download/01005264d44e90c8495ca495325d46fc9059.png)

## 5 注意事项

- 当查询受控基础资料时，若当前用户要查询的受控基础资料有维护数据规则，则只允许传入一个业务组织。
- 新版 RESTful API 引擎，默认校验代理用户的组织权限、数据规则（含受控基础资料）及特殊数据权限。
- RESTful API仅支持通过请求头参数（`X-BD-CTRL-ORGIDS`）传入业务组织，不支持 query 参数或请求体参数的传入方式。

## 6 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&type=Knowledge&productLineId=29&lang=zh-CN)以及[金蝶AI苍穹OpenAPI接口规范](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=386536775126291968&id=448792125560557568&productLineId=29)。
