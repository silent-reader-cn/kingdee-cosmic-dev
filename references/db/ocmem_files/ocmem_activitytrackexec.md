# 活动执行记录（分录）-ocmem_activitytrackexec

## 活动执行记录（分录）-主表 t_ocmem_activitytrackexec

- **表名称：** 活动执行记录（分录）-主表
- **表名：** t_ocmem_activitytrackexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicture7 | 图片7 | varchar | 255 |  | √ | ' ' | 图片7 |
| 3 | fpicture6 | 图片6 | varchar | 255 |  | √ | ' ' | 图片6 |
| 4 | fpicture5 | 图片5 | varchar | 255 |  | √ | ' ' | 图片5 |
| 5 | ftracktime | 实际执行时间 | timestamp | 0 |  |  | null | 实际执行时间 |
| 6 | fpicture4 | 图片4 | varchar | 255 |  | √ | ' ' | 图片4 |
| 7 | fpicture3 | 图片3 | varchar | 255 |  | √ | ' ' | 图片3 |
| 8 | fpicture2 | 图片2 | varchar | 255 |  | √ | ' ' | 图片2 |
| 9 | fpicture1 | 图片1 | varchar | 255 |  | √ | ' ' | 图片1 |
| 10 | factivityplanld | 活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 11 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 12 | fdescription | 执行跟踪说明 | varchar | 500 |  | √ | ' ' | 执行跟踪说明 |
| 13 | ftrackuserid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frecordid | 活动执行id | int8 | 64 |  | √ | 0 | 活动执行id |
| 15 | fnexttracktime | 下次跟踪时间 | timestamp | 0 |  |  | null | 下次跟踪时间 |
| 16 | fpicture8 | 图片8 | varchar | 255 |  | √ | ' ' | 图片8 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activitytrackexec |  | fid |
| 2 | idx_ocmem_activitytrackexec_01 |  | factivityplanld |
