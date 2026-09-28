# 分支进项税额抵扣统计明细-tcvat_fz_jxsedktjmx

## 分支进项税额抵扣统计明细-主表 t_tcvat_fz_jxsedktjmx

- **表名称：** 分支进项税额抵扣统计明细-主表
- **表名：** t_tcvat_fz_jxsedktjmx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 1 :增值税电子普通发票 10 :飞机票 9 :火车票 16,20 :客运票 |
| 5 | fpid | 父id | int8 | 64 |  | √ | 0 | 父id |
| 6 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | finvoiceamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 9 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_jxsedktjmx |  | fpid |
| 2 | pk_tcvat_fz_jxsedktjmx |  | fid |
