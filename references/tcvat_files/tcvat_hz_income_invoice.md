# 总机构收入台账开票收入明细-tcvat_hz_income_invoice

## 总机构收入台账开票收入明细-主表 t_tcvat_hz_income_invoice

- **表名称：** 总机构收入台账开票收入明细-主表
- **表名：** t_tcvat_hz_income_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: 5 :增值税专用发票不含税收入 6 :增值税专用发票税额 |
| 9 | fsuborgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 12 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 13 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 14 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 15 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 16 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 17 | fdifferenceinvoice | 差额发票 | bpchar | 1 |  | √ | '0' | 差额发票 |
| 18 | ffiltercondition | 过滤条件设置 | varchar | 255 |  | √ | ' ' | 过滤条件设置 |
| 19 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 20 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_income_invoice |  | fsuborgid,fstartdate,fenddate |
| 2 | idx_income_invoice_fserialno |  | ftaxaccountserialno |
| 3 | pk_tcvat_hz_income_invoice |  | fid |
