# 初始化数据录入-cas_cashmgtinit

## 银行账户分录-子表 t_cas_cashmgtinitbank

- **表名称：** 银行账户分录-子表
- **表名：** t_cas_cashmgtinitbank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatementbalance | 对账单初始余额 | numeric | 23 | 10 | √ | 0.0000000000 | 对账单初始余额 |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fstatementdebit | 对账单本年累计借方 | numeric | 23 | 10 | √ | 0.0000000000 | 对账单本年累计借方 |
| 5 | fjournalbalanceloc | 日记账初始余额本位币 | numeric | 23 | 10 | √ | 0 | 日记账初始余额本位币 |
| 6 | fbatchno | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fjournalcredit | 日记账本年累计贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 日记账本年累计贷方 |
| 9 | fjournalbalanceadj | 调整后日记账余额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整后日记账余额 |
| 10 | fjournaldebit | 日记账本年累计借方 | numeric | 23 | 10 | √ | 0.0000000000 | 日记账本年累计借方 |
| 11 | fjournalcreditloc | 日记账本年累计贷方本位币 | numeric | 23 | 10 | √ | 0 | 日记账本年累计贷方本位币 |
| 12 | fstatementcredit | 对账单本年累计贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 对账单本年累计贷方 |
| 13 | fstatementbalanceadj | 调整后对账单总余额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整后对账单总余额 |
| 14 | fjournalbalance | 日记账初始余额 | numeric | 23 | 10 | √ | 0.0000000000 | 日记账初始余额 |
| 15 | fjournalsumbalanceadj | 调整后日记账总余额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整后日记账总余额 |
| 16 | fequal | 银行平衡 | bpchar | 1 |  | √ | '0' | 银行平衡,枚举: 0 : 1 :true |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 20 | fjournaldebitloc | 日记账本年累计借方本位币 | numeric | 23 | 10 | √ | 0 | 日记账本年累计借方本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ib_fpid |  | fid |
| 2 | t_cas_cashmgtinitbank_pkey |  | fentryid |

---

## 现金分录-子表 t_cas_cashmgtinitcash

- **表名称：** 现金分录-子表
- **表名：** t_cas_cashmgtinitcash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyeardebitloc | 本年累计借方本位币 | numeric | 23 | 10 | √ | 0 | 本年累计借方本位币 |
| 3 | faccountcashid | 现金账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 4 | fbatchno | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 5 | fbalance | 初始余额 | numeric | 23 | 10 | √ | 0.0000000000 | 初始余额 |
| 6 | fyearcreditloc | 本年累计贷方本位币 | numeric | 23 | 10 | √ | 0 | 本年累计贷方本位币 |
| 7 | fbalanceloc | 初始余额本位币 | numeric | 23 | 10 | √ | 0 | 初始余额本位币 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fyeardebit | 本年累计借方 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方 |
| 12 | fyearcredit | 本年累计贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ic_fpid |  | fid |
| 2 | t_cas_cashmgtinitcash_pkey |  | fentryid |

---

## 初始化数据录入-主表 t_cas_cashmgtinit

- **表名称：** 初始化数据录入-主表
- **表名：** t_cas_cashmgtinit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmigperiod | 迁移期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fxkisenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fisfinishinit | 是否已经初始化 | bpchar | 1 |  | √ | '0' | 是否已经初始化 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcashmiginfo | 迁移数据信息 | varchar | 255 |  | √ | ' ' | 迁移数据信息 |
| 15 | fstacurrencyid | 业务主币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 17 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_cas_init_org |  | forgid |
| 2 | t_cas_cashmgtinit_pkey |  | fid |
