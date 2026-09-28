# 项目-pmpd_project

## 项目-使用范围表 t_pmpd_project_mcc_u

- **表名称：** 项目-使用范围表
- **表名：** t_pmpd_project_mcc_u

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
| 1 | idx_t_pmpd_project_mcc_u_uo |  | fuseorgid |
| 2 | pk_t_pmpd_project_mcc_u |  | fdataid,fuseorgid |

---

## 项目-多语言表 t_pmpd_project_mcc_l

- **表名称：** 项目-多语言表
- **表名：** t_pmpd_project_mcc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmpd_projctl_fid |  | fid,flocaleid |
| 2 | pk_pmpd_project_mcc_l |  | fpkid |
| 3 | idx_pmpd_projctl_fname |  | fname |

---

## 项目-使用范围位图表 t_pmpd_project_mcc_m

- **表名称：** 项目-使用范围位图表
- **表名：** t_pmpd_project_mcc_m

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
| 1 | pk_t_pmpd_project_mcc_m |  | forgid |

---

## 工时信息-子表 t_fmm_project_hours

- **表名称：** 工时信息-子表
- **表名：** t_fmm_project_hours

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalhour | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 3 | fhourtype | 工时类型 | varchar | 50 |  | √ | ' ' | 工时类型 |
| 4 | fnoskillhour | 不含技能工时 | numeric | 23 | 10 | √ | 0 | 不含技能工时 |
| 5 | fskillhour | 含技能工时 | numeric | 23 | 10 | √ | 0 | 含技能工时 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbasichour | 标准工时 | numeric | 23 | 10 | √ | 0 | 标准工时 |
| 8 | fnrchour | 非例行工时 | numeric | 23 | 10 | √ | 0 | 非例行工时 |
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

## 合同信息分录-子表 t_fmm_project_mcc_cust

- **表名称：** 合同信息分录-子表
- **表名：** t_fmm_project_mcc_cust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpsourcetypeid | 来源单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fsourcenumber | 来源单据编码 | varchar | 30 |  | √ | ' ' | 来源单据编码 |
| 4 | fsaleconstractname | 销售合同名称 | varchar | 255 |  | √ | ' ' | 销售合同名称 |
| 5 | fsaleorderno | 销售订单编号 | varchar | 255 |  | √ | ' ' | 销售订单编号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsaleconstractno | 销售合同编号 | varchar | 255 |  | √ | ' ' | 销售合同编号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsaleconstract | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 10 | fcustomerid | 客户（废弃） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 11 | fsaleorder | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_project_mcc_cust |  | fentryid |
| 2 | idx_pmpd_projectmcust_fid |  | fid |
| 3 | idx_pmpd_projectmcust_fseq |  | fseq |

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

---

## 项目-主表 t_pmpd_project_mcc

- **表名称：** 项目-主表
- **表名：** t_pmpd_project_mcc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | festcostamount | 预计总成本/投资 | numeric | 23 | 10 | √ | 0 | 预计总成本/投资 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | frealstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 5 | fplanmode | 计划模式 | varchar | 5 |  | √ | ' ' | 计划模式,枚举: 1 :标准 2 :敏捷 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fpjcaleid | 项目日历 | int8 | 64 |  | √ | 0 | 项目日历 pmbd_calendar |
| 8 | fdevices | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 9 | fpreschedate | 最近排程日期 | timestamp | 0 |  |  | null | 最近排程日期 |
| 10 | fprojectclass | 项目班制 | varchar | 30 |  | √ | ' ' | 项目班制,枚举: 1 :1 2 :2 3 :3 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fplanfinshdate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 13 | fpjmglevel | 项目管理等级 | varchar | 5 |  | √ | ' ' | 项目管理等级,枚举: 100 :A 99 :B 98 :C 97 :D 96 :E |
| 14 | fhrorgid | HR组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fdifsupenddate | 异地支援结束日期 | timestamp | 0 |  |  | null | 异地支援结束日期 |
| 16 | fmodeltrd | 型号L3 | varchar | 255 |  | √ | ' ' | 型号L3 |
| 17 | fpjstatu | 项目状态（旧） | varchar | 5 |  | √ | ' ' | 项目状态（旧）,枚举: |
| 18 | fworkcontent | 工作内容描述 | varchar | 255 |  | √ | ' ' | 工作内容描述 |
| 19 | fsrcsys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 20 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 21 | fresballevel | 资源平衡优先级 | int4 | 32 |  | √ | 0 | 资源平衡优先级 |
| 22 | festrevamount | 预计收入 | numeric | 23 | 10 | √ | 0 | 预计收入 |
| 23 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 24 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 25 | fdeliveryscheme | fdeliveryscheme | int8 | 64 |  | √ | 0 |  |
| 26 | fjobcodeprefix | 任务编码前缀（废弃） | varchar | 50 |  | √ | ' ' | 任务编码前缀（废弃） |
| 27 | fispsync | 同步成功 | bpchar | 1 |  | √ | '0' | 同步成功 |
| 28 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fnumber | 项目编号 | varchar | 30 |  | √ | ' ' | 项目编号 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fexpstartdate | 预计开始日期 | timestamp | 0 |  |  | null | 预计开始日期 |
| 34 | fpartname | 部件维修名称 | varchar | 255 |  | √ | ' ' | 部件维修名称 |
| 35 | fpertimeunit | 任务工期时间单位（废弃） | varchar | 5 |  | √ | ' ' | 任务工期时间单位（废弃）,枚举: hour :时 day :天 week :周 month :月 quarter :季 year :年 |
| 36 | fepsid | 企业项目结构 | int8 | 64 |  | √ | 0 | 企业项目结构 pmbd_orgpros |
| 37 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fplanperiod | 计划工期 | int8 | 64 |  | √ | 0 | 计划工期 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 41 | fproductorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fplanroom | 计划室 | int8 | 64 |  | √ | 0 | 计划室 mpdm_planroom |
| 43 | fpjtypeid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 44 | fcapitalorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 46 | fmodelone | 型号L1 | varchar | 255 |  | √ | ' ' | 型号L1 |
| 47 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fworkrange | 工作内容 | int8 | 64 |  | √ | 0 | 工作内容 mpdm_workscopeins |
| 49 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 51 | fjobcomppertype | 任务完成百分比类型（废弃） | varchar | 5 |  | √ | ' ' | 任务完成百分比类型（废弃）,枚举: 1 :实际 2 :工期 3 :数量 |
| 52 | fexpfinshdate | 预计完成日期 | timestamp | 0 |  |  | null | 预计完成日期 |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fflyhours | 飞行小时数 | numeric | 23 | 10 | √ | 0 | 飞行小时数 |
| 55 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fisspecial | 特殊项目 | bpchar | 1 |  | √ | '0' | 特殊项目 |
| 57 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 58 | fprojecttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: A :标准项目 B :检修项目 |
| 59 | fplanstarttime | 计划迭代开始日期 | timestamp | 0 |  |  | null | 计划迭代开始日期 |
| 60 | fautoclose | 允许项目自动关闭 | bpchar | 1 |  | √ | '0' | 允许项目自动关闭 |
| 61 | festperiod | 预计工期 | int8 | 64 |  | √ | 0 | 预计工期 |
| 62 | fcabinconfig | 客舱构型 | int8 | 64 |  | √ | 0 | 客舱构型 mpdm_cabinconfig |
| 63 | flicensegroup | 发证机构 | int8 | 64 |  | √ | 0 | 发证机构 mpdm_licensegroup |
| 64 | fsumcost | 累计成本/投资 | numeric | 23 | 10 | √ | 0 | 累计成本/投资 |
| 65 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 66 | fflyrepeat | 飞行循环数 | numeric | 23 | 10 | √ | 0 | 飞行循环数 |
| 67 | fscheattr | 任务排程属性（废弃） | varchar | 5 |  | √ | ' ' | 任务排程属性（废弃）,枚举: 1 :标准 2 :WSB汇总 3 :开始里程碑 4 :完成里程碑 |
| 68 | fpicture | fpicture | varchar | 255 |  | √ | ' ' |  |
| 69 | fplanstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 70 | fqualityorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 71 | fprintsws | 允许打印补充工作单 | bpchar | 1 |  | √ | '0' | 允许打印补充工作单 |
| 72 | fversionno | 版本号(弃用) | varchar | 255 |  | √ | ' ' | 版本号(弃用) |
| 73 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 74 | fsharecenterid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 75 | fworkdaytype | 任务工期类型（废弃） | varchar | 5 |  | √ | ' ' | 任务工期类型（废弃）,枚举: 1 :固定工期与资源用量 2 :固定单位时间用量 3 :固定资源用量 4 :固定工期与单位时间用量 |
| 76 | ffixlevel | 检修级别 | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 77 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 78 | fpjmanagerid | 项目经理 | int8 | 64 |  | √ | 0 | 项目经理名册 pmpd_asspjmginfo |
| 79 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 80 | fpackagename | 工作包名称(弃用) | varchar | 255 |  | √ | ' ' | 工作包名称(弃用) |
| 81 | fdifsupbegindate | 异地支援开始日期 | timestamp | 0 |  |  | null | 异地支援开始日期 |
| 82 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 83 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | 工作中心检修信息 mpdm_workcenter_info |
| 84 | ftimeunit | 工期单位 | int8 | 64 |  | √ | 0 | 工期单位 pmpd_timeunit |
| 85 | fnrccontrol | 允许创建非例行工卡 | bpchar | 1 |  | √ | '0' | 允许创建非例行工卡 |
| 86 | fmodeltwo | 型号L2 | varchar | 255 |  | √ | ' ' | 型号L2 |
| 87 | fismain | 主项目 | bpchar | 1 |  | √ | '0' | 主项目 |
| 88 | fpsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 1 :手工新增 0 :系统生成 |
| 89 | fautojob | 允许手工创建工单 | bpchar | 1 |  | √ | '0' | 允许手工创建工单 |
| 90 | fsyncdate | 同步日期 | timestamp | 0 |  |  | null | 同步日期 |
| 91 | fpartno | 部件维修号 | varchar | 50 |  | √ | ' ' | 部件维修号 |
| 92 | fsysproject | 系统云项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 93 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 94 | fdutyorg | 责任部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 95 | fexepkgid | fexepkgid | int8 | 64 |  | √ | 0 |  |
| 96 | fisbdproject | 系统云引入 | bpchar | 1 |  | √ | '0' | 系统云引入 |
| 97 | fpdunit | 工期单位 | varchar | 30 |  | √ | ' ' | 工期单位,枚举: 1 :天 |
| 98 | fweightvariant | 重量差异 | bpchar | 1 |  | √ | '0' | 重量差异 |
| 99 | flabelcolor | 标签颜色 | int8 | 64 |  | √ | 0 | 标签颜色 mpdm_label_color |
| 100 | fassetsorgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 101 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 102 | fisneedjob | 需要签卡 | bpchar | 1 |  | √ | '0' | 需要签卡 |
| 103 | forderqty | 检修工单数量 | numeric | 23 | 10 | √ | 0 | 检修工单数量 |
| 104 | fsupuser | 支援人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 105 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 106 | fjobcodepreincre | 任务编码增量（废弃） | numeric | 23 | 10 | √ | 0 | 任务编码增量（废弃） |
| 107 | fisarcapproval | 需要ARC放行 | bpchar | 1 |  | √ | '0' | 需要ARC放行 |
| 108 | fmodelmpdone | 型号L1-MPD | varchar | 255 |  | √ | ' ' | 型号L1-MPD |
| 109 | frealfinshdate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 110 | fplanner | 计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 111 | frealperiod | 实际工期 | int8 | 64 |  | √ | 0 | 实际工期 |
| 112 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 113 | fpjstageid | 项目阶段 | int8 | 64 |  | √ | 0 | 项目阶段 pmbd_projectstage |
| 114 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 115 | fprjstate | 项目状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 116 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 117 | ffixdevicetype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 118 | fprojectscheme | 项目归档方案 | varchar | 255 |  | √ | ' ' | 项目归档方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmpd_projecmcc |  | fid |
| 2 | idx_pmpd_projct_fcreatetime |  | fcreatetime |
| 3 | idx_t_pmpd_project_mcc_master |  | fmasterid |
| 4 | idx_t_pmpd_project_mcc_createorg |  | fcreateorgid |
| 5 | idx_pmpd_projct_fnumber |  | fnumber |
