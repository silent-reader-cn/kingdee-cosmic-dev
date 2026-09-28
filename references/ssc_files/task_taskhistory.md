# 任务管理-task_taskhistory

## 单据信息-子表 t_tk_taskhistory_billinfo

- **表名称：** 单据信息-子表
- **表名：** t_tk_taskhistory_billinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseamount | 报销金额 | numeric | 19 | 6 | √ | 0.000000 | 报销金额 |
| 3 | fsupplier | fsupplier | varchar | 255 |  | √ | ' ' |  |
| 4 | fcostdept | 承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fexpenseitem | fexpenseitem | varchar | 255 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ssc_his_billinfo_amount |  | fexpenseamount |
| 2 | ssc_his_billinfo_supplier |  | fsupplier |
| 3 | t_tk_taskhistory_billinfo_pkey |  | fentryid |
| 4 | ssc_his_billinfo_expitem |  | fexpenseitem |

---

## 单据信息-多语言表 t_tk_taskhistory_billinfo_l

- **表名称：** 单据信息-多语言表
- **表名：** t_tk_taskhistory_billinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsupplier | 供应商 | varchar | 255 |  | √ | ' ' | 供应商 |
| 2 | fexpenseitem | 费用项目 | varchar | 255 |  | √ | ' ' | 费用项目 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ssc_hisbillinfo_l_flocaleid |  | fentryid,flocaleid |
| 2 | t_tk_taskhistory_billinfo_l_pkey |  | fpkid |

---

## 任务管理-分表 t_tk_taskhistory_q

- **表名称：** 任务管理-分表
- **表名：** t_tk_taskhistory_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpredictlevel | 风险预测等级 | varchar | 50 |  | √ | ' ' | 风险预测等级,枚举: 低 :[0,0.4) 中 :[0.4,0.6) 高 :[0.6-1] |
| 3 | frescanopinion | 退扫原因 | varchar | 1000 |  | √ | ' ' | 退扫原因 |
| 4 | fpredictvalue | 风险预测分数 | numeric | 19 | 6 | √ | 0.000000 | 风险预测分数 |
| 5 | fdecisionitemnew | 决策项 | int8 | 64 |  | √ | 0 | 决策项 task_decisionitem |
| 6 | fdecisionvalue | 决策项值（弃用） | varchar | 255 |  | √ | ' ' | 决策项值（弃用） |
| 7 | fpendingopinion | 暂挂原因 | varchar | 1000 |  | √ | ' ' | 暂挂原因 |
| 8 | fdecisionitem | 操作类型 | bpchar | 1 |  | √ | ' ' | 操作类型,枚举: 1 :不通过 2 :打回（不含影像） 3 :退回（共享审核） 4 :打回（含影像） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_taskhistory_q |  | fid |
| 2 | idx_ssc_taskhistory_q_val |  | fpredictvalue |

---

## 单据体-子表 t_tk_subhistory

- **表名称：** 单据体-子表
- **表名：** t_tk_subhistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvoucherid | 凭证id | varchar | 60 |  | √ | ' ' | 凭证id |
| 3 | fvouchernumber | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_subhistory_pkey |  | fdetailid |
| 2 | index_ssc_subhistory_taskid |  | fid |

---

## 任务管理-主表 t_tk_taskhistory

- **表名称：** 任务管理-主表
- **表名：** t_tk_taskhistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusergroup | 用户组 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 3 | foldtaskstate | 任务原状态 | varchar | 10 |  | √ | ' ' | 任务原状态 |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fassignid | 工作流任务 | varchar | 100 |  | √ | ' ' | 工作流任务 |
| 7 | fautoprocess | 自动审批 | bpchar | 1 |  | √ | '0' | 自动审批 |
| 8 | fexpirestate | 超期状态 | varchar | 10 |  | √ | ' ' | 超期状态,枚举: 2 :超期 3 :即将超期 1 :未超期 |
| 9 | fapplytime | 提单日期 | timestamp | 0 |  |  | null | 提单日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | funpassreasondesc_tag | 批退原因描述_详情 | text | 0 |  |  | null | 批退原因描述_详情 |
| 12 | fpooltype | 任务池类型（处理环节） | varchar | 10 |  | √ | ' ' | 任务池类型（处理环节）,枚举: 0 :待分配 1 :处理中 2 :已完成 3 :待上传影像 |
| 13 | fapprevalmessage | 审批意见 | varchar | 2000 |  | √ | ' ' | 审批意见 |
| 14 | funpassreasondesc | 批退原因描述 | text | 0 |  |  | null | 批退原因描述 |
| 15 | ftasklevelid | 任务优先级 | int8 | 64 |  | √ | 0 | 任务优先级 task_tasklevel |
| 16 | foprt | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作 |
| 17 | fqualitysamplelibraryid | 质检样本库 | int8 | 64 |  | √ | 0 | 质检样本库 task_qualitysamplelibrary |
| 18 | freverseoprt | 反向操作 | varchar | 50 |  | √ | ' ' | 反向操作 |
| 19 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 20 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fpausewaittime | 暂挂等待时间 | numeric | 23 | 10 | √ | 0.0000000000 | 暂挂等待时间 |
| 22 | fextenderpid | 外部系统 | int8 | 64 |  | √ | 0 | 业务系统 bas_extenderp |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fflowbackstgid | 打回策略 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 25 | frecyclestate | 回收后状态 | varchar | 10 |  | √ | ' ' | 回收后状态 |
| 26 | fflagmsg | 关注说明 | varchar | 255 |  |  | null | 关注说明 |
| 27 | fallocatecount | 分配次数 | int8 | 64 |  | √ | 0 | 分配次数 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fconsignerid | 委托人 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 30 | fbillnumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 31 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 32 | fqualitychecktime | 检验日期 | timestamp | 0 |  |  | null | 检验日期 |
| 33 | fresttime | 剩余时间 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余时间 |
| 34 | forglongnumber | 组织长编码 | varchar | 200 |  |  | null | 组织长编码 |
| 35 | funpassreasonid | 批退原因 | int8 | 64 |  | √ | 0 | 批退原因 task_withdrawal |
| 36 | fimageuploadtime | 影像上传时间 | timestamp | 0 |  |  | null | 影像上传时间 |
| 37 | fbillid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 38 | fpersonid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fcompletetime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |
| 42 | fsourcetaskid | 原任务id | int8 | 64 |  | √ | 0 | 原任务id |
| 43 | fiscalculated | 是否计算过信用 | bpchar | 1 |  | √ | '0' | 是否计算过信用 |
| 44 | fislastaudit | 是否终审 | bpchar | 1 |  | √ | ' ' | 是否终审 |
| 45 | fcreateruleid | 任务创建规则 | int8 | 64 |  | √ | 0 | 业务单据-子页面 task_taskbill_child |
| 46 | fcostwaittime | 任务完成消耗的工作时间 | numeric | 23 | 10 | √ | 0.0000000000 | 任务完成消耗的工作时间 |
| 47 | fbizdata_tag | 业务数据_详情 | text | 0 |  |  | null | 业务数据_详情 |
| 48 | fprocinstid | 流程实例 | varchar | 100 |  | √ | ' ' | 流程实例 |
| 49 | fsource | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :工作流 2 :单据操作 3 :前置任务 4 :外部系统 |
| 50 | fhasallocated | 是否分配过 | bpchar | 1 |  | √ | ' ' | 是否分配过 |
| 51 | frescanwaittime | 退回重扫等待时间 | int8 | 64 |  | √ | 0 | 退回重扫等待时间 |
| 52 | fqualitystate | 质检状态（弃用） | varchar | 30 |  | √ | ' ' | 质检状态（弃用）,枚举: 0 :待分配 1 :处理中 2 :待整改 3 :待复核 4 :已完成 5 :已关闭 6 :暂挂 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | ftaskcreatetime | 任务创建时间 | timestamp | 0 |  |  | null | 任务创建时间 |
| 55 | finnermsg | 内部说明 | varchar | 2000 |  | √ | ' ' | 内部说明 |
| 56 | fsysbillid | 内部单据ID | int8 | 64 |  | √ | 0 | 内部单据ID |
| 57 | freformperson | 整改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 58 | fwaittime | 等待时间 | numeric | 23 | 10 | √ | 0.0000000000 | 等待时间 |
| 59 | finfo | 消息 | varchar | 255 |  |  | null | 消息 |
| 60 | fcoefficient | 任务量系数 | numeric | 23 | 10 | √ | 0.0000000000 | 任务量系数 |
| 61 | forignalpersonid | 原质检人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 62 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 63 | fsubject | 主题 | varchar | 255 |  |  | null | 主题 |
| 64 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 65 | fmultistate | 多级处理状态 | varchar | 10 |  | √ | ' ' | 多级处理状态,枚举: 1 :正常 2 :打回 3 :重审 |
| 66 | fishandled | 是否是处理过 | bpchar | 1 |  | √ | '0' | 是否是处理过 |
| 67 | flevel | 级次 | numeric | 16 | 9 | √ | 0.000000000 | 级次 |
| 68 | fstate | 任务状态 | varchar | 10 |  | √ | ' ' | 任务状态,枚举: 11 :待上传影像 12 :待分配 22 :待手工分配 10 :分配异常 8 :回收 13 :待审核 0 :暂挂 2 :退回重扫 7 :影像重传 3 :审核通过 4 :审核不通过 14 :待质检 15 :待整改 16 :待复核 17 :质检暂挂 18 :整改暂挂 19 :复核暂挂 21 :质检完成 20 :取消 1 :正常（弃用） 5 :废弃（弃用） 6 :打回（弃用） 9 :去重（弃用） |
| 69 | fqualityresult | 质检结果 | varchar | 10 |  | √ | '0' | 质检结果,枚举: 0 :不合格 1 :合格 |
| 70 | fautoprocessforcheck | 审批类型 | bpchar | 1 |  | √ | '0' | 审批类型,枚举: 0 :人工审批 1 :自动审批 2 :所有任务 |
| 71 | fbizdata | 业务数据 | text | 0 |  |  | null | 业务数据 |
| 72 | fimageok | 影像是否OK | varchar | 10 |  | √ | ' ' | 影像是否OK,枚举: 0 :否 1 :是 |
| 73 | freceivetime | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_fbillnumber_taskhistory |  | fbillnumber |
| 2 | index_applytime_taskhistory |  | fapplytime |
| 3 | index_fbillid_taskhistory |  | fbillid |
| 4 | index__ssc_hisqualitysamplib |  | fqualitysamplelibraryid |
| 5 | index_createtime_taskhistory |  | fcreatetime |
| 6 | index_personid_taskhistory |  | fpersonid |
| 7 | index_ftasktypeid_taskhistory |  | ftasktypeid |
| 8 | index_ssc_taskhistory |  | fsourcetaskid |
| 9 | index_receivetime_taskhistory |  | freceivetime |
| 10 | index_sscid_taskhistory |  | fsscid |
| 11 | t_tk_taskhistory_pkey |  | fid |
| 12 | index_completetime_taskhistory |  | fcompletetime |
| 13 | index_fbilltypeid_taskhistory |  | fbilltypeid |
