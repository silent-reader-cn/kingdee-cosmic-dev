# 监控方案基础资料-warn_schedule

## 监控方案基础资料-主表 t_warn_schedule

- **表名称：** 监控方案基础资料-主表
- **表名：** t_warn_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | flastsynctime | flastsynctime | timestamp | 0 |  |  | null |  |
| 3 | fbyentry | fbyentry | bpchar | 1 |  | √ | '0' |  |
| 4 | fmodeltype | fmodeltype | varchar | 30 |  | √ | 'WarnScheduleModel' |  |
| 5 | fisv | fisv | varchar | 10 |  | √ | ' ' |  |
| 6 | fbizappid | fbizappid | varchar | 36 |  | √ | ' ' |  |
| 7 | fmonitorfrequency | fmonitorfrequency | varchar | 200 |  | √ | ' ' |  |
| 8 | fplanid | fplanid | varchar | 36 |  | √ | ' ' |  |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 11 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | fdata | fdata | text | 0 |  |  | null |  |
| 15 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fearlywarnid | fearlywarnid | varchar | 36 |  | √ | ' ' |  |
| 18 | fparentid | fparentid | varchar | 36 |  | √ | ' ' |  |
| 19 | fjobid | fjobid | varchar | 36 |  | √ | ' ' |  |
| 20 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 21 | fplannumber | fplannumber | varchar | 80 |  |  | ' ' |  |
| 22 | fmonitorrange | fmonitorrange | varchar | 50 |  | √ | ' ' |  |
| 23 | ftype | ftype | bpchar | 1 |  | √ | '0' |  |
| 24 | fstartdate | fstartdate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 25 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
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

## 监控方案基础资料-多语言表 t_warn_schedule_l

- **表名称：** 监控方案基础资料-多语言表
- **表名：** t_warn_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
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
