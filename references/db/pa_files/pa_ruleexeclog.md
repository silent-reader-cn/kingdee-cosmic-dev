# 执行规则日志-pa_ruleexeclog

## 执行规则日志-主表 t_pa_ruleexeclog

- **表名称：** 执行规则日志-主表
- **表名：** t_pa_ruleexeclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 3 | fexecution_status | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :新增 1 :进行中 2 :成功 9 :失败 |
| 4 | frule_type | 规则类型 | bpchar | 1 |  | √ | '1' | 规则类型,枚举: A :推导 B :分摊 |
| 5 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 6 | fexecution_logid | 执行日志id | int8 | 64 |  | √ | 0 | 执行日志id |
| 7 | fexecution_time | 日期 | timestamp | 0 |  |  | null | 日期 |
| 8 | fdetailtime | 详细时间 | int8 | 64 |  | √ | 0 | 详细时间 |
| 9 | frule_id | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_ruleexeclog |  | fid |
| 2 | idx_pa_rule_execution_log_1 |  | fexecution_logid |
