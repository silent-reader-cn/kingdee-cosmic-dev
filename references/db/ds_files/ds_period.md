# 会计期间-ds_period

## 会计期间-主表 t_ds_period

- **表名称：** 会计期间-主表
- **表名：** t_ds_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | 来源系统 ds_srcsys |
| 4 | fperiodquarter | 会计季度 | varchar | 100 |  | √ | ' ' | 会计季度 |
| 5 | fperiodnumber | 期间 | varchar | 100 |  | √ | ' ' | 期间 |
| 6 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fperiodyear | 会计年度 | varchar | 100 |  | √ | ' ' | 会计年度 |
| 8 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_period_key |  | fssid,fsoid |
| 2 | t_ds_period_pkey |  | fid |
