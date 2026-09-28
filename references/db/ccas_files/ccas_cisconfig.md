# 集成服务配置-ccas_cisconfig

## 单据体-子表 t_ccas_cisconfig_entry

- **表名称：** 单据体-子表
- **表名：** t_ccas_cisconfig_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfig_value | 字段值 | varchar | 2000 |  | √ | ' ' | 字段值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fconfig_key | 字段名 | varchar | 80 |  | √ | ' ' | 字段名 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_cisconfig_entry |  | fentryid |
| 2 | idx_ccas_cisconfig_entry |  | fid |

---

## 集成服务配置-主表 t_ccas_cisconfig

- **表名称：** 集成服务配置-主表
- **表名：** t_ccas_cisconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fuser | 登录用户 | varchar | 64 |  | √ | ' ' | 登录用户 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcisconfig | fcisconfig | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmenuconfiguration | 是否展示菜单配置项 | varchar | 1 |  | √ | ' ' | 是否展示菜单配置项,枚举: 0 :否 1 :是 |
| 8 | fpassword | 登录密码 | varchar | 64 |  | √ | ' ' | 登录密码 |
| 9 | fintegratedserviceid | 集成服务标识 | varchar | 200 |  | √ | ' ' | 集成服务标识 |
| 10 | fcisconfigshowflag | 集成配置展示开关 | varchar | 1 |  | √ | '1' | 集成配置展示开关 |
| 11 | fcisconfigflag | 集成配置开关 | varchar | 1 |  | √ | '1' | 集成配置开关 |
| 12 | fcreateorg | 集成服务商 | varchar | 200 |  | √ | ' ' | 集成服务商 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fintegservicetypenumber | 集成服务类型编码 | varchar | 256 |  | √ | ' ' | 集成服务类型编码 |
| 15 | fmenushowflag | 菜单配置展示开关 | varchar | 1 |  | √ | '0' | 菜单配置展示开关 |
| 16 | fintegservicetype | 集成服务类型 | varchar | 200 |  | √ | ' ' | 集成服务类型 |
| 17 | fpkgname | 集成服务名称 | varchar | 200 |  | √ | ' ' | 集成服务名称 |
| 18 | fenable | 单据状态 | varchar | 1 |  | √ | '0' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 19 | fistimeout | 超时设置 | varchar | 1 |  | √ | '0' | 超时设置 |
| 20 | ftimeout | 超时设置(秒) | int4 | 32 |  | √ | 3 | 超时设置(秒) |
| 21 | fmenuflag | 菜单配置开关 | varchar | 1 |  | √ | '0' | 菜单配置开关 |
| 22 | fisfreelogin | 免密登录 | varchar | 1 |  | √ | '0' | 免密登录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_cisconfig_service |  | fintegratedserviceid |
| 2 | pk_t_ccas_cisconfig |  | fid |
