# 现金账户F7-cas_accountcashtreelistf7

## 币别-多选基础资料表 t_cas_currencycash

- **表名称：** 币别-多选基础资料表
- **表名：** t_cas_currencycash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_currencycash_pkey |  | fpkid |
| 2 | idx_cas_cc_fpid |  | fid |

---

## 现金账户F7-主表 t_cas_accountcashs

- **表名称：** 现金账户F7-主表
- **表名：** t_cas_accountcashs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdefaultcurrencyid | 默认币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fclosedate | 销户日期 | timestamp | 0 |  |  | null | 销户日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fadminid | 账户管理员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fisdefaultpayee | 默认收款户 | bpchar | 1 |  | √ | '0' | 默认收款户 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fissysgen | 是否系统预插 | bpchar | 1 |  | √ | '0' | 是否系统预插 |
| 16 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fisdefaultpayer | 默认付款户 | bpchar | 1 |  | √ | '0' | 默认付款户 |
| 20 | fname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | faccountpropertyid | 账户用途 | varchar | 30 |  | √ | ' ' | 账户用途,枚举: |
| 23 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 24 | fcurrencyname | 币别 | varchar | 255 |  |  | null | 币别 |
| 25 | fclosestatus | 是否销户 | bpchar | 1 |  | √ | '0' | 是否销户,枚举: 0 :正常 1 :销户 |
| 26 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fisbycurrency | 单一币别 | bpchar | 1 |  | √ | '0' | 单一币别 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 账户编码 | varchar | 80 |  | √ | ' ' | 账户编码 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_accountcashs_on |  | forgid,fnumber |
| 2 | idx_t_cas_accountcashs_master |  | fmasterid |
| 3 | t_cas_accountcashs_pkey |  | fid |
| 4 | idx_cas_ac_fnumber |  | fnumber |
| 5 | idx_t_cas_accountcashs_createorg |  | fcreateorgid |

---

## 现金账户F7-多语言表 t_cas_accountcashs_l

- **表名称：** 现金账户F7-多语言表
- **表名：** t_cas_accountcashs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_accountcashs_l_pkey |  | fpkid |
| 2 | idx_cas_ac_fid |  | fid,flocaleid |

---

## 现金账户F7-使用范围表 t_cas_accountcashs_u

- **表名称：** 现金账户F7-使用范围表
- **表名：** t_cas_accountcashs_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cas_accountcashs_u_uo |  | fuseorgid |
| 2 | t_cas_accountcashs_u_pkey |  | fdataid,fuseorgid |
