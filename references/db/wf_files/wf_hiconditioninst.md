# 历史条件规则实例-wf_hiconditioninst

## 历史条件规则实例-主表 t_wf_hiconditioninst

- **表名称：** 历史条件规则实例-主表
- **表名：** t_wf_hiconditioninst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factinstid | 活动实例ID | int8 | 64 |  | √ | 0 | 活动实例ID |
| 3 | fexpression | 表达式 | text | 0 |  |  | null | 表达式 |
| 4 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | factivityid | 活动节点ID | varchar | 255 |  | √ | ' ' | 活动节点ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | flogmsg | 条件执行明细 | text | 0 |  |  | null | 条件执行明细 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 11 | fconditionalruleid | 条件规则ID | int8 | 64 |  | √ | 0 | 条件规则ID |
| 12 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 13 | fkey | 关联key | varchar | 500 |  | √ | ' ' | 关联key |
| 14 | fbusinesskey | 单据id | varchar | 150 |  | √ | ' ' | 单据id |
| 15 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 16 | fversion | 版本 | varchar | 36 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hiconditioninst_pkey |  | fid |
| 2 | idx_wf_hiconditioninst_proc |  | fprocinstid |
| 3 | idx_wf_hicondinst_buskeyactid |  | fbusinesskey,factivityid |
