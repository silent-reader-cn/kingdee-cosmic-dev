# 历史修复日志-wf_repairlog

## 历史修复日志-主表 t_wf_repairlog

- **表名称：** 历史修复日志-主表
- **表名：** t_wf_repairlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 3 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 6 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_repairlog |  | fid |
| 2 | idx_wf_repairlog_taskid |  | ftaskid |
