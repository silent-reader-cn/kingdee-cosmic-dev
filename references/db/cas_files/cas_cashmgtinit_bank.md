# 银行存款期初-cas_cashmgtinit_bank

## 银行存款期初-主表 t_cas_cashmgtinit_bank

- **表名称：** 银行存款期初-主表
- **表名：** t_cas_cashmgtinit_bank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fstacurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_cashmgtinit_bank |  | fid |
| 2 | ix_cas_init_bank |  | forgid |

---

## 银行账户分录-子表 t_cas_cashmgbank

- **表名称：** 银行账户分录-子表
- **表名：** t_cas_cashmgbank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatementbalance | 银行对账单期初余额 | numeric | 23 | 10 | √ | 0 | 银行对账单期初余额 |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fjournalbalanceloc | 日记账期初余额本位币 | numeric | 23 | 10 | √ | 0 | 日记账期初余额本位币 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjournalcredit | 日记账本年累计付款金额 | numeric | 23 | 10 | √ | 0 | 日记账本年累计付款金额 |
| 7 | fjournalbalanceadj | 调整后日记账期初余额 | numeric | 23 | 10 | √ | 0 | 调整后日记账期初余额 |
| 8 | fjournaldebit | 日记账本年累计收款金额 | numeric | 23 | 10 | √ | 0 | 日记账本年累计收款金额 |
| 9 | fjournalcreditloc | 日记账本年累计付款本位币 | numeric | 23 | 10 | √ | 0 | 日记账本年累计付款本位币 |
| 10 | fstatementbalanceadj | 调整后银行对账单期初余额 | numeric | 23 | 10 | √ | 0 | 调整后银行对账单期初余额 |
| 11 | fquotation | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fjournalbalance | 日记账期初余额 | numeric | 23 | 10 | √ | 0 | 日记账期初余额 |
| 13 | fjournalsumbalanceadj | 调整后日记账总余额 | numeric | 23 | 10 | √ | 0 | 调整后日记账总余额 |
| 14 | fequal | 余额调节表平衡 | bpchar | 1 |  | √ | '0' | 余额调节表平衡,枚举: 0 : 1 :true |
| 15 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 19 | fjournaldebitloc | 日记账本年累计收款本位币 | numeric | 23 | 10 | √ | 0 | 日记账本年累计收款本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_cashmgbank |  | fentryid |
| 2 | idx_cas_bank_fpid |  | fid |
