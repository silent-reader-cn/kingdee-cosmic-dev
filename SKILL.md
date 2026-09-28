---
name: kingdee-cosmic-dev
summary: 金蝶云苍穹（Kingdee Cloud Cosmic）开发知识库 —— 22,769 张物理表结构 + 144 篇 OpenAPI 开放平台官方手册，内置统一全文检索。
description: >-
  金蝶云苍穹（Kingdee Cloud Cosmic / 金蝶AI苍穹）开发指南，覆盖两大块内容：
  (1) 数据库 —— 22,769 张物理表结构（列名/中文名/类型/长度/精度/非空/默认值/备注枚举）、
  列规则与索引定义，覆盖财务、供应链、制造、人力、基础资料、平台等 224 个模块；
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
| **块一 数据库** | 全量物理表结构（字段 / 列规则 / 索引） | 22,769 张表 / 224 模块 | [`references/db/`](./references/db/) |
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
> 全库检索约 1–3 秒。修改文档后跑 `python scripts/build_index.py` 重建索引。

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

### 4.6 常见坑

| 现象 | 处理 |
|---|---|
| `access_token` 调用失败但 `accesstoken` 成功 | Nginx 版本较低，需设 `underscores_in_headers on` |
| 基础资料关联拿到的是内码不是编码 | 基础资料引用**默认使用 number 而非内码** |
| 接口超时 | 批量数据过大，参考「批量处理数据时接口超时问题」 |
| 高并发产生重复数据 | 参考「高并发时接口生成重复数据问题」与 API 幂等性规范 |
| 权限相关报错 | 操作API 按用户权限管控；**自定义API 需在插件中自行处理权限控制** |

---

## 五、目录结构

```
kingdee-cosmic-dev/
├── SKILL.md                       # 本文件
├── README.md
├── LICENSE
├── scripts/
│   ├── search.py                  # 统一检索（块一 + 块二）
│   └── build_index.py             # 从 Markdown 生成各级 _INDEX.md
├── tools/
│   ├── html2md.py                 # HTML→Markdown 转换器（零依赖）
│   ├── fetch_manual.py            # 抓取金蝶云社区专题手册
│   └── selftest.py                # 内容/检索完整性自检
└── references/
    ├── _INDEX.md                  # 总索引
    ├── db/                        # 【块一】数据库
    │   ├── _INDEX.md              #   224 个模块统计概览
    │   └── <模块>_files/
    │       ├── _INDEX.md          #   本模块表清单
    │       └── <对象>.md          #   一个文件可含主表/分录/多语言表多个 ## 块
    └── openapi/                   # 【块二】OpenAPI 手册
        ├── _INDEX.md              #   分类目录
        ├── _source/               #   原始 JSON 存档 + 目录缓存
        └── <分类>/…/<标题>.md     #   144 篇手册正文（含 frontmatter 与原文链接）
```

---

## 六、手册维护

内容是从线上抓的，不是手写的。需要更新时：

```bash
python tools/fetch_manual.py            # 重新抓取（已存在的跳过）
python tools/fetch_manual.py --force    # 全部重抓
python tools/fetch_manual.py --render   # 不联网，用 _source/ 存档重新渲染
python scripts/build_index.py           # 重建全部索引
```

`fetch_manual.py` 会把原始 JSON 存到 `references/openapi/_source/`，
所以格式调整（改 `tools/html2md.py`）后可以直接 `--render` 离线重出，不必再联网。

改完记得跑一遍完整性自检，确认没有悄悄丢内容：

```bash
python tools/selftest.py            # 全量自检（约 20 秒）
python tools/selftest.py --quick    # 跳过逐篇文本比对
```

它会校验「目录/存档/正文三方一致」「HTML 文本 100% 落在 Markdown 里」
「`--full` 返回完整正文」「224 个模块索引与表定义逐条一致」等 11 项。

---

## 七、免责声明

- **块一**：表结构整理自金蝶云苍穹数据字典导出，最终解释权归金蝶所有，请以实际数据库为准。
- **块二**：手册内容抓取自金蝶云社区公开专题，版权归金蝶所有，仅供学习与开发参考；
  文档内所有外链均指向原站，请以线上最新版本为准。
