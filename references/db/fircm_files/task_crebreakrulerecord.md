# 信用--任务审批违规记录-task_crebreakrulerecord

## 信用--任务审批违规记录-主表 t_tk_crebreakrulerecord

- **表名称：** 信用--任务审批违规记录-主表
- **表名：** t_tk_crebreakrulerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbreakrule | 审批通过但有违规 | int8 | 64 |  | √ | 0 | [减分规则--违规减分 task_creditbybreakrule](../som_files/task_creditbybreakrule.md) |
| 3 | fhistaskid | 历史任务id | int8 | 64 |  | √ | 0 | 历史任务id |
| 4 | fsubscorerule | 审核信用扣分规则 | int8 | 64 |  | √ | 0 | [审核扣分规则 fircm_subscorerule](../fircm_files/fircm_subscorerule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_crebreakrulerecord_pkey |  | fid |
| 2 | idx_ssc_br_record_fhistaskid |  | fhistaskid |
