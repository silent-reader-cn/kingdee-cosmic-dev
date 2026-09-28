# 余额快照表-cal_balance_snapshoot

## 余额快照表-主表 t_cal_snapshootbalance

- **表名称：** 余额快照表-主表
- **表名：** t_cal_snapshootbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fheadid | 成本记录ID/余额表ID | int8 | 64 |  | √ | 0 | 成本记录ID/余额表ID |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 7 | fmainid | 成本记录结转明细ID/余额表结转明细ID | int8 | 64 |  | √ | 0 | 成本记录结转明细ID/余额表结转明细ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_bal_snap_creid |  | fmainid |
| 2 | t_cal_snapshootbalance_pkey |  | fid |
