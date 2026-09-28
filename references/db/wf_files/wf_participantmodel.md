# 参与人模型-wf_participantmodel

## 参与人模型-多语言表 t_wf_participantmodel_l

- **表名称：** 参与人模型-多语言表
- **表名：** t_wf_participantmodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaindescription | 参与人主描述 | varchar | 500 |  | √ | ' ' | 参与人主描述 |
| 3 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fdescription | 参与人描述 | varchar | 500 |  | √ | ' ' | 参与人描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_participantmodel_l_pkey |  | fpkid |
| 2 | idx_wf_participantmodel_loc |  | fid,flocaleid |

---

## 参与人模型-主表 t_wf_participantmodel

- **表名称：** 参与人模型-主表
- **表名：** t_wf_participantmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskactivityid | 任务ID | varchar | 255 |  | √ | ' ' | 任务ID |
| 3 | freportto | 岗位汇报类型 | varchar | 50 |  | √ | ' ' | 岗位汇报类型 |
| 4 | fpersonrelation | 人员关系 | varchar | 100 |  | √ | ' ' | 人员关系 |
| 5 | fmodelid | 流程模型Id | int8 | 64 |  | √ | 0 | 流程模型Id |
| 6 | fschemeid | 方案ID | int8 | 64 |  | √ | 0 | [流程动态方案配置 wf_processdynamicconfig](../wf_files/wf_processdynamicconfig.md) |
| 7 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 8 | fbusinessorgfield | 单据组织字段 | varchar | 255 |  | √ | ' ' | 单据组织字段 |
| 9 | frequired | 是否必选 | bpchar | 1 |  | √ | '0' | 是否必选 |
| 10 | fcondruleid | 条件规则ID | int8 | 64 |  | √ | 0 | 条件规则ID |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fcreatorid | 创建人ID | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdimensionfield | 维度字段 | varchar | 1000 |  | √ | ' ' | 维度字段 |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 16 | fconditionexpression | 条件表达式 | text | 0 |  |  | null | 条件表达式 |
| 17 | freporttype | 汇报类型 | varchar | 100 |  | √ | ' ' | 汇报类型 |
| 18 | forgrelation | 组织关系 | varchar | 100 |  | √ | ' ' | 组织关系 |
| 19 | freferenceperson | 参照人 | varchar | 500 |  | √ | ' ' | 参照人 |
| 20 | freferenceorg | 参照组织 | varchar | 500 |  | √ | ' ' | 参照组织 |
| 21 | forgunitid | 所属组织ID | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人ID | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fmaindescription | 参与人主描述 | varchar | 500 |  | √ | ' ' | 参与人主描述 |
| 24 | fshowvalue | 参与人扩展页面设置的显示value | text | 0 |  |  | null | 参与人扩展页面设置的显示value |
| 25 | froleid | 工作流角色 | int8 | 64 |  | √ | 0 | [工作流角色 wf_role](../wf_files/wf_role.md) |
| 26 | fproperty | 属性 | varchar | 255 |  |  | null | 属性 |
| 27 | fdescription | 参与人描述 | varchar | 500 |  | √ | ' ' | 参与人描述 |
| 28 | fvalue | （参与人）值 | varchar | 3000 |  | √ | ' ' | （参与人）值 |
| 29 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 30 | fmodjsonpartid | Json模型上的参与人Id | int8 | 64 |  | √ | 0 | Json模型上的参与人Id |
| 31 | fdefaultcondition | 是否默认分支 | bpchar | 1 |  | √ | '0' | 是否默认分支 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_particimodel_modelid |  | fmodelid,ftaskactivityid |
| 2 | t_wf_participantmodel_pkey |  | fid |
| 3 | idx_wf_participantmodel_pedf |  | fprocdefid |
| 4 | idx_wf_particimodel_schemeid |  | fschemeid,ftaskactivityid |
