---
name: kingdee-cosmic-dev
summary: 金蝶云苍穹（Kingdee Cloud Cosmic）开发知识库 —— 31,547 张物理表结构 + 144 篇 OpenAPI 开放平台官方手册，内置统一全文检索。
description: >-
  金蝶云苍穹（Kingdee Cloud Cosmic / 金蝶AI苍穹）开发指南，覆盖两大块内容：
  (1) 数据库 —— 31,547 张物理表结构（列名/中文名/类型/长度/精度/非空/默认值/备注枚举）、
  列规则与索引定义，覆盖财务、供应链、制造、人力、基础资料、平台等 267 个模块；
  (2) OpenAPI（开放平台）—— 144 篇官方手册，覆盖认证鉴权（AccessToken/JWT/摘要/基本/签名）、
  操作API、自定义API（Java插件/脚本/Servlet/文件流）、RESTful API、Webservice、
  开放事件、API 管理、限流与排错。
  当需要定位业务对象对应的物理表（如「销售订单」→ t_sm_salorder）、解释字段业务含义与枚举值、
  梳理主子表与多语言表关联、编写兼容 PostgreSQL 12 的金蝶规范 SQL；
  或对接/开发金蝶云苍穹 OpenAPI、获取 access_token、排查接口报错、
  开发自定义API插件、配置开放事件回调、使用 KingScript 时使用。
  全部内容可用内置统一检索脚本按关键词定位，无需逐个打开文档。
---

# 金蝶云苍穹开发指南

本 skill 由两大块构成，**全部内容都可用同一个检索脚本定位**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构（字段 / 列规则 / 索引） | 31,547 张表 / 267 模块 | [`references/db/`](./references/db/) |
| **块二 OpenAPI 手册** | 金蝶云社区开放平台官方手册 | 144 篇 / 8 分类 | [`references/openapi/`](./references/openapi/) |

> 数据库目标版本 **PostgreSQL 12**；OpenAPI 内容抓取自金蝶云社区专题
> 「OpenAPI（开放平台）」，原文链接保留在每篇文档的 frontmatter 中。

---

## 一、何时用本 skill

| 场景 | 去哪一块 |
|---|---|
| 业务术语 → 物理表名（「销售订单」是哪张表） | 块一：`search.py 销售订单` |
| 已知表名 → 字段清单、类型、枚举值 | 块一：`search.py t_sm_salorder --table --full` |
| 主子表 / 多语言表怎么关联 | 块一：检索到表后看 `### 表格列定义` |
| 写业务 SQL | 块一：检索定位 → 取字段与枚举 → 按第三节约定编写 |
| 调 OpenAPI 报错、拿不到 token | 块二：`search.py access_token --scope openapi` |
| 自定义API 插件怎么写 | 块二：`search.py 自定义API --scope openapi` |
| 开放事件 / 回调怎么配 | 块二：`search.py 回调 --scope openapi --category 开放事件` |
| 刚拿到一个环境，怎么接入（账套 / 凭据 / 登录） | **第五节 环境接入与排错** |
| 报错看不懂（401/403/404/603 分别是什么意思） | **第五节 5.3 错误码对照** |
| 想要个能跑的查询示例 | [`examples/salorder_query.py`](./examples/salorder_query.py) |

---

## 二、统一检索（核心用法）

```bash
PY="<你的 python3 路径>"
"$PY" "$SKILL_DIR/scripts/search.py" <关键词...> [选项]
```

`$SKILL_DIR` 指本 skill 根目录。常用示例：

```bash
# —— 块一 数据库 ——
"$PY" scripts/search.py 销售订单                              # 全库检索
"$PY" scripts/search.py t_sm_salorder --table --full           # 精确取完整字段表
"$PY" scripts/search.py 凭证 --scope db --category gl          # 只搜总账模块
"$PY" scripts/search.py 结算方式 --brief --limit 30            # 按字段中文名反查

# —— 块二 OpenAPI 手册 ——
"$PY" scripts/search.py 认证 --scope openapi                   # 搜开发手册
"$PY" scripts/search.py 自定义API --scope openapi --brief
"$PY" scripts/search.py 回调 --scope openapi --category 开放事件
"$PY" scripts/search.py getToken --scope openapi --full

# —— 导航 ——
"$PY" scripts/search.py --list                                 # 列出全部模块与分类
```

**选项**：`--scope db|openapi|all`（默认 `all`）· `--category C`（块一按模块、块二按分类过滤）·
`--table`（按表名精确匹配，仅块一；**默认返回完整字段定义**）· `--brief`（精简一行）·
`--full` / `-d`（完整正文）· `--all`（多词全命中）· `--limit N`（默认 20）·
`--max N`（非 `--full` 时正文上限，默认 1600）· `--list`

> 检索**直接读 Markdown**，不依赖预生成字典，因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
> 正文超长时，截取的是**关键词命中位置附近的片段**（不是从头截断），所以答案在文末也看得到。
> 全库检索约 2–4 秒（11,294 个文件 / 31,547 张表，瓶颈是打开上万个小文件）；
> 用 `--scope db --category <模块>` 限定范围会快很多。
> 修改文档后跑 `python scripts/build_index.py` 重建索引。

---

## 三、块一 数据库：写 SQL 前必读

1. **多语言表**：以 `_l` 结尾（如 `t_bd_account_l`），关联时需过滤 `flocaleid`
   （通常取当前语言，如 `WHERE flocaleid = 'zh_CN'`）。
2. **主从关联**：主表含 `fid`，分录/子表含 `fentryid`，通过 `fid`（或 `fparentid`）关联；
   另常见 `fpkid` 用于多语言表等特殊主键。
3. **枚举值**：字段的**备注**列通常直接写出枚举定义（如 `A: 暂存, B: 已提交`），
   编写 SQL 时应据此取值，不要臆造。
4. **通用字段**：`fid`、`fnumber`（编码）、`fname`（名称）、`fcreatetime`、`fmodifytime`、
   `fcreatorid`、`fmodifierid`、`flastupdatetime` 等在绝大多数业务表出现。
5. **表名前缀**：`t_<模块前缀>_<对象>`，模块前缀与 `references/db/<模块>_files/` 对应
   （如 `sm_` 销售、`pm_` 采购、`gl_` 总账、`bd_` 基础资料）。
6. **分表**：部分大表有 `_r` 后缀的分表（如 `t_pm_purorderbillentry_r`），注意与主表区分。

---

## 四、块二 OpenAPI：开发要点速查

> 以下为速查，细节以 `search.py --scope openapi --full` 返回的原文为准。

### 4.1 调用流程（三步）

```
注册第三方应用 → 获取 access_token → 携带 access_token 调业务接口
```

- **注册**：`【开放服务云】→【OpenAPI】→【第三方应用】`，填写系统编码、加密认证密钥。
- **取 token**：`POST /kapi/oauth2/getToken`（另有 `/kapi/oauth2/verifyToken`、`/kapi/oauth2/withdrawToken`）。
- **access_token 默认有效期 2 小时**，建议调用方定时缓存、快过期时刷新。
- 请求头携带：`access_token: {token}`、`Content-Type: application/json`、`charset: utf-8`。

### 4.2 五种认证方式

`AccessToken`（最广泛）· `JWT` · `摘要认证` · `基本认证`（最方便）· `签名认证`。
在【第三方应用】中为外部系统选择其中一种。

> V7.0.13 起增强型 Token / 摘要 / 签名认证支持多时区，时间戳传零时区。

### 4.3 业务接口地址规范

```
/kapi/v2/{isv}/{appId}/{serviceName}
```

- `isv`：开发商标识，**金蝶标准接口为空**
- `appId`：业务对象所属的应用编码
- `serviceName`：API 编码（自定义 API 由类中定义）

例：`http://{host}/kapi/v2/kdtest/basedata/bd_supplier/save`

### 4.4 服务类型

| 类型 | 说明 |
|---|---|
| **操作服务（操作API）** | 把单据/基础资料的查询、保存、删除、审核等操作快速发布为 API |
| **自定义服务** | 不依附业务对象，出入参完全自定义，逻辑用 Java 插件 / 脚本 / Servlet 实现 |
| **AI 服务** | 对接金蝶 AI 平台，把 AI 平台命令与插件适配 |
| **RESTful API** | 按 REST 风格设计与管理，支持 POST/DELETE 标准方法与自定义方法 |
| **Webservice** | SOAP 协议对接 |

### 4.5 统一响应契约

```json
{ "data": {}, "errorCode": "", "message": null, "status": true }
```

成功判定看 `status === true`；失败时看 `errorCode` 与 `message`。

### 4.6 操作API 的请求体：扁平结构（实测）

**这是最容易卡住的一步。** 苍穹 OpenAPI 操作API 的请求体是**扁平结构**，
分页参数在**顶层**，同时**必须带一个 `data` 键**（查询时传空对象即可）：

```json
{ "data": {}, "pageNo": 1, "pageSize": 20 }
```

两种写错的方式，报错完全不同，都很容易被误判成别的问题：

| 写法 | 报错 |
| :--- | :--- |
| 完全不带 `data` 键 | `400 请求参数没有 data 数据。` |
| 把分页参数塞进 `data` 里 | `400 页大小pageSize不能为空。` |

成功时返回：

```json
{"data": {"rows": [ {…}, {…} ], "pageNo": 1, "pageSize": 20,
          "lastPage": false, "filter": "[1 = 1]"}}
```

> 别被「扁平化出入参」这句话误导成「什么都不用包」——
> `data` 这层壳是必须的，只是**业务字段**和分页参数平铺在顶层。

查询操作API 的其它可用顶层参数：`filter`（如 `billno like 'SO%'`）、
`selectFields`（逗号分隔）。

> ⚠️ **`orderBy` 实测被静默忽略**：试了 12 种写法（`billno desc`、`fbillno desc`、
> `-billno`、`sortField`+`sortOrder`、JSON 数组…）全部返回 `code=0` 但顺序不变。
> 排序由 API 配置决定，运行时改不了。**这类「不报错但不生效」最危险**，
> 需要排序就在客户端做（参考 `examples/salorder_query.py --sort`）。

### 4.7 代理用户：第三方应用的隐藏必填项

第三方应用有个开关叫「**启用代理用户控制**」（V6.0.1 起支持，官方建议开启）。
开启后，`getToken` 里的 `username` **必须在该应用的「代理用户」列表里**，否则：

```
603  第三方应用（client_id）的代理用户为空或userName不在代理用户中。
```

注意这条报错和「用户名不存在」是**两回事**，别搞混：

| 报错 | 含义 |
| :--- | :--- |
| `代理用户为空或userName不在代理用户中` | 用户名**有效**，但没被授权给这个应用 |
| `username：用户无效或不可用` | 这个用户名在系统里**不存在** |

处理：【开放服务云】→【OpenAPI】→【安全策略】→【第三方应用】→ 该应用，
把 `username` 加进「代理用户」，或者关掉「启用代理用户控制」。

### 4.8 常见坑
| 现象 | 处理 |
|---|---|
| `access_token` 调用失败但 `accesstoken` 成功 | Nginx 版本较低，需设 `underscores_in_headers on` |
| 基础资料关联拿到的是内码不是编码 | 基础资料引用**默认使用 number 而非内码** |
| 接口超时 | 批量数据过大，参考「批量处理数据时接口超时问题」 |
| 高并发产生重复数据 | 参考「高并发时接口生成重复数据问题」与 API 幂等性规范 |
| 权限相关报错 | 操作API 按用户权限管控；**自定义API 需在插件中自行处理权限控制** |
| `403 该接口需要第三方应用授权` | 该 API 的「第三方应用授权」开关**打开**了，服务端在 `checkThirdACL` 里直接拒掉 cookie / 匿名认证。网页登录拿到会话也没用，必须用第三方应用的 `client_id`/`client_secret` 取 token |
| `400 请求参数没有 data 数据` | 请求体少了 `data` 键，见 4.6 |
| `400 页大小pageSize不能为空` | 分页参数塞进 `data` 里了，要放顶层，见 4.6 |
| `603 代理用户为空或userName不在代理用户中` | 应用开了「启用代理用户控制」，见 4.7 |

---

## 五、环境接入与排错（实测补充）

> 以下是官方手册**没覆盖**的平台级接入细节，为真实环境实测所得，供对接起步时参考。
> 具体接口与开关以目标环境实际配置为准。

### 5.1 三步接入

```
列账套（拿 accountId） → 建第三方应用（拿 client_id/client_secret） → 取 token → 调业务接口
```

**列账套**（无需登录，可直接调）：

```
POST /ierp/auth/getAllDatacenters.do
→ [{"accountId":"…","accountNumber":"<accountNumber>","accountName":"某账套"}, …]
```

`accountId` 就是 `getToken` 要传的那个。**「账套」= 数据中心 = accountId。**

**建第三方应用**：网页登录 → 【开放服务云】→【OpenAPI】→【第三方应用】→ 新增。
系统编码 = `client_id`，AccessToken 认证密钥 = `client_secret`。
这一步**只能在 UI 里做**，没有对应的开放接口。

### 5.2 只有网页账号密码时（应急）

官方手册没讲这条路径，实测契约如下：

```
POST /ierp/api/login.do
Content-Type: application/json
{"user": "<用户名>", "password": "<密码>"}      ← 键名是 user，不是 username
→ {"data":{"access_token":"<accountId>_<…>","KERPSESSIONID":"<同值>","success":true}}
```

`access_token` 与 `KERPSESSIONID` 同值，作为 Cookie 回传即可通过内部接口认证
（实测 `/ierp/kapi/v2` 用该 Cookie 能过认证关）。

⚠️ 但**仅当目标 API 的「第三方应用授权」开关关闭时**才能用它调业务接口；
开关打开时一律 403。所以网页会话只能用于调试，不能作为生产方案。

### 5.3 错误码对照（可用它反推路径对不对）

| errorCode | 含义 | 怎么用 |
| :--- | :--- | :--- |
| `401` | 未经授权的访问 | 没带 token / token 失效 |
| `403` | 该接口需要第三方应用授权 | **路径是对的**，但认证方式不合规 |
| `404` | `Cannot found OpenAPI(or disabled)` | **路径不对**：`appId`/`formId`/`serviceName` 组合错 |
| `405` | 请求方式不对 | 如 `getToken` 只支持 POST |
| `603` | 请求参数错误（会指明缺哪个） | 如 `client_id为空` |

> **实用技巧**：不确定某对象的查询 API 路径时，把候选路径挨个 POST 一次，
> **`403` 说明路径存在**、`404` 说明不存在 —— 比翻文档快得多。
>
> ⚠️ **前提：必须已认证。** 未认证时服务端在鉴权阶段就返回 `401`，
> 存在的路径和不存在的路径返回**完全一样**，据此判断会把不存在的路径误判成「存在」。
> 实测对比：
>
> | 路径 | 未认证 | 已认证 |
> | :--- | :--- | :--- |
> | `/kapi/v2/sm/sm_salorder/query` | 401 | **403**（存在） |
> | `/kapi/v2/sm/sm_salorder/list` | 401 | **404**（不存在） |
> | `/kapi/v2/sm/sm_salorder/save` | 401 | **404**（不存在） |

### 5.4 认证相关的其它探针

| 接口 | 用途 |
| :--- | :--- |
| `POST /ierp/auth/queryParameters.do` | 返回 `closeEncrypt`（密码是否需要加密）、`userSourceType` 等 |
| `POST /ierp/auth/isNeedDisplayVerify.do` | 是否需要图形验证码 |
| `POST /ierp/auth/getLoginErrorMessage.do` | 取上一次登录失败的原因 |

### 5.5 别高频试密码 / 试密钥

**登录接口**：连续多次失败后，会返回**含糊**的
「无法获取云通行证AccessToken，原因：远程服务不可用，或者用户名与密码不匹配」——
它既可能是密码错，也可能是**被限流**，还可能是环境连不上金蝶云。
写自动化脚本时务必退避重试，不要无脑循环。

**`getToken` 的 client_secret**：这条更硬 —— **连续 5 次密钥验证失败就锁定 180 秒**：

```
errorCode: 401
message: 不正确的第三方应用编码client_id或client_secret的访问错误已连续5次，
         该账号登录已锁定，请在180秒后再试。
```

报错里还会带一个递增的计数器（`第 N 次密钥验证失败`），可以用来观察自己消耗了几次机会。
**不要靠猜密钥** —— 它是长随机串，猜不出来，只会把应用锁住。

> **一个免费的诊断技巧**：用**第 1 次**尝试同时验证两件事。
> - 回 `第三方应用client_id：xxx在系统中不存在或未启用` → **client_id 写错了**
>   （这种错误在更早的阶段就被拦下，**不消耗**密钥尝试次数）
> - 回 `第三方应用（client_id）或AccessToken密钥（client_secret）不正确, 第 1 次密钥验证失败`
>   → **client_id 是对的**，只是密钥不对
>
> 也就是说：**只要看到「密钥验证失败」，就说明 client_id 已经验证通过了。**

### 5.5.1 nonce 必须每次不同

`getToken` 的 `nonce` 参数会被服务端记录，**重复使用会被拒**：

```
errorCode: 603
message: 本次参数nonce:1已经调用过了，不需要重复调用。
```

调试时如果为了省事把 nonce 写死，会误以为是自己参数写错了。每次都生成新的随机值：

```python
"nonce": uuid.uuid4().hex[:16]
```

### 5.6 可运行示例

| 文件 | 用途 |
| :--- | :--- |
| [`examples/kd_doctor.py`](./examples/kd_doctor.py) | **环境接入诊断**：连通性、账套、登录契约、取令牌接口、接口路径与授权开关，一键体检 |
| [`examples/salorder_query.py`](./examples/salorder_query.py) | 销售订单查询工具，含 `--probe` 探路模式 |

```bash
# 只做匿名检查（不碰账号，不会触发限流）
python examples/kd_doctor.py --base-url http://<host>:<port>

# 带凭据做完整检查（默认只登录 1 次，不重试）
python examples/kd_doctor.py --base-url ... --username admin --password ... --account-id ...

# 体检别人给的一个 token：常见摆放方式全试一遍，给明确结论
python examples/kd_doctor.py --base-url ... --token <AccessToken> --identity <x-acgw-identity>
```

用法与踩坑记录见 [`examples/README.md`](./examples/README.md)。

## 六、目录结构

```
kingdee-cosmic-dev/
├── SKILL.md                       # 本文件
├── README.md
├── LICENSE
├── scripts/
│   ├── search.py                  # 统一检索（块一 + 块二）
│   └── build_index.py             # 从 Markdown 生成各级 _INDEX.md
├── tools/
│   ├── html2md.py                 # HTML→Markdown 转换器（零依赖，块二用）
│   ├── fetch_manual.py            # 抓取金蝶云社区专题手册（块二）
│   ├── build_db_from_dict.py      # 数据字典导出包 → 表结构 Markdown（块一）
│   └── selftest.py                # 内容/检索完整性自检
├── examples/                      # 可运行示例
│   ├── salorder_query.py          #   销售订单查询工具（含 --probe 探路模式）
│   └── README.md                  #   用法与实测踩坑记录
└── references/
    ├── _INDEX.md                  # 总索引
    ├── db/                        # 【块一】数据库（来自官方数据字典导出 V5.0.011.0）
    │   ├── _INDEX.md              #   267 个模块统计概览
    │   └── <模块>_files/
    │       ├── _INDEX.md          #   本模块表清单
    │       └── <对象>.md          #   一个文件可含主表/分录/多语言表多个 ## 块
    └── openapi/                   # 【块二】OpenAPI 手册
        ├── _INDEX.md              #   分类目录
        ├── _source/               #   原始 JSON 存档 + 目录缓存
        └── <分类>/…/<标题>.md     #   144 篇手册正文（含 frontmatter 与原文链接）
```

---

## 七、内容维护

两块内容都是**从上游生成的，不是手写的**。

### 7.1 块一 数据库（数据字典导出包）

```bash
python tools/build_db_from_dict.py <数据字典导出.zip>    # 转换（自动清理过期文件）
python tools/build_db_from_dict.py <zip> --list          # 只看统计
python tools/build_db_from_dict.py <zip> --keep-stale    # 保留旧文件
python scripts/build_index.py                            # 重建索引
```

- 导出包结构：`<root>/<模块>_files/<对象>.html`（模块概览页 `index.html` 等会被忽略）。
- 转换会把单元格里指向其它表的 `<a>` 转成 Markdown 链接，
  例如 `[业务单元 bos_org](../base_files/bos_org.md)`，方便顺着关联摸过去。
- 源包不在仓库里（几十 MB），需要时从金蝶导出。

### 7.2 块二 OpenAPI 手册

```bash
python tools/fetch_manual.py            # 重新抓取（已存在的跳过）
python tools/fetch_manual.py --force    # 全部重抓
python tools/fetch_manual.py --render   # 不联网，用 _source/ 存档重新渲染
```

`fetch_manual.py` 会把原始 JSON 存到 `references/openapi/_source/`，
所以格式调整（改 `tools/html2md.py`）后可以直接 `--render` 离线重出，不必再联网。

### 7.3 改完必须跑自检

```bash
python tools/selftest.py                          # 基础 11 项（约 30 秒）
python tools/selftest.py --quick                  # 跳过逐篇文本比对
python tools/selftest.py --dict-zip <导出包>       # 额外校验块一 HTML→Markdown 保真
```

基础项校验「目录/存档/正文三方一致」「HTML 文本 100% 落在 Markdown 里」
「`--full` 返回完整正文」「267 个模块索引与表定义逐条一致」等。
带 `--dict-zip` 时额外跑 A5/A6：全量比对每个文件的表数/小节数/表格数，
并抽样**逐单元格**与源 HTML 对账。

---

## 八、免责声明

- **块一**：表结构整理自金蝶云苍穹数据字典导出，最终解释权归金蝶所有，请以实际数据库为准。
- **块二**：手册内容抓取自金蝶云社区公开专题，版权归金蝶所有，仅供学习与开发参考；
  文档内所有外链均指向原站，请以线上最新版本为准。
