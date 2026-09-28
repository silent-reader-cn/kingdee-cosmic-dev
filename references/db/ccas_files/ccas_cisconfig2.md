# 集成服务配置-ccas_cisconfig2

## 集成服务配置-多语言表 t_ccas_cisconfig_l

- **表名称：** 集成服务配置-多语言表
- **表名：** t_ccas_cisconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 集成服务配置-主表 t_ccas_cisconfig

- **表名称：** 集成服务配置-主表
- **表名：** t_ccas_cisconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | fcreator | int8 | 64 |  | √ | 0 |  |
| 3 | fuser | fuser | varchar | 64 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcisconfig | fcisconfig | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 7 | fmenuconfiguration | fmenuconfiguration | varchar | 1 |  | √ | ' ' |  |
| 8 | fpassword | fpassword | varchar | 64 |  | √ | ' ' |  |
| 9 | fintegratedserviceid | fintegratedserviceid | varchar | 200 |  | √ | ' ' |  |
| 10 | fcisconfigshowflag | fcisconfigshowflag | varchar | 1 |  | √ | '1' |  |
| 11 | fcisconfigflag | fcisconfigflag | varchar | 1 |  | √ | '1' |  |
| 12 | fcreateorg | fcreateorg | varchar | 200 |  | √ | ' ' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fintegservicetypenumber | fintegservicetypenumber | varchar | 256 |  | √ | ' ' |  |
| 15 | fmenushowflag | fmenushowflag | varchar | 1 |  | √ | '0' |  |
| 16 | fintegservicetype | fintegservicetype | varchar | 200 |  | √ | ' ' |  |
| 17 | fpkgname | fpkgname | varchar | 200 |  | √ | ' ' |  |
| 18 | fenable | 使用状态 | varchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fistimeout | fistimeout | varchar | 1 |  | √ | '0' |  |
| 20 | ftimeout | ftimeout | int4 | 32 |  | √ | 3 |  |
| 21 | fmenuflag | fmenuflag | varchar | 1 |  | √ | '0' |  |
| 22 | fisfreelogin | fisfreelogin | varchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_cisconfig_service |  | fintegratedserviceid |
| 2 | pk_t_ccas_cisconfig |  | fid |
