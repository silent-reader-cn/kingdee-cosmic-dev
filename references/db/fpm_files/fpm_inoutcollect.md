# 计划采集单-fpm_inoutcollect

## 计划采集单-主表 t_fpm_inoutcollect

- **表名称：** 计划采集单-主表
- **表名：** t_fpm_inoutcollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcrontemplateid | 周期性计划模板id | int8 | 64 |  | √ | 0 | 周期性计划模板id |
| 3 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: InOutPlanApply :收支计划申报 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fapplyuserid | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fabandonstatus | 废弃状态 | varchar | 50 |  | √ | ' ' | 废弃状态 |
| 9 | fapprovalbillno | 报批记录单 | varchar | 50 |  | √ | ' ' | 报批记录单 |
| 10 | fsynctime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fapplystatus | 申报状态 | varchar | 30 |  | √ | ' ' | 申报状态,枚举: A :未申报 B :申报中 C :已申报 |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fversion | 采集版本 | int4 | 32 |  | √ | 0 | 采集版本 |
| 14 | fabandonreason | 废弃原因 | varchar | 256 |  | √ | ' ' | 废弃原因 |
| 15 | fremark | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 18 | fextra1 | 自定义字段1 | varchar | 255 |  | √ | ' ' | 自定义字段1 |
| 19 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 20 | fapplyorgid | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fbatchno | 采集单批次号 | varchar | 50 |  | √ | ' ' | 采集单批次号 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fapprovalstatus | 报批状态 | varchar | 30 |  | √ | ' ' | 报批状态,枚举: A :未报批 B :报批中 C :已报批 |
| 25 | frepeatcollect | 重复采集 | bpchar | 1 |  | √ | '0' | 重复采集 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fextra4 | 自定义字段4 | varchar | 255 |  | √ | ' ' | 自定义字段4 |
| 28 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fextra5 | 自定义字段5 | varchar | 255 |  | √ | ' ' | 自定义字段5 |
| 30 | fsourcebill | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 31 | fdiscard | 系统废弃 | bpchar | 1 |  | √ | '0' | 系统废弃 |
| 32 | fextra2 | 自定义字段2 | varchar | 255 |  | √ | ' ' | 自定义字段2 |
| 33 | fapprovalbillid | 报批记录单id | int8 | 64 |  | √ | 0 | 报批记录单id |
| 34 | fextra3 | 自定义字段3 | varchar | 255 |  | √ | ' ' | 自定义字段3 |
| 35 | fsourcebillnumber | 采集单据编号 | varchar | 50 |  | √ | ' ' | 采集单据编号 |
| 36 | fcollectionsourcebill | 采集单据类型 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 37 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 38 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: HandNew :手工新增 CronPlan :周期性计划 IntelligentCollect :智能采集 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_inout_applyorg |  | fapplyorgid |
| 2 | idx_fpm_inout_cron |  | fcrontemplateid |
| 3 | pk_t_fpm_inoutcollect |  | fid |
| 4 | idx_fpm_inout |  | fbillno |
| 5 | idx_fpm_inout_sourceid |  | fsourcebillid,fsourcebillentryid |

---

## 计划采集单-关联追踪表 t_fpm_inoutcollect_tc

- **表名称：** 计划采集单-关联追踪表
- **表名：** t_fpm_inoutcollect_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_inoutcollect_tc_ftbillid |  | ftbillid |
| 2 | idx_fpm_inoutcollect_tc_tid |  | ftid |
| 3 | idx_fpm_inoutcollect_tc_tbill |  | ftbillid |
| 4 | pk_t_fpm_inoutcollect_tc |  | fid |

---

## 关联子实体-子表 t_fpm_inoutcollect_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_inoutcollect_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_inoutcollect_lk_fid |  | fid |
| 2 | pk_t_fpm_inoutcollect_lk |  | fpkid |

---

## 计划采集单-反写记录表 t_fpm_inoutcollect_wb

- **表名称：** 计划采集单-反写记录表
- **表名：** t_fpm_inoutcollect_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_inoutcollect_wb |  | fentryid |
| 2 | idx_inoutcollect_wb_fid |  | fid |

---

## 单据体-子表 t_fpm_collectrelatereport

- **表名称：** 单据体-子表
- **表名：** t_fpm_collectrelatereport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelateplanreportid | 关联计划编制表单据id | int8 | 64 |  | √ | 0 | 关联计划编制表单据id |
| 3 | freportperiodid | 编报期间 | int8 | 64 |  | √ | 0 | [计划日历分录 fpm_planningcalendarentry](../fpm_files/fpm_planningcalendarentry.md) |
| 4 | fbatchno | 采集单批次号 | varchar | 50 |  | √ | ' ' | 采集单批次号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freferplanamount | 参考金额 | numeric | 23 | 10 | √ | 0 | 参考金额 |
| 7 | frelateplanreport | 关联计划编制表 | varchar | 50 |  | √ | ' ' | 关联计划编制表 |
| 8 | fbodysysid | 计划方案 | int8 | 64 |  | √ | 0 | [资金计划方案 fpm_scheme](../fpm_files/fpm_scheme.md) |
| 9 | freporttypeid | freporttypeid | int8 | 64 |  | √ | 0 |  |
| 10 | freportorgid | 编报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | freferplandate | 参考计划日期 | timestamp | 0 |  |  | null | 参考计划日期 |
| 12 | freporttype | 编报类型 | varchar | 50 |  | √ | ' ' | 编报类型,枚举: 3 :月 5 :周 |
| 13 | frelatereportno | 计划编制表单据编号 | varchar | 100 |  | √ | ' ' | 计划编制表单据编号 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_collectrelatereport |  | fentryid |
| 2 | idx_collectrelate_freportid |  | frelateplanreportid |

---

## 计划采集单-分表 t_fpm_inoutcollect_e

- **表名称：** 计划采集单-分表
- **表名：** t_fpm_inoutcollect_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffundorgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcurrentplanamount | 本次计划金额 | numeric | 23 | 10 | √ | 0 | 本次计划金额 |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | ffundpurposeid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 6 | fcontractname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 7 | fexpectdate | 期望日期 | timestamp | 0 |  |  | null | 期望日期 |
| 8 | fexpectcashamount | 期望收付金额 | numeric | 23 | 10 | √ | 0 | 期望收付金额 |
| 9 | fopusername | 往来单位名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fcorebillremaincashamt | 核心单据剩余收付金额 | numeric | 23 | 10 | √ | 0 | 核心单据剩余收付金额 |
| 11 | fcontractno | 合同编号 | varchar | 100 |  | √ | ' ' | 合同编号 |
| 12 | ffeeprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 13 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 14 | fcurrentplandate | 本次计划日期 | timestamp | 0 |  |  | null | 本次计划日期 |
| 15 | finoutdirection | 收支方向 | varchar | 50 |  | √ | ' ' | 收支方向,枚举: In :流入 Out :流出 Other :其他 |
| 16 | fopusertype | 往来单位类型 | varchar | 50 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 other :其他 cas_othercontactunit :其他往来单位 |
| 17 | fcorebillsumamount | 核心单据业务总额 | numeric | 23 | 10 | √ | 0 | 核心单据业务总额 |
| 18 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_inoutcollect_e |  | fid |
| 2 | idx_inoutcollect_e_ffundorgid |  | ffundorgid |
