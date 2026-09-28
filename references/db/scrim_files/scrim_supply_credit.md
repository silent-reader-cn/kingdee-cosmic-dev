# 供应商信用表-scrim_supply_credit

## 供应商信用表-主表 t_scrim_supply_credit

- **表名称：** 供应商信用表-主表
- **表名：** t_scrim_supply_credit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fcreditscore | 信用评分 | numeric | 19 | 6 | √ | 0 | 信用评分 |
| 5 | fcreditrecord | 信用记录 | varchar | 100 |  |  | null | 信用记录 |
| 6 | fsupplyname | 供应商名称 | varchar | 256 |  | √ | ' ' | 供应商名称 |
| 7 | fposition | 位置 | varchar | 100 |  |  | null | 位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_supply_credit |  | fid |
| 2 | idx_credit_supplyname |  | fsupplyname |
