---
title: "RESTful  API操作服务响应状态码及返回参数"
entityId: "818843535867457024"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/818843535867457024?productLineId=29&lang=zh-CN"
createdAt: "2026-03-09 13:51:52"
updatedAt: "2026-03-09 13:54:49"
views: 342
---

# RESTful  API操作服务响应状态码及返回参数

> **2xx（成功响应）**：请求被服务器成功处理并返回预期结果。 核心语义：客户端行为正确，服务器已按预期完成操作。
>
> **4xx（客户端错误）**：请求存在问题（语法错误、权限不足、业务规则违反等），服务器无法处理。 核心语义：错误由客户端行为导致，需客户端修正后重试。
>
> **5xx（服务器错误）**：服务器在处理合法请求时发生内部故障，与客户端请求无关。 核心语义：错误由服务器端问题导致，客户端可在服务器恢复后重试。

### 新增

#### 单条

##### 新增单据

**状态码 201**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 单据ID | 1 | 2184074116397546496 |
| 2 | create_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "create_time": "2025-04-08T07:16:45.750Z"
}
```

##### 新增分录

**状态码 201**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 分录ID | 1 | 2184074116397546496 |
| 2 | create_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "create_time": "2025-04-08T07:16:45.750Z"
}
```

#### 批量

##### 新增单据

**状态码 201（不允许部分成功）**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 单据ID | 1 | 2184074116397546496 |
| 2 | create_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "create_time": "2025-04-08T07:16:45.750Z"
}
```

**状态码 207 （允许部分成功）**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | summary | object |  | 摘要信息 | 1 |  |
| 1.1 | total_count | integer |  | 总数 | 2 | 3 |
| 1.2 | success_count | integer |  | 成功数量 | 2 | 2 |
| 1.3 | fail_count | integer |  | 失败数量 | 2 | 1 |
| 2 | results | object | Y | 结果 | 1 |  |
| 2.1 | id | string |  | 单据ID | 2 | 2327541153953529856 |
| 2.2 | billno | string |  | 单据编号 | 2 | unittest-00001 |
| 2.3 | index | integer |  | 索引 | 2 | 0 |
| 2.4 | success | boolean |  | 是否成功 | 2 | false |
| 2.5 | error_code | string |  | 错误代码 | 2 | fi.100001 |
| 2.6 | error_message | string |  | 错误信息 | 2 | invalid data string : |

```
{
    "summary": {
      "total_count": 3,
      "success_count": 2,
      "fail_count": 1
    },
    "results": [
      {
        "id": "2327541153953529856",
        "billno": "unittest-00001",
        "index": 0,
        "success": false,
        "error_code": "fi.100001",
        "error_message": "invalid data string :"
      }
    ]
  }
```

##### 新增分录

**状态码 201**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 分录ID | 1 | 2184074116397546496 |
| 2 | create_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "create_time": "2025-04-08T07:16:45.750Z"
}
```

### 更新

#### 单条

##### 全量更新/部分更新

**状态码 200**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 单据ID | 1 | 2184074116397546496 |
| 2 | modify_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "modify_time": "2025-04-08T07:16:45.750Z"
}
```

#### 批量

##### 全量更新/部分更新

**状态码 200（不允许部分成功）**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 单据ID | 1 | 2184074116397546496 |
| 2 | modify_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "modify_time": "2025-04-08T07:16:45.750Z"
}
```

**状态码 207 （允许部分成功）**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | summary | object |  | 摘要信息 | 1 |  |
| 1.1 | total_count | integer |  | 总数 | 2 | 3 |
| 1.2 | success_count | integer |  | 成功数量 | 2 | 2 |
| 1.3 | fail_count | integer |  | 失败数量 | 2 | 1 |
| 2 | results | object | Y | 结果 | 1 |  |
| 2.1 | id | string |  | 单据ID | 2 | 2327541153953529856 |
| 2.2 | billno | string |  | 单据编号 | 2 | unittest-00001 |
| 2.3 | index | integer |  | 索引 | 2 | 0 |
| 2.4 | success | boolean |  | 是否成功 | 2 | false |
| 2.5 | error_code | string |  | 错误代码 | 2 | fi.100001 |
| 2.6 | error_message | string |  | 错误信息 | 2 | invalid data string |

```
{
    "summary": {
      "total_count": 3,
      "success_count": 2,
      "fail_count": 1
    },
    "results": [
      {
        "id": "2327541153953529856",
        "billno": "unittest-00001",
        "index": 0,
        "success": false,
        "error_code": "fi.100001",
        "error_message": "invalid data string :"
      }
    ]
  }
```

### 删除

**状态码 200**

#### 单条

##### 删除单据

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 单据ID | 1 | 2184074116397546496 |
| 2 | delete_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "delete_time": "2025-04-08T07:16:45.750Z"
}
```

##### 删除分录

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 分录ID | 1 | 2184074116397546496 |
| 2 | delete_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "delete_time": "2025-04-08T07:16:45.750Z"
}
```

#### 批量

##### 删除单据

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 单据ID | 1 | 2184074116397546496 |
| 2 | delete_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "delete_time": "2025-04-08T07:16:45.750Z"
}
```

##### 删除分录

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 分录ID | 1 | 2184074116397546496 |
| 2 | delete_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "delete_time": "2025-04-08T07:16:45.750Z"
}
```

### 查询

**状态码 200**

#### 单条

##### 详情查询

> 响应结果数据以api所选字段为准

```
{
    ...
}
```

#### 批量

##### 列表查询

> 响应结果数据以api所选字段为准

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | pagination | object |  | 分页信息 | 1 |  |
| 1.1 | offset | integer |  | 起始位置（第一页从0开始） | 2 | 0 |
| 1.2 | limit | integer |  | 每页条数 | 2 | 10 |
| 1.3 | has_more | boolean |  | 是否还有下一页 | 2 | false |
| 1.4 | count | string |  | 返回数据的总条数 | 2 | 10 |
| 1.5 | total | string |  | 由Query参数with_total控制，为true返回总条数，为false返回-1 | 2 | -1 |
| 2 | data | object | Y | 数据 | 1 |  |

```
{
  "pagination": {
    "offset": 0,
    "limit": 10,
    "has_more": false,
    "count": "10",
    "total": "-1"
  },
  "data": [
    {
       ...
    }
  ]
}
```

### 状态变更

**状态码 200**

#### 单条

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string |  | 单据ID | 1 | 2184074116397546496 |
| 2 | modify_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": "2184074116397546496",
    "modify_time": "2025-04-08T07:16:45.750Z"
}
```

#### 批量

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | id | string | Y | 单据ID | 1 | 2184074116397546496 |
| 2 | modify_time | string |  | 操作时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 | 2025-04-08T07:16:45.750Z |

```
{
    "id": [
        "2184074116397546496",
        "2184074116397546488"
    ],
    "modify_time": "2025-04-08T07:16:45.750Z"
}
```

### 通用

**状态码 400**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error_class | string |  | 异常类 | 1 |  |
| 2 | error_code | string |  | 异常代码 | 1 |  |
| 3 | error_message | string |  | 异常信息 | 1 |  |
| 4 | timestamp | string |  | 时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 |  |
| 5 | stack_trace | string |  | 异常堆栈 | 1 |  |

```
{
    "error_class": "异常类。例如：kd.bos.open.v3.common.exception.RestApiException",
    "error_code": "fi.100001",
    "error_message": "invalid data string :",
    "timestamp": "2025-04-08T07:16:45.750Z",
    "stack_trace": "异常堆栈，通过OpenAPI系统参数开关`显示异常Stack`控制"
}
```

**状态码 404**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error_class | string |  | 异常类 | 1 |  |
| 2 | error_code | string |  | 异常代码 | 1 |  |
| 3 | error_message | string |  | 异常信息 | 1 |  |
| 4 | timestamp | string |  | 时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 |  |
| 5 | stack_trace | string |  | 异常堆栈 | 1 |  |

```
{
    "error_class": "异常类。例如：kd.bos.open.v3.common.exception.RestApiException",
    "error_code": "404",
    "error_message": "根据过滤条件找不到任何数据。",
    "timestamp": "2025-04-08T07:16:45.750Z",
    "stack_trace": "异常堆栈，通过OpenAPI系统参数开关`显示异常Stack`控制"
}
```

**状态码 409**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error_class | string |  | 异常类 | 1 |  |
| 2 | error_code | string |  | 异常代码 | 1 |  |
| 3 | error_message | string |  | 异常信息 | 1 |  |
| 4 | timestamp | string |  | 时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 |  |
| 5 | stack_trace | string |  | 异常堆栈 | 1 |  |

```
{
    "error_class": "异常类。例如：kd.bos.open.v3.common.exception.RestApiException",
    "error_code": "409",
    "error_message": "请求因查询到多条记录、数据重复或唯一性约束冲突而无法完成。",
    "timestamp": "2025-04-08T07:16:45.750Z",
    "stack_trace": "异常堆栈，通过OpenAPI系统参数开关`显示异常Stack`控制"
}
```

**状态码 500**

| **序号** | **参数名称** | **参数类型** | **多值** | **参数说明** | **层级** | **示例** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error_class | string |  | 异常类 | 1 |  |
| 2 | error_code | string |  | 异常代码 | 1 |  |
| 3 | error_message | string |  | 异常信息 | 1 |  |
| 4 | timestamp | string |  | 时间（yyyy-MM-dd'T'HH:mm:ss.SSS'Z'） | 1 |  |
| 5 | stack_trace | string |  | 异常堆栈 | 1 |  |

```
{
    "error_class": "异常类。例如：kd.bos.open.v3.common.exception.RestApiException",
    "error_code": "500",
    "error_message": "根据字段flexfield的值是[kingdeewin]找不到实体bos_flex_property中存在对应的基础资料。",
    "timestamp": "2025-04-08T07:16:45.750Z",
    "stack_trace": "异常堆栈，通过OpenAPI系统参数开关`显示异常Stack`控制"
}
```
