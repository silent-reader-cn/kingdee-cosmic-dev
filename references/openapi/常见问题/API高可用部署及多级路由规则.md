---
title: "API高可用部署及多级路由规则"
entityId: "262143039974276608"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/262143039974276608?productLineId=29&lang=zh-CN"
createdAt: "2021-12-24 09:02:51"
updatedAt: "2025-12-29 10:49:54"
views: 1100
---

# API高可用部署及多级路由规则

发布说明

发布版本：苍穹V4.0

适用范围：苍穹开放平台所有用户

上线日期：2021-08-26

补丁号：V4.0.006（BOS）

 更多内容

## 1. 简介

我们知道，苍穹是微服务容器的调用方式，可以非常方便的进行弹性扩容伸缩容器。

针对api开放接口调用，当调用的QPS较高时，为了不影响正常的系统功能，可以按需部署微服务容器，

具体的容器路由规则如下：

## 2. 开放平台微服务节点查找规则

- 确认 API 配置核心属性：需先查看 API 所属应用，并由运维确认相关插件已部署至该应用节点对应的容器中（容器启动属性 BizLibs 需包含对应 JAR 包）。
- 路由匹配优先级（从高到低）：实体名 → 应用 Id-Api - api (常量) → 应用 ID（示例：ar/ap）→ bos (常量)。
- 补充备注：invokerAppids 格式示例为 [bos.fi.api.fi-api.gl](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fbos.fi.api.fi-api.gl)_voucher 或 [bos.fi.api.fi](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fbos.fi.api.fi)-api.custapi。

## 3. API 容器部署规则（4 种模式，按优先级排序）

1. 单实体 API 独立容器：将单个实体对象的 API 配置为独立容器，容器 appId 命名规则：
   - 零代码配置 API：[bos.fi.api.fi-api.gl](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fbos.fi.api.fi-api.gl)_voucher
   - 自定义 API：[bos.fi.api.fi](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fbos.fi.api.fi)-api.custapi
2. 全量 API 统一容器：所有 API 配置至同一个独立容器，容器 appId 固定命名为 api。
3. 单应用 API 独立容器：将某一应用下的所有 API 配置为独立容器，容器 appId 命名为 fiapi（需同步将 API 配置的所属应用设为 fiapi）。
4. bos 节点兜底：以上模式均不匹配时，默认路由至 bos 节点。

## 4. 苍穹微服务路由规则

1. 节点服务标识（APPID）：由`appIdsFromAppStore（XML配置）` + `appIds（运维容器配置）`共同决定。
2. 集群 APPID 匹配：优先匹配集群已注册的 registedAppIds 清单；若未匹配到，且已部署 custom 节点，则路由至 custom。
3. 容器 JAR 包配置（运维侧）：需在容器属性 BIZLIBS 中配置加载的 JAR 包清单，格式示例：hr.xml,ebg.xml,xxx.xml。

### 核心优先级总结

gl_voucher → fi-api → api → fi → bos

### 核心路由规则公式

bos.[appid].api.[实体 formId|custapi|aiapi|scriptapi]
