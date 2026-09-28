# 日记账余额-cas_journalbalance

## 日记账余额-主表 t_cas_journalbalance

- **表名称：** 日记账余额-主表
- **表名：** t_cas_journalbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyeardebitloc | 年借方金额本位币 | numeric | 23 | 10 | √ | 0 | 年借方金额本位币 |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | faccountcashid | 现金账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmonthcredit | 期贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 期贷方 |
| 8 | fyeardebit | 年借方 | numeric | 23 | 10 | √ | 0.0000000000 | 年借方 |
| 9 | fyearcredit | 年贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 年贷方 |
| 10 | fyearbalance | 年末余额 | numeric | 23 | 10 | √ | 0.0000000000 | 年末余额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fmonthbalance | 期末余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额 |
| 17 | fyearcreditloc | 年贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 年贷方金额本位币 |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fisbalanced | 是否结账 | bpchar | 1 |  | √ | '0' | 是否结账 |
| 20 | fyearstart | 年初余额 | numeric | 23 | 10 | √ | 0.0000000000 | 年初余额 |
| 21 | fmonthdebit | 期借方 | numeric | 23 | 10 | √ | 0.0000000000 | 期借方 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fremark | fremark | varchar | 255 |  |  | null |  |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 26 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fmonthdebitloc | 期借方金额本位币 | numeric | 23 | 10 | √ | 0 | 期借方金额本位币 |
| 29 | fmonthcreditloc | 期贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 期贷方金额本位币 |
| 30 | fmonthstart | 期初余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额 |
| 31 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fyearbalanceloc | 年末余额本位币 | numeric | 23 | 10 | √ | 0 | 年末余额本位币 |
| 34 | fyearstartloc | 年初余额本位币 | numeric | 23 | 10 | √ | 0 | 年初余额本位币 |
| 35 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :现金 2 :日记账 3 :对账单 |
| 36 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fmonthbalanceloc | 期末余额本位币 | numeric | 23 | 10 | √ | 0 | 期末余额本位币 |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fmonthstartloc | 期初余额本位币 | numeric | 23 | 10 | √ | 0 | 期初余额本位币 |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 42 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cas_journalbalance_createorg |  | fcreateorgid |
| 2 | ix_cas_journalb_acctcash |  | forgid,faccountcashid,fcurrencyid,fperiodid |
| 3 | t_cas_journalbalance_pkey |  | fid |
| 4 | idx_t_cas_journalbalance_master |  | fmasterid |

---

## 日记账余额-使用范围表 t_cas_journalbalance_u

- **表名称：** 日记账余额-使用范围表
- **表名：** t_cas_journalbalance_u

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
| 1 | idx_t_cas_journalbalance_u_uo |  | fuseorgid |
| 2 | pk_t_cas_journalbalance_u |  | fdataid,fuseorgid |

---

## 日记账余额-多语言表 t_cas_journalbalance_l

- **表名称：** 日记账余额-多语言表
- **表名：** t_cas_journalbalance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  |  | null |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_journalbalance_l_pkey |  | fpkid |
| 2 | idx_cas_jbl_fid |  | fid,flocaleid |

---

## 日记账余额-使用范围位图表 t_cas_journalbalance_m

- **表名称：** 日记账余额-使用范围位图表
- **表名：** t_cas_journalbalance_m

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
| 1 | pk_t_cas_journalbalance_m |  | forgid |
