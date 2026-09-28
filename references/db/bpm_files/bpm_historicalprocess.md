# 历史流程-bpm_historicalprocess

## 历史流程-主表 t_wf_hiprocinst

- **表名称：** 历史流程-主表
- **表名：** t_wf_hiprocinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 3 | fsuperprocinstid | 父流程实例ID | int8 | 64 |  | √ | 0 | 父流程实例ID |
| 4 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码,枚举: |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbusinessid | 流程标识 | varchar | 255 |  | √ | ' ' | 流程标识 |
| 10 | fstarusernameformat | 发起人姓名格式化 | varchar | 500 |  | √ | ' ' | 发起人姓名格式化 |
| 11 | fpriorityshow | 标记显示 | varchar | 50 |  | √ | ' ' | 标记显示,枚举: transfer :移交给我的 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 14 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 15 | fendtype | 结束类型 | varchar | 10 |  | √ | '10' | 结束类型,枚举: 10 :正常结束 20 :提交撤回结束 30 :审批终止 40 :管理员强制终止 50 :例外终止 60 :整单撤回终止 25 :终止 70 :父流程跳转结束 80 :父流程终止结束 90 :父流程整单撤回结束 |
| 16 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 17 | frealduration | 真正办理时长 | int8 | 64 |  | √ | 0 | 真正办理时长 |
| 18 | fstartactid | 开始节点ID | varchar | 255 |  | √ | ' ' | 开始节点ID |
| 19 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 20 | fstartuserid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 23 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 24 | ftestingplanid | 测试计划id | int8 | 64 |  | √ | 0 | 测试计划id |
| 25 | fsubject | 单据主题 | varchar | 3000 |  | √ | ' ' | 单据主题 |
| 26 | fdeletereason | 删除原因 | varchar | 2000 |  | √ | ' ' | 删除原因 |
| 27 | fendactid | 结束节点ID | varchar | 255 |  | √ | ' ' | 结束节点ID |
| 28 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 29 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 30 | fmainorgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 31 | frootprocessinstanceid | 根流程实例ID | int8 | 64 |  | √ | 0 | 根流程实例ID |
| 32 | fduration | 总办理时长 | int8 | 64 |  | √ | 0 | 总办理时长 |
| 33 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 34 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 35 | fentrabillname | 入口单据名称 | varchar | 255 |  | √ | ' ' | 入口单据名称 |
| 36 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiproc_sprocinst |  | fsuperprocinstid |
| 2 | idx_wf_hi_pro_i_buskey |  | fbusinesskey |
| 3 | idx_wf_hiproc_traceno_type |  | fbiztraceno,fprocesstype |
| 4 | t_wf_hiprocinst_pkey |  | fid |
| 5 | idx_wf_hiproc_endtype |  | fendtype |
| 6 | idx_wf_hiproc_createdate |  | fcreatedate |
| 7 | idx_wf_hi_pro_inst_end |  | fendtime |
| 8 | idx_wf_hiprocinst_tc_count |  | fcreatorid,fentitynumber,fendtime |
| 9 | idx_wf_hiproc_procdef |  | fprocdefid |

---

## 历史流程-多语言表 t_wf_hiprocinst_l

- **表名称：** 历史流程-多语言表
- **表名：** t_wf_hiprocinst_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fstarusernameformat | 发起人姓名格式化 | varchar | 500 |  | √ | ' ' | 发起人姓名格式化 |
| 4 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 5 | fsubject | 单据主题 | varchar | 3000 |  | √ | ' ' | 单据主题 |
| 6 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 7 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 8 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 9 | fentrabillname | 入口单据名称 | varchar | 255 |  | √ | ' ' | 入口单据名称 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiprocinst_localeid |  | fid,flocaleid |
| 2 | t_wf_hiprocinst_l_pkey |  | fpkid |
