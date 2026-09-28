# 外部集成信息（废弃）-isc_sysconn

## 外部集成信息（废弃）-使用范围位图表 t_isc_connection_m

- **表名称：** 外部集成信息（废弃）-使用范围位图表
- **表名：** t_isc_connection_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frabbituser | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 3 | frabitpwd | 密码 | varchar | 100 |  | √ | ' ' | 密码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_conn_m_fuser |  | frabbituser |
| 2 | t_isc_connection_m_pkey |  | fid |

---

## 外部集成信息（废弃）-多语言表 t_isc_connection_l

- **表名称：** 外部集成信息（废弃）-多语言表
- **表名：** t_isc_connection_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_connection_l_pkey |  | fpkid |
| 2 | idx_isc_conn_l_fid |  | fid,flocaleid |

---

## 外部集成信息（废弃）-分表 t_isc_connection_o

- **表名称：** 外部集成信息（废弃）-分表
- **表名：** t_isc_connection_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fouser | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 3 | fopassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_conn_o_funame |  | fouser |
| 2 | t_isc_connection_o_pkey |  | fid |

---

## 外部集成信息（废弃）-分表 t_isc_connection_n

- **表名称：** 外部集成信息（废弃）-分表
- **表名：** t_isc_connection_n

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

## 外部集成信息（废弃）-分表 t_isc_connection_e

- **表名称：** 外部集成信息（废弃）-分表
- **表名：** t_isc_connection_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatacenter | 数据中心 | varchar | 100 |  | √ | ' ' | 数据中心,枚举: |
| 3 | fusername | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 4 | flanguage | 语言 | varchar | 100 |  | √ | ' ' | 语言,枚举: l2 :简体中文 l3 :繁体中文 l1 :英文 |
| 5 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 6 | fidentification | 登录标志 | varchar | 100 |  | √ | ' ' | 登录标志 |
| 7 | fcustomdatacenter | 数据中心 | varchar | 100 |  | √ | ' ' | 数据中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_conn_e_fname |  | fusername |
| 2 | t_isc_connection_e_pkey |  | fid |

---

## 外部集成信息（废弃）-主表 t_isc_connection

- **表名称：** 外部集成信息（废弃）-主表
- **表名：** t_isc_connection

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant | ftenant | varchar | 100 |  | √ | ' ' |  |
| 3 | fdatacenter1 | 数据中心名称 | varchar | 100 |  | √ | ' ' | 数据中心名称 |
| 4 | faddress | 服务器地址 | varchar | 100 |  | √ | ' ' | 服务器地址 |
| 5 | fconnectableothersystem | 可连接 | varchar | 50 |  | √ | ' ' | 可连接 |
| 6 | fassigncode | 认证标志 | varchar | 100 |  | √ | ' ' | 认证标志 |
| 7 | ftag | 队列Tag | varchar | 32 |  | √ | ' ' | 队列Tag |
| 8 | fusesubserver | 项目名 | bpchar | 1 |  | √ | '0' | 项目名 |
| 9 | fvhost | 虚拟主机 | varchar | 32 |  | √ | ' ' | 虚拟主机 |
| 10 | fsystype | 连接系统类型 | int8 | 64 |  | √ | 0 | 连接类型（废弃） isc_conntype |
| 11 | fconnectiontype | 连接类型 | varchar | 30 |  | √ | ' ' | 连接类型,枚举: EAS :EAS 金蝶云 :金蝶云苍穹 Rabbit :Rabbit MQ other :其它 |
| 12 | furlpreview | 访问地址预览 | varchar | 200 |  | √ | ' ' | 访问地址预览 |
| 13 | fprotocol | 协议类型 | varchar | 30 |  | √ | ' ' | 协议类型,枚举: http:// :http https:// :https |
| 14 | fsubserver | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 15 | fislocal | 当前系统 | int8 | 64 |  | √ | 0 | 当前系统 |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fport | 端口 | varchar | 100 |  | √ | ' ' | 端口 |
| 18 | fenable | 单据状态 | int8 | 64 |  | √ | 1 | 单据状态,枚举: 0 :禁用 1 :启用 |
| 19 | fapiport | API调用端口 | varchar | 5 |  | √ | ' ' | API调用端口 |
| 20 | fencryptcode | 加密密钥 | varchar | 100 |  | √ | ' ' | 加密密钥 |
| 21 | fversion | 版本 | varchar | 100 |  | √ | ' ' | 版本 |
| 22 | fdatacenterfornext | fdatacenterfornext | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_conn_fcontype |  | fconnectiontype |
| 2 | t_isc_connection_pkey |  | fid |
