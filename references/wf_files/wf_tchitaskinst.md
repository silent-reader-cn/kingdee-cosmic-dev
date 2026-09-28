# 任务中心自定义列表-wf_tchitaskinst

## 任务中心自定义列表-分表 t_wf_hitaskinst_a

- **表名称：** 任务中心自定义列表-分表
- **表名：** t_wf_hitaskinst_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextendnumber2 | 数字2(金额) | numeric | 23 | 10 | √ | 0 | 数字2(金额) |
| 3 | fextenddate2 | 时间2 | timestamp | 0 |  |  | null | 时间2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_hitaskinst_a |  | fid |
| 2 | idx_wf_hitaskinst_a_extdate |  | fextenddate2 |

---

## 任务中心自定义列表-多语言表 t_wf_hitaskinst_l

- **表名称：** 任务中心自定义列表-多语言表
- **表名：** t_wf_hitaskinst_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcaptionpc | 页面标题_PC | varchar | 300 |  | √ | ' ' | 页面标题_PC |
| 3 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 4 | fsubactivityname | 节点子标题 | varchar | 200 |  | √ | ' ' | 节点子标题 |
| 5 | fstartname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 6 | fsubject | 主题 | varchar | 3000 |  | √ | ' ' | 主题 |
| 7 | fsendername | 上一步处理人名称 | varchar | 1000 |  | √ | ' ' | 上一步处理人名称 |
| 8 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 9 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 10 | fcaptionmob | 页面标题_mob | varchar | 300 |  | √ | ' ' | 页面标题_mob |
| 11 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 12 | fdescription | 节点描述 | varchar | 500 |  | √ | ' ' | 节点描述 |
| 13 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 14 | fassignee | 处理人 | varchar | 255 |  | √ | ' ' | 处理人 |
| 15 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 16 | fparticipantname | 当前参与人 | varchar | 3000 |  | √ | ' ' | 当前参与人 |
| 17 | fpresentassignee | 当前处理人 | varchar | 2000 |  | √ | ' ' | 当前处理人 |
| 18 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 19 | fstartnameformat | 发起人显示设置 | varchar | 500 |  | √ | ' ' | 发起人显示设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hitaskinst_l_pkey |  | fpkid |
| 2 | idx_wf_hitaskinst_localeid |  | fid,flocaleid |

---

## 任务中心自定义列表-主表 t_wf_hitaskinst

- **表名称：** 任务中心自定义列表-主表
- **表名：** t_wf_hitaskinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaptionpc | 页面标题_PC | varchar | 300 |  | √ | ' ' | 页面标题_PC |
| 3 | fbatchop | 批量标识 | varchar | 30 |  | √ | ' ' | 批量标识 |
| 4 | fvalidateoperation | 校验操作 | varchar | 500 |  | √ | ' ' | 校验操作 |
| 5 | fsendername | 上一步处理人名称 | varchar | 1000 |  | √ | ' ' | 上一步处理人名称 |
| 6 | fextendnumber | 数字(金额) | numeric | 23 | 10 | √ | 0 | 数字(金额) |
| 7 | fcaptionmob | 页面标题_mob | varchar | 300 |  | √ | ' ' | 页面标题_mob |
| 8 | fassignee | 处理人 | varchar | 255 |  | √ | ' ' | 处理人 |
| 9 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 10 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 11 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 12 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 13 | fendtype | 处理端类型 | varchar | 30 |  | √ | '1' | 处理端类型,枚举: all :PC和移动处理 pc :仅PC处理 mb :仅移动处理 |
| 14 | frealduration | 真正办理时长 | int8 | 64 |  | √ | 0 | 真正办理时长 |
| 15 | fyzjgroupid | 云之家组ID | varchar | 255 |  | √ | ' ' | 云之家组ID |
| 16 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 17 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 18 | fextendformat | 业务字段格式 | text | 0 |  |  | null | 业务字段格式 |
| 19 | fformkey | 表单ID | varchar | 36 |  | √ | ' ' | 表单ID |
| 20 | fcategory | 类别 | varchar | 100 |  | √ | ' ' | 类别 |
| 21 | fstartname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 22 | fstarterid | 发起人id | int8 | 64 |  | √ | 0 | 发起人id |
| 23 | fhandlestate | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: approve :已同意 reject :已驳回 forceReject :已强制驳回 terminate :已终止 handled :已处理 dismissed :被驳回 willApproval :待审批 freeze :已冻结 willHandled :待处理 manualSuspended :已挂起 converted :已转换 converting :转换中 unConverted :待转换 |
| 24 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 25 | fparenttaskid | 父任务ID | int8 | 64 |  | √ | 0 | 父任务ID |
| 26 | fdescription | 节点描述 | varchar | 500 |  | √ | ' ' | 节点描述 |
| 27 | fprocessingpage | 处理页面 | varchar | 50 |  | √ | ' ' | 处理页面 |
| 28 | fownerid | 拥有人ID | int8 | 64 |  | √ | 0 | 拥有人ID |
| 29 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 30 | fclaimtime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 31 | fmobileformkey | 移动表单KEY | varchar | 50 |  | √ | ' ' | 移动表单KEY |
| 32 | fextenddate | 时间 | timestamp | 0 |  |  | null | 时间 |
| 33 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 34 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 35 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 36 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 37 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 38 | fentitynumber | 实体编码 | varchar | 255 |  | √ | ' ' | 实体编码,枚举: |
| 39 | fgroupnumber | 待办分组 | int8 | 64 |  | √ | 0 | 待办分组 wf_tohandlegroup |
| 40 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 41 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 42 | fexecutiontype | 执行类型 | varchar | 50 |  | √ | ' ' | 执行类型 |
| 43 | fsenderid | 发送人 | text | 0 |  |  | null | 发送人 |
| 44 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fparticipantname | 当前参与人 | varchar | 500 |  | √ | ' ' | 当前参与人 |
| 46 | fextendstr1 | 字符1 | varchar | 255 |  | √ | ' ' | 字符1 |
| 47 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 48 | fextendstr2 | 字符2 | varchar | 255 |  | √ | ' ' | 字符2 |
| 49 | fcontrol | 控件标识 | varchar | 300 |  | √ | ' ' | 控件标识 |
| 50 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 51 | fstartnameformat | 发起人显示设置 | varchar | 500 |  | √ | ' ' | 发起人显示设置 |
| 52 | forgunitid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 53 | fprocessingmobilepage | 移动处理页面 | varchar | 50 |  | √ | ' ' | 移动处理页面 |
| 54 | fsubactivityname | 节点子标题 | varchar | 200 |  | √ | ' ' | 节点子标题 |
| 55 | fsubject | 主题 | varchar | 3000 |  | √ | ' ' | 主题 |
| 56 | fdeletereason | 删除原因 | text | 0 |  |  | null | 删除原因 |
| 57 | fprocesstype | 流程类型 | varchar | 100 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 58 | fowner | 拥有人 | varchar | 100 |  | √ | ' ' | 拥有人 |
| 59 | fduedate | 到期时间 | timestamp | 0 |  |  | null | 到期时间 |
| 60 | fduration | 总办理时间 | int8 | 64 |  | √ | 0 | 总办理时间 |
| 61 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 62 | fpresentassignee | 当前处理人 | varchar | 2000 |  | √ | ' ' | 当前处理人 |
| 63 | fdelegation | 委托类型 | varchar | 30 |  | √ | ' ' | 委托类型 |
| 64 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |
| 65 | ftaskdefkey | 任务定义ID | varchar | 255 |  | √ | ' ' | 任务定义ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hitask_ptaskid |  | fparenttaskid |
| 2 | idx_wf_hitask_businesskey |  | fbusinesskey |
| 3 | idx_wf_hitask_entitynumber |  | fentitynumber |
| 4 | t_wf_hitaskinst_pkey |  | fid |
| 5 | idx_wf_hi_task_inst_procinst |  | fprocinstid |
| 6 | idx_wf_hitask_endtimeprocdef |  | fendtime,fprocdefid,fcategory |
| 7 | idx_wf_hitaskinst_tc_count |  | fassigneeid,fendtime,fisdisplay,fexecutiontype,fendtype |
| 8 | idx_wf_hitask_billtype |  | fbilltype |
