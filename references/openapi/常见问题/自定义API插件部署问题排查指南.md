---
title: "自定义API插件部署问题排查指南"
entityId: "453492067319191552"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/453492067319191552?productLineId=29&lang=zh-CN"
createdAt: "2023-06-05 09:35:34"
updatedAt: "2025-12-18 15:19:45"
views: 3657
---

# 自定义API插件部署问题排查指南

## 问题描述

开发自定义API时需要确保相关的Java插件部署在相应应用节点的容器中，否则在生产环境由于分应用部署原因，在运行时无法找到相关API插件，导致API初始化失败。如下例所示：“找不到Java类，或无法初始化xxxxController”。

![](https://vip.kingdee.com/download/01099af0f86783484589afb979004047ecac.png)

## 排查指南

1） 查看此API，所属应用是否正确。例如财务应收模块的插件一般要选择相应的appId应为：ar – 应收，采购管理应用ID应为：pm。

备注：注意是否选到了扩展后的应用，如pm_ext，此时可能会路由不到，容器里默认只会配置标品的应用，如必须要选到扩展的应用，请容器里同步配置

2） 确保相应的Java插件，已打包部署到对应的业务JAR包中。

![](https://vip.kingdee.com/download/010945eaa5c61beb45839e15e8912260d504.png)

3）如果问题还无法排除，可查看Monitor以下属性 appIdsFromAppStore及 appIds，查看配置的appId是否正确，且BizLibs中配置加载了相关业务JAR包。如果配置有误，可让运维同事配置容器以下环境变量。

![](https://vip.kingdee.com/download/01090d3b10ebd2d24b4bba80ada921f92442.png)

开放平台自定义API插件部署指南.pdf
