---
title: "脚本开发RESTful API"
entityId: "754667702886790144"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/754667702886790144?productLineId=29&lang=zh-CN"
createdAt: "2025-09-13 11:40:01"
updatedAt: "2025-12-11 19:24:29"
views: 1252
---

# 脚本开发RESTful API

## 1. 简介

## 1.1 功能介绍

脚本开发RESTful API用于处理复杂业务场景（如多系统数据联动、自定义业务逻辑计算、调用 Java 插件方法），适用于实体服务 API 无法满足的个性化需求（如查询物料可用量时需联动库存系统与采购系统数据，或自定义数据校验规则）。此类 API 不依附任何业务对象，请求/响应参数可完全自定义，灵活性更高。

注意：脚本开发RESTful API 虽然灵活度更高，但开发人员一定要遵循RESTful 规范，即资源导向和HTTP动作语义化，详见[RESTful API 设计指南](https://developer.kingdee.com/knowledge/743509706684845824)。

## 1.2 应用场景

使用脚本开发API，供外部第三方应用调用，解决复杂的API集成场景。

## 1.3 系统路径

【开放服务云】→【OpenAPI】→【RESTful API】**→**【RESTful API管理】

## 2. 主要操作

在 RESTful API 管理列表点击 “新增自定义脚本API”，进入自定义脚本 API 编辑页。

1. 维护基本信息：如名称、编码、所属应用、自定义分组、创建人、服务类型、请求/响应参数摘要模板、日志级别、详细描述等。
2. 请求端点配置：方法、资源路径、路由唯一标识、完整请求地址。注意：自定义脚本API灵活性较高，开发人员一定要遵循RESTful 规范设计API，并在脚本中自行保障API安全性。
3. 维护请求参数：用户可完全自定义Path路径参数、Query参数、请求体参数或请求头参数，遵循RESTful API成熟度规范，定义好的参数可以在自定义脚本中进行引用。
4. 编写自定义脚本：结合实际业务场景，维护API脚本，开发对应逻辑。产品中有脚本帮助手册提供参考。
5. 维护响应参数：展示不同HTTP状态码下的响应示例。请求成功时状态码为200-OK，返回参数根据需要，手工添加或通过Json导入。

### 2.1 新增自定义脚本API

![上传图片](https://vip.kingdee.com/download/0100ee5662afc0754cdfb25b0daaee27d810.png)

在自定义脚本API开发页面，输入资源路径，页面会生成API的完整请求路径。

![上传图片](https://vip.kingdee.com/download/010014f01172539746558472c5581be9e73d.png)

![上传图片](https://vip.kingdee.com/download/01008a826b25577f43c9937dfb152c0382d3.png)

### 2.2 POST请求（用户通过请求体传递参数）

请求体参数分录可以直接通过JSON导入，如入参示例JSON为：

```
{
    "order_id": "ORD202410230001",
    "order_status": "paid",
    "customer_info": {
        "customer_id": "CUST10086",
        "name": "张三",
        "phone": "13800138000",
        "email": "zhangsan@example.com",
        "vip_level": 2
    },
    "order_items": [
        {
            "product_id": "P1001",
            "product_name": "iPhone 15 Pro",
            "unit_price": 7999.00,
            "quantity": 1,
            "subtotal": 7999.00,
            "in_stock": true
        },
        {
            "product_id": "P2005",
            "product_name": "AirPods Pro",
            "unit_price": 1899.00,
            "quantity": 2,
            "subtotal": 3798.00,
            "in_stock": true
        }
    ]
}
```

导入后即能生成所有参数分录：

![上传图片](https://vip.kingdee.com/download/010067d01e9c4fa64cd09235b82303009492.png)

### 2.3 GET请求（用户通过query传递参数）

可在请求参数中，新增query参数id

![上传图片](https://vip.kingdee.com/download/01001262b1a6e8514bb3b1bc2a1b58237522.png)

则后续调用openapi时使用 ?id=xxx 传递。

### 2.4 维护成功响应体模型

响应体参数跟请求体参数模型一样，也可以通过JSON导入自动生成。也可以自行新增分录维护。

![上传图片](https://vip.kingdee.com/download/01003b362479bb0e47629e7de7f737ce0560.png)

### 2.5 编写脚本业务逻辑

- 脚本上下文预置变量：Path参数（$path_params）、Query参数（$query_params）、请求体（$body_params） ，可通过这些变量取值使用。
- 脚本上下文预置调用微服务函数：invokeMicroService2(cloudid, appid, servicename, method, params, proxyuser);

函数参数说明：

| **参数名** | **参数描述** | **参数类型** | **必填** |
| --- | --- | --- | --- |
| cloudid | 云ID | String | 是 |
| appid | 应用ID | String | 是 |
| servicename | 服务接口名称 | String | 是 |
| method | 方法名称 | String | 是 |
| params | 参数 | List | 是 |
| proxyuser | 代理用户（用户id或编码，调用微服务时会优先使用该值构造上下文 | String/Long | 否 |

- 编写自定义脚本逻辑，组装结果返回。如下图脚本所示，返回map结构，结构中包含id entry。

![上传图片](https://vip.kingdee.com/download/01008442d842007942a6ae7b1d68f7a29927.png)

标准微服务调用示例：

var result = invokeMicroService2("isc", "iscb", "IscTestService", "targetHandle", [$body_params], null);

注意：二开微服务的cloudid为二开工厂类的部署包路径，并以@isv结尾。

如示例脚本中登记的二开微服务工厂为

kd.isc.iscb.platform.core.isv.ServiceFactory

则调用脚本应该为

var result =

invokeMicroService2("kd.isc.iscb.platform.core.isv@isv","iscb","IscTestService", "targetHandle", [$body_params], null);

### 2.6 测试验证

![上传图片](https://vip.kingdee.com/download/01003dbdc26f51c84d398d4d9a7c8f9c8410.png)
