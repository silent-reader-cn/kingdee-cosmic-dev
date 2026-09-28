---
title: "操作API支持自动提交并审核"
entityId: "563359453068652288"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/563359453068652288?productLineId=29&lang=zh-CN"
createdAt: "2024-04-03 13:49:20"
updatedAt: "2024-11-07 10:46:57"
views: 6312
---

# 操作API支持自动提交并审核

## 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V6.0.8 | 初始版本 | 2024年3月 |
| V6.0.8 | 新增工作流参数，支持自动审核时，不进入工作流 | 2024年6月 |

---

## 1 简介

1.1 功能介绍

苍穹平台保存操作API，支持使用用户级操作参数，数据会直接提交并自动审核。

1.2 应用场景

当发生API集成时，若在异构系统中单据已审核通过，新增同步到苍穹平台后，希望单据或基础资料状态同样为已审核，而不需要再进行人为干预，此时可以通过该功能，将单据或基础资料自动提交并保存。

若单据保存插件中含有复杂的单据金额计算逻辑，不推荐使用该功能，建议使用脚本API，分别对保存、提交、审核操作API，进行组合封装。

注意事项：

1. 配置forcedAudit 或forcedSubmit参数后，接口会将请求数据直接提交，而不是执行保存操作，若保存操作save插件中有额外的自动计算逻辑，此时不会触发！请谨慎使用并严格测试！！！

2. 配置forcedAudit参数后，接口只支持新增数据提交，不支持更新数据。

3. 若单据或基础资料配置了[流程服务](https://www.kingdee.com/products/cosmic_process_service.html?utm_source=shequ)云的工作流，只审核人通过消息中心手工审核，此时，若接口需要直接审核成功，那么在保存操作API的操作参数中，用户可手工新增参数“WF”，该参数可控制OpenAPI是否进入工作流，将该值设为false后，即可直接审核成功。

4. 由于是分两个事务执行操作，若单据审核失败，单据仍然会以提交状态，存在系统中，用户需要手工进行补偿，请慎重使用！如果需要自动补偿推荐使用脚本API和集成服务云服务流程。

1.3 系统路径

【开放服务云云】→【OpenAPI】→【API管理】 →【API开发】

2 主要操作

打开API管理列表，维护一个零代码配置的保存操作API。
![](https://vip-admin.kingdee.com/download/0109762aac39bce24edca93d324e08ecf65a.png)

维护完API基本信息、请求参数等信息后，需要用户手工维护操作参数，点击新增按钮，参数：forcedAudit，当值为 true 时，新增保存时会自动提交并审核单据。

![](https://vip-admin.kingdee.com/download/0109b2a487c207234af6bec2a16a2b58986d.png)

维护完成后点击API测试按钮，用户可以在线调试参数效果，单据在通过接口保存后，状态会自动变为已审核状态。

![](https://vip-admin.kingdee.com/download/010998981515bd694058b41e0c8d0a23ef2b.png)

![](https://vip-admin.kingdee.com/download/0109d5cd3d0fd8704049835e7cb2f05ff29b.png)

## 3 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
