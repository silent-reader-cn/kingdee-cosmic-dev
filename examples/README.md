# examples —— 可运行示例

| 文件 | 用途 |
| :--- | :--- |
| [`kd_doctor.py`](./kd_doctor.py) | **环境接入诊断**：连通性、账套、登录契约、取令牌接口、接口路径与授权开关，一键体检 |
| [`salorder_query.py`](./salorder_query.py) | 销售订单查询工具 |

---

## kd_doctor.py · 环境接入诊断

刚拿到一个环境时先跑它，把我踩过的坑一次性检出来：

```bash
# 只做匿名检查（不碰账号，不会触发限流）
python examples/kd_doctor.py --base-url http://<host>:<port>

# 带凭据做完整检查（默认只登录 1 次、不重试，避免触发限流）
python examples/kd_doctor.py --base-url ... \
    --username admin --password <密码> --account-id <数据中心ID>

# 批量探测候选接口路径
python examples/kd_doctor.py --base-url ... \
    --probe-paths /ierp/kapi/v2/sm/sm_salorder/query,/ierp/kapi/v2/sm/sm_salorder/list

# 体检「别人给的一个 token」—— 把常见摆放方式全试一遍并给结论
python examples/kd_doctor.py --base-url ... --token <AccessToken>
python examples/kd_doctor.py --base-url ... --token <Token> --identity <x-acgw-identity>
```

`--token` 会做格式体检（是否像 `<accountId>_<随机串>`、是否含占位符特征），
再依次尝试 `access_token` 头 / `Authorization: Bearer` / 两种 Cookie / `x-acgw-identity`，
最后明确告诉你**哪个摆放方式生效**、或者**全都无效**。

`--identity` 会先 base64 解码出结构再试 —— 实测解出来是
`v1|<20位hex>|<13位数字>|<32字节签名>`，看着像「API 网关」的身份串，
未必是苍穹 `/ierp` 直连用的。

---

## salorder_query.py · 销售订单查询工具

```bash
# 基本查询
python examples/salorder_query.py --base-url ... --client-id ... --client-secret ... \
    --account-id ... --username admin --limit 20

# 过滤（filter 支持 SQL 风格表达式，实测可用）
... --filter "billno like 'HSH%'"
... --filter "bizdate >= '2025-03-01'"
... --filter "totalamount > 5000"

# 排序（服务端不认，这里是客户端排序）
... --sort "totalamount:desc,billno:asc"

# 翻页取全量
... --all --limit 100

# 只看指定字段 / 看全部字段
... --fields "billno,customer_name,totalamount"
... --json

# 导出（.csv 带 BOM，Excel 打开不乱码；.json 原样）
... --export salorder.csv
... --export salorder.json

# 直接给请求体（JSON 字符串或 @文件）
... --body '{"data":{},"pageNo":1,"pageSize":10,"filter":"totalamount > 5000"}'
```

| 参数 | 说明 |
| :--- | :--- |
| `--limit N` | 每页条数（默认 20） |
| `--page N` | 页码（默认 1） |
| `--filter EXPR` | SQL 风格过滤表达式，实测支持 `like` / `>=` / `>` 等 |
| `--sort F[:desc]` | **客户端**排序，逗号分隔多字段 |
| `--order-by` | 发给服务端的 orderBy —— ⚠️ 实测被静默忽略，别依赖 |
| `--all` | 翻页取全量（按响应里的 `lastPage` 判断结束） |
| `--fields a,b,c` | 只取这些字段（同时作为展示列） |
| `--json` | 原样输出 JSON |
| `--export FILE` | 导出 `.csv` 或 `.json` |

---

## kd_doctor.py · 环境接入诊断

只读工具：登录 → 取令牌 → 调用销售订单查询操作API，把结果打成表格。

```bash
# 0) 探路：不需要任何凭据，先摸清环境
python examples/salorder_query.py --base-url http://<host>:<port> --probe

# 1) 列出账套（拿到 accountId）
python examples/salorder_query.py --base-url ... --list-datacenters

# 2) OpenAPI 方式查询（推荐）
python examples/salorder_query.py --base-url ... \
    --client-id <系统编码> --client-secret <密钥> \
    --account-id <数据中心ID> --username admin \
    --limit 20 --filter "fbillno like '%SO%'"

# 3) 网页会话方式（仅当接口未开「第三方应用授权」时可用）
python examples/salorder_query.py --base-url ... --auth web \
    --username admin --password <密码> --account-id <数据中心ID>
```

凭据不要写在命令行历史里，用环境变量或本地配置文件（`kd.json` 已在 `.gitignore` 中）：

```bash
export KD_BASE_URL=http://host:port
export KD_CLIENT_ID=... KD_CLIENT_SECRET=... KD_ACCOUNT_ID=...
python examples/salorder_query.py --limit 10
```

---

## 这个工具踩过的坑（都是实测定出来的）

### 1. 查询接口长什么样

```
POST /ierp/kapi/v2/{appId}/{formId}/{serviceName}
     /ierp/kapi/v2/sm/sm_salorder/query        ← 销售订单标准查询API
```

`appId`=业务对象所属应用编码（销售订单是 `sm`），`formId`=业务对象编码
（`sm_salorder`），`serviceName`=API 编码（标准查询是 `query`）。
金蝶标准接口的 `isv` 段为空，所以路径里没有它。

**怎么确认路径对不对**：错路径返回 `404 Cannot found OpenAPI(or disabled)`，
对路径返回别的错误码。用错误码区分，比翻文档快。

⚠️ **但必须已认证**。未认证时服务端在鉴权阶段就返回 `401`，
存在的和不存在的路径返回一模一样 —— 据此判断会把不存在的路径误判成「存在」。
实测对比：

| 路径 | 未认证 | 已认证（带会话） |
| :--- | :--- | :--- |
| `/kapi/v2/sm/sm_salorder/query` | 401 | **403** ← 存在 |
| `/kapi/v2/sm/sm_salorder/list` | 401 | **404** ← 不存在 |
| `/kapi/v2/sm/sm_salorder/save` | 401 | **404** ← 不存在 |

> 这个坑是我先写了个诊断脚本、跑出「三个路径都存在」的假阳性才发现的。
> `kd_doctor.py` 现在会在未登录时明确标注「无法判定」。

### 2. 「该接口需要第三方应用授权」= 不能用 cookie 认证

```
errorCode=403  该接口需要第三方应用授权
  at kd.bos.openapi.base.dataservice.OpenApiDataServiceImpl.checkThirdACL(...)
```

这是**每个 API 上单独配的开关**（API 配置界面里的「第三方应用授权」）。
打开时，服务端在 `checkThirdACL` 里直接拒掉 cookie / 匿名认证。
所以：**网页登录拿到会话也没用**，必须走第三方应用拿 `access_token`。

### 3. 网页登录接口的真实契约（文档里查不到，实测得出）

```
POST /ierp/api/login.do
Content-Type: application/json
{"user": "admin", "password": "..."}      ← 键名是 user，不是 username！
```

返回：

```json
{"data": {"access_token": "<accountId>_<...>", "KERPSESSIONID": "<accountId>_<...>",
          "success": true, "error_code": "0"}, "status": true}
```

`access_token` 与 `KERPSESSIONID` 同值，作为 Cookie 回传即可访问内部接口
（实测 `/ierp/kapi/v2` 用这个 Cookie 能通过认证）。

⚠️ 用 `username` 当键名会得到 `参数错误，请填写正确的用户账号、密码、租户代码、
登录类型和数据中心ID。` —— 报错信息完全没提是键名错了，很容易卡住。

### 4. 账套 = 数据中心，可以匿名查

```
POST /ierp/auth/getAllDatacenters.do      （无需登录）
→ [{"accountId":"...","accountNumber":"<accountNumber>","accountName":"某测试账套"}, ...]
```

`accountId` 就是取令牌时要传的 `accountId`。

### 5. 别高频试密码

实测连续几十次登录尝试后，账号会返回：

```
无法获取云通行证AccessToken，原因：远程服务不可用，或者用户名与密码不匹配。
```

这个报错**有歧义**（既可能是密码错，也可能是被限流，还可能是环境连不上金蝶云）。
写自动化脚本时要退避重试，不要无脑循环。

### 6. 请求体是「扁平结构」，但 `data` 壳必须有 ⭐

**这是最容易卡住的一步。** 分页参数在**顶层**，同时必须带一个 `data` 键：

```json
{ "data": {}, "pageNo": 1, "pageSize": 20 }
```

两种写错的方式报错完全不同，都容易被误判：

| 写法 | 报错 |
| :--- | :--- |
| 不带 `data` 键 | `400 请求参数没有 data 数据。` |
| 把分页参数塞进 `data` | `400 页大小pageSize不能为空。` |

成功返回：

```json
{"data": {"rows": [...], "pageNo": 1, "pageSize": 20,
          "lastPage": false, "filter": "[1 = 1]"}}
```

> 文档说「扁平化出入参」，别理解成「什么都不用包」——
> `data` 这层壳是必须的，只是**业务字段**和分页参数平铺在顶层。
> 其它可用顶层参数：`filter`、`orderBy`、`selectFields`。

### 7. 代理用户：第三方应用的隐藏必填项

第三方应用有个开关「**启用代理用户控制**」（V6.0.1 起，官方建议开启）。
开启后 `getToken` 的 `username` **必须在该应用的「代理用户」列表里**：

```
603  第三方应用（client_id）的代理用户为空或userName不在代理用户中。
```

别和「用户名不存在」搞混：

| 报错 | 含义 |
| :--- | :--- |
| `代理用户为空或userName不在代理用户中` | 用户名**有效**，但没授权给这个应用 |
| `username：用户无效或不可用` | 用户名**不存在** |

处理：【开放服务云】→【OpenAPI】→【安全策略】→【第三方应用】→ 该应用，
把 `username` 加进「代理用户」，或关掉「启用代理用户控制」。

### 8. `getToken` 各阶段的报错对照

按校验顺序，看到哪条就知道走到哪一步了：

| 报错 | 走到哪 | 说明 |
| :--- | :--- | :--- |
| `client_id为空` | 参数校验 | 没传 client_id |
| `第三方应用client_id：xxx在系统中不存在或未启用` | 应用查找 | **client_id 错**，或**账套(accountId)不对** |
| `密钥验证失败, 第 N 次` | 密钥校验 | **client_id 是对的**，secret 错。⚠️ 连续 5 次锁 180 秒 |
| `代理用户为空或userName不在代理用户中` | 代理用户校验 | **凭据全对**，只是应用没配代理用户 |
| `username：用户无效或不可用` | 用户校验 | username 不存在 |
| `本次参数nonce:xxx已经调用过了` | 重放校验 | nonce 必须每次不同 |
| `不正确的…已连续5次，该账号登录已锁定，请在180秒后再试` | 锁定 | 等 180 秒 |

> **第三方应用是按数据中心(accountId)隔离的**：
> 同一个 `client_id` 换一个账套就会报「不存在或未启用」。
> 实测 `<client_id>` 只在「某测试账套」下有效，换到「另一账套」就报不存在。

### 9. ⚠️ 排序参数被静默忽略（最坑的一条）

实测 `orderBy` **完全不生效**，而且**不报错**（`code=0`，顺序不变）。
试过 12 种写法全部无效：

```
orderBy=billno desc / billno DESC / billno / fbillno desc / -billno
orderBy=totalamount desc / createtime desc
orderby= / order= / sort= / sortBy= / orderField=
sortField=billno + sortOrder=desc
orderBy=[{"field":"billno","desc":true}]
orderBy="billno:desc"
```

结论：**排序由 API 配置决定，运行时改不了**。
这类「不报错但不生效」的行为最危险 —— 调用方会以为排序已经生效。

所以工具用 `--sort` 做**客户端排序**（拿回数据后本地排）：

```bash
python examples/salorder_query.py ... --sort "totalamount:desc,billno:asc"
```

`--order-by` 仍然会发给服务端（别的环境可能认），但不要依赖它。

### 10. 其它有用的事实

| 接口 | 用途 |
| :--- | :--- |
| `POST /ierp/auth/queryParameters.do` | 返回 `closeEncrypt`（密码是否需加密）、`userSourceType` 等 |
| `POST /ierp/auth/isNeedDisplayVerify.do` | 是否需要图形验证码 |
| `POST /ierp/kapi/oauth2/getToken` | 第三方应用取 access_token（有效期 2 小时） |

---

## 端到端跑通（已实测成功）

**实测环境**：`http://<host>:<port>` 账套「某测试账套」（`accountId=<accountId>`）

### 一次性准备

1. 用管理员登录网页 → **【开放服务云】→【OpenAPI】→【安全策略】→【第三方应用】** → 新增
2. 记下 **系统编码**（= `client_id`）与 **AccessToken 认证密钥**（= `client_secret`）
3. 配好「**代理用户**」（见上面第 7 条），否则取不到 token
4. 确认目标 API 的「第三方应用授权」开关状态与你的认证方式一致

### 跑

```bash
python examples/kd_doctor.py --base-url ... \
    --username admin --account-id ... --client-id ... --client-secret ...   # 先体检

python examples/salorder_query.py --base-url ... \
    --client-id ... --client-secret ... --account-id ... --username admin --limit 10
```

### 实测输出

> 下面这段是真实跑出来的结果，但**已做脱敏**：
> 主机地址、accountId、client_id、账套名、客户名、单据号都替换成了占位符，
> 结构、状态码、字段名、金额一律保持原样。

```
已获取 access_token（有效期默认 2 小时）
共返回 6 条（请求体：{"data": {}, "pageNo": 1, "pageSize": 6}）

（共 102 个字段，默认只展示 9 个关键列；加 --fields 可指定，--json 看全部）

单据编号                    单据状态  订单状态  业务日期                 客户                    金额      审核日期
----------------------  ----  ----  -------------------  --------------------  ------  -------------------
SO-20250303-0296  C     K     2025-03-03 00:00:00  某供应链公司（JXS）  9600.0  2025-03-03 14:15:28
SO-20250303-0297  C     C     2025-03-03 00:00:00  某食品公司           0.0     2025-03-03 18:24:25
SO-20250303-0298  C     K     2025-03-03 00:00:00  某贸易公司（JXS）      4245.0  2025-03-03 14:15:28
```

查询接口默认返回 **102 个字段**（含 `customer_name`、`org_name`、`billtype_name` 等
已展开的基础资料名称），所以工具默认只展示 9 个关键列，用 `--fields` 或 `--json` 看更多。
