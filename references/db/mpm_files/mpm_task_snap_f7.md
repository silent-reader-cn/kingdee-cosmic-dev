# 项目任务快照F7-mpm_task_snap_f7

## 项目任务快照F7-多语言表 t_mpm_task_snap_l

- **表名称：** 项目任务快照F7-多语言表
- **表名：** t_mpm_task_snap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 4 | ftaskstatusinwf | 任务状态(流程中) | varchar | 50 |  | √ | ' ' | 任务状态(流程中) |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_task_snap_l |  | fpkid |
| 2 | idx_mpmc_tasksnap_l_id |  | fid |

---

## 项目任务快照F7-分表 t_mpm_task_snap_a

- **表名称：** 项目任务快照F7-分表
- **表名：** t_mpm_task_snap_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmode | fplanmode | varchar | 50 |  | √ | ' ' |  |
| 3 | fpublishstatus | 发布状态 | varchar | 50 |  | √ | ' ' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 4 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |
| 5 | fcalcduration | fcalcduration | numeric | 23 | 10 | √ | 0 |  |
| 6 | frelatedbasetaskid | 关联基础任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 7 | frelparentmilestoneid | frelparentmilestoneid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctaskid | fsrctaskid | int8 | 64 |  | √ | 0 |  |
| 9 | frelplmprojecth | frelplmprojecth | varchar | 512 |  | √ | ' ' |  |
| 10 | fsourcetype | 任务类别 | varchar | 50 |  | √ | ' ' | 任务类别,枚举: A :任务 B :模板任务 |
| 11 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 12 | fcooperatestatus | fcooperatestatus | varchar | 50 |  | √ | ' ' |  |
| 13 | fiskeytask | fiskeytask | bpchar | 1 |  | √ | '0' |  |
| 14 | fplanversionid | fplanversionid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_planversionid |  | fplanversionid |
| 2 | pk_t_mpm_task_snap_a |  | fid |

---

## 项目任务快照F7-主表 t_mpm_task_snap

- **表名称：** 项目任务快照F7-主表
- **表名：** t_mpm_task_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaststartdate | flaststartdate | timestamp | 0 |  |  | null |  |
| 3 | fisleaf | 叶节点 | bpchar | 1 |  | √ | '0' | 叶节点 |
| 4 | ftaskseq | 顺序号(已废弃) | int8 | 64 |  | √ | 0 | 顺序号(已废弃) |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | fdeviationrate | fdeviationrate | numeric | 23 | 10 | √ | 0 |  |
| 7 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 10 | ftaskstatusinwf | 任务状态(流程中) | varchar | 50 |  | √ | ' ' | 任务状态(流程中) |
| 11 | flastenddate | flastenddate | timestamp | 0 |  |  | null |  |
| 12 | fassignerid | fassignerid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 项目任务号 | varchar | 30 |  | √ | ' ' | 项目任务号 |
| 14 | fcopysrcid | fcopysrcid | int8 | 64 |  | √ | 0 |  |
| 15 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 19 | flockdate | flockdate | bpchar | 1 |  | √ | '0' |  |
| 20 | freporthours | freporthours | numeric | 23 | 10 | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | fsrctype | fsrctype | varchar | 50 |  | √ | ' ' |  |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | ftimeunit | ftimeunit | varchar | 50 |  | √ | ' ' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fprojectphaseid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 27 | fpriority | fpriority | varchar | 50 |  | √ | ' ' |  |
| 28 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 29 | fprjapprovalbillid | fprjapprovalbillid | int8 | 64 |  | √ | 0 |  |
| 30 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | [任务业务类型 mpm_taskcntrcode](../mpm_files/mpm_taskcntrcode.md) |
| 31 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 34 | fschedule | fschedule | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 36 | fdurationsec | fdurationsec | numeric | 23 | 10 | √ | 0 |  |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 39 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 40 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |
| 42 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 43 | fganttid | fganttid | varchar | 50 |  | √ | ' ' |  |
| 44 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 45 | fassigntime | fassigntime | timestamp | 0 |  |  | null |  |
| 46 | fplanhours | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 47 | fduration | fduration | numeric | 23 | 10 | √ | 0 |  |
| 48 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 49 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |
| 50 | frootid | 根节点 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_task_snap |  | fid |
| 2 | idx_mpmc_projectid |  | fprojectid |
