---
title: "OpenAPI扩展插件：KingScript使用说明"
entityId: "704264410990195712"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/704264410990195712?productLineId=29&lang=zh-CN"
createdAt: "2025-04-27 09:35:20"
updatedAt: "2025-12-19 14:22:56"
views: 5046
---

# OpenAPI扩展插件：KingScript使用说明

## 变更记录

| 产品版本 | 更新内容 | 更新日期 |
| --- | --- | --- |
| V7.0.9 | 初始版本 | 2025年3月 |

---

1 简介

### 1.1 使用须知

自苍穹7.0.9版本起，OpenAPI扩展插件已全面支持KingScript脚本引擎。若需了解原插件的编写及使用方法，请参阅以下指南：

- [API参数预处理](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=512935531722959360&type=Knowledge&productLineId=29&lang=zh-CN)
- [序列化出入参](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=512929770527401216&type=Knowledge&productLineId=29&lang=zh-CN)

在开始使用KingScript之前，请确保阅读了以下资源：

- [KingScript 脚本使用手册](https://vip.kingdee.com/knowledge/474603833067386624?productLineId=29&isKnowledge=2&lang=zh-CN&extInfo=%7B%7D#0)
- [KingScript开发助手 VScode插件用户手册](https://vip.kingdee.com/knowledge/611949903778113792?productLineId=29&isKnowledge=2&lang=zh-CN)<https://vip.kingdee.com/knowledge/611949903778113792?productLineId=29&isKnowledge=2&lang=zh-CN>

<https://vip.kingdee.com/knowledge/611949903778113792?productLineId=29&isKnowledge=2&lang=zh-CN>

### 1.2 功能介绍

OpenAPI现在允许用户在操作API、自定义API、脚本API中注册KingScript插件。通过编写这些插件，用户可以自定义API的入参和出参的序列化与反序列化过程，以适应特定的业务需求。

### 1.3 系统路径

【开放服务云】→【OpenAPI】→【API管理】 →【API开发】

## 2 主要操作

### 2.1 配置扩展插件

在OpenAPI中完成API的开发和注册后，用户可以点击“扩展插件”来进行配置。

![](https://vip.kingdee.com/download/01095c5c4307a04b464a920c741fbe656d93.png)

### 2.2 选择注册脚本

在脚本编辑器界面，点击“注册脚本”按钮创建新的脚本。

![](https://vip.kingdee.com/download/01094a206b6f7cab42df9f2effb156ce3ecb.png)

### 2.3 维护脚本信息

在弹出的窗口中，填写脚本的编码、名称及描述等基本信息。

![](https://vip.kingdee.com/download/010986a67c2a65144053b61ab1faa5492d83.png)

### 2.4 编写脚本

利用开发平台提供的编辑器编写插件脚本，以实现对API请求的入参和出参的干预。

![](https://vip.kingdee.com/download/0109b036f95ea86e4b4fb84a872f507500ea.png)

## 3 插件脚本示例

### 3.1 查询操作API

备注：状态变更类如提交、审核等操作API也可参考。

```
import { ApiQueryPlugin } from "@cosmic/bos-core/kd/bos/openapi/api/plugin";
import { ApiQueryOrderByModel } from "@cosmic/bos-core/kd/bos/openapi/api/model";
import { QCP, QFilter } from "@cosmic/bos-core/kd/bos/orm/query";
import { HashMap } from "@cosmic/bos-script/java/util";

class MyQuery implements ApiQueryPlugin {

//自定义查询过滤条件
    getFilter(qfilter: QFilter, map: HashMap): QFilter {
            return new QFilter("billstatus", QCP.equals, "A").and(qfilter);
    }
    //自定义排序
    getOrderBy(model: ApiQueryOrderByModel): string {
        let odb = model.getOrderBy(); //原排序规则
        let reqData = model.getReqData(); //请求入参
        let header = model.getReqHeaders(); //请求头

        return "id desc";
    }

}
let plugin = new MyQuery();
export { plugin };
```

### 3.2 保存操作API

```
import { ApiSavePlugin } from "@cosmic/bos-core/kd/bos/openapi/api/plugin";
import { List } from "@cosmic/bos-script/java/util";

class MySave implements ApiSavePlugin {

    preHandleRequestData(list: List): List {
        //业务逻辑处理
        let map = list.get(0);
        let usage = map.get("usage");
        map.put("usage", usage+"-经过MySave插件干预");
        return list;
    }

}let plugin = new MySave();
export { plugin };
```

### 3.3 反序列化入参插件

```
import { ApiDeserializerPlugin } from "@cosmic/bos-core/kd/bos/openapi/api/plugin";
import { JSONUtils } from "@cosmic/bos-core/kd/bos/util";
import { HashMap } from "@cosmic/bos-script/java/util";
//反序列化
class MyDeSerializerPlugin implements ApiDeserializerPlugin {

    deserializer(request: string, contentType: string): HashMap {
      let reqMap = JSONUtils.cast(request,HashMap);
      //以下为业务逻辑处理
      let data = reqMap.get("data");
      let param = data.get(0);
      let usage = param.get("usage");
      param.put("usage",usage+"-经过反序列化处理");
      return reqMap;
    }

}let plugin = new MyDeSerializerPlugin();
export { plugin };
```

### 3.4 序列化出参插件

```
import { ApiSerializerPlugin } from "@cosmic/bos-core/kd/bos/openapi/api/plugin";
import { SerializerResult } from "@cosmic/bos-core/kd/bos/openapi/api/plugin";
import { ApiSerializerVersion } from "@cosmic/bos-core/kd/bos/openapi/api/model";
import { ApiSerializerModel } from "@cosmic/bos-core/kd/bos/openapi/api/model";
import { OpenApiResult } from "@cosmic/bos-core/kd/bos/openapi/common/result";
import { JSONUtils } from "@cosmic/bos-core/kd/bos/util";
//序列化出参插件
class MySerializerPlugin implements ApiSerializerPlugin {

    serialize(response: object, accept: string, contentType: string): SerializerResult {        //取原出参信息
        let resp= <OpenApiResult> response;
        let message=resp.getMessage();
        let status=resp.isStatus();
        let data=resp.getData();
        let errorcode=resp.getErrorCode();
        //...业务逻辑处理

        return new SerializerResult("application/json", JSONUtils.toString(resp));
    }    //serializeByModel 方法，可以取到入参相关信息
    serializeByModel(model:ApiSerializerModel): SerializerResult {		//取入参信息
        let contentType = model.getContentType();//报文格式 json、xml、text
	let accept = model.getAccept(); //响应报文格式
	let reqData = model.getReqData(); //请求参数
	let response = model.getResponse();//返回参数
	//取原出参信息
        let resp= <OpenApiResult> response;
        let message=resp.getMessage(); //出参message
        let status=resp.isStatus(); //出参status
        let data=resp.getData(); //出参data域
        let errorcode=resp.getErrorCode(); //出参errorcode

        //...业务逻辑处理

        return new SerializerResult("application/json", JSONUtils.toString(resp));
    }

    getVersion():ApiSerializerVersion{
    //return ApiSerializerVersion.MODEL; //使用serializeByModel(model:ApiSerializerModel)方法返回
    return ApiSerializerVersion.DEFAULT; //使用serialize(response: object, accept: string, contentType: string)方法返回
    }

}
let plugin = new MySerializerPlugin();export { plugin };
```

## 4 更多资讯

<https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=386536775126291968&id=448792125560557568&productLineId=29>关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
