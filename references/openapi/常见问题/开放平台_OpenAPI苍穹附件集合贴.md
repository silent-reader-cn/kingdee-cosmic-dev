---
title: "开放平台/OpenAPI苍穹附件集合贴"
entityId: "654991151715398912"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/654991151715398912?productLineId=29&lang=zh-CN"
createdAt: "2024-12-12 10:21:00"
updatedAt: "2024-12-12 17:38:40"
views: 3523
---

# 开放平台/OpenAPI苍穹附件集合贴

## 1 概述

OpenAPI是自研的企业级API接口服务引擎，平台基于OpenAPI提供丰富的符合Restful 规范的API接口，全面覆盖各领域开放接口的使用场景，帮助企业快速接入外部第三方应用，连接用户、员工和上下游伙伴。目前第三方想要对苍穹附件进行增删改查，需要通过开放平台对外提供接口（自定义api）；OpenAPI分为V1.0和V2.0版本，不通版本处理方式也不一样

## 2 知识贴

OpenAPI2.0：

[自定义API（文件流处理）](https://vip.kingdee.com/link/s/lDywK)

[OpenAPI2.0实现上传附件到指定单据（附件面板和附件字段）](https://vip.kingdee.com/article/652511650938959104)

[OpenAPI2.0实现获取单据的附件信息（附件面板和附件字段）](https://vip.kingdee.com/article/652511650938959104)

[OpenAPI2.0实现获取（下载）附件并返回OpenApiFile](https://vip.kingdee.com/article/654734901064776960)

OpenAPI1.0：

[如何实现第三方系统远程查询苍穹系统内指定单据的附件信息](https://vip.kingdee.com/article/163327702105903872?productLineId=29)

[如何实现第三方系统远程下载苍穹系统内指定单据的所有附件](https://vip.kingdee.com/article/279250909165777664?productLineId=29)

[如何实现第三方系统远程上传业务单据&多个附件至苍穹系统](https://vip.kingdee.com/article/271698499203693056?productLineId=29)

## 3 注意事项

1、以上实现都是通过自定义API（JAVA）实现，也可以通过自定义API（Servlet）实现，业务代码都是一样的，只是开发部署的形式不一样；Servlet还支持批量上传附件，[自定义Servlet开发API接口](https://vip.kingdee.com/link/s/lDD10)

2、[【附件】AttachmentAction--API接口介绍](https://vip.kingdee.com/link/s/lKyPK)提供的.do接口（例如：preview.do、download.do），只能用login.do返回token进行认证调用，**增强型token不适用这些接口**

3、第三方想对苍穹附件进行处理，无特殊情况（苍穹版本过低、已上线使用登），推荐用OpenAPI2.0的方式进行附件的处理

## 4相关文档

[SDK（附件介绍）](https://dev.kingdee.com/open/detail/sdk/2077750775919948800)

[附件图片水印官网文档](https://vip.kingdee.com/knowledge/specialDetail/294832938980257024?productLineId=29&lang=zh-CN)

[如何根据单据获取附件信息](https://vip.kingdee.com/link/s/leNzj)

[附件字段如何删除和引用某个附件](https://vip.kingdee.com/link/s/ljxFC)

[如何在单据列表批量上传附件](https://vip.kingdee.com/link/s/lUtoR)

[如何二开实现批量下载附件](https://vip.kingdee.com/link/s/leNz5)
