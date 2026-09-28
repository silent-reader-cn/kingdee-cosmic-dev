# 预警监控方案-bos_warnschedule

## 预警监控方案-主表 t_warn_schedule

- **表名称：** 预警监控方案-主表
- **表名：** t_warn_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | flastsynctime | 上次同步时间 | timestamp | 0 |  |  | null | 上次同步时间 |
| 3 | fbyentry | 按条件发送分录 | bpchar | 1 |  | √ | '0' | 按条件发送分录 |
| 4 | fmodeltype | fmodeltype | varchar | 30 |  | √ | 'WarnScheduleModel' |  |
| 5 | fisv | fisv | varchar | 10 |  | √ | ' ' |  |
| 6 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 7 | fmonitorfrequency | 监控频率 | varchar | 200 |  | √ | ' ' | 监控频率 |
| 8 | fplanid | 调度计划id | varchar | 36 |  | √ | ' ' | 调度计划id |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 11 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | fdata | fdata | text | 0 |  |  | null |  |
| 15 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fearlywarnid | 预警对象 | varchar | 36 |  | √ | ' ' | [业务预警对象 warn_earlywarn](../mdl_files/warn_earlywarn.md) |
| 18 | fparentid | fparentid | varchar | 36 |  | √ | ' ' |  |
| 19 | fjobid | 调度作业id | varchar | 36 |  | √ | ' ' | 调度作业id |
| 20 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 21 | fplannumber | fplannumber | varchar | 80 |  |  | ' ' |  |
| 22 | fmonitorrange | 有效期 | varchar | 50 |  | √ | ' ' | 有效期 |
| 23 | ftype | ftype | bpchar | 1 |  | √ | '0' |  |
| 24 | fstartdate | fstartdate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 25 | fenable | 方案状态 | bpchar | 1 |  | √ | '0' | 方案状态,枚举: 0 :未启用 1 :已启用 |
| 26 | fnumber | 方案编码 | varchar | 36 |  | √ | ' ' | 方案编码 |
| 27 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_schedule_fnumber |  | fnumber |
| 2 | t_warn_schedule_pkey |  | fid |

---

## 预警监控方案-多语言表 t_warn_schedule_l

- **表名称：** 预警监控方案-多语言表
- **表名：** t_warn_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_schedule_name |  | fname |
| 2 | idx_warn_schedule_fid |  | fid,flocaleid |
| 3 | t_warn_schedule_l_pkey |  | fpkid |
