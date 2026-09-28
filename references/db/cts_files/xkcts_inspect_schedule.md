# 巡检计划-xkcts_inspect_schedule

## 单据体-子表 t_xkinsp_schedentry

- **表名称：** 单据体-子表
- **表名：** t_xkinsp_schedentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 3 | fparamids | 参数ids | varchar | 255 |  | √ | ' ' | 参数ids |
| 4 | fparamids_tag | 参数ids_详情 | text | 0 |  |  | ' ' | 参数ids_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_schedentry |  | fentryid |
| 2 | idx_schedentry_fid |  | fid,fseq |

---

## 巡检计划-多语言表 t_xkinsp_schedule_l

- **表名称：** 巡检计划-多语言表
- **表名：** t_xkinsp_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 计划名称 | varchar | 200 |  | √ | ' ' | 计划名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 计划描述 | varchar | 200 |  | √ | ' ' | 计划描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_schedule_l |  | fpkid |
| 2 | idx_xkinsp_schedule_l |  | fid,flocaleid |

---

## 巡检计划-主表 t_xkinsp_schedule

- **表名称：** 巡检计划-主表
- **表名：** t_xkinsp_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 计划名称 | varchar | 200 |  | √ | ' ' | 计划名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finspectjobid | 巡检任务 | int8 | 64 |  | √ | 0 | [巡检任务 xkcts_inspectjob](../cts_files/xkcts_inspectjob.md) |
| 7 | fdescription | 计划描述 | varchar | 200 |  | √ | ' ' | 计划描述 |
| 8 | frepeatmode | 重复时间单位 | varchar | 50 |  | √ | ' ' | 重复时间单位,枚举: n :不重复 mi :分钟 h :小时 d :天 w :星期 m :月 y :年 def :自定义 |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftypeid | 巡检分类 | int8 | 64 |  | √ | 0 | [巡检业务分类 xkcts_inspectitemtype](../cts_files/xkcts_inspectitemtype.md) |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fscheduleid | 关联调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 17 | fenable | 计划状态 | bpchar | 1 |  | √ | '0' | 计划状态,枚举: 0 :未启用 1 :已启用 |
| 18 | fnumber | 计划编码 | varchar | 30 |  | √ | ' ' | 计划编码 |
| 19 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 20 | fdesc | 调度计划示例 | varchar | 2000 |  | √ | ' ' | 调度计划示例 |
| 21 | fcyclenum | 重复周期 | int8 | 64 |  | √ | 0 | 重复周期 |
| 22 | fplan | cron表达式 | varchar | 100 |  | √ | ' ' | cron表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_schedule |  | fid |
| 2 | idx_xkinsp_schedule_type |  | ftypeid |
| 3 | idx_xkinsp_schedule_job |  | finspectjobid |
