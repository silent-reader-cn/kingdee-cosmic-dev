# 任务预览-pa_taskpreview

## 任务预览-主表 t_pa_taskpreview

- **表名称：** 任务预览-主表
- **表名：** t_pa_taskpreview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstaticstatus_info | 工作任务的状态信息 | varchar | 255 |  | √ | ' ' | 工作任务的状态信息 |
| 4 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :新增 1 :进行中 2 :成功完成 9 :失败 5 :手动中断 |
| 5 | fsyncdataschemeid | 数据同步方案Id | int8 | 64 |  | √ | 0 | 数据同步方案Id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftasktype | 任务类型 | bpchar | 1 |  | √ | ' ' | 任务类型,枚举: 4 :从实体同步数据任务 |
| 8 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | fsyncschemename | 取数方案名称 | varchar | 255 |  | √ | ' ' | 取数方案名称 |
| 10 | fexecutiontime | 执行时长 | varchar | 50 |  | √ | ' ' | 执行时长 |
| 11 | fstaticstatus_info_tag | 工作任务的状态信息_详情 | text | 0 |  |  | null | 工作任务的状态信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_taskpreview |  | fid |
| 2 | idx_pa_task_preview |  | fsyncdataschemeid |
