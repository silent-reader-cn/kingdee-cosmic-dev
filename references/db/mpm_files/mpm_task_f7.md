# 项目任务F7-mpm_task_f7

## 项目任务F7-主表 t_mpm_task

- **表名称：** 项目任务F7-主表
- **表名：** t_mpm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaststartdate | flaststartdate | timestamp | 0 |  |  | null |  |
| 3 | fisleaf | 叶节点 | bpchar | 1 |  | √ | '1' | 叶节点 |
| 4 | ftaskseq | 顺序号(已废弃) | int4 | 32 |  | √ | 0 | 顺序号(已废弃) |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | fdeviationrate | fdeviationrate | numeric | 23 | 10 | √ | 0 |  |
| 7 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplanedhours | fplanedhours | numeric | 23 | 10 | √ | 0 |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 11 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 12 | flastenddate | flastenddate | timestamp | 0 |  |  | null |  |
| 13 | fassignerid | fassignerid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 项目任务号 | varchar | 80 |  | √ | ' ' | 项目任务号 |
| 15 | fcopysrcid | fcopysrcid | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 20 | flockdate | flockdate | bpchar | 1 |  | √ | '0' |  |
| 21 | freporthours | freporthours | numeric | 23 | 10 | √ | 0 |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fsrctype | fsrctype | bpchar | 1 |  | √ | ' ' |  |
| 24 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 25 | ftimeunit | ftimeunit | bpchar | 1 |  | √ | 'A' |  |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 27 | fprojectphaseid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 28 | fpriority | fpriority | bpchar | 1 |  | √ | ' ' |  |
| 29 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 30 | fprjapprovalbillid | fprjapprovalbillid | int8 | 64 |  | √ | 0 |  |
| 31 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | [任务业务类型 mpm_taskcntrcode](../mpm_files/mpm_taskcntrcode.md) |
| 32 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 35 | fschedule | fschedule | numeric | 23 | 10 | √ | 0 |  |
| 36 | fsrcbillentity | fsrcbillentity | varchar | 80 |  | √ | ' ' |  |
| 37 | fdurationsec | fdurationsec | numeric | 23 | 10 | √ | 0 |  |
| 38 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fganttid | fganttid | varchar | 36 |  | √ | ' ' |  |
| 45 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 46 | fassigntime | fassigntime | timestamp | 0 |  |  | null |  |
| 47 | fplanhours | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 48 | fduration | fduration | numeric | 23 | 10 | √ | 0 |  |
| 49 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 50 | frootid | 根节点 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 51 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |

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
| 2 | fplanmode | fplanmode | bpchar | 1 |  | √ | 'A' |  |
| 3 | fpublishstatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 4 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |
| 5 | frelplmprojecth | frelplmprojecth | varchar | 512 |  | √ | ' ' |  |
| 6 | fsourcetype | 任务类别 | bpchar | 1 |  | √ | 'A' | 任务类别,枚举: A :任务 B :模板任务 |
| 7 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 8 | fcooperatestatus | fcooperatestatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fcalcduration | fcalcduration | numeric | 23 | 10 | √ | 0 |  |
| 10 | frelatedbasetaskid | 关联基础任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 11 | fiskeytask | fiskeytask | bpchar | 1 |  | √ | '0' |  |
| 12 | frelparentmilestoneid | frelparentmilestoneid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_task_a |  | fid |
| 2 | idx_mpm_task_atask |  | frelatedbasetaskid |
| 3 | pk_mpm_task_a |  | fid |

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
