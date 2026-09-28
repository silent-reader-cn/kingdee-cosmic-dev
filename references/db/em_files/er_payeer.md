# 收款信息-er_payeer

## 使用人-多选基础资料表 t_er_payeeuser

- **表名称：** 使用人-多选基础资料表
- **表名：** t_er_payeeuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_payeeuser_baseid |  | fid,fbasedataid |
| 2 | t_er_payeeuser_pkey |  | fpkid |
| 3 | idx_er_payeeuser_baseid2 |  | fbasedataid |

---

## 收款信息-主表 t_er_payee

- **表名称：** 收款信息-主表
- **表名：** t_er_payee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpayeraccount01 | 银行账号4位 | varchar | 25 |  | √ | ' ' | 银行账号4位 |
| 5 | foutpayer | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 6 | fpayer | 收款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | '0' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 25 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fishare | 授权使用 | bpchar | 1 |  | √ | '0' | 授权使用 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 18 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 19 | fpublicaccount | fpublicaccount | bpchar | 1 |  | √ | '0' |  |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fisemployee | 职员 | bpchar | 1 |  | √ | '1' | 职员 |
| 23 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 24 | fpayerbankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 25 | fistopublic | 对公账号 | bpchar | 1 |  | √ | '0' | 对公账号 |
| 26 | fcomment | fcomment | varchar | 255 |  |  | null |  |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fmigsrc | fmigsrc | int4 | 32 |  | √ | 0 |  |
| 30 | fbackgroundimg | 银行卡背景图片 | varchar | 255 |  | √ | ' ' | 银行卡背景图片 |
| 31 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fbanklogo | 银行logo图标 | varchar | 255 |  | √ | ' ' | 银行logo图标 |
| 33 | fbanklogo1 | 银行logo图片 | varchar | 255 |  | √ | ' ' | 银行logo图片 |
| 34 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fpayeraccount02 | 银行账号前后四位 | varchar | 25 |  | √ | ' ' | 银行账号前后四位 |
| 36 | fpayeraccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 37 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 38 | fuseorgid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 40 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 41 | fisdefault | 默认收款信息 | bpchar | 1 |  | √ | '0' | 默认收款信息 |
| 42 | fopenareaid | fopenareaid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_payee_createorg |  | fcreateorgid |
| 2 | idx_er_paye_fcreatorid |  | fcreatorid |
| 3 | idx_t_er_payee_master |  | fmasterid |
| 4 | idx_er_paye_fstatus |  | fstatus |
| 5 | idx_er_paye_fpayer |  | fpayer |
| 6 | t_er_payee_pkey |  | fid |
| 7 | idx_er_paye_fenable |  | fenable |
| 8 | idx_er_paye_fisdefault |  | fisdefault |

---

## 收款信息-使用范围表 t_er_payee_u

- **表名称：** 收款信息-使用范围表
- **表名：** t_er_payee_u

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
| 1 | idx_t_er_payee_u_uo |  | fuseorgid |
| 2 | t_er_payee_u_pkey |  | fdataid,fuseorgid |

---

## 收款信息-多语言表 t_er_payee_l

- **表名称：** 收款信息-多语言表
- **表名：** t_er_payee_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_payi_fid |  | fid,flocaleid |
| 2 | t_er_payee_l_pkey |  | fpkid |

---

## 收款信息-使用范围位图表 t_er_payee_m

- **表名称：** 收款信息-使用范围位图表
- **表名：** t_er_payee_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_payee_m |  | forgid |
