# 付款计划-fa_lease_pay_plan

## 付款计划-主表 t_fa_lease_pay_plan

- **表名称：** 付款计划-主表
- **表名：** t_fa_lease_pay_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 当前关联合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 2 | fdiscountdays | fdiscountdays | int4 | 32 |  | √ | 0 |  |
| 3 | frealpayamount | 实际付款金额 | numeric | 19 | 4 | √ | 0 | 实际付款金额 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 4 | √ | 0.0000 | 税率(%) |
| 5 | fdiscountdays2 | fdiscountdays2 | int4 | 32 |  | √ | 0 |  |
| 6 | fpresentvalue2 | fpresentvalue2 | numeric | 19 | 4 | √ | 0.0000 |  |
| 7 | fplanunpay | 计划未付金额 | numeric | 19 | 4 | √ | 0 | 计划未付金额 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fpushedamount | 已下推金额 | numeric | 19 | 4 | √ | 0 | 已下推金额 |
| 10 | fenddate | 受益期结束日 | timestamp | 0 |  |  | null | 受益期结束日 |
| 11 | fdiscountfactor2 | fdiscountfactor2 | numeric | 19 | 4 | √ | 0.0000 |  |
| 12 | frealunpay | 实际未付金额 | numeric | 19 | 4 | √ | 0 | 实际未付金额 |
| 13 | fentrysrcid | fentrysrcid | int8 | 64 |  | √ | 0 |  |
| 14 | fpresentvalue | fpresentvalue | numeric | 19 | 4 | √ | 0.0000 |  |
| 15 | fdiscountfactor | fdiscountfactor | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fownerorgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fpayitemid | 付款项目 | int8 | 64 |  | √ | 0 | [付款项目 fa_payment_item](../xkzlzc_files/fa_payment_item.md) |
| 18 | frentwithtax | 计划付款金额 | numeric | 19 | 4 | √ | 0.0000 | 计划付款金额 |
| 19 | fcontractsrcid | 源合同号 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 20 | fplanstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fplannumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |
| 22 | finvoicetype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: A :专用发票 B :普通发票 |
| 23 | ftax | 税额 | numeric | 19 | 4 | √ | 0.0000 | 税额 |
| 24 | fstartdate | 受益期开始日 | timestamp | 0 |  |  | null | 受益期开始日 |
| 25 | fdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fplanpaydate | 计划付款日 | timestamp | 0 |  |  | LOCALTIMESTAMP | 计划付款日 |
| 29 | frentnotax | 不含税金额 | numeric | 19 | 4 | √ | 0.0000 | 不含税金额 |
| 30 | funpaidrent | funpaidrent | numeric | 19 | 4 | √ | 0.0000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_pay_plan_fk |  | fid |
| 2 | t_fa_lease_pay_plan_pkey |  | fentryid |
