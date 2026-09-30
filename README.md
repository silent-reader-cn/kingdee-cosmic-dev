# kingdee-cosmic-dev

**金蝶云苍穹（Kingdee Cloud Cosmic / 金蝶AI苍穹）开发知识库与 AI Skill** —— 31,547 张物理表结构 + 144 篇 OpenAPI 开放平台官方手册，两块内容用一套全文检索脚本统一检索，另附可直接运行的接口对接示例。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Kingdee](https://img.shields.io/badge/Kingdee-Cloud%20Cosmic-green.svg)
![Tables](https://img.shields.io/badge/DB%20tables-31%2C547-orange.svg)
![Modules](https://img.shields.io/badge/modules-267-orange.svg)
![OpenAPI](https://img.shields.io/badge/OpenAPI%20docs-144-blueviolet.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB.svg)

---

## 这是什么

金蝶云苍穹二开 / 运维时最常查的两类资料，全部收在一处，**并且都能用同一个命令搜出来**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构（列名/中文名/类型/长度/精度/非空/默认值/备注枚举）+ 列规则 + 索引定义 | 31,547 张表 / 267 模块 | [`references/db/`](./references/db/) |
| **块二 OpenAPI 手册** | 开放平台官方手册：认证鉴权、操作API、自定义API、RESTful API、Webservice、开放事件、限流与排错 | 144 篇 / 8 分类 | [`references/openapi/`](./references/openapi/) |
| **示例工具** | 销售订单查询工具 + 环境接入诊断，**已在真实环境端到端验证** | 2 个脚本 | [`examples/`](./examples/) |

- 块一来自金蝶官方**数据字典导出 V5.0.011.0**（2026-09-28 导出），目标库 **PostgreSQL 12**；
  表定义里的跨表引用已转成站内 Markdown 链接，可顺着关联关系直接跳转。
- 块二抓取自金蝶云社区专题「OpenAPI（开放平台）」，每篇文档的 frontmatter 里保留了原文链接。

---

## 30 秒上手

```bash
git clone https://github.com/silent-reader-cn/kingdee-cosmic-dev.git
cd kingdee-cosmic-dev

# 不知道「销售订单」是哪张表？直接搜
python scripts/search.py 销售订单

# 已知表名，要完整字段定义？精确匹配 + 全量输出
python scripts/search.py t_sm_salorder --table --full

# 调接口报 access_token 错？搜手册
python scripts/search.py access_token --scope openapi

# 自定义API 插件怎么写？
python scripts/search.py 自定义API --scope openapi --brief

# 有哪些模块和分类？
python scripts/search.py --list
```

只依赖 Python 3（标准库），无需安装任何第三方包。

---

## 检索脚本用法

```bash
python scripts/search.py <关键词...> [选项]
```

| 选项 | 说明 |
| :--- | :--- |
| `--scope S` | 检索范围：`db`（数据库）\| `openapi`（开发手册）\| `all`（默认） |
| `--category C` | 块一按模块过滤（如 `gl`）；块二按分类过滤（如 `用户手册/常见问题`） |
| `--table` | 关键词按**表名**精确匹配（仅块一）；此时默认返回**完整字段定义**，避免上百字段的表被截断后当成完整定义 |
| `--brief` | 精简输出：仅一行摘要 |
| `--full` / `-d` | 输出命中条目的完整正文（不截断） |
| `--all` | 多个关键词需**全部**命中（默认任一命中即可） |
| `--limit N` | 最多返回结果数（默认 20） |
| `--max N` | 非 `--full` 时每条正文最多展示字符数（默认 1600） |
| `--list` | 列出全部数据库模块与手册分类 |

**设计要点**

- **Markdown 是唯一真相源**：脚本直接读 Markdown，不依赖任何预生成字典，
  不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- **块一精确到「表」**：一张表 = 一个 `## <中文名> t_<表名>` 块，多语言表（`_l`）、
  分录子表会被拆成独立条目。
- **块二截取命中位置**：正文超长时截取的是关键词附近的片段，而不是从头截断，
  答案在文末也看得到。
- 全库检索约 2–4 秒（11,294 个文件 / 31,547 张表，瓶颈是打开上万个小文件；用
  `--scope db --category <模块>` 限定范围会快很多，实测 0.5 秒）。

---

## 可运行示例

### `examples/salorder_query.py` · 销售订单查询工具

只读工具，走 OpenAPI 查询销售订单。**已在真实苍穹环境端到端验证通过。**

```bash
# 基本查询
python examples/salorder_query.py --base-url http://<host>:<port> \
    --client-id <系统编码> --client-secret <密钥> \
    --account-id <数据中心ID> --username <代理用户> --limit 20

# 过滤（实测支持 like / >= / > 等 SQL 风格表达式）
... --filter "billno like 'HSH%'"
... --filter "bizdate >= '2025-03-01'"
... --filter "totalamount > 5000"

# 排序（服务端不认排序参数，这里是客户端排序）
... --sort "totalamount:desc,billno:asc"

# 翻页取全量
... --all --limit 100

# 只看指定字段 / 看全部字段
... --fields "billno,customer_name,totalamount"
... --json

# 导出（.csv 带 BOM，Excel 打开不乱码；.json 原样）
... --export salorder.csv
```

实测输出：

> 已脱敏：主机地址、accountId、客户名、单据号替换为占位符，
> 结构、状态码、字段名、金额保持原样。

```
已获取 access_token（有效期默认 2 小时）
共返回 6 条（请求体：{"data": {}, "pageNo": 1, "pageSize": 6}）

（共 102 个字段，默认只展示 9 个关键列；加 --fields 可指定，--json 看全部）

单据编号                    单据状态  订单状态  业务日期      客户                          金额      审核日期
----------------------  ----  ----  ----------  --------------------------  ------  -------------------
SO-20250303-0296  C     K     2025-03-03  某供应链公司（JXS）    9600.0  2025-03-03 14:15:28
SO-20250303-0297  C     C     2025-03-03  某食品公司                0.0     2025-03-03 18:24:25
SO-20250303-0298  C     K     2025-03-03  某贸易公司（JXS）          4245.0  2025-03-03 14:15:28
```

> 查询接口默认返回 **102 个字段**，且基础资料已展开成 `customer_name` / `org_name` /
> `billtype_name` 这种，不用自己再关联。所以工具默认只展示 9 个关键列。

### `examples/kd_doctor.py` · 环境接入诊断

刚拿到一个环境时先跑它，把接入路上的坑一次性检出来：

```bash
# 匿名检查（不碰账号，不会触发限流）
python examples/kd_doctor.py --base-url http://<host>:<port>

# 带凭据做完整检查（默认只登录 1 次、不重试，避免触发限流）
python examples/kd_doctor.py --base-url ... \
    --username admin --password ... --account-id ... \
    --client-id ... --client-secret ...

# 探测候选接口路径（403=存在 / 404=不存在，需先认证）
python examples/kd_doctor.py --base-url ... \
    --probe-paths /ierp/kapi/v2/sm/sm_salorder/query,/ierp/kapi/v2/sm/sm_salorder/list

# 体检「别人给的一个 token」——常见摆放方式全试一遍并给结论
python examples/kd_doctor.py --base-url ... --token <AccessToken>
```

---

## 接入一个真实环境的踩坑清单

下面每一条都是**实测确认**的，官方手册没有覆盖或没讲清。完整版见
[`examples/README.md`](./examples/README.md)。

### 1. 三步接入

```
列账套（拿 accountId） → 建第三方应用（拿 client_id/client_secret） → 取 token → 调业务接口
```

**账套 = 数据中心**，可以匿名列全：

```bash
POST /ierp/auth/getAllDatacenters.do
→ [{"accountId":"…","accountNumber":"<accountNumber>","accountName":"某账套"}, …]
```

第三方应用在 **【开放服务云】→【OpenAPI】→【安全策略】→【第三方应用】** 里创建，
**只能在 UI 做**。系统编码 = `client_id`，AccessToken 认证密钥 = `client_secret`。

### 2. ⭐ 请求体是「内外两层」，`data` 键必须有

**这是最容易卡住的一步。** 请求体分内外两层，职责不同：

```json
{
  "data": { … },          ← 内层：业务入参，由每个 API 的配置决定
  "pageNo": 1,            ← 外层：通用分页/过滤参数
  "pageSize": 20,
  "filter": "…"
}
```

| 写法 | 报错 |
| :--- | :--- |
| 不带 `data` 键 | `400 请求参数没有 data 数据` |
| 分页参数塞进 `data` 里 | `400 页大小pageSize不能为空` |
| 业务必填参数放外层（如采购订单的 `billno`） | `603 参数【billno】必填` |

⚠️ **同名操作在不同对象上必填参数不同** —— 操作API 是**按业务对象逐个配置**的：

| 对象 | 路径 | 业务必填参数 |
| :--- | :--- | :--- |
| 销售订单 | `/kapi/v2/sm/sm_salorder/query` | 无（`data` 传 `{}` 即可） |
| 采购订单 | `/kapi/v2/pm/pm_purorderbill/query` | **`billno` 必填，且必须放在 `data` 里** |

文档说「扁平化出入参」，很容易理解成「什么都不用包」——结果这些写法全错。
**别假设 `/query` 的行为在对象之间通用。**

### 3. 代理用户是第三方应用的隐藏必填项

应用开启「**启用代理用户控制**」后，`getToken` 的 `username` 必须在其代理用户列表里。
注意这两条报错是**两回事**：

| 报错 | 含义 |
| :--- | :--- |
| `代理用户为空或userName不在代理用户中` | 用户名**有效**，但没授权给这个应用 |
| `username：用户无效或不可用` | 用户名**不存在** |

### 4. `getToken` 各阶段报错对照（按校验顺序）

看到哪条就知道走到哪一步了 —— 这个「**报错逐步推进**」的排查法很省时间：

```
client_id为空                                    ← 参数校验
  ↓
client_id：xxx在系统中不存在或未启用              ← 应用查找（client_id 错 或 账套不对）
  ↓
密钥验证失败, 第 N 次                             ← 密钥校验（说明 client_id 已通过！）
  ↓
代理用户为空或userName不在代理用户中              ← 代理用户校验（说明凭据全对！）
  ↓
username：用户无效或不可用                        ← 用户校验
  ↓
成功
```

⚠️ **密钥连续失败 5 次会锁定 180 秒**，不要靠猜。

### 5. ⚠️ 排序参数被静默忽略

`orderBy` 试了 **12 种写法**全部无效，而且**全部返回 `code=0`**（不报错、顺序不变）。
排序由服务端 API 配置决定，运行时改不了。

**这类「不报错但不生效」最危险** —— 调用方看到成功码就以为排序生效了。
需要排序请在客户端做。

### 6. 第三方应用按数据中心（accountId）隔离

同一个 `client_id` 换一个账套就报「不存在或未启用」。
**报错说的是 A，原因可能是 B** —— 看到「凭据不存在」先确认账套对不对。

### 7. 错误码对照（可用于反推接口路径）

| errorCode | 含义 |
| :--- | :--- |
| `401` | 未经授权的访问 |
| `403` | 该接口需要第三方应用授权（路径**对**，认证方式不合规） |
| `404` | `Cannot found OpenAPI` —— 路径**不存在** |
| `405` | 请求方式不对 |
| `603` | 请求参数错误（会指明缺哪个） |

> **前提**：用 403/404 反推路径**必须已认证**。未认证时所有 kapi 路径都返回 401，
> 存在与不存在的路径返回完全一样，据此判断会得出错误结论。

### 8. 只有网页账号密码时（应急）

```
POST /ierp/api/login.do
{"user": "<用户名>", "password": "<密码>"}      ← 键名是 user，不是 username
```

但**仅当目标 API 的「第三方应用授权」开关关闭时**才能用它调业务接口，
开关打开时一律 403。所以网页会话只能用于调试，不能作为生产方案。

---

## 索引重建

`references/**/_INDEX.md` 全部由脚本从 Markdown 派生，**请勿手工编辑**：

```bash
python scripts/build_index.py          # 全量重建
python scripts/build_index.py gl som   # 只重建指定数据库模块
```

---

## 自检（内容完整性与检索完整性）

内容是从上游生成的，所以仓库自带一套审计脚本，用来回答「有没有悄悄丢内容」：

```bash
python tools/selftest.py                          # 基础 11 项（约 30 秒）
python tools/selftest.py --quick                  # 跳过逐篇文本比对
python tools/selftest.py --dict-zip <数据字典包>   # 额外校验块一 HTML→Markdown 保真
```

| 检查 | 内容 |
| :--- | :--- |
| **A1** | 目录 / 原始存档 / 正文三方条目数一致 |
| **A2** | 每篇 HTML 的可见文本切块，逐块必须在 Markdown 中出现（**当前 100%，9,465 个文本块全保留**） |
| **A3** | 结构元素数量守恒：table / pre / img |
| **A4** | Markdown 中不残留未处理的 HTML 块级标签 |
| **A5** | 块一：全量比对每个数据字典文件的**表数 / 小节数 / 表格数**（需 `--dict-zip`） |
| **A6** | 块一：逐单元格与源 HTML 对账（`--dict-samples 0` 为全量） |
| **B1** | `--full` 输出包含该文档**全部正文行** |
| **B2** | 非 `--full` 时若截断，必须打印明确的截断提示（不静默丢内容） |
| **B3** | `--limit` 生效，且报告的「总命中数」口径正确 |
| **B4** | 全部 267 个模块的 `_INDEX.md` 与表定义**逐条一致**（31,547 个表块 / 31,547 行索引） |
| **B5** | 端到端召回抽检：正文深处的关键词也能被检索到 |

**最近一次全量自检结果**：11,294 个文件 / 31,547 张表 / 570,400 行 /
**4,570,268 个单元格逐格一致，0 处不一致**。

> 已知的**上游数据特征**（非本仓库问题，自检会以警告形式列出）：
> 384 个表名不以 `t_` 开头（如 `community_user`、`entryentity_lk`）；
> 622 个表块在源文档里本身就没有字段定义。

---

## 内容更新

两块内容都是**从上游生成的，不是手写的**。

### 块一 数据库（官方数据字典导出包）

```bash
python tools/build_db_from_dict.py <数据字典导出.zip>    # 转换（自动清理过期文件）
python tools/build_db_from_dict.py <zip> --list          # 只看统计，不写文件
python scripts/build_index.py                            # 重建索引
```

- 导出包结构为 `<root>/<模块>_files/<对象>.html`，模块概览页会被忽略。
- 转换会把单元格里指向其它表的 `<a>` 转成 Markdown 链接，例如
  `[业务单元 bos_org](../base_files/bos_org.md)`，方便顺着关联关系摸过去。
- 导出包几十 MB，不入库，需要时从金蝶自行导出。

### 块二 OpenAPI 手册

```bash
python tools/fetch_manual.py            # 重新抓取（已存在的跳过，可增量）
python tools/fetch_manual.py --force    # 全部重抓
python tools/fetch_manual.py --render   # 不联网，用 _source/ 存档重新渲染
python tools/fetch_manual.py --list     # 只看目录树
```

- 抓取源是 vip.kingdee.com 的 JSON 接口（`/knowledgeapi/...`），**无需登录**。
- 原始 JSON 存档在 `references/openapi/_source/`，所以调整 `tools/html2md.py`
  的转换规则后可以 `--render` 离线重出，不必再联网。
- `tools/html2md.py` 是零依赖的 HTML→Markdown 转换器（只用标准库 `html.parser`），
  针对金蝶社区的 UEditor 富文本做了适配：表格、围栏代码块、嵌套列表、图片绝对路径。

---

## 安装为 Skill

```bash
git clone https://github.com/silent-reader-cn/kingdee-cosmic-dev.git
mkdir -p ~/.workbuddy-ai/skills/kingdee-cosmic-dev
cp -r kingdee-cosmic-dev/. ~/.workbuddy-ai/skills/kingdee-cosmic-dev/
```

安装后，AI 助手在遇到金蝶库表或 OpenAPI 问题时会自动加载本 skill，
并用 `scripts/search.py` 定位内容、用 `examples/kd_doctor.py` 诊断环境。

---

## 目录结构

```
kingdee-cosmic-dev/
├── SKILL.md                       # Skill 定义：检索用法 + 库表约定 + OpenAPI 速查 + 环境接入
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
├── examples/                      # 可运行示例（已在真实环境验证）
│   ├── salorder_query.py          #   销售订单查询工具
│   ├── kd_doctor.py               #   环境接入诊断 + 外部凭据体检
│   └── README.md                  #   用法与实测踩坑记录
└── references/
    ├── _INDEX.md                  # 总索引
    ├── db/                        # 块一：数据库（数据字典导出 V5.0.011.0）
    │   ├── _INDEX.md
    │   └── <模块>_files/
    └── openapi/                   # 块二：OpenAPI 手册
        ├── _INDEX.md
        ├── _source/
        └── <分类>/…/<标题>.md
```

---

## 免责声明

- **块一**：表结构整理自金蝶云苍穹数据字典导出，最终解释权归金蝶所有，请以实际数据库为准。
- **块二**：手册内容抓取自金蝶云社区公开专题，版权归金蝶所有，仅供学习与开发参考；
  文档内所有外链均指向原站，请以线上最新版本为准。
- **示例工具**：凭据请用环境变量或本地配置文件（`kd.json` 已在 `.gitignore` 中），
  不要把真实凭据提交到任何仓库。示例脚本默认只读，不涉及数据写入。

## License

[MIT](./LICENSE) © 2026 silent-reader-cn
