# 项目变更单-pmpd_changeproject

## 工时信息-子表 t_fmm_project_hours

- **表名称：** 工时信息-子表
- **表名：** t_fmm_project_hours

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalhour | ftotalhour | numeric | 23 | 10 | √ | 0 |  |
| 3 | fhourtype | fhourtype | varchar | 50 |  | √ | ' ' |  |
| 4 | fnoskillhour | fnoskillhour | numeric | 23 | 10 | √ | 0 |  |
| 5 | fskillhour | fskillhour | numeric | 23 | 10 | √ | 0 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbasichour | fbasichour | numeric | 23 | 10 | √ | 0 |  |
| 8 | fnrchour | fnrchour | numeric | 23 | 10 | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_project_hours |  | fentryid |
| 2 | idx_fmm_project_hours_fs |  | fid,fseq |

---

## 项目变更单-使用范围位图表 t_fmm_project_change_m

- **表名称：** 项目变更单-使用范围位图表
- **表名：** t_fmm_project_change_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fmm_project_change_m |  | forgid |

---

## 项目变更单-多语言表 t_fmm_project_change_l

- **表名称：** 项目变更单-多语言表
- **表名：** t_fmm_project_change_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_project_change_l |  | fid,flocaleid |
| 2 | pk_fmm_project_change_l |  | fpkid |

---

## 项目变更单-使用范围表 t_fmm_project_change_u

- **表名称：** 项目变更单-使用范围表
- **表名：** t_fmm_project_change_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_project_change_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_project_change_u |  | fdataid,fuseorgid |

---

## 合同信息分录-子表 t_fmm_pchang_cust

- **表名称：** 合同信息分录-子表
- **表名：** t_fmm_pchang_cust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpsourcetypeid | 来源单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fsourcenumber | 来源单据编码 | varchar | 30 |  | √ | ' ' | 来源单据编码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcustomerid | 客户（废弃） | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_pchang_cust |  | fentryid |
| 2 | idx_fmm_pchang_cust_fseq |  | fseq |
| 3 | idx_fmm_pchang_cust_fid |  | fid |

---

## 关联子实体-子表 t_pmpd_project_mcc_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pmpd_project_mcc_lk

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
| 1 | pk_pmpd_project_mcc_lk |  | fpkid |
| 2 | idx_pmpd_project_mcc_lk_fk |  | fid |

---

## 项目变更单-主表 t_fmm_project_change

- **表名称：** 项目变更单-主表
- **表名：** t_fmm_project_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | festcostamount | 预计总成本/投资 | numeric | 23 | 10 | √ | 0 | 预计总成本/投资 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | frealstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 5 | festperiod | 预计工期 | int8 | 64 |  | √ | 0 | 预计工期 |
| 6 | fplanmode | 计划模式 | varchar | 5 |  | √ | ' ' | 计划模式,枚举: 1 :标准 2 :敏捷 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fpjcaleid | 项目日历 | int8 | 64 |  | √ | 0 | 项目日历 pmbd_calendar |
| 9 | fpreschedate | 最近排程日期 | timestamp | 0 |  |  | null | 最近排程日期 |
| 10 | fsumcost | 累计成本/投资 | numeric | 23 | 10 | √ | 0 | 累计成本/投资 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fscheattr | 任务排程属性（废弃） | varchar | 5 |  | √ | ' ' | 任务排程属性（废弃）,枚举: 1 :标准 2 :WSB汇总 3 :开始里程碑 4 :完成里程碑 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fplanfinshdate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 15 | fplanstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 16 | fpjmglevel | 项目管理等级 | varchar | 5 |  | √ | ' ' | 项目管理等级,枚举: 100 :A 99 :B 98 :C 97 :D 96 :E |
| 17 | fhrorgid | HR组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fqualityorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fsharecenterid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fpjstatu | 项目状态（旧） | varchar | 5 |  | √ | ' ' | 项目状态（旧）,枚举: |
| 22 | fname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 23 | fsrcsys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 24 | fresballevel | 资源平衡优先级 | int4 | 32 |  | √ | 0 | 资源平衡优先级 |
| 25 | festrevamount | 预计收入 | numeric | 23 | 10 | √ | 0 | 预计收入 |
| 26 | fworkdaytype | 任务工期类型（废弃） | varchar | 5 |  | √ | ' ' | 任务工期类型（废弃）,枚举: 1 :固定工期与资源用量 2 :固定单位时间用量 3 :固定资源用量 4 :固定工期与单位时间用量 |
| 27 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 28 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 29 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 30 | fpjmanagerid | 项目经理 | int8 | 64 |  | √ | 0 | 项目经理名册 pmpd_asspjmginfo |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 33 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fjobcodeprefix | 任务编码前缀（废弃） | varchar | 50 |  | √ | ' ' | 任务编码前缀（废弃） |
| 35 | ftimeunit | 工期单位 | int8 | 64 |  | √ | 0 | 工期单位 pmpd_timeunit |
| 36 | fispsync | 同步成功 | bpchar | 1 |  | √ | ' ' | 同步成功 |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fpsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 1 :手工新增 0 :系统生成 |
| 39 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 41 | fsyncdate | 同步日期 | timestamp | 0 |  |  | null | 同步日期 |
| 42 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 45 | fexpstartdate | 预计开始日期 | timestamp | 0 |  |  | null | 预计开始日期 |
| 46 | fisbdproject | 系统云引入 | bpchar | 1 |  | √ | ' ' | 系统云引入 |
| 47 | fpdunit | 工期单位 | varchar | 30 |  | √ | ' ' | 工期单位,枚举: 1 :天 |
| 48 | fpertimeunit | 任务工期时间单位（废弃） | varchar | 5 |  | √ | ' ' | 任务工期时间单位（废弃）,枚举: hour :时 day :天 week :周 month :月 quarter :季 year :年 |
| 49 | fepsid | 企业项目结构 | int8 | 64 |  | √ | 0 | 企业项目结构 pmbd_orgpros |
| 50 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 51 | fplanperiod | 计划工期 | int8 | 64 |  | √ | 0 | 计划工期 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 54 | fassetsorgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 56 | fproductorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 57 | fpjtypeid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 58 | fcapitalorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 59 | fpnumber | 项目编码 | varchar | 30 |  | √ | ' ' | 项目编码 |
| 60 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 61 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 62 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 64 | fjobcomppertype | 任务完成百分比类型（废弃） | varchar | 5 |  | √ | ' ' | 任务完成百分比类型（废弃）,枚举: 1 :实际 2 :工期 3 :数量 |
| 65 | fexpfinshdate | 预计完成日期 | timestamp | 0 |  |  | null | 预计完成日期 |
| 66 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 项目变更单 pmpd_changeproject |
| 67 | fjobcodepreincre | 任务编码增量（废弃） | numeric | 23 | 10 | √ | 0 | 任务编码增量（废弃） |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | frealfinshdate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 70 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 71 | frealperiod | 实际工期 | int8 | 64 |  | √ | 0 | 实际工期 |
| 72 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 73 | fpjstageid | 项目阶段 | int8 | 64 |  | √ | 0 | 项目阶段 pmbd_projectstage |
| 74 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 75 | fprjstate | 项目状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 76 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 77 | fprojecttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: A :标准项目 B :检修项目 |
| 78 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 79 | fplanstarttime | 计划迭代开始日期 | timestamp | 0 |  |  | null | 计划迭代开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_project_change_createorg |  | fcreateorgid |
| 2 | pk_fmm_project_change |  | fid |
| 3 | idx_fmm_project_fnum |  | fnumber |
| 4 | idx_t_fmm_project_change_master |  | fmasterid |

---

## 来源信息分录-子表 t_fmm_project_source

- **表名称：** 来源信息分录-子表
- **表名：** t_fmm_project_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fsourcebillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsourcebillno | 来源单据编码 | varchar | 50 |  | √ | ' ' | 来源单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_project_mcc_cust_fs |  | fid,fseq |
| 2 | pk_fmm_project_source |  | fentryid |
