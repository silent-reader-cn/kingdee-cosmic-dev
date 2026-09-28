# 费用分摊累加费用分摊-cal_fee_totalsharefee

## 费用分摊累加费用分摊-主表 t_cal_totalsharefee

- **表名称：** 费用分摊累加费用分摊-主表
- **表名：** t_cal_totalsharefee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffeeshareid | 分摊记录id | int8 | 64 |  | √ | 0 | 分摊记录id |
| 3 | fcostrecordentryid | 核算成本记录分录id | int8 | 64 |  | √ | 0 | 核算成本记录分录id |
| 4 | ftotalfee | 累加分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累加分摊金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_totalsharefee_pkey |  | fid |
| 2 | idx_cal_totalsharefee_sid |  | ffeeshareid |
