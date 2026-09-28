---
title: "RESTful API设计指南"
entityId: "743509706684845824"
category: "用户手册 / RESTful API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/743509706684845824?productLineId=29&lang=zh-CN"
createdAt: "2025-08-13 16:42:08"
updatedAt: "2025-12-18 14:00:57"
views: 2687
---

# RESTful API设计指南

# 1. 简介

本指南主要面向苍穹平台API开发者，是在设计RESTful API时遵循的指南。RESTful 是目前最流行的 API 设计规范，用于 Web 数据接口的设计（更详细的RESTful 规范可以参考[REST-API-Design-Guid](https://vip.kingdee.com/tolink?target=https%3A%2F%2Fgithub.com%2FHighflyer%2FREST-API-Design-Guide)e）。

我们强烈建议开发者在设计API时遵循这些设计原则，另外随着时间的推移，我们会不断完善本指南，帮助用户不断优化 API 设计，提供更好的API接入体验。

# 2 术语

下面是与 RESTful API 相关的非常重要的一些术语：

- **资源** - 资源是某个事物的对象或表示形式，它与某事物有一些关联的数据，和可以对其进行操作的方法集。例如，用户、商品和订单是资源，新增、查询、更新、删除是要对这些资源执行的操作。
- **集合** - 集合是指资源的集合，例如，products 是 product 资源的集合。
- **URI** - 统一资源标识符（Uniform Resource Identifier）是一个用于标识某一互联网资源名称的字符串，可以通过它定位资源，并对其执行某些操作。
- **端点** - 端点（Endpoint）是动词和 URI 的组合。例如：`GET /products`。
- **状态码** - 一个响应的状态由其状态码（<u>HTTP Status Code</u>）指定。

# 3 成熟度模型

REST API 成熟度模型的提出者 Leonard Richardson 将API的成熟度分为4个级别：

- **级别 0：仅使用 HTTP 作为通道**，未遵循REST原则。存在如get、set、add、delete 等命名的接口，没有基于资源的概念，GET 和 POST 方法也时常混用。- 示例：POST /api?action=createUser，通过请求参数区分操作。
- **级别 1：以资源为中心**，通过不同的URI标识资源，操作依赖单一HTTP方法（如POST或GET），通过URI路径或参数区分操作，状态码简单。- 示例：POST /users/create，通过URI参数区分操作。
- **级别 2：利用 HTTP 动作的语义**（如GET、POST、PUT、DELETE等），迈向RESTful设计。使用HTTP方法表明操作意图，结合标准化状态码，资源通过URI标识。- 示例：POST /user，POST请求表示新增，通过HTTP方法区分操作。
- **级别 3：超媒体控制**（HATEOAS，参见 HATEOAS - Wikipedia），除了返回资源的 JSON 等数据之外，还会额外返回一组 Link，这组 Link 描述了对于该资源可以做哪些操作，以及具体的操作方式。- 示例：{ "rel": "self", "href": "/users/123", "method": "GET" }，在响应中返回额外信息。

根据 REST 架构提出者 Roy Fielding 的定义，级别3是真正完全REST规范的API。但实践中，多数公开API达到级别2即满足需求。

# 4 核心设计规范

| 接口名称 | 接口名称需**清晰易懂**，直接点明核心用途（如 “查询用户详情”、“创建商品”），避免冗余、嵌套或模糊表述（如“商品新增创建操作” 这类冗余表述）。 |
| --- | --- |
| 接口描述 | 1. **明确接口核心功能**（如 “查询单个用户详情”“全量更新商品信息”）；2. 说明适用场景（如 “用于前端用户详情页数据获取”“用于商品信息完整替换”）。 |
| 请求方法规范 | 1. GET：查询资源 / 资源集合（如列表查询、单个资源详情查询）；2. POST：创建资源、非 CRUD 自定义操作（如提交、审核）；3. PUT：全量更新资源（需传递完整字段）；4. PATCH：部分更新资源（仅传递修改字段）；5. DELETE：删除资源。 |
| URI 规范 | 1. 全小写，资源间用下划线 “_” 连接；2. 常用CRUD操作**不建议在URI中出现动词，****资源路径用名词**，集合类建议复数（如`/products`“商品列表”、`/users/{user_id}`“单个用户”）；3. 只有非 CRUD 操作允许包含动词（如`/orders/{id}/submit`），仅限无标准 HTTP 方法匹配场景；4. 层级结构体现资源关系5. 不传递敏感信息（密码、令牌等）。 |
| 请求设计规范 | 1.Path 参数仅用于非敏感资源定位，2.Query 参数用于结果过滤、分页等，3.Header 参数传递认证、内容类型等信息；4.Body参数 仅在 POST/PUT/PATCH 请求中承载请求数据，更新操作需通过 Path 参数传资源标识。5.分页查询时需用 offset/limit 参数，响应返回 total、has_more 等分页元数据；6.所有请求 / 响应数据总大小不超 5MB，支持租户自定义报文大小上限。 |
| 错误码规范 | 1. 成功响应：200 OK（查询 / 更新）、201 Created（创建资源）；2. 客户端错误：400（参数无效）、401（未登录 / 令牌无效）、403（无权限）、404（资源不存在 / 路径错误）、405（方法不支持）、415（格式不支持）、429（请求超限）；3. 服务器错误：500（未知内部错误）、503（服务暂不可用）；4. 异常响应格式统一包含：error_class、error_code、error_message、timestamp、stack_trace（可选）。 |

## 4.1面向资源的设计

- URI 使用小写，路径中连字符和苍穹平台实体命名规则保持一致，使用下划线“_”；
- 面向资源设计，资源命名使用名词，如/user、/product；
- URI中表示资源的名词使用复数还是单数，没有统一的规定。若资源表示一个集合，建议使用复数，如列表查询 `GET /products`要好于 `GET /product` ；
- 使用层级结构表示资源关系（如/users/{id}），如GET /users/123，表示获取id 为123的用户。users是顶级资源，即 URI 中最外层的资源，某个实体的集合或单例。
- 避免多层嵌套冗余路径，建议资源层级最多不超过3层。

注意：针对非 CRUD 的自定义操作（如提交、审核等），允许 URI 包含动词，如/orders/{id}/submit（动词命名需统一），牺牲部分规范性来体现操作意图，仅限无法通过标准 HTTP 方法 + 资源路径表达的场景。

## 4.2 HTTP语义化设计

RESTful 的核心思想除了面向资源设计外，还有HTTP请求语义化，即使用以下五种 HTTP 方法，来对应对资源的 CRUD 操作。

- GET：查询资源或资源集合
- POST：创建资源
- PUT：全量更新资源
- PATCH：部分更新资源
- DELETE：删除资源

注意：针对非 CRUD 的自定义操作（如提交、审核等），若无匹配的标准 HTTP 方法，推荐使用 POST 请求。

## 4.3 请求响应设计

### 4.3.1 HTTP 请求构成

HTTP 请求需明确区分参数类型及用途，包含以下核心部分：

- **Path 参数**：用于资源定位，仅支持非敏感的资源标识信息。
- **Query 参数**：用于结果修饰（如过滤、分页），不承载核心资源定位逻辑。
- **请求头（Header）**：用于传递如认证令牌、内容类型等关键信息。
- **请求体（Body）**：用于承载复杂数据（如创建 / 更新资源的完整信息），仅在 `POST`/`PUT`/`PATCH` 等请求中使用。

### 4.3.2 Path 参数设计规范

- 唯一标识资源：目前默认通过 `{id}` 作为唯一资源标识，来定位单个资源（如 `/users/{user_id}`）。
- 资源层级：通过多级路径体现资源间的从属关系（如 `/departments/{dept_id}/employees/{employee_id}`），路径参数层级建议不超过 3 级（如`/a/{a_id}/b/{b_id}/c/{c_id}` ），避免 URL 冗长难以维护。

### 4.3.3 Query 参数设计规范

- 结果过滤：通过条件筛选资源（如 `?org_number=00&statue=C` 筛选特定组织下状态为 “已审核” 的资源）。
- 分页控制：使用GET请求进行列表查询时，由于查询结果记录数较多，必须使用分页参数（见下文 “分页设计规范”）。
- 列表查询场景设计：针对同一资源的列表查询，应使用唯一基础路径（如`GET /kapi/v3/资源`），通过组合不同查询参数（如状态、日期范围等）实现多场景过滤，而不是创建多个接口路径。
- 参数数量限制：单次请求的 Query 参数组合不宜超过 5 个，避免逻辑过于复杂。
- 避免敏感信息： 无论路径参数还是查询参数，均不应传递密码、令牌等敏感数据。

### 4.3.4 分页设计规范

- **分页参数（Query 参数）**`offset`：起始位置，即从第 N 条记录开始返回（默认值为 0，代表从第一条开始）。`limit`：每页最大记录数（建议设置默认值，如 20；目前最大值支持100000，但是不建议调整到最大）。
- **响应分页元数据** 响应报文在 `pagination` 字段中包含以下分页信息：`total`：符合条件的总记录数。`offset`：当前请求的起始位置（与请求参数一致）。`limit`：当前请求的每页记录数（与请求参数一致）。`has_more`：是否为最后一页（布尔值，便于前端判断是否显示 “下一页” 按钮）。

### 4.3.5 请求Body参数规范

- **请求体使用场景**`POST`：用于创建资源，请求体包含新资源的完整信息（无需在 URL 中传递资源标识）。`PUT`/`PATCH`：用于更新资源，其中`PUT` 适用于全量更新，请求体包含资源的完整字段，`PATCH` 适用于部分更新，请求体仅包含需修改的字段。资源标识传递：更新操作需通过 Path 参数传入唯一标识（如 `PUT /users/{user_id}`）。
- **数据大小限制**入参（请求体、Path/Query 参数总大小）和出参（响应体）均需 ≤ 5MB。支持租户级配置：通过 `open_rest_max_payload_size` 参数自定义单个租户的最大报文限制（优先级高于默认值）。

### 4.3.6 异常响应规范

当发生4XX或5XX错误时，响应参数规范如下：

```
{

"error_class" : "异常类。例如：kd.bos.open.v3.common.exception.RestApiException",

"error_code" : "fi.100001",

"error_message" : "错误消息",

"timestamp" : "2025-04-08T07:16:45.750Z",

"stack_trace" : "异常堆栈，通过OpenAPI系统参数开显示异常Stack控制"

}
```

## 4.4 状态码设计

客户端的每一次请求，服务器都必须给出回应。回应包括 HTTP 状态码和数据两部分。HTTP 状态码是一个三位数，苍穹平台RESTful API 响应HTTP状态码包含以下三类：

- **2xx（成功响应）**：请求被服务器成功处理并返回预期结果。 核心语义：客户端行为正确，服务器已按预期完成操作。
- **4xx（客户端错误）**：请求存在问题（语法错误、权限不足、业务规则违反等），服务器无法处理。 核心语义：错误由客户端行为导致，需客户端修正后重试。
- **5xx（服务器错误）**：服务器在处理合法请求时发生内部故障，与客户端请求无关。 核心语义：错误由服务器端问题导致，客户端可在服务器恢复后重试。

**2xx - 成功响应**

| **状态码** | **场景说明** | **业务示例** |
| --- | --- | --- |
| **200 OK** | 通用成功响应，服务器已成功处理请求并返回预期数据，适用于 GET（查询）、PUT（全量更新）、PATCH（部分更新）等操作。 | GET /users/123：成功返回 ID 为 123 的用户详情PUT /users/123：成功更新用户信息并返回用户ID |
| **201 Created** | 仅用于 POST 请求，标识资源被成功创建，服务器会返回新资源的详情 | POST /user：成功创建新用户，返回用户 ID 及信息 |

**4xx - 客户端错误**

| **状态码** | **场景说明** | **业务示例** |
| --- | --- | --- |
| **400 Bad Request** | 请求参数无效(如缺少必填、字段格式错误) | JSON 格式解析失败、必选参数缺失、参数类型错误（如数字字段传字符串） |
| **401 Unauthorized** | 用户未登录或令牌无效 | 客户端未携带令牌、令牌过期、令牌格式错误 |
| **403 Forbidden** | 用户没有权限访问某个资源 | 客户端尝试访问了无权访问的资源，如第三方应用无接口权限、代理用户无应用或资源权限 |
| **404 Not Found** | 请求的资源不存在或路径错误 | 客户端请求的资源不存在或URL 路径拼写错误或 |
| **405 Method Not Allowed** | 请求方法不支持 | 用 HEAD 调用创建接口（应使用 POST） |
| **415 Unsupported Media Type** | 请求体格式不支持 | 接口仅支持 application/json 却传入 application/x-www-form-urlencoded |
| **429 Too Many Requests** | 超过请求速率限制 | 短时间内频繁调用接口、API 调用次数超过租户配额 |

**5xx - 服务器错误**

| **状态码** | **场景说明** | **业务示例** |
| --- | --- | --- |
| **500 Internal Server Error** | 服务器内部未知错误（兜底） | 代码未捕获的异常、框架级错误 |
| **503 Service Unavailable** | 服务器暂时不可用（如维护、过载） | 服务器依赖的外部服务暂时不可用 |

常见状态码参考：

维基百科：https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81

互联网号码分配局：https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml RFC7231：https://datatracker.ietf.org/doc/html/rfc7231#section-6.2.1

# 5 异常处理规范

## 5.1 通用 REST API 异常类

- `kd.bos.open.v3.common.exception.RestApiException` 核心异常基类，构造时需明确传入 HTTP 状态码，规则如下：① 若异常由客户端参数错误、权限问题等可通过调整请求修复的情况引发，使用 **4xx 状态码**（如参数无效用 400，权限不足用 403）。② 若异常由服务器内部问题（如数据库连接失败、代码未捕获异常、第三方服务故障等）引发，使用 **5xx 状态码**（如未知错误用 500，服务暂不可用用 503）。③ `businessErrorCode`是业务错误码，格式推荐为 `应用ID.错误代码`（例如开放平台错误 `open.100001`），该错误码将随响应体返回，便于通过业务错误码字典快速定位问题。

## 5.2 特定 REST API 异常类

- `kd.bos.open.v3.common.exception.ResourceNotFoundException` 特定异常类，用于资源不存在场景（如请求的 ID 对应记录不存在），建议关联 HTTP 404 状态码。
- `kd.bos.open.v3.common.exception.InvalidRequestException` 特定异常类，用于请求参数无效（格式错误、缺失必选参数等）场景，建议关联 HTTP 400 状态码。

## 5.3 REST API 状态码枚举类

- `kd.bos.open.v3.common.http.HttpStatusCode`

# 6 结果处理规范

- 响应结果统一使用封装类： `kd.bos.open.v3.common.http.RestApiResponse`，确保客户端能通过固定结构解析成功 / 失败结果，简化对接逻辑。

# 7 最佳实践

## 7.1 标准方法

如需了解标准方法的最佳实践，请参考以下 AIP示例：

对于 GET 方法，请参考[标准GET方法 - 查询资源详情](https://developer.kingdee.com/knowledge/754643845081672448)、[标准GET方法 - 查询资源列表](https://developer.kingdee.com/knowledge/754649104336220928)

对于 POST 新增资源，请参考[标准POST方法 - 新增资源](https://developer.kingdee.com/knowledge/754650218427263488)

对于 PUT 全量更新资源，请参考[标准PUT方法 - 全量更新资源](https://developer.kingdee.com/knowledge/754651581559286272)

对于 PATCH 部分更新资源，请参考[标准PATCH方法 - 部分更新资源](https://developer.kingdee.com/knowledge/754652944724863744)

对于 DELETE 删除资源，请参考[标准DELETE方法 - 删除资源](https://developer.kingdee.com/knowledge/754655738114550528)

## 7.2 自定义方法

如需了解自定义方法，请参考[自定义方法 - 提交、审核资源](https://developer.kingdee.com/knowledge/754660607567262720)

# 8 更多资讯

关于OpenAPI的更多资讯，请随时关注[新特性公告](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=226337371640594944&id=226708319996323072&productLineId=29)。
