# 组件任务监控-fpy_relation_task

## 组件任务监控-主表 tk_fpy_relation_task

- **表名称：** 组件任务监控-主表
- **表名：** tk_fpy_relation_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_source | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 3 | fk_fpy_end_time | 关联结束时间 | timestamp | 0 |  |  | null | 关联结束时间 |
| 4 | fk_fpy_combofield | 关联状态 | varchar | 50 |  | √ | ' ' | 关联状态,枚举: 1 :关联中 2 :关联完成 3 :关联异常 |
| 5 | fk_fpy_progress | 关联进度 | varchar | 50 |  | √ | ' ' | 关联进度 |
| 6 | fk_fpy_task_no | 组件批次号 | varchar | 50 |  | √ | ' ' | 组件批次号 |
| 7 | fk_fpy_datetimefield | 关联开始时间 | timestamp | 0 |  |  | null | 关联开始时间 |
| 8 | fk_fpy_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fk_fpy_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fk_fpy_result_desc | 关联结果描述 | varchar | 1000 |  | √ | ' ' | 关联结果描述 |
| 11 | fk_eafc_arcorg | 创建人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 12 | fk_fpy_targets | 目标单据类型 | varchar | 200 |  | √ | ' ' | 目标单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_relation_task |  | fid |
