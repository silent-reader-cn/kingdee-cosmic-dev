# 预缴分支收入台账开票收入明细-tcvat_fz_pre_in_invoice

## 预缴分支收入台账开票收入明细-主表 t_tcvat_fz_pre_in_invoice

- **表名称：** 预缴分支收入台账开票收入明细-主表
- **表名：** t_tcvat_fz_pre_in_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 9 | ffiltercondition | 过滤条件设置 | varchar | 255 |  | √ | ' ' | 过滤条件设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_pre_in_invoice |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_fz_pre_in_invoice |  | fid |
