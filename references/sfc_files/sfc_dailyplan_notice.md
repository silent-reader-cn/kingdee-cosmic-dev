# 工作清单(通知)(废弃)-sfc_dailyplan_notice

## 分配明细-子表 t_sfc_dpsubentry_alloc

- **表名称：** 分配明细-子表
- **表名：** t_sfc_dpsubentry_alloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fclassgroupid | 班组 | int8 | 64 |  | √ | 0 | 班组 mpdm_classgroup |
| 2 | fjobsrctype | 任务来源类型 | varchar | 50 |  | √ | ' ' | 任务来源类型,枚举: A :分配 B :分派 C :交接 D :退回 E :通知 F :转交 |
| 3 | fstudystatus | 学习状态 | varchar | 50 |  | √ | ' ' | 学习状态,枚举: A :未学习 B :已学习 C :手工编辑 |
| 4 | froleid | 角色编码 | varchar | 36 |  | √ | ' ' | 通用角色 perm_role |
| 5 | fuserinchargeid | 责任人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 6 | fissure | 接收状态 | varchar | 50 |  | √ | ' ' | 接收状态,枚举: A :待确认 B :已确认 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fuserprofession | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 11 | fnoticeinfo | 通知内容 | varchar | 512 |  | √ | ' ' | 通知内容 |
| 12 | fhandoveruser | 交接人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dpsubentry_alloc |  | fdetailid |
| 2 | idx_sfc_dpsubentry_alloc_fk |  | fentryid |

---

## 关联子实体-子表 t_sfc_dpentry_opr_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_dpentry_opr_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dpentry_opr_lk_fk |  | fentryid |
| 2 | pk_sfc_dpentry_opr_lk |  | fpkid |

---

## 关联子实体-子表 t_sfc_dailyplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_dailyplan_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dailyplan_lk |  | fpkid |
| 2 | idx_sfc_dailyplan_lk_fk |  | fid |

---

## 工作清单(通知)(废弃)-反写记录表 t_sfc_dailyplan_wb

- **表名称：** 工作清单(通知)(废弃)-反写记录表
- **表名：** t_sfc_dailyplan_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dailyplan_wb_fk |  | fid |
| 2 | pk_sfc_dailyplan_wb |  | fentryid |

---

## 工作清单(通知)(废弃)-主表 t_sfc_dailyplan_new

- **表名称：** 工作清单(通知)(废弃)-主表
- **表名：** t_sfc_dailyplan_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftasktype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: pom_coordination_FAC_S :表面处理 pom_coordination_HEA_S :热处理 pom_coordination_INWORK_S :工作内部单 pom_coordination_MAC_S :机型加工 pom_coordination_SPR_S :零件喷漆 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :计划 B :下达 |
| 5 | fallocationstatus | 分配状态 | varchar | 50 |  | √ | ' ' | 分配状态,枚举: A :未分配 B :已分配 |
| 6 | fisfilltask | 是否补全任务 | bpchar | 1 |  | √ | '0' | 是否补全任务 |
| 7 | fplantimedym_tag | 计划时间(列表显示)_详情 | text | 0 |  |  | null | 计划时间(列表显示)_详情 |
| 8 | fmodifytime | 排班时间 | timestamp | 0 |  |  | null | 排班时间 |
| 9 | fbegintime | 任务起始时间 | timestamp | 0 |  |  | null | 任务起始时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fjobsrctypedym | 任务来源类型(列表显示) | varchar | 50 |  | √ | ' ' | 任务来源类型(列表显示),枚举: A :分配 B :分派 C :交接 D :退回 E :通知 F :转交 |
| 12 | ftaskno | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 13 | fbeginstatusdym | 开工状态(列表显示) | varchar | 50 |  | √ | ' ' | 开工状态(列表显示) |
| 14 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 |
| 15 | fisexception | 异常状态 | bpchar | 1 |  | √ | '0' | 异常状态 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fprofessiondym | 行业(列表显示) | varchar | 50 |  | √ | ' ' | 行业(列表显示) |
| 18 | fmodifierid | 排班人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fplanuserdym | 计划执行人(列表显示) | varchar | 255 |  | √ | ' ' | 计划执行人(列表显示) |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fclassgroupdym | 班组(列表显示) | varchar | 50 |  | √ | ' ' | 班组(列表显示) |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | ftaskname | 任务描述 | varchar | 255 |  | √ | ' ' | 任务描述 |
| 25 | fplantimedym | 计划时间(列表显示) | varchar | 255 |  | √ | ' ' | 计划时间(列表显示) |
| 26 | fplanuserdym_tag | 计划执行人(列表显示)_详情 | text | 0 |  |  | null | 计划执行人(列表显示)_详情 |
| 27 | fnoticeuserdym | 通知人/行业(列表显示) | varchar | 512 |  | √ | ' ' | 通知人/行业(列表显示) |
| 28 | fissuredym | 接收状态(列表显示) | varchar | 50 |  | √ | 'B' | 接收状态(列表显示),枚举: A :待确认 B :已确认 |
| 29 | fnoticeinfodym | 通知内容(列表显示) | varchar | 512 |  | √ | ' ' | 通知内容(列表显示) |
| 30 | fistaskchange | 上游任务是否变更 | bpchar | 1 |  | √ | '0' | 上游任务是否变更 |
| 31 | fdispatchstatus | 派工状态 | varchar | 50 |  | √ | ' ' | 派工状态,枚举: A :待派工 B :已派工 |
| 32 | fendtime | 任务完结时间 | timestamp | 0 |  |  | null | 任务完结时间 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dp_fallocstatus |  | fallocationstatus |
| 2 | pk_sfc_dailyplan_new |  | fid |

---

## 计划明细-子表 t_sfc_dpentry_plan

- **表名称：** 计划明细-子表
- **表名：** t_sfc_dpentry_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisouttime | 超出计划 | bpchar | 1 |  | √ | '0' | 超出计划 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fplanendtime | 计划结束时间 | timestamp | 0 |  |  | null | 计划结束时间 |
| 5 | fplanbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :计划 B :下达 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fplanstarttime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dpentry_plan |  | fentryid |
| 2 | idx_sfc_dpentry_plan_fk |  | fid |

---

## 报工明细子单据体-子表 t_sfc_dpsubentry_rpt

- **表名称：** 报工明细子单据体-子表
- **表名：** t_sfc_dpsubentry_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freportbegintime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 2 | fworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fworktype | 业务活动 | varchar | 50 |  | √ | ' ' | 业务活动,枚举: A :维修开工 B :检验开工 |
| 4 | fpersonid | 责任人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | freportendtime | 收工时间 | timestamp | 0 |  |  | null | 收工时间 |
| 7 | ffinishlog | 收工记录 | varchar | 512 |  | √ | ' ' | 收工记录 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | factualhour | 实际工时 | numeric | 23 | 10 | √ | 0 | 实际工时 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dpsubentry_rpt |  | fdetailid |
| 2 | idx_sfc_dpsubentry_rpt_fk |  | fentryid |

---

## 后置作业关系-子表 t_sfc_post_task

- **表名称：** 后置作业关系-子表
- **表名：** t_sfc_post_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fposttaskrelation | 后置任务关系 | varchar | 50 |  | √ | ' ' | 后置任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 2 | fposttaskid | 后置任务 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 3 | fpostdelay | 后置延时 | numeric | 23 | 10 | √ | 0 | 后置延时 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_post_task_fk |  | fentryid |
| 2 | pk_sfc_post_task |  | fdetailid |

---

## 工作清单(通知)(废弃)-关联追踪表 t_sfc_dailyplan_tc

- **表名称：** 工作清单(通知)(废弃)-关联追踪表
- **表名：** t_sfc_dailyplan_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dailyplan_tc_tbill |  | ftbillid |
| 2 | pk_sfc_dailyplan_tc |  | fid |
| 3 | idx_sfc_dailyplan_tc_tid |  | ftid |

---

## 工序明细单据体-子表 t_sfc_dpentry_opr

- **表名称：** 工序明细单据体-子表
- **表名：** t_sfc_dpentry_opr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffinishworktime | 工作人员完工时间 | timestamp | 0 |  |  | null | 工作人员完工时间 |
| 3 | ftaskendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fworkcardid | 工卡 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 6 | ffinishworkuser | 工作完工人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 7 | fprocessgroupid | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 8 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :未开工 E :开工 F :检验完工 H :维修完工 G :异常 |
| 9 | fcheckworktime | 检验人员完工时间 | timestamp | 0 |  |  | null | 检验人员完工时间 |
| 10 | fmroorderentryid | 检修工单分录ID | int8 | 64 |  | √ | 0 | 检修工单分录F7(废弃) sfc_mroorder_f7 |
| 11 | ftechno | 工序计划编号 | varchar | 50 |  | √ | ' ' | 工序计划编号 |
| 12 | fzoneid | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 13 | fisoprexception | 异常 | bpchar | 1 |  | √ | '0' | 异常 |
| 14 | fcheckhours | 检修人员合计消耗工时 | numeric | 23 | 10 | √ | 0 | 检修人员合计消耗工时 |
| 15 | fsrctime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | foprworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 18 | frecheckworkuser | 复检完工人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 20 | fisemergent | 紧急 | bpchar | 1 |  | √ | '0' | 紧急 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | frecheckworktime | 复检人员完工时间 | timestamp | 0 |  |  | null | 复检人员完工时间 |
| 23 | fsrcbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 24 | fpmtstask | 项目任务清单 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 25 | forderno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 26 | fplanareaid | 计划区域 | int8 | 64 |  | √ | 0 | 计划区域 fmm_planningarea |
| 27 | fcheckworkuser | 检验完工人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 28 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 29 | fsrctype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型,枚举: sfc_mromanuftech :检修工序计划 pom_mroorder :检修工单 |
| 30 | fworkcardtitle | 工卡标题 | varchar | 50 |  | √ | ' ' | 工卡标题 |
| 31 | fstageid | 工作类别 | int8 | 64 |  | √ | 0 | 工作类别 mpdm_workcategories |
| 32 | fmaterialmtcid | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 33 | fresreadys | 资源就绪 | varchar | 512 |  | √ | ' ' | 资源就绪,枚举: A1 :物料未就绪 B1 :物料预计就绪 C1 :物料已就绪 A2 :设备未就绪 B2 :设备预计就绪 C2 :设备已就绪 A3 :工具未就绪 B3 :工具预计就绪 C3 :工具已就绪 A4 :文件未就绪 B4 :文件预计就绪 C4 :文件已就绪 A5 :技术支持未就绪 B5 :技术支持预计就绪 C5 :技术支持已就绪 A6 :工卡未就绪 B6 :工卡预计就绪 C6 :工卡已就绪 |
| 34 | fdefaultworksort | 默认工作顺序 | int8 | 64 |  | √ | 0 | 默认工作顺序 |
| 35 | fareaid | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 36 | fworkhour | 标准工时 | numeric | 23 | 10 | √ | 0 | 标准工时 |
| 37 | fresready | 资源就绪(弃用) | varchar | 50 |  | √ | ' ' | 资源就绪(弃用),枚举: A1 :物料未就绪 B1 :物料预计就绪 C1 :物料已就绪 A2 :设备未就绪 B2 :设备预计就绪 C2 :设备已就绪 A3 :工具未就绪 B3 :工具预计就绪 C3 :工具已就绪 A4 :文件未就绪 B4 :文件预计就绪 C4 :文件已就绪 A5 :技术支持未就绪 B5 :技术支持预计就绪 C5 :技术支持已就绪 A6 :工卡未就绪 B6 :工卡预计就绪 C6 :工卡已就绪 |
| 38 | frepairhours | 维修人员合计消耗工时 | numeric | 23 | 10 | √ | 0 | 维修人员合计消耗工时 |
| 39 | ftaskbegintime | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dpentry_opr_fk |  | fid |
| 2 | pk_sfc_dpentry_opr |  | fentryid |

---

## 前置作业关系-子表 t_sfc_pre_task

- **表名称：** 前置作业关系-子表
- **表名：** t_sfc_pre_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpretaskid | 前置任务 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fpretaskrelation | 前置任务关系 | varchar | 50 |  | √ | ' ' | 前置任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpredelay | 前置延时 | numeric | 23 | 10 | √ | 0 | 前置延时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_pre_task |  | fdetailid |
| 2 | idx_sfc_pre_task_fk |  | fentryid |
