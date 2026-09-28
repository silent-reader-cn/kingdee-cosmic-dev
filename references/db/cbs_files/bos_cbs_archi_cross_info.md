# 迁移信息（中间表）-bos_cbs_archi_cross_info

## 迁移信息（中间表）-主表 t_cbs_archi_cross_info

- **表名称：** 迁移信息（中间表）-主表
- **表名：** t_cbs_archi_cross_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 3 | ftasktype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: archive :归档转储 unarchive :反归档 |
| 4 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 5 | fscheduleid | 调度id | int8 | 64 |  | √ | 0 | 调度id |
| 6 | fconfigid | 单据配置id | int8 | 64 |  | √ | 0 | 单据配置id |
| 7 | farchiveroute | 归档库 | varchar | 50 |  | √ | ' ' | 归档库 |
| 8 | fcleanstatus | 中间表清理状态 | bpchar | 1 |  | √ | ' ' | 中间表清理状态,枚举: 0 :未清理 1 :清理中 2 :已清理 |
| 9 | fdatabase_type | 归档库类型 | varchar | 50 |  | √ | ' ' | 归档库类型,枚举: db :数据库 es :Elasticsearch |
| 10 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | fbatchnum | 调度任务号 | varchar | 50 |  | √ | ' ' | 调度任务号 |
| 12 | ftotalcount | 迁移数据量 | int8 | 64 |  | √ | 0 | 迁移数据量 |
| 13 | freversestatus | 反归档状态 | bpchar | 1 |  | √ | ' ' | 反归档状态,枚举: 0 :已归档 1 :反归档迁移中 2 :已反归档 |
| 14 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_cross_info |  | fid |
| 2 | idx_cbs_archi_cross_info |  | fentitynumber,farchiveroute |
