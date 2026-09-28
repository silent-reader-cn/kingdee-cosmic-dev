# 资金计划单-fpm_mainplanbill

## 计划明细-子表 t_fpm_mainplan_entry

- **表名称：** 计划明细-子表
- **表名：** t_fpm_mainplan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | freferamount | 参考金额 | numeric | 23 | 10 | √ | 0 | 参考金额 |
| 4 | fsourceentryid | 源单分录id（分录ID） | int8 | 64 |  | √ | 0 | 源单分录id（分录ID） |
| 5 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdecuserid | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsmartdetailid | 智能取值明细id | int8 | 64 |  | √ | 0 | 智能取值明细id |
| 9 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | fundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 11 | frelateddetail | 明细信息类型 | varchar | 50 |  | √ | ' ' | 明细信息类型,枚举: procurement :采购明细信息 sale :销售明细信息 investment :投融资明细信息 other :其他明细信息 |
| 12 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 14 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fdetailplanno | 计划明细 | varchar | 50 |  | √ | ' ' | 计划明细 |
| 16 | fbizunitid | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fexpenseid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 19 | fentrysourceid | 分录源单id（单头ID） | int8 | 64 |  | √ | 0 | 分录源单id（单头ID） |
| 20 | fbmreportid | 预算报表id | varchar | 80 |  | √ | ' ' | 预算报表id |
| 21 | fbudgetvalueid | 预算后台数id | int8 | 64 |  | √ | 0 | 预算后台数id |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 24 | fplanlocamount | 计划金额（本位币） | numeric | 23 | 10 | √ | 0 | 计划金额（本位币） |
| 25 | fdecbillno | 申报单编号 | varchar | 50 |  | √ | ' ' | 申报单编号 |
| 26 | fdetailplanid | 计划明细id | int8 | 64 |  | √ | 0 | 计划明细id |
| 27 | fdirection | 流向 | varchar | 50 |  | √ | ' ' | 流向,枚举: A :流入/流出 B :流入 C :流出 D :期初余额 E :期末余额 |
| 28 | fdecdeptid | 申报人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fplanamount | 计划金额 | numeric | 23 | 10 | √ | 0 | 计划金额 |
| 32 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_mainplan_entry |  | fid |
| 2 | pk_fpm_mainplan_entry |  | fentryid |

---

## 资金计划单-主表 t_fpm_mainplanbill

- **表名称：** 资金计划单-主表
- **表名：** t_fpm_mainplanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbeginamount | 期初金额（本位币） | numeric | 23 | 10 | √ | 0 | 期初金额（本位币） |
| 3 | fperiodentryid | 编报期间 | int8 | 64 |  | √ | 0 | [计划日历分录 fpm_planningcalendarentry](../fpm_files/fpm_planningcalendarentry.md) |
| 4 | forgid | 编报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fschemeid | 计划方案 | int8 | 64 |  | √ | 0 | [资金计划方案 fpm_scheme](../fpm_files/fpm_scheme.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fperiodseq | 期间序号 | int4 | 32 |  | √ | 0 | 期间序号 |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fiseffect | 是否生效 | bpchar | 1 |  | √ | '0' | 是否生效 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fisback | 是否被打回 | bpchar | 1 |  | √ | '0' | 是否被打回 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | ftoporgid | 汇总组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fendamount | 期末金额（本位币） | numeric | 23 | 10 | √ | 0 | 期末金额（本位币） |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftemplateid | 计划模板 | int8 | 64 |  | √ | 0 | [资金计划模板 fpm_mainplantemplate](../fpm_files/fpm_mainplantemplate.md) |
| 18 | fperiodid | 计划日历 | int8 | 64 |  | √ | 0 | [计划日历 fpm_planningcalendar](../fpm_files/fpm_planningcalendar.md) |
| 19 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: fpm_plandeclarebill :资金申报单 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | finamount | 流入金额（本位币） | numeric | 23 | 10 | √ | 0 | 流入金额（本位币） |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | foutamount | 流出金额（本位币） | numeric | 23 | 10 | √ | 0 | 流出金额（本位币） |
| 24 | fissumaudit | 需汇总审批 | bpchar | 1 |  | √ | '0' | 需汇总审批 |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fexratedatetype | 汇率日期类型 | varchar | 50 |  | √ | ' ' | 汇率日期类型,枚举: 0 :期间开始日当日 1 :期间所在月份的上月末 2 :期间所在月份的月初第一天 |
| 27 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fsourcebillnumber | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |
| 29 | freportmode | 编制方式 | varchar | 50 |  | √ | ' ' | 编制方式,枚举: 0 :自下而上 1 :自上而下 |
| 30 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 31 | fperiodtype | 周期类型 | varchar | 50 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 4 :旬 5 :周 6 :日 |
| 32 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 33 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fissubmitparent | 是否提交上级 | bpchar | 1 |  | √ | '0' | 是否提交上级 |
| 36 | feffectiveyear | 生效年度 | varchar | 50 |  | √ | ' ' | 生效年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_mainplanbill |  | fid |
| 2 | idx_fpm_mainplanbill |  | fbillno |

---

## 关联子实体-子表 t_fpm_mainplan_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_mainplan_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_mainplan_entry_lk_fnt |  | fentryid |
| 2 | pk_fpm_mainplan_entry_lk |  | fpkid |

---

## 关联子实体-子表 t_fpm_mainplanbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_mainplanbill_lk

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
| 1 | pk_fpm_mainplanbill_lk |  | fpkid |
| 2 | idx_fpm_mainplanbill_lk_fid |  | fid |

---

## 资金计划单-关联追踪表 t_fpm_mainplanbill_tc

- **表名称：** 资金计划单-关联追踪表
- **表名：** t_fpm_mainplanbill_tc

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
| 1 | idx_fpm_mainplanbill_tc_tbill |  | ftbillid |
| 2 | pk_fpm_mainplanbill_tc |  | fid |
| 3 | idx_fpm_mainplanbill_tc_ftb |  | ftbillid |
| 4 | idx_fpm_mainplanbill_tc_tid |  | ftid |

---

## 资金计划单-反写记录表 t_fpm_mainplanbill_wb

- **表名称：** 资金计划单-反写记录表
- **表名：** t_fpm_mainplanbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
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
| 1 | pk_fpm_mainplanbill_wb |  | fentryid |
| 2 | idx_fpm_mainplanbill_wb_fid |  | fid |
