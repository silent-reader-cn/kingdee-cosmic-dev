# 任务流程操作记录-mpm_task_operate_log

## 任务流程操作记录-主表 t_mpm_taskoplog

- **表名称：** 任务流程操作记录-主表
- **表名：** t_mpm_taskoplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjectid | fbizobjectid | varchar | 80 |  | √ | ' ' |  |
| 3 | foptime | foptime | timestamp | 0 |  |  | null |  |
| 4 | foptype | 操作类型 | bpchar | 1 |  | √ | 'A' | 操作类型 |
| 5 | fobjectid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | frelationbillid | frelationbillid | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskoplog |  | fid |
| 2 | idx_mpm_taskoplog_fi |  | fobjectid |
