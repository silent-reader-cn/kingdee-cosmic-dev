# 单据发票关系-sim_bill_inv_relation

## 单据发票关系-主表 t_sim_bill_inv_relation

- **表名称：** 单据发票关系-主表
- **表名：** t_sim_bill_inv_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisdelete | 是否删除 | varchar | 50 |  | √ | ' ' | 是否删除,枚举: Y :是 N :否 |
| 3 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 4 | fsbillno | 源单单据编号 | varchar | 50 |  | √ | ' ' | 源单单据编号 |
| 5 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftbillid | 发票id | int8 | 64 |  | √ | 0 | 发票id |
| 8 | ftdetailid | 发票明细id | int8 | 64 |  | √ | 0 | 发票明细id |
| 9 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 10 | fpushtype | 下推类型 | varchar | 50 |  | √ | ' ' | 下推类型,枚举: 1 :下推 -1 :关联 |
| 11 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 12 | fsbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 13 | ftbillno | 目标单单据编号 | varchar | 50 |  | √ | ' ' | 目标单单据编号 |
| 14 | fttable | 目标单类型 | varchar | 50 |  | √ | ' ' | 目标单类型,枚举: sim_vatinvoice :待开 sim_red_info :红字信息表 |
| 15 | fsdetailid | 源单明细id | int8 | 64 |  | √ | 0 | 源单明细id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_bill_inv_tbillid |  | ftbillid |
| 2 | pk_t_sim_bill_inv_relation |  | fid |
| 3 | idx_sim_bill_inv_sbillid |  | fsbillid |
