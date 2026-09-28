# 对账关联关系-pur_checkrelation

## 对账关联关系-主表 t_pur_checkrelation

- **表名称：** 对账关联关系-主表
- **表名：** t_pur_checkrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpoentryid | 源订单分录id | varchar | 50 |  | √ | ' ' | 源订单分录id |
| 3 | fqty | 反写数量 | numeric | 23 | 10 | √ | 0.000000 | 反写数量 |
| 4 | fsrcid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 5 | fsrcentitykey | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 6 | fsrcentryid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftarentryid | 目标单分录id | int8 | 64 |  | √ | 0 | 目标单分录id |
| 9 | ftarid | 目标单id | varchar | 50 |  | √ | ' ' | 目标单id |
| 10 | ftarentitykey | 目标单标识 | varchar | 50 |  | √ | ' ' | 目标单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_checkrelation_pkey |  | fid |
| 2 | idx_pur_cr_ftarentryid |  | ftarentryid |
| 3 | idx_pur_cr_fsrcentryid |  | fsrcentryid |
