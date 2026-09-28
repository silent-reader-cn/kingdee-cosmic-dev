# 现金日记账（分录）-cas_cashjournalentry

## 现金日记账（分录）-主表 t_cas_cashjournalentry

- **表名称：** 现金日记账（分录）-主表
- **表名：** t_cas_cashjournalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 现金记账单ID | int8 | 64 |  | √ | 0 | 现金记账单ID |
| 2 | famount_enp | famount_enp | text | 0 |  |  | null |  |
| 3 | faccountcashid | 账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 4 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 5 | flocalamount_enp | flocalamount_enp | text | 0 |  |  | null |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | foppunit | 对方单位 | varchar | 255 |  |  | null | 对方单位 |
| 8 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 9 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 10 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cje_fpid |  | fid |
| 2 | t_cas_cashjournalentry_pkey |  | fentryid |
