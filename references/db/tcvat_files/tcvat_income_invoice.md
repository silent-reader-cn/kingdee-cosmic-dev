# 收入台账开票收入明细-tcvat_income_invoice

## 收入台账开票收入明细-主表 t_tcvat_income_invoice

- **表名称：** 收入台账开票收入明细-主表
- **表名：** t_tcvat_income_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxaccountid | ftaxaccountid | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 7 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 8 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 9 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 10 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | finvoicecode | finvoicecode | varchar | 100 |  | √ | ' ' |  |
| 13 | finvoicedata | finvoicedata | timestamp | 0 |  |  | null |  |
| 14 | finvoiceno | finvoiceno | varchar | 100 |  | √ | ' ' |  |
| 15 | fmaingoodsname | fmaingoodsname | varchar | 100 |  | √ | ' ' |  |
| 16 | ffiltercondition | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 17 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 18 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 19 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 20 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 21 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 22 | ftaxruleid | ftaxruleid | int8 | 64 |  | √ | 0 |  |
| 23 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: 5 :增值税专用发票不含税收入 6 :增值税专用发票税额 |
| 24 | finvoicetype | finvoicetype | varchar | 30 |  | √ | ' ' |  |
| 25 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 26 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 27 | fdifferenceinvoice | 差额发票 | bpchar | 1 |  | √ | '0' | 差额发票 |
| 28 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_income_invoice_pkey |  | fid |
| 2 | idx_t_tcvat_income_invoice |  | forgid,ftaxperiod |
