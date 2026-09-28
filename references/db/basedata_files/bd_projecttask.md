# 项目任务-bd_projecttask

## 项目任务-主表 t_bd_projecttask

- **表名称：** 项目任务-主表
- **表名：** t_bd_projecttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |
| 3 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 bd_tasktype](../basedata_files/bd_tasktype.md) |
| 5 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsourceid | 来源任务id | int8 | 64 |  | √ | 0 | 来源任务id |
| 7 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 8 | frelparentmilestoneid | 父项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 12 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 16 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fstatustype | 状态类型 | int8 | 64 |  | √ | 0 | [状态类型 bd_statustype](../basedata_files/bd_statustype.md) |
| 22 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 25 | frootid | 根节点 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 26 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 项目任务号 | varchar | 80 |  | √ | ' ' | 项目任务号 |
| 29 | fprojectphaseid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_projecttask_root |  | frootid |
| 2 | idx_bd_projecttask_parent |  | fparentid |
| 3 | pk_bd_projecttask |  | fid |
| 4 | idx_bd_projecttask_number |  | fnumber |
| 5 | idx_bd_projecttask_prj |  | fprojectid |

---

## 项目任务-多语言表 t_bd_projecttask_l

- **表名称：** 项目任务-多语言表
- **表名：** t_bd_projecttask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 3 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_projtask_l |  | fid,flocaleid |
| 2 | pk_bd_projecttask_l |  | fpkid |
