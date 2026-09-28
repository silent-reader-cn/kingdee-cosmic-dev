---
title: "OpenAPI扩展插件：API参数预处理"
entityId: "512935531722959360"
category: "用户手册 / 开发指南"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/512935531722959360?productLineId=29&lang=zh-CN"
createdAt: "2023-11-16 10:22:41"
updatedAt: "2025-12-19 10:13:31"
views: 17642
---

# OpenAPI扩展插件：API参数预处理

## 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| V5.0.014 | 初始版本 | 2023年1月 |
| V6.0.8 | 扩展插件支持自定义查询操作API的出参排序 | 2024年4月 |

---

**1 简介**

**1.1 功能介绍**

OpenAPI支持在操作API中注册扩展插件，实现通过插件对查询、提交、审核等操作API的请求参数进行过滤，以及在保存API中通过插件进行入参的预处理。

**1.2 应用场景**

OpenAPI插件扩展可以根据业务场景定制化API的请求参数，不需要对整个API进行修改，降低开发成本，提升开发效率。

**1.3 系统路径**

【开放服务云】→【OpenAPI】→【API管理】 →【API开发】

**2 主要操作**

进行系统集成时，通过OpenAPI零代码配置的操作API，**若过滤条件不满足实际业务需求，可通过编写插件自定义过滤条件，来扩展查询API的功能。**

![上传图片](https://vip.kingdee.com/download/01001967cf2f1f7f40eea97dc8225a63c79a.png)

### 2.1 编写插件代码

不同操作插件类需要实现不同的接口，如下表：

| 操作类型 | 实现接口 |
| --- | --- |
| 查询 | kd.bos.openapi.api.plugin.ApiQueryPlugin |
| 保存 | kd.bos.openapi.api.plugin.ApiSavePlugin |
| 提交 | kd.bos.openapi.api.plugin.ApiSubmitPlugin |
| 反提交 | kd.bos.openapi.api.plugin.ApiUnSubmitPlugin |
| 审核 | kd.bos.openapi.api.plugin.ApiAuditPlugin |
| 反审核 | kd.bos.openapi.api.plugin.ApiUnAuditPlugin |
| 删除 | kd.bos.openapi.api.plugin.ApiDeletePlugin |
| 启用 | kd.bos.openapi.api.plugin.ApiEnablePlugin |
| 禁用 | kd.bos.openapi.api.plugin.ApiDisablePlugin |
| 非以上其他操作 | kd.bos.openapi.api.plugin.ApiCommonPlugin |

表 1 插件可实现接口

在插件中实现查询的接口，并重写getFilter方法，其中方法参数filter为原接口的过滤条件， reqData为原接口的请求入参。处理逻辑是返回一个新的过滤条件，即覆盖原过滤条件。

```
import kd.bos.openapi.api.plugin.ApiQueryPlugin;
public class DemoApiQueryPlugin implements ApiQueryPlugin {
  @Override
  public QFilter getFilter(QFilter filter, Map<String, Object> reqData) {
    return new QFilter("billstatus", QCP.equals, "B")
        .and(new QFilter("creator.name", QCP.equals, "fjp"));
  }
}
```

### 2.2 注册并启用插件

在API详情页面中找到扩展插件，注册并启用插件。

![上传图片](https://vip.kingdee.com/download/0100653a7e7b44014129b182286d9c362d70.png)

### 2.3 API在线测试

点击“API测试”按钮，实时调试API功能。若插件正常执行，则返回参数会根据新的过滤条件进行查询。

![上传图片](https://vip.kingdee.com/download/010061e3acf075ca454fa413747e16c01364.png)

对于**保存操作API**，因为保存并无过滤条件，所以重写的方法中只有一个原入参，可对这个入参进行预处理，具体方法如下。

```
public interface ApiSavePlugin extends ApiPlugin {
  /**
    * 请求参数处理
    * @param reqData 原请求参数
    * @return 处理后参数
    */
   default List<Map<String, Object>> preHandleRequestData(List<Map<String, Object>> reqData) {
     return reqData;
   }
}
```

注意，方法返回的值，数据结构必需与原入参的保持一致。

补充说明：若用户在集成场景中需要自定义查询API出参排序规则，扩展插件也提供了方法来实现该场景。

```
import kd.bos.openapi.api.plugin.ApiQueryPlugin;

public class DemoApiQueryPlugin implements ApiQueryPlugin {

	/**
	 * 自定义过滤
	 **/
	@Override
	public QFilter getFilter(QFilter filter, Map<String, Object> reqData) {
		return new QFilter("billstatus", QCP.equals, "B")
				.and(new QFilter("creator.name", QCP.equals, "fjp"));
	}

	/**
	 * 自定义排序
	 **/
	@Override
	public String getOrderBy(ApiQueryOrderByModel model) {
		return "createtime desc, number asc, id desc";
	}
}
```

## 3 更多资讯

<https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=386536775126291968&id=448792125560557568&productLineId=29>关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。<https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=358247193897143040&id=511857478473304576&productLineId=29>
