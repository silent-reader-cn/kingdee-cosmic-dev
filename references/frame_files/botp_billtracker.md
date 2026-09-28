# 单据关联关系-botp_billtracker

## 单据关联关系-主表 t_botp_billtracker

- **表名称：** 单据关联关系-主表
- **表名：** t_botp_billtracker

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbillid | 目标单内码 | int8 | 64 |  |  | null | 目标单内码 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fttableid | 目标单类型 | int8 | 64 |  |  | null | 目标单类型 |
| 6 | fstableid | 源单类型 | int8 | 64 |  |  | null | 源单类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_billtracker_tid |  | ftbillid |
| 2 | idx_botp_billtracker_sid |  | fsbillid |
| 3 | t_botp_billtracker_pkey |  | fid |
