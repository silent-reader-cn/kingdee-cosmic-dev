---
title: "OpenAPI扩展插件：序列化出入参"
entityId: "512929770527401216"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/512929770527401216?productLineId=29&lang=zh-CN"
createdAt: "2023-11-16 09:59:47"
updatedAt: "2026-01-08 19:11:28"
views: 15878
---

# OpenAPI扩展插件：序列化出入参

# 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V5.0.018 | 初始版本 | 2023年3月 |
| V6.0.8 | 序列化插件新增方法，支持获取全部参数 | 2024年4月 |

---

# 1 简介

## 1.1 功能介绍

OpenAPI支持在**操作API、自定义API、脚本API**中注册序列化插件，通过编写插件，可以根据具体业务场景自定义API的出参和入参的序列化和反序列化类。

## 1.2 系统路径

【开放服务云】→【OpenAPI】→【API管理】 →【API开发】

# 2 主要操作

## 2.1 反序列化入参

当接口传参时，可能存在请求头Content-Type类型为Text/plain，但OpenAPI暂没对这种类型的入参进行处理，那么此时可以编写反序列化插件进行入参的反序列化，拿到反序列化后的入参后，对入参进行干预。

![](https://vip.kingdee.com/download/0109a59d10aab62a41219c17896d395f9262.png)

1）首先，用户需要编写反序列化插件，在类中需实现对应接口，该方法中，request即为还没反序列化的原入参，处理逻辑是将原Text/plain类型的入参反序列化为map，然后进行入参干预处理，最后返回这个map给OpenAPI进行处理。

| 操作 | 接口 | 重写方法 |
| --- | --- | --- |
| 反序列化 | kd.bos.openapi.api.plugin.ApiDeserializerPlugin | deserializer |

```
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import kd.bos.openapi.api.plugin.ApiDeserializerPlugin;
import kd.bos.openapi.common.constant.MediaType;

import java.util.Map;

public class DemoApiDeserializerPlugin implements ApiDeserializerPlugin {
	private static final long serialVersionUID = 4568461229506221705L;

	@Override
	public Map<String, Object> deserializer(String request, String contentType) {
		try {
			if(contentType.contains(MediaType.TEXT_PLAIN)){
				//请求的text/plain类型反序列化为Map
				Map<String, Object> map = new ObjectMapper().readValue(request, new TypeReference<Map<String, Object>>() {});
				//干预入参
				Map<String, Object> data = (Map<String, Object>) map.get("data");
				data.put("billno","unittest-001");
				return map;
			}else if(contentType.contains(MediaType.APPLICATION_XML)){
				//XML格式反序列化逻辑
				return ...;
			}else {
				return ...;
			}
		} catch (JsonProcessingException e) {
			throw new RuntimeException(e);
		}
	}
}
```

2）接下来，回到OpenAPI应用，在API详情中注册并启用插件。

![](https://vip.kingdee.com/download/010980f50a5884a8402c8ff0e8850686ba9b.png)

3）最后，点击“API测试”按钮，打开在线测试弹窗，在系统中实时调试API功能，若插件执行生效，传Text文本时正常能正常解析入参并返回保存结果。

![](https://vip.kingdee.com/download/010957c606ddc11d40f1a627695ae57398df.png)

## 2.2 序列化出参

在实际的业务场景中，第三方需要接收的返回参数可能是特定的非JSON格式数据，如Text文本格式，结果不带引号，那么此时也可以通过编写序列化插件对出参进行个性化处理。

1）首先，仍然是编写插件，重写serialize方法。

| 操作 | 接口 | 重写方法 |
| --- | --- | --- |
| 序列化 | kd.bos.openapi.api.plugin.ApiSerializerPlugin | serialize |

其中参数response为还没序列化的原出参，这里逻辑直接重新返回一个自定义的字符文本。

**注意：序列化出参插件严禁直接抛出异常，需要用户自行处理并返回异常错误信息。**

```
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import kd.bos.openapi.api.plugin.ApiSerializerPlugin;
import kd.bos.openapi.api.plugin.SerializerResult;
import kd.bos.openapi.common.constant.MediaType;

public class DemoApiSerializerPlugin implements ApiSerializerPlugin {
	private static final long serialVersionUID = 1747368553053757065L;

	@Override
	public SerializerResult serialize(Object response, String accept, String contentType) {
		try {
			if (contentType.contains(MediaType.APPLICATION_JSON)) {
				//返回text文本
				String responseStr = new ObjectMapper().writeValueAsString(response);
				return new SerializerResult(MediaType.TEXT_PLAIN, "实际返回：" + responseStr);
			} else {
				//其他类型的出参序列化
				return ...;
			}
		} catch (JsonProcessingException e) {
			//处理异常时严禁抛出异常，可以定义自己的错误返回信息
			String result="...";
			return new SerializerResult(MediaType.TEXT_PLAIN,result);
		}
	}
}
```

2）接下来，用户需要注册插件并打开在线测试弹窗，在系统中实时调试API功能，若插件执行生效，则返回参数会从被替换成自定义的Text文本出参。

![](https://vip.kingdee.com/download/01094b780a317a6c4f2ba06cf79c3e014f9a.png)

补充说明：若用户在集成场景中需要获取全部参数，扩展插件也提供了以下序列化方法来获取更多参数。

```
	/**
	 * 模型参数序列化方法，提供更多参数信息
	 **/
	@Override
	public SerializerResult serializeByModel(ApiSerializerModel model) {
		String s = JacksonUtil.writeValueAsPrettyString(model.getResponse());
		return new SerializerResult(MediaType.APPLICATION_JSON, s);
	}

	/**
	 * 根据版本来决定执行那个序列化方法 (只需要实现相应版本的序列化方法即可)
	 * ApiSerializerVersion.DEFAULT -  执行 serialize 序列化方法（默认）
	 * ApiSerializerVersion.MODEL	-  执行 serializeByModel 序列化方法
	 **/
	@Override
	public ApiSerializerVersion getVersion() {
		return ApiSerializerVersion.MODEL;
	}
}
```

# 3 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
