# 无代码历史活动实例-wf_nocode_hiactinst

## 无代码历史活动实例-多语言表 t_wf_nocode_hiactinst_l

- **表名称：** 无代码历史活动实例-多语言表
- **表名：** t_wf_nocode_hiactinst_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeletereason | 删除原因 | varchar | 2000 |  | √ | ' ' | 删除原因 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fskipreason | 忽略原因 | varchar | 2000 |  | √ | ' ' | 忽略原因 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | factname | 活动名称 | varchar | 500 |  | √ | ' ' | 活动名称 |
| 7 | fassignee | 处理人 | varchar | 115 |  | √ | ' ' | 处理人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nocode_hiactinst_l |  | fid,flocaleid |
| 2 | pk_wf_nocode_hiactinst_l |  | fpkid |

---

## 无代码历史活动实例-主表 t_wf_nocode_hiactinst

- **表名称：** 无代码历史活动实例-主表
- **表名：** t_wf_nocode_hiactinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcallprocinstid | 子流程实例ID | int8 | 64 |  | √ | 0 | 子流程实例ID |
| 3 | fjoinflag | 汇聚标识 | varchar | 2000 |  | √ | ' ' | 汇聚标识 |
| 4 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | fentitynumber | 实体编码 | varchar | 255 |  | √ | ' ' | 实体编码 |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | factname | 活动名称 | varchar | 500 |  | √ | ' ' | 活动名称 |
| 9 | fassignee | 处理人 | varchar | 115 |  | √ | ' ' | 处理人 |
| 10 | fexecutiontype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型,枚举: byHand :手工执行 byAuto :自动执行 skip :忽略执行 jump :跳转执行 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | factid | 活动ID | varchar | 255 |  | √ | ' ' | 活动ID |
| 13 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 14 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 15 | frealduration | 真正办理时长 | int8 | 64 |  | √ | 0 | 真正办理时长 |
| 16 | facttype | 活动类型 | varchar | 50 |  | √ | ' ' | 活动类型 |
| 17 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 18 | fstep | 步骤 | int4 | 32 |  | √ | 0 | 步骤 |
| 19 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 20 | fdeletereason | 删除原因 | varchar | 2000 |  | √ | ' ' | 删除原因 |
| 21 | fparenttaskid | 父任务ID | int8 | 64 |  | √ | 0 | 父任务ID |
| 22 | fsourceelementid | 来源节点ID | int8 | 64 |  | √ | 0 | 来源节点ID |
| 23 | flevel | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 24 | fduration | 总办理时长 | int8 | 64 |  | √ | 0 | 总办理时长 |
| 25 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 26 | fcycle | 轮回 | varchar | 255 |  | √ | ' ' | 轮回 |
| 27 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 28 | fskipreason | 忽略原因 | varchar | 2000 |  | √ | ' ' | 忽略原因 |
| 29 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 30 | fforkpath | 分支路径 | varchar | 2000 |  | √ | ' ' | 分支路径 |
| 31 | ftargetelementid | 目标节点ID | int8 | 64 |  | √ | 0 | 目标节点ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nocode_hiact_credate |  | fcreatedate |
| 2 | idx_wf_nocode_hiact_parenttask |  | fparenttaskid |
| 3 | idx_wf_nocode_hiact_acttype |  | facttype |
| 4 | idx_wf_nocode_hiact_endtime |  | fendtime |
| 5 | idx_wf_nocode_hiact_execactid |  | fexecutionid,factid |
| 6 | idx_wf_nocode_hiact_procactid |  | fprocinstid,factid |
| 7 | pk_wf_nocode_hiactinst |  | fid |
| 8 | idx_wf_nocode_hiact_buskeyenti |  | fbusinesskey,fentitynumber |
| 9 | idx_wf_nocode_hiact_taskstep |  | ftaskid,fstep |
