---
title: "标准DELETE方法 - 删除分录"
entityId: "754664800713648640"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/754664800713648640?productLineId=29&lang=zh-CN"
createdAt: "2025-09-13 11:28:29"
updatedAt: "2025-12-18 09:52:13"
views: 832
---

# 标准DELETE方法 - 删除分录

## 1 接口介绍

将删除业务对象主资源下的子资源（如采购订单的“物料明细”分录）的操作发布为RESTful API，适用于外部系统调整主资源关联子资源的场景（如删除采购订单中错误的物料明细）。

## 2 接口示例

列表点击“新增”按钮，新增RESTful API，“操作类型选择“删除”，“操作选择“删除分录”。

- **实体信息：**业务对象、操作类型和操作会根据创建向导中的配置自动带出，手工选择需要删除的实体对象的分录标识，如物料明细（billentry）；
- **维护基本信息：**名称：录入“删除采购订单物料明细分录信息（需体现业务语义）”；编码：系统自动生成，支持手工修改；所属应用：按业务对象关联自动带出；日志级别：默认记录基本日志，可选择 “详细日志”（记录出入参，便于故障排查）；详细描述：手工录入，如“删除采购订单物料明细分录信息”。
- **请求端点配置：**方法：DELETE资源路径：系统自动生成，支持修改；路由唯一标识：系统自动拼接。完整请求地址：系统自动拼接。
- **维护请求参数：**Path 参数：id（主资源ID）、billentry_id（子资源ID），均为必填。
- **维护响应参数：**成功返回 “200-OK”，包含billentry_id和delete_time；异常返回 404（主资源 / 分录不存在）。

![上传图片](https://vip.kingdee.com/download/01002e23ee1147ed4c2fba9cea8b9f0b5cc1.png)

![上传图片](https://vip.kingdee.com/download/0100dde3269e69bd44079181c95f146ef148.png)

点击 “保存”及“启用”按钮，API 即可对外调用；用户在获取到请求令牌后，可通过完整请求地址，传入主键和分录id，即可完成删除指定分录操作。

注意：若需批量删除分录，请求方式改为“POST”，在请求Path参数中传入主资源id，同时还需要在请求体传入billentry_id列表，如{"billentry_id":["1747725418550","1747725418551"]}。
