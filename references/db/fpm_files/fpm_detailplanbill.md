# 计划明细-fpm_detailplanbill

## 明细信息-子表 t_fpm_detailplan_entry

- **表名称：** 明细信息-子表
- **表名：** t_fpm_detailplan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactunittype | 往来单位类型 | varchar | 50 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 5 | fbizbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型,枚举: cas_paybill :付款单 ap_payapply :付款申请单 ap_finapbill :财务应付单 ar_finarbill :财务应收单 ap_busbill :暂估应付单 conm_purcontract :采购合同 pm_purorderbill :采购订单 conm_salcontract :销售合同 sm_salorder :销售订单 cas_recbill :收款单 fpm_inoutcollect :计划采集单 fpm_cronplanmaintain :周期性收支计划维护 cfm_loanbill_loan :提款处理单 other :其他 |
| 6 | famount | 计划金额 | numeric | 23 | 10 | √ | 0 | 计划金额 |
| 7 | fusage | 申报用途 | varchar | 500 |  | √ | ' ' | 申报用途 |
| 8 | fbizbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 9 | fbizbillnumber | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 10 | finvestproject | 投融资项目名称 | varchar | 255 |  | √ | ' ' | 投融资项目名称 |
| 11 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 12 | fcontractnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_detailplan_entry |  | fid |
| 2 | pk_fpm_detailplan_entry |  | fentryid |

---

## 计划明细-反写记录表 t_fpm_detailplanbill_wb

- **表名称：** 计划明细-反写记录表
- **表名：** t_fpm_detailplanbill_wb

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
| 1 | pk_fpm_detailplanbill_wb |  | fentryid |
| 2 | idx_fpm_detailplanbill_wb_fid |  | fid |

---

## 计划明细-关联追踪表 t_fpm_detailplanbill_tc

- **表名称：** 计划明细-关联追踪表
- **表名：** t_fpm_detailplanbill_tc

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
| 1 | idx_fpm_detailplanbill_tc_ftb |  | ftbillid |
| 2 | idx_fpm_detailplanbill_tc_tid |  | ftid |
| 3 | pk_fpm_detailplanbill_tc |  | fid |
| 4 | idx_fpm_detailplanbill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_fpm_detailplanbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_detailplanbill_lk

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
| 1 | pk_fpm_detailplanbill_lk |  | fpkid |
| 2 | idx_fpm_detailplanbill_lk_fid |  | fid |

---

## 计划明细-主表 t_fpm_detailplanbill

- **表名称：** 计划明细-主表
- **表名：** t_fpm_detailplanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodentryid | 编报期间 | int8 | 64 |  | √ | 0 | [计划日历分录 fpm_planningcalendarentry](../fpm_files/fpm_planningcalendarentry.md) |
| 3 | forgid | 编报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 9 | fsumamount | 计划金额合计 | numeric | 23 | 10 | √ | 0 | 计划金额合计 |
| 10 | fbillno | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | ftemplateid | 计划模板 | int8 | 64 |  | √ | 0 | [资金计划模板 fpm_mainplantemplate](../fpm_files/fpm_mainplantemplate.md) |
| 14 | fbizunitid | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 21 | fsourcebillnumber | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |
| 22 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 23 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fbilltype | 明细类型 | varchar | 50 |  | √ | ' ' | 明细类型,枚举: other :补充明细计划 procurement :采购明细计划 sale :销售明细计划 investment :投融资明细计划 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_detailplanbill |  | fid |
| 2 | idx_fpm_detailplanbill |  | fbillno |
