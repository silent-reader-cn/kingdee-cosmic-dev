---
title: "金蝶AI苍穹OpenAPI调用流程"
entityId: "213309216805890816"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/213309216805890816?productLineId=29&lang=zh-CN"
createdAt: "2021-08-11 14:54:40"
updatedAt: "2025-12-19 10:04:35"
views: 333444
---

# 金蝶AI苍穹OpenAPI调用流程

**变更记录**

|产品版本|更新内容|更新日期|
|-|-|-|
|V4.0.006  |初始版本|2021年8月|
|V6.0.1  |应用更名为OpenAPI，迁移至开放服务云；第三方应用支持增强型Token认证|2023年10月|

---

## 1 适用范围
本文档为外部系统调用金蝶AI苍穹OpenAPI接口指南和流程。

## 2 调用流程
外部系统访问金蝶AI苍穹OpenAPI，首先需要通过第三方应用和苍穹用户（user）获取access_token，然后在请求头中携带access_token访问接口服务了。

备注：access_token中包含接口用户信息，操作API会根据用户权限对业务进行管控，自定义API需在插件中自行处理权限控制。
若access_token调用失败，但accesstoken调用成功，可能是Nginx版本较低的原因，需手动将Nginx中的underscores_in_headers 设为on。

![1.png](/download/010066181ed892ce4d29bc8fad018d5b5381.png)

### 2.1 注册第三方应用
路径：【开放服务云】→【OpenAPI】→【第三方应用】，点击“新增”按钮后，打开第三方应用新增界面，填写系统编码，AccessToken加密认证密钥等信息，点击保存按钮。

![2.png](/download/0100ba7020e8b9b540d4910624dc4b26dde4.png)

### 2.2 获取access_token

调用方根据第三方应用信息获取access_token，access_token默认有效期是两小时，详见[获取access_token](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=489812471545485056&productLineId=29)

（若苍穹版本低于V6.0.1，[获取access_token参考](https://vip.kingdee.com/article/491614364106171648?productLineId=29&isKnowledge=2)）

备注：接口调用状态根据参数status进行判断，若成功则为"true"，失败则为"false"。
当接口调用失败时，还会返回错误码ErrorCode。

![Image_20230918152739.png](/download/0100618a390f423d424c92e378abc63bd4e3.png)

### 2.3 调用服务

#### 2.3.1 操作服务
金蝶AI苍穹可直接将单据或基础资料的常用操作如查询、保存、删除、审核等快速发布为操作API，然后供第三方应用调用。请求头参数需要携带access_token（访问令牌）和content-type（内容格式）信息，按照规范的请求方式调用接口。
详见[操作API介绍](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=322414926260669696&id=263964194037744640&productLineId=29)

#### 2.3.2 自定义服务

自定义服务不依附任何业务对象，请求参数和响应参数可以完全自定义，主要处理逻辑通过Java插件、脚本或Servlet开发的方式实现，自定义服务主要用于处理特殊的集成场景。
详见[自定义API（Java插件）](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=358247193897143040&id=294499338368404736&productLineId=29)、[自定义API（脚本开发）](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=358247193897143040&id=322686880653270784&productLineId=29)

#### 2.3.3 AI服务
 AI服务是金蝶AI苍穹对接金蝶AI平台的一种特殊服务，可以将AI平台的命令与插件适配，并执行对应插件逻辑。详见[苍穹对话平台使用帮助](https://ai.kingdee.com/doc/#/)

#### 2.3.4 服务的共性
服务接口支持Http和Soap协议，存在如下共性特征：
① 请求的header中必须包括Content-Type（默认application/json）、charset（utf-8）的属性；请求头中须包含参数 access_token={accesstoken}；
③ 若接口涉及到基础资料引用，默认使用number而不是内码；
④ API Response最新统一契约为:

         {

            “data  { }                      //结果数据
            “errorCode”: “”,                //错误码
            “message”: null,                //失败时的提示信息
            “status”: true/false            //是否成功

         }

## 3 注意事项
- 第三方在调用API时，建议将access_token放在请求头中传递，可以有效提升安全性。
- 请求令牌的获取是有限制的，且默认有效期为 2 小时，建议调用方定时缓存access_token，在令牌快过期时，重新调用接口获取或调用刷新令牌接口延长有效期。
- 开发人员可以借助postman等API调试工具，对API功能进行完整测试后，再同调用方进行集成对接。
