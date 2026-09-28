---
title: "OpenAPI支持快速发布webservice接口"
entityId: "292625960673645824"
category: "用户手册"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/292625960673645824?productLineId=29&lang=zh-CN"
createdAt: "2022-03-18 11:51:06"
updatedAt: "2025-12-19 14:09:00"
views: 13603
---

# OpenAPI支持快速发布webservice接口

发布说明

发布版本：苍穹V4.0

适用范围：苍穹开放平台所有用户

上线日期：2021-03-10

补丁号：V4.0.017（BOS）

 更多内容

 变更记录

| 产品版本 | 更新内容 | 更新日期 |
| --- | --- | --- |
| V4.0.017 | 初始版本 | 2021年3月 |
| V6.0.1 | 应用更名为OpenAPI，迁移至开放服务云 | 2023年10月 |
| V7.0.1 | WebService支持urn=http://openapi.kingdee.com格式配置命名空间，生成wsdl中namespace的tag以urn开头 | 2024年10月 |

---

## 1 适用范围

OpenAPI支持将接口发布为WebService协议，支持SOAP1.1、SOAP1.2 协议标准。

服务发布方式如下：

- 低代码开发：使用配置的方式将操作对象发布操作API；
-
  高代码开发：用 JAVA代码可开发复杂的接口逻辑，并发布为自定义API。

## 2 操作API发布WebService

### 2.1 零代码配置操作API

以采购订单保存接口为例，维护API基本信息和请求参数等信息。

![](https://vip.kingdee.com/download/0109ea3f3b28676c4f618553059f7f734bb7.png)

### 2.2 维护WebService信息

- ‌命名空间（targetNamespace）‌：指定Web服务的命名空间，是Web服务的一个全局唯一标识符，用于确保Web服务的唯一性和可寻址性。
- ‌输入参数名‌：用于标识WebService接口的输入参数。
- 输出参数名‌‌：用于标识WebService接口的输出参数。
- ‌WSDL方法名‌：根据业务需求、功能描述定义Web服务的具体方法名，方便进行测试和管理。

![](https://vip.kingdee.com/download/010941f07387a5ad425da241c8d2bb5c45f2.png)

### 2.3 测试WebService接口

点击API测试按钮，即可快速测试接口。也可以导出WSDL，在接口测试工具如SOAPUI中进行测试。

![](https://vip.kingdee.com/download/010915be7a18bc7a4cd88a730c98c97576f0.png)

## 3 自定义API发布WebService

### 3.1 定义出入参实体类

为出入参定义 Java 实体类，可使用相应的注解标识字段描述及校检参数取数范围、是否必填等。

注：Java 实体类应继承 Serializable 接口

![](https://vip.kingdee.com/download/01003e868b730783429d968be883c079e5a4.png)

### 3.2 开发控制类 APIController

开发 XXController 类，并为类添加 ApiController 注解，为方法添加 ApiPostMapping或 ApiGetMapping 注解。控制类中可以调用苍穹微服务接口或业务服务逻辑。

![](https://vip.kingdee.com/download/0100bcd1ad758a934a74a2f3739d08cc3834.png)

### 3.3 配置自定义 API

路径：【开放服务云】 →【OpenAPI】 →【API管理】→ 【API开发】，点击“新增”按钮，添加 “自定义API”。

操作步骤：

1）选择所属应用，填写 API 编码及名称，API 分类。

2）在“类名”处输入你的控制类全路径名称，如：kd.bos.openapi.base.custom.demo.CustomDemoTestController 。

3）选择方法名（在 WebService 信息一节可以修改其命名空间）。

至此已将此 JAVA 代码发布为自定义 API。此时可以直接使用 Postman 测试 REST 协议的API。或使用 SOAP UI 测试 WebService 协议。

![](https://vip.kingdee.com/download/0109eba8ee260a3842c1af39e9d8d7a0c43b.png)

### 3.4 测试 API

点击API测试按钮，可快速调试、验证 API 逻辑是否正确。

![](https://vip.kingdee.com/download/010004bd221b04a54e08a6d323a791ebe420.png)

### 3.5 使用 SoapUI 测试 WebService

a) 查看WSDL

可点击 API 详情页的“测试”按钮获取完整 API 地址，API 完整地址为：http://苍穹服

务 URL/kapi/API 请求地址。如：http://localhost:8080/ierp/kapi/v2/ai/openapi/test2/getCustomTest

![](https://vip.kingdee.com/download/0100efdf0f11ef9a4f1f8faca2148a530ca2.png)

WSDL 地址为 API 地址后添加字符串“?wsdl”。但在浏览器中测试或在 SoapUI 添加 WSDL

时要先获取 token，请在 URL 后面添加：“&access_token=你的 token”。如：

http://localhost:8080/ierp/kapi/v2/ai/openapi/test2/getCustomTest?wsdl&acces

s_token=1134768014277739520_3gBxxxxx

b) 在SoapUI中添加Webservice 接口

将上一步带有 accesstoken 的 URL 添加为 WSDL。

![](https://vip.kingdee.com/download/01000cab9fab1e274f7da9ad7b010eee8966.png)

c) 在SoapUI中测试Webservice 接口

设置相应的请求参数，注意参数值的类型及值的合法性，并添加请求 Headers：

accessToken。点击测试按钮，测试是否返回正确的 SOAP 报文。

![](https://vip.kingdee.com/download/010009842cbf8d0d41a39e9379e49c592768.png)

## 4 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
