# 报销单的收款分录-ocmem_mc_receiventry

## 报销单的收款分录-主表 t_ocmem_mc_receentry

- **表名称：** 报销单的收款分录-主表
- **表名：** t_ocmem_mc_receentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaycustomerid | fpaycustomerid | int8 | 64 |  | √ | 0 |  |
| 3 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 4 | faccountname | faccountname | varchar | 255 |  | √ | ' ' |  |
| 5 | fpaycurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | freceivableamt | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 8 | fpaytype | fpaytype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fpayrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | freceivableamtlocal | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 11 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 12 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsettlementtypeid | fsettlementtypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mc_receentry_fid |  | fid |
| 2 | pk_ocmem_mc_receentry |  | fentryid |
