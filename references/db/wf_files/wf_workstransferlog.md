# 工作移交日志-wf_workstransferlog

## 工作移交日志-主表 t_wf_workstransferlog

- **表名称：** 工作移交日志-主表
- **表名：** t_wf_workstransferlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigauditorname | 原审批人员名称 | varchar | 50 |  | √ | ' ' | 原审批人员名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 5 | froleid | 工作流角色Id | int8 | 64 |  | √ | 0 | 工作流角色Id |
| 6 | fprocdefid | 流程定义Id | int8 | 64 |  | √ | 0 | 流程定义Id |
| 7 | factivityid | 节点id | varchar | 2000 |  | √ | ' ' | 节点id |
| 8 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 9 | fnewauditorname | 现审批人员名称 | varchar | 2000 |  | √ | ' ' | 现审批人员名称 |
| 10 | fnewauditorid | 现审批人员Id | varchar | 2000 |  | √ | ' ' | 现审批人员Id |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | ftype | 工作移交类型 | varchar | 30 |  | √ | ' ' | 工作移交类型,枚举: task :待处理任务 process :涉及的流程场景 role :涉及的工作流角色 execution :涉及的在办申请 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | factivityname | 节点名称 | varchar | 2000 |  | √ | ' ' | 节点名称 |
| 16 | fbatchnomsg | 批次信息 | varchar | 50 |  | √ | ' ' | 批次信息 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | ftaskid | 任务Id | int8 | 64 |  | √ | 0 | 任务Id |
| 19 | forigauditorid | 原审批人员Id | int8 | 64 |  | √ | 0 | 原审批人员Id |
| 20 | fprocversion | 流程版本号 | varchar | 36 |  | √ | ' ' | 流程版本号 |
| 21 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_workstransferlog |  | ftaskid,forigauditorid |
| 2 | idx_wf_worktrslog_oriadtproc |  | fprocinstid,forigauditorid |
| 3 | pk_t_wf_workstransferlog |  | fid |

---

## 工作移交日志-多语言表 t_wf_workstransferlog_l

- **表名称：** 工作移交日志-多语言表
- **表名：** t_wf_workstransferlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forigauditorname | 原审批人员名称 | varchar | 50 |  | √ | ' ' | 原审批人员名称 |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | factivityname | 节点名称 | varchar | 2000 |  | √ | ' ' | 节点名称 |
| 5 | fbatchnomsg | 批次信息 | varchar | 50 |  | √ | ' ' | 批次信息 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fnewauditorname | 现审批人员名称 | varchar | 2000 |  | √ | ' ' | 现审批人员名称 |
| 8 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_workstransferlog_l |  | fpkid |
| 2 | idx_wf_workstransferlog_l |  | fid,flocaleid |
