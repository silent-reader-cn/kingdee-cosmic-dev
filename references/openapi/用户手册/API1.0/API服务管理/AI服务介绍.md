---
title: "AI服务介绍"
entityId: "221633800180961536"
category: "用户手册 / API1.0 / API服务管理"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/221633800180961536?productLineId=29&lang=zh-CN"
createdAt: "2021-09-03 14:13:36"
updatedAt: "2025-12-18 14:47:03"
views: 7032
---

# AI服务介绍

1 简介

1.1 功能介绍

AI服务是金蝶AI苍穹对接金蝶AI平台的一种特殊自定义服务，可以将AI平台的命令与插件适配，在调用API时执行对应的插件逻辑。

1.2 应用场景

1）发布苍穹AI服务接口供外部第三方应用调用；

2）预置标准AI接口，提供给苍穹其他模块调用。

1.3 操作路径

路径：【开发服务云】→【开放平台】→【其他】→【API1.0】→【API服务管理1.0】

1.4 字段/按钮说明

**字段解释**

| **字段名称** | **详细解释** |
| --- | --- |
| API服务信息 |  |
| 服务操作码 | AI服务编码 |
| 名称 | AI服务名称 |
| 所属应用 | AI服务所属应用 |
| 描述 | API详细描述及功能用途 |
| 匿名访问 | 设置API匿名，API不需要通过认证即可调用，但存在数据泄露风险，谨慎使用 |
| API高级信息 |  |
| 请求路径 | 请求url地址，自动生成，默认为/ai/do |
| 请求方式 | API请求方法，支持GET/POST |
| 内容格式 | 请求参数的内容格式，默认为application/json |
| 插件 | 具体API服务逻辑运行的地方 |
| AI命令 |  |
| AI命令操作码 | AI服务调用的标识，全局唯一 |
| AI名称 | AI名称 |
| AI命令描述 | AI命令的描述 |

**按钮解释**

| **按钮名称** | **详细解释** |
| --- | --- |
| 保存 | 保存AI服务信息 |
| 退出 | 退出当前弹窗界面 |

2 主要操作

2.1 开发AI服务插件

AI服务与自定义服务类似，主要处理逻辑都写在插件之中，所以也需要先开发插件，然后发布API。用户在开发插件可以使用自定义的java插件或脚本插件，不同的AI服务实现的效果和处理逻辑都有差异，但都会根据AI服务中的命令，去进行方法的调用和逻辑处理。

**AI服务插件代码示例：**

| import kd.bos.bill.IBillWebApiPlugin;import kd.bos.bill.events.AICommandEvent;import kd.bos.entity.api.AICommand;import kd.bos.entity.api.ApiResult;public class DemoAPIAIService implements IBillWebApiPlugin{@Overridepublic void doAICommand(AICommandEvent event) {// AI服务的请求，抽象成 AICommandAICommand command = event.getCommand();// 可以获取API请求中携带的参数Map<String, Object> parameter = command.getParameter();// 可以获取API请求中携带的APPIDString appId = Command.getAppId();// 具体业务逻辑// 返回数据ApiResult result = event.getResult();result.setData("success");result.setSuccess(true);}} |
| --- |

2.2 维护AI服务基本信息

打开【API服务管理】菜单，点击“新增”按钮，选择AI服务，进入到操作服务新增界面，录入API服务信息等字段。

![](https://vip.kingdee.com/download/0109ce770fc238754339a3fe0ad072e5bc28.png)

2.3  发布AI服务

在API高级信息的最下方插件栏，注册已经开发好的插件等信息，点击“保存”按钮，AI服务完成发布。

![](https://vip.kingdee.com/download/01003da1f2d7c39d449fa62a693014fa807f.png)

![](https://vip.kingdee.com/download/01003efce7b4427d49a9b8417e88b9574b9f.png)

2.4 服务访问

**请求地址**

• url：{{host}}/kapi/ai/do

**HTTP请求头**

• Content-Type：内容类型，目前默认为application/json

• accessToken：用户认证后的访问令牌，在请求头中传输

**请求body示例：**

| {"taskid":"1001","appid":"xxx","command":"xxxx","parameter":{key:value}} |
| --- |

**参数说明：**

| 参数名称 | 说明 |
| --- | --- |
| taskid | AI平台每次和业务系统交互的id（自动生成） |
| appid | 应用id（用户在某个场景下的具体目的，可指定对应的应用id，如果业务系统没有区分应用，可以忽略该参数） |
| command | 业务指令，即AI命令操作码 |
| parameter | 具体的请求参数 |

**POSTMAN 示例：**

| {"taskid": "1001","appid": "ISRM","command":"getFrontPeriods", "parameter":{ "periods": "本月" }} |
| --- |

![](https://vip.kingdee.com/download/01007a2b9faaab864aa3af4e422df82d83ec.png)

更多

[苍穹对话平台开发者指南](https://ai.kingdee.com/doc/#/)
