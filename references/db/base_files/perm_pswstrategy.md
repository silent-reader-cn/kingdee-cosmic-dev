# 密码策略-perm_pswstrategy

## 密码策略-多语言表 t_perm_pswstrategy_l

- **表名称：** 密码策略-多语言表
- **表名：** t_perm_pswstrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_perm_pswstrategy_l_fid |  | fid,flocaleid |
| 2 | t_perm_pswstrategy_l_pkey |  | fpkid |

---

## 密码策略-主表 t_perm_pswstrategy

- **表名称：** 密码策略-主表
- **表名：** t_perm_pswstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frepeattimes | 密码间隔次数 | int8 | 64 |  | √ | 0 | 密码间隔次数 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | flogincheckstgy | 登录时校验密码规则 | bpchar | 1 |  | √ | '0' | 登录时校验密码规则 |
| 5 | fhascaseletter | 大小写字母 | bpchar | 1 |  | √ | '0' | 大小写字母 |
| 6 | floginoptions | 默认登录选项 | varchar | 30 |  | √ | '1' | 默认登录选项,枚举: 1 :账号+密码 3 :账号+密码+图形验证码 2 :账号+密码+短信验证码 4 :账号+密码+邮箱验证码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdefault | fdefault | varchar | 36 |  | √ | ' ' |  |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fvalidity | 密码有效期(天) | int8 | 64 |  | √ | 0 | 密码有效期(天) |
| 13 | flockcount | 账号锁定次数 | int8 | 64 |  | √ | 0 | 账号锁定次数 |
| 14 | fweakpsw | 弱口令校验 | bpchar | 1 |  | √ | '0' | 弱口令校验 |
| 15 | fenablelock | 是否启用锁定 | bpchar | 1 |  | √ | '1' | 是否启用锁定 |
| 16 | flockterm | 帐号锁定(分钟) | int8 | 64 |  | √ | 0 | 帐号锁定(分钟) |
| 17 | fforewarnday | 失效预警期(天) | int8 | 64 |  | √ | 0 | 失效预警期(天) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fvercodectrl | 图形验证码控制次数 | int8 | 64 |  | √ | 0 | 图形验证码控制次数 |
| 21 | fneedverifycode | 修改密码校验验证码 | bpchar | 1 |  | √ | '1' | 修改密码校验验证码 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fisletter | 字母 | bpchar | 1 |  | √ | ' ' | 字母 |
| 24 | fsmscount | 短信验证码阀值 | int4 | 32 |  | √ | 0 | 短信验证码阀值 |
| 25 | fisspecial | 特殊符号 | bpchar | 1 |  | √ | ' ' | 特殊符号 |
| 26 | fminlength | 密码最小长度 | int8 | 64 |  | √ | 0 | 密码最小长度 |
| 27 | fisrequirechange | fisrequirechange | bpchar | 1 |  | √ | ' ' |  |
| 28 | fenablesmscode | 是否启用短信验证码 | bpchar | 1 |  | √ | '0' | 是否启用短信验证码 |
| 29 | fenablegraphiccode | 是否启用图形验证码 | bpchar | 1 |  | √ | '1' | 是否启用图形验证码 |
| 30 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 32 | fisnumber | 数字 | bpchar | 1 |  | √ | ' ' | 数字 |
| 33 | fisdefault | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_pswstrategy_pkey |  | fid |
| 2 | idx_t_perm_pswstrategy_number |  | fnumber |
