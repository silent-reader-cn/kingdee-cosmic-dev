# 重算节点信息-cal_recal_point

## 重算节点信息-主表 t_cal_recal_point

- **表名称：** 重算节点信息-主表
- **表名：** t_cal_recal_point

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 3 | fendid | 单据截止ID | int8 | 64 |  | √ | 0 | 单据截止ID |
| 4 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :已确认 B :待处理 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fruleid | 余额规则 | varchar | 30 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_bal_rp_rid |  | fruleid |
| 2 | pk_cal_recal_point |  | fid |
