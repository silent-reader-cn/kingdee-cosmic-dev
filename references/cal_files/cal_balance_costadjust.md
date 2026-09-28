# 期末余额汇总出单表-cal_balance_costadjust

## 期末余额汇总出单表-主表 t_cal_balance_costadjust

- **表名称：** 期末余额汇总出单表-主表
- **表名：** t_cal_balance_costadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostadjustbillno | 成本调整单据编号 | varchar | 80 |  | √ | ' ' | 成本调整单据编号 |
| 3 | fexportflag | 出单标识 | bpchar | 1 |  | √ | '0' | 出单标识 |
| 4 | fbalanceid | 核算余额表id | int8 | 64 |  | √ | 0 | 核算余额表id |
| 5 | fcostadjustbillid | 成本调整单id | int8 | 64 |  | √ | 0 | 成本调整单id |
| 6 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_balance_costadjust_pkey |  | fid |
| 2 | idx_cal_balcostad_balid |  | fbalanceid |
