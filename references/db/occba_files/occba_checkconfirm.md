# 数据确认表-occba_checkconfirm

## 数据确认表-主表 t_occba_checkconfirm

- **表名称：** 数据确认表-主表
- **表名：** t_occba_checkconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckamount | 确认金额 | numeric | 23 | 10 | √ | 0 | 确认金额 |
| 3 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fcheckerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fsrcbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型 |
| 7 | fchecktime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_checkconfirm_sbno |  | fsrcbillno |
| 2 | idx_occba_checkconfirm_sbid |  | fsrcbillid |
| 3 | pk_t_occba_checkconfirm |  | fid |
