# 项目任务F7-mpm_task_f7

## 项目任务F7-主表 t_mpm_task

- **表名称：** 项目任务F7-主表
- **表名：** t_mpm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaststartdate | flaststartdate | timestamp | 0 |  |  | null |  |
| 3 | fisleaf | fisleaf | bpchar | 1 |  | √ | '1' |  |
| 4 | ftaskseq | 顺序号(已废弃) | int4 | 32 |  | √ | 0 | 顺序号(已废弃) |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | fdeviationrate | fdeviationrate | numeric | 23 | 10 | √ | 0 |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 10 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 11 | flastenddate | flastenddate | timestamp | 0 |  |  | null |  |
| 12 | fassignerid | fassignerid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 项目任务号 | varchar | 80 |  | √ | ' ' | 项目任务号 |
| 14 | fcopysrcid | fcopysrcid | int8 | 64 |  | √ | 0 |  |
| 15 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 19 | flockdate | flockdate | bpchar | 1 |  | √ | '0' |  |
| 20 | freporthours | freporthours | numeric | 23 | 10 | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | fsrctype | fsrctype | bpchar | 1 |  | √ | ' ' |  |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | ftimeunit | ftimeunit | bpchar | 1 |  | √ | 'A' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fprojectphaseid | 阶段 | int8 | 64 |  | √ | 0 | 项目阶段 mpm_projectphase |
| 27 | fpriority | fpriority | bpchar | 1 |  | √ | ' ' |  |
| 28 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 29 | fprjapprovalbillid | fprjapprovalbillid | int8 | 64 |  | √ | 0 |  |
| 30 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | 任务业务类型 mpm_taskcntrcode |
| 31 | frelprojectid | 关联子项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 34 | fschedule | fschedule | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbillentity | fsrcbillentity | varchar | 80 |  | √ | ' ' |  |
| 36 | fdurationsec | fdurationsec | numeric | 23 | 10 | √ | 0 |  |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 39 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 40 | fmanagerid | fmanagerid | int8 | 64 |  | √ | 0 |  |
| 41 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 42 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 43 | fganttid | fganttid | varchar | 36 |  | √ | ' ' |  |
| 44 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 45 | fassigntime | fassigntime | timestamp | 0 |  |  | null |  |
| 46 | fplanhours | fplanhours | numeric | 23 | 10 | √ | 0 |  |
| 47 | fduration | fduration | numeric | 23 | 10 | √ | 0 |  |
| 48 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | 任务状态 mpm_taskstatus |
| 49 | frootid | 根节点 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 50 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_task_fbillno |  | fbillno,fcreateorgid |
| 2 | idx_mpm_task_fparent |  | fparentid |
| 3 | idx_mpm_task_froot |  | frootid |
| 4 | pk_mpm_task |  | fid |
| 5 | idx_mpm_task_fprj |  | fprojectid |

---

## 项目任务F7-分表 t_mpm_task_a

- **表名称：** 项目任务F7-分表
- **表名：** t_mpm_task_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_task_a |  | fid |
| 2 | pk_mpm_task_a |  | fid |

---

## 项目任务F7-多语言表 t_mpm_task_l

- **表名称：** 项目任务F7-多语言表
- **表名：** t_mpm_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 4 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_task_l |  | fpkid |
| 2 | idx_mpm_task_l |  | fid,flocaleid |
