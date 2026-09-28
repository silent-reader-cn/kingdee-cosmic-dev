# 总机构进项税额抵扣统计明细-tcvat_hz_deduct_cou_det

## 总机构进项税额抵扣统计明细-主表 t_tcvat_hz_deduct_cou_det

- **表名称：** 总机构进项税额抵扣统计明细-主表
- **表名：** t_tcvat_hz_deduct_cou_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 1 :增值税电子普通发票 10 :飞机票 9 :火车票 16 :汽车票 20 :轮船票 |
| 4 | fpid | 父id | int8 | 64 |  | √ | 0 | 父id |
| 5 | finvoiceamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 7 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_deduct_cou_det |  | fid |
| 2 | idx_tcvat_hz_deduct_cou_det |  | fpid |
