---
title: "OpenAPI2.0脚本API支持删除分录"
entityId: "826454882831234816"
category: "用户手册 / 自定义API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/826454882831234816?productLineId=29&lang=zh-CN"
createdAt: "2026-03-30 13:56:39"
updatedAt: "2026-03-30 16:48:42"
views: 655
---

# OpenAPI2.0脚本API支持删除分录

### 变更记录

| **产品版本** | **更新内容** | **更新日期** |
| --- | --- | --- |
| 8.0.7（初始版本） | OpenAPI2.0提供API删除分录微服务 | 2026.03.25 |

### 一、背景

目前OpenAPI2.0操作API删除分录只在保存操作里加上参数控制 OverrideEntry 为 true，此参数会将原表单分录数据清除后追加分录，不能指定某行分录来删除，为此提供了脚本里调微服务的方式来支持此场景。

### 二、注意

- 目前不支持删除子分录行
- 仅支持根据主单ID和分录行ID删除，不支持候选键（请自行查出ID）

### 三、脚本API示例

##### 3.1 创建脚本API

集成的脚本编写，参考帖子最下面**附件dts文件**，通过API列表导入API，只需修改请求入参直接测试。

实际场景可通过脚本自行修改入参出参，注意**部分入参格式需固定**。

![上传图片](https://vip.kingdee.com/download/0100f77229d88bba44e28c7bcf2a5924af31.png)

##### 3.2 具体脚本编写

```
//取上面请求体入参，按需取，或直接是具体的标识，这样就不需上方配置入参
//如完全取入参的，下面四行固定不变（如果入参名称修改，需要同步修改这里的取值）
var entity_number=entity_number; //业务对象标识
var entry_key=entry_key; //需要删除分录的标识
var pk=pk;//主单ID
var entry_ids={entry_key+"_id":entry_ids};//分录行ID
​
//操作参数。（按需加，如：{"WF":"false"}不走工作流）
var option={};
​
//调微服务，此行固定不变
var res = MS.invokeService("kd.bos.openapi.servicehelper","open", "RestApiSdkService"
 , "deleteEntry",[entity_number, pk, entry_key, entry_ids, option]);
​
//构造需要的返回参数（需在下方返回参数配置）
//取上面微服务方法的返回
delete_time=res.delete_time;
id=res.id;
```

##### 3.3 测试

```
//入参
{
  "entity_number":"openapi_unittest",
  "entry_key":"entryentity",
  "pk":"2437121517801208832",
  "entry_ids":[
    "2437215221606027264"
  ]
}
//出参
{
  "data":{
    "delete_time":"2026-03-17 17:11:48",
    "id":[2437215221606027264]
  },
  "errorCode":"0",
  "message":null,
  "status":true
}
​
```

### 四、Java微服务调用示例

方法：[kd.bos.open](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fkd.bos.open).v3.core.service.impl.RestApiSdkServiceImpl#deleteEntry

```
import kd.bos.servicehelper.DispatchServiceHelper;
​
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
​
public class Test {
​
  public static void main(String[] args) {
    String entityNumber = "openapi_unittest"; //主单据标识
    Object pk = 2442795748608396288L; //主单ID
    Map<String, Object> body = new HashMap<>();//请求体
    String entryKey="entryentity"; //分录标识
    List<Object> entryIds = new ArrayList<>();//删除的分录行ID
    entryIds.add(2442795748613106688L);
    body.put(entryKey + "_id", entryIds);//固定KEY勿修改
    Map<String,String> option = new HashMap<>();//操作参数
    Map<String, Object> result = DispatchServiceHelper.invokeService("kd.bos.openapi.servicehelper", "open",
        "RestApiSdkService", "deleteEntry", entityNumber,pk,entryKey, body, option);
  }
}
```

脚本服务_删除分录demo(delete_entry_demo).zip
