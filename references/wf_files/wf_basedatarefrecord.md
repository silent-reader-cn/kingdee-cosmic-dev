# 基础资料引用记录-wf_basedatarefrecord

## 基础资料引用记录-主表 t_wf_basedatarefrecord

- **表名称：** 基础资料引用记录-主表
- **表名：** t_wf_basedatarefrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | int8 | 64 |  | √ | 0 | 值 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 5 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | 流程动态方案配置 wf_processdynamicconfig |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |
| 7 | fproperty | 属性 | varchar | 50 |  | √ | ' ' | 属性,枚举: conditionalRule :线上条件 skipCondition :跳过条件 outMsg :离开节点时消息 participant :参与人 inMsg :进入节点时消息 condrule :参与人满足条件 participantRangeSetting :指定参与人时限定选择范围 startUpCondition :启动条件 schemaCondition :方案条件 autoAudit.autoAuditCondition :自动审批条件 batchApprove.batchApproveCond :批量同意条件 batchReject.batchRejectCond :批量驳回条件 rule :审批要点/任务主题条件 autoCoordinateModel.autoCoordinate :自动协办接收人 circulateModel.circulate :自动传阅接收人 expireModel.timeControls.operation :任务处理时限控制 |
| 8 | factivityid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 9 | fprocnum | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_basedatarefrecord |  | fvalue,ftype |
| 2 | idx_wf_basedatarefrecord_del |  | fprocdefid,fschemeid,factivityid,fproperty |
| 3 | pk_t_wf_basedatarefrecord |  | fid |
| 4 | idx_wf_basedataref_schemeid |  | fschemeid |

---

## 基础资料引用记录-多语言表 t_wf_basedatarefrecord_l

- **表名称：** 基础资料引用记录-多语言表
- **表名：** t_wf_basedatarefrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_basedatarefrecord_l |  | fid,flocaleid |
| 2 | pk_wf_basedatarefrecord_l |  | fpkid |
