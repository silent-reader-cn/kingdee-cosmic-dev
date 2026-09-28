# 审批要点实例-wf_auditpointinstance

## 审批要点实例-主表 t_wf_hiauditpointinst

- **表名称：** 审批要点实例-主表
- **表名：** t_wf_hiauditpointinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitynumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 3 | ffailedreason | 未通过原因 | varchar | 2000 |  | √ | ' ' | 未通过原因 |
| 4 | fbusinessrule | 业务规则 | text | 0 |  |  | null | 业务规则 |
| 5 | fisneedreason | 是否说明原因 | bpchar | 1 |  | √ | '0' | 是否说明原因 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 8 | fisneedmark | 是否必须标注结果 | bpchar | 1 |  | √ | '0' | 是否必须标注结果 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | factid | 节点id | varchar | 255 |  | √ | ' ' | 节点id |
| 11 | fcheckresult | 检查结果 | varchar | 50 |  | √ | ' ' | 检查结果,枚举: approve :通过 failed :不通过 unconfirmed :待确认 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 14 | fcondition | 条件 | text | 0 |  |  | null | 条件 |
| 15 | factivityinstanceid | 活动实例id | int8 | 64 |  | √ | 0 | 活动实例id |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdisplayname | 显示名称 | varchar | 1000 |  | √ | ' ' | 显示名称 |
| 18 | fexecutionid | 执行实例id | int8 | 64 |  | √ | 0 | 执行实例id |
| 19 | fdescription | 详细说明 | varchar | 1000 |  | √ | ' ' | 详细说明 |
| 20 | ffailedexpression | 未通过原因表达式 | text | 0 |  |  | null | 未通过原因表达式 |
| 21 | fisimmediately | 是否即时计算 | bpchar | 1 |  | √ | '0' | 是否即时计算 |
| 22 | fauditpointseq | 审批要点项顺序 | int8 | 64 |  | √ | 0 | 审批要点项顺序 |
| 23 | fassigneename | 处理人 | varchar | 100 |  | √ | ' ' | 处理人 |
| 24 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: textreminder :文字提示 automaticchecks :自动检查项 manualchecks :手动检查项 |
| 25 | fprocessinstanceid | 流程实例id | int8 | 64 |  | √ | 0 | 流程实例id |
| 26 | fdescexpression | 详细说明表达式 | text | 0 |  |  | null | 详细说明表达式 |
| 27 | fbusinesskey | 业务主键 | varchar | 50 |  | √ | ' ' | 业务主键 |
| 28 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hiauditpointinst_pkey |  | fid |
| 2 | idx_wf_hiauditpoint_proc_act |  | fprocessinstanceid,factid |
| 3 | idx_wf_hiauditpointinst_task |  | ftaskid |

---

## 审批要点实例-多语言表 t_wf_hiauditpointinst_l

- **表名称：** 审批要点实例-多语言表
- **表名：** t_wf_hiauditpointinst_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassigneename | 处理人 | varchar | 100 |  | √ | ' ' | 处理人 |
| 3 | fdisplayname | 显示名称 | varchar | 1000 |  | √ | ' ' | 显示名称 |
| 4 | fdescexpression | 详细说明表达式 | text | 0 |  |  | null | 详细说明表达式 |
| 5 | ffailedreason | 未通过原因 | varchar | 2000 |  | √ | ' ' | 未通过原因 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 详细说明 | varchar | 1000 |  | √ | ' ' | 详细说明 |
| 8 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 9 | ffailedexpression | 未通过原因表达式 | text | 0 |  |  | null | 未通过原因表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hiauditpointinst_l_pkey |  | fpkid |
| 2 | idx_wf_hiauditpointinst_l |  | fid,flocaleid |
