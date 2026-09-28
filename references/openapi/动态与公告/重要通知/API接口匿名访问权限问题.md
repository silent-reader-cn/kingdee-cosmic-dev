---
title: "API接口匿名访问权限问题"
entityId: "329557236689250560"
category: "动态与公告 / 重要通知"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/329557236689250560?productLineId=29&lang=zh-CN"
createdAt: "2022-06-28 09:42:48"
updatedAt: "2023-10-27 17:45:21"
views: 3228
---

# API接口匿名访问权限问题

发布说明

发布版本：苍穹V4.0

适用范围：苍穹开放平台所有用户

上线日期：2021-12-23

补丁号：V4.0.014（BOS）

 更多内容

 背景：金蝶AI苍穹API接口允许匿名访问，但若不控制权限则存在安全风险，会导致企业数据资产被恶意修改或删除。

新版本（BOS_V4.0.014）加强了企业数据安全管控，若通过匿名的形式，调用API保存操作等接口，则会提示error:oAuth认证失败，guest用户没有访问权限？

此时，若要匿名调用API接口，必须按照元数据配置或白名单配置匿名访问能访问的元数据范围（公共基础资料如币别不会限制匿名访问）。

方法1：设计器修改相关元数据的属性，勾选匿名访问；

![](https://vip.kingdee.com/download/0100b71fd212113e42edae509677b1c8820c.png)

方法2：mc增加租户级参数：security.meta.guestwhitelist，值为表单编码(小写逗号，分隔）;

注意：2种方法都有被非法访问的风险。

**更多资讯：**[API接口支持匿名访问](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=322033766435165696&id=119023921520783104&productLineId=29)
