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

### 6. 其它有用的事实

| 接口 | 用途 |
| :--- | :--- |
| `POST /ierp/auth/queryParameters.do` | 返回 `closeEncrypt`（密码是否需加密）、`userSourceType` 等 |
| `POST /ierp/auth/isNeedDisplayVerify.do` | 是否需要图形验证码 |
| `POST /ierp/kapi/oauth2/getToken` | 第三方应用取 access_token（有效期 2 小时） |

---

## 端到端跑通需要的一次性准备

1. 用管理员登录网页 → **【开放服务云】→【OpenAPI】→【第三方应用】** → 新增
2. 记下 **系统编码**（= `client_id`）与 **AccessToken 认证密钥**（= `client_secret`）
3. 确认目标 API 的「第三方应用授权」开关状态与你的认证方式一致
4. 跑：
   ```bash
   python examples/salorder_query.py --base-url ... --probe          # 先探路
   python examples/salorder_query.py --base-url ... --client-id ... --client-secret ... \
       --account-id ... --username admin --limit 10
   ```
