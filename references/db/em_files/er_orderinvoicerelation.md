# 订单发票关联表-er_orderinvoicerelation

## 订单发票关联表-主表 t_er_orderinvoicerelation

- **表名称：** 订单发票关联表-主表
- **表名：** t_er_orderinvoicerelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forderid | 订单id | int8 | 64 |  | √ | 0 | 订单id |
| 3 | finvoiceid | 发票id | int8 | 64 |  | √ | 0 | 发票id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_orderinvoicerelation_pkey |  | fid |
| 2 | idx_er_ordinvrel_ordid_invid |  | forderid,finvoiceid |
