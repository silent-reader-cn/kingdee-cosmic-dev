# 智能审批预测结果数据-task_approval_result

## 智能审批预测结果数据-主表 t_tk_approval_result

- **表名称：** 智能审批预测结果数据-主表
- **表名：** t_tk_approval_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flimewithdrawal | 批退原因影响因子 | varchar | 300 |  | √ | ' ' | 批退原因影响因子 |
| 3 | fsimilartask | 相似任务 | varchar | 150 |  | √ | ' ' | 相似任务 |
| 4 | frealpredictresult | 实际预测结果 | varchar | 50 |  | √ | ' ' | 实际预测结果,枚举: 0 :失败 1 :成功 |
| 5 | foperation | 操作类型 | varchar | 100 |  | √ | ' ' | 操作类型 |
| 6 | fpredictpassratio | 通过/不通过概率 | numeric | 19 | 6 | √ | 0 | 通过/不通过概率 |
| 7 | frealpass | 实际是否审批通过 | bpchar | 1 |  | √ | ' ' | 实际是否审批通过 |
| 8 | fpredictresultinfo | 预测结果信息 | varchar | 255 |  | √ | ' ' | 预测结果信息 |
| 9 | fsubject | 主题 | varchar | 255 |  | √ | ' ' | 主题 |
| 10 | fbreakrule | 违规项 | varchar | 100 |  | √ | ' ' | 违规项 |
| 11 | fwithdrawal | 批退原因 | varchar | 100 |  | √ | ' ' | 批退原因 |
| 12 | flimebreakrule | 违规项影响因子 | varchar | 300 |  | √ | ' ' | 违规项影响因子 |
| 13 | frealoperation | 实际操作类型 | varchar | 50 |  | √ | ' ' | 实际操作类型 |
| 14 | frealbreakrule | 实际违规项 | varchar | 1000 |  | √ | ' ' | 实际违规项 |
| 15 | fpredictresult | 预测结果 | varchar | 255 |  | √ | ' ' | 预测结果 |
| 16 | fpredictpass | 通过/不通过 | bpchar | 1 |  | √ | '0' | 通过/不通过,枚举: 1 :通过 0 :不通过 |
| 17 | fbillnumber | 原单据编号 | varchar | 100 |  | √ | ' ' | 原单据编号 |
| 18 | fpredictresult_tag | 预测结果_详情 | text | 0 |  |  | null | 预测结果_详情 |
| 19 | frealwithdrawal | 实际批退原因 | varchar | 1000 |  | √ | ' ' | 实际批退原因 |
| 20 | faffect | 影响因素及概率 | varchar | 600 |  | √ | ' ' | 影响因素及概率 |
| 21 | fpredicttime | 预测时间 | timestamp | 0 |  |  | null | 预测时间 |
| 22 | fbillid | 原单据号 | varchar | 50 |  | √ | ' ' | 原单据号 |
| 23 | flimeoperation | 操作类型影响因子 | varchar | 300 |  | √ | ' ' | 操作类型影响因子 |
| 24 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 25 | fpredictsuccess | 是否预测成功 | bpchar | 1 |  | √ | '0' | 是否预测成功,枚举: 0 :成功 1 :无需预测 -1 :失败 -2 :异常 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_apprresult_taskid |  | ftaskid |
| 2 | pk_t_tk_approval_result |  | fid |
