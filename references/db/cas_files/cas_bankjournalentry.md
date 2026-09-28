# 银行日记账（分录）-cas_bankjournalentry

## 银行日记账（分录）-主表 t_cas_bankjournalentry

- **表名称：** 银行日记账（分录）-主表
- **表名：** t_cas_bankjournalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 银行记账单ID | int8 | 64 |  | √ | 0 | 银行记账单ID |
| 2 | famount_enp | famount_enp | text | 0 |  |  | null |  |
| 3 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 4 | flocalamount_enp | flocalamount_enp | text | 0 |  |  | null |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foppunit | 对方单位 | varchar | 255 |  |  | null | 对方单位 |
| 7 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 8 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bje_faccountbankid |  | faccountbankid |
| 2 | t_cas_bankjournalentry_pkey |  | fentryid |
| 3 | idx_cas_bje_fpid |  | fid |
