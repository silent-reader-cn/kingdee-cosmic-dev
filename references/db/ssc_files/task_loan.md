# 个人借款-task_loan

## 个人借款-主表 t_tk_taskloan

- **表名称：** 个人借款-主表
- **表名：** t_tk_taskloan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frateprecision | 汇率精度 | int8 | 64 |  | √ | 0 | 汇率精度 |
| 3 | feasid | easid | varchar | 44 |  | √ | ' ' | easid |
| 4 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | famountbalance | 本位币可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币可用余额 |
| 6 | famountbalanceori | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 7 | fexpensetype | 费用类型 | varchar | 100 |  | √ | ' ' | 费用类型 |
| 8 | fcause | 事由 | varchar | 2000 |  | √ | ' ' | 事由 |
| 9 | frateconvertmode | 汇率折算方式 | bpchar | 1 |  | √ | ' ' | 汇率折算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | frate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 0 :任务数据 1 :导入数据 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | famountused | famountused | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fentryid | 分录ID | varchar | 44 |  | √ | ' ' | 分录ID |
| 16 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_taskloan_pkey |  | fid |
| 2 | index_ssc_taskload |  | feasid |
