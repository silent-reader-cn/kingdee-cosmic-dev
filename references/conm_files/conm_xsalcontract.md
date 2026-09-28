# 销售合同变更单-conm_xsalcontract

## 物料明细-子表 t_conm_xsalcontractentry

- **表名称：** 物料明细-子表
- **表名：** t_conm_xsalcontractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fbillentrysrcid | 源单行ID | int8 | 64 |  | √ | 0 | 源单行ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 6 | fprojectconfqty | 已确认项目服务数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务数量 |
| 7 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 8 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fmpmopportno | 商机号 | int8 | 64 |  | √ | 0 | 商机登记F7 mpm_bizopregf7 |
| 13 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 14 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 19 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 21 | fisprojassociated | 是否关联立项 | bpchar | 1 |  | √ | '0' | 是否关联立项 |
| 22 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fmaterialmasterid | 主物料(废弃) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 24 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 25 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fentrychangetype | fentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 28 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 29 | fprojassinvoicebaseqty | 关联项目开票申请基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请基本数量 |
| 30 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 31 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 33 | fsupplierlot | fsupplierlot | varchar | 80 |  | √ | ' ' |  |
| 34 | fprojectinvoicedbaseqty | 项目已申请开票基本数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票基本数量 |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 36 | fprojassinvoiceqty | 关联项目开票申请数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请数量 |
| 37 | frownum | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 38 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 39 | fbillentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 40 | fprojectinvoicedqty | 项目已申请开票数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票数量 |
| 41 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 42 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 43 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 44 | fentrypurorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 46 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 47 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 48 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 49 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 50 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_xsalcontractentry |  | fid |
| 2 | t_conm_xsalcontractentry_pkey |  | fentryid |

---

## 物料明细-分表 t_conm_xsalcontractentry_f

- **表名称：** 物料明细-分表
- **表名：** t_conm_xsalcontractentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 11 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 12 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontractentry_f_pkey |  | fentryid |
| 2 | idx_conm_xsalcontractentry_f |  | fid |

---

## 收款计划-子表 t_conm_xsalcontractpentry

- **表名称：** 收款计划-子表
- **表名：** t_conm_xsalcontractpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayentrysrcid | 源单行ID | int8 | 64 |  | √ | 0 | 源单行ID |
| 3 | frecentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | factprecontrol | 按实际预收控制 | bpchar | 1 |  | √ | '0' | 按实际预收控制 |
| 6 | fintervaltime | 间隔时间 | int8 | 64 |  | √ | 0 | 间隔时间 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | frpmilestone | 里程碑 | varchar | 50 |  | √ | ' ' | 里程碑 |
| 9 | fpayamount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 10 | fplanmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 11 | fisprepay | 是否预收 | bpchar | 1 |  | √ | '0' | 是否预收 |
| 12 | fplanexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 13 | fjoinpayamount | 关联收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联收款金额 |
| 14 | frpmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 15 | frpprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 16 | fcontrolsend | 控制环节 | varchar | 20 |  | √ | ' ' | 控制环节,枚举: delivernotice :发货通知 salout :销售出库 mftorder :生产工单 |
| 17 | fplanconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 18 | fplanentrycomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 19 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 20 | fpayrate | 应收比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应收比例(%) |
| 21 | ftimeunit | 时间单位 | varchar | 5 |  | √ | ' ' | 时间单位,枚举: A :工作日 B :自然日 C :月 |
| 22 | frpprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 23 | fpaidamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 26 | fpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontractpentry_pkey |  | fentryid |
| 2 | idx_conm_xsalcontractpentry |  | fid |

---

## 收款计划-多语言表 t_conm_xsalcontractpentry_l

- **表名称：** 收款计划-多语言表
- **表名：** t_conm_xsalcontractpentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frpmilestone | 里程碑 | varchar | 255 |  | √ | ' ' | 里程碑 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_xsalcontractpentry_l |  | fentryid,flocaleid |
| 2 | pk_t_conm_xsalcontractpentry_l |  | fpkid |

---

## 物料明细-分表 t_conm_xsalcontractentry_r

- **表名称：** 物料明细-分表
- **表名：** t_conm_xsalcontractentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fdeliveraddress | 发货地址 | varchar | 512 |  |  | ' ' | 发货地址 |
| 4 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | farjoinqty | 关联应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收数量 |
| 6 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货基本数量 |
| 7 | fjoinpricebaseqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 8 | farjoinbaseqty | 关联应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收基本数量 |
| 9 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fjoinpriceqty | 应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收数量 |
| 12 | fdeliverdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 13 | fentryinvorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | forderqty | 已订货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货数量 |
| 16 | faramount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 17 | fjoinorderbaseqty | 关联订货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联订货基本数量 |
| 18 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fjoinorderqty | 关联订货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联订货数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontractentry_r_pkey |  | fentryid |
| 2 | idx_conm_xsalcontractentry_r |  | fid |

---

## 销售合同变更单-分表 t_conm_xsalcontract_x

- **表名称：** 销售合同变更单-分表
- **表名：** t_conm_xsalcontract_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangebillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 3 | fsourcebillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 4 | fchangecanceldate | 变更单作废日期 | timestamp | 0 |  |  | null | 变更单作废日期 |
| 5 | fchangereason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 6 | fchangecancelerid | 变更单作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fchangeactiverid | fchangeactiverid | int8 | 64 |  | √ | 0 |  |
| 9 | fchangeactivedate | fchangeactivedate | timestamp | 0 |  |  | null |  |
| 10 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 11 | fchangecancelstatus | 变更单作废状态 | varchar | 5 |  | √ | ' ' | 变更单作废状态,枚举: A :正常 B :已作废 |
| 12 | fchangeactivestatus | fchangeactivestatus | varchar | 5 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontract_x_pkey |  | fid |
| 2 | idx_conm_xsalcontract_x |  | fchangebillno |

---

## 销售合同变更单-分表 t_conm_xsalcontract_f

- **表名称：** 销售合同变更单-分表
- **表名：** t_conm_xsalcontract_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 3 | freceiptallamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | fprereceiptallamount | 已预收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预收金额 |
| 6 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fisentrysumamt | 明细金额汇总 | bpchar | 1 |  | √ | '1' | 明细金额汇总 |
| 10 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 11 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | forderallamount | 已订货金额 | numeric | 23 | 10 | √ | 0 | 已订货金额 |
| 14 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 17 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontract_f_pkey |  | fid |
| 2 | idx_conm_xsalcontract_f |  | fsettlecurrencyid |

---

## 销售合同变更单-多语言表 t_conm_xsalcontract_l

- **表名称：** 销售合同变更单-多语言表
- **表名：** t_conm_xsalcontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 2000 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontract_l_pkey |  | fpkid |
| 2 | idx_conm_xsalcontract_l |  | fid,flocaleid |
| 3 | idx_conm_xsalcontract_l_name |  | fbillname,fid |

---

## 销售合同变更单-分表 t_conm_xsalcontract_c

- **表名称：** 销售合同变更单-分表
- **表名：** t_conm_xsalcontract_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterminatorid | 终止人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 4 | fcontpartiesid | 合同主体 | int8 | 64 |  | √ | 0 | 合同主体 conm_contparties |
| 5 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 6 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 7 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 8 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 9 | fphone2nd | 乙方电话 | varchar | 255 |  |  | null | 乙方电话 |
| 10 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fframename | 框架协议名称 | varchar | 100 |  | √ | ' ' | 框架协议名称 |
| 14 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 15 | fframeversion | 框架协议版本 | varchar | 30 |  | √ | ' ' | 框架协议版本 |
| 16 | fframenum | 框架协议编号 | varchar | 80 |  | √ | ' ' | 框架协议编号 |
| 17 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 18 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 20 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 21 | fphone1st | 甲方电话 | varchar | 255 |  |  | null | 甲方电话 |
| 22 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 23 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |
| 24 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | freceiveaddress | 收货联系地址 | varchar | 512 |  |  | ' ' | 收货联系地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_xsalcontract_c |  | fcustomerid |
| 2 | t_conm_xsalcontract_c_pkey |  | fid |

---

## 销售合同变更单-主表 t_conm_xsalcontract

- **表名称：** 销售合同变更单-主表
- **表名：** t_conm_xsalcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 5 | fxtemplateentryid | 变更单模板版本 | int8 | 64 |  | √ | 0 | 模板版本 conm_tempfileentry |
| 6 | fsplitschemeid | 收款计划方案 | int8 | 64 |  | √ | 0 | 收款计划方案 ar_plansplit_scheme |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | freviewstatus | 评审状态 | varchar | 5 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 9 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 10 | ffreezerid | 冻结人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | 合同种类 conm_category |
| 12 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 15 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 16 | fconfirmdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 17 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | ftemplateid | 合同模板 | int8 | 64 |  | √ | 0 | 合同模板 conm_template |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fmpmrecmethod | 项目收入确认方式 | varchar | 50 |  | √ | ' ' | 项目收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 23 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 24 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 25 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 26 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 27 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 28 | fpartaid | 合同甲方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fisonlist | 基于清单 | bpchar | 1 |  | √ | '0' | 基于清单 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 33 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 35 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 36 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :未确认 B :已确认 |
| 37 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 38 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单 |
| 39 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 40 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fxtemplateid | 变更单模板 | int8 | 64 |  | √ | 0 | 合同模板 conm_template |
| 42 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | ffilingstatus | 归档状态 | varchar | 5 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 45 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 46 | fsignstatus | 签章状态 | varchar | 5 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 47 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 48 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 49 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 51 | fbizmode | 业务模式 | varchar | 5 |  | √ | ' ' | 业务模式,枚举: A :统谈统签 B :统谈分签 C :分谈分签 |
| 52 | fconmprop | 合同属性 | varchar | 5 |  | √ | ' ' | 合同属性,枚举: A :框架协议 B :合同 |
| 53 | fcomment | 备注 | varchar | 2000 |  |  | ' ' | 备注 |
| 54 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 58 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 59 | ffreezestatus | 冻结状态 | varchar | 5 |  | √ | ' ' | 冻结状态,枚举: A :未冻结 B :已冻结 |
| 60 | fpartbid | 合同乙方 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 61 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 62 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 63 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | 模板版本 conm_tempfileentry |
| 64 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_xsalcontract_pkey |  | fid |
| 2 | idx_conm_xsalcontract_billno |  | fbillno |

---

## 合同条款-子表 t_conm_xsalcontracttentry

- **表名称：** 合同条款-子表
- **表名：** t_conm_xsalcontracttentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | 合同条款分组 conm_termgroup |
| 3 | ftermentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | ftermentrysrcid | 源单行ID | int8 | 64 |  | √ | 0 | 源单行ID |
| 5 | ftermcontent | 条款内容 | varchar | 2000 |  |  | ' ' | 条款内容 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftermid | 合同条款 | int8 | 64 |  | √ | 0 | 合同条款 conm_term |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_xsalcontracttentry |  | fid |
| 2 | t_conm_xsalcontracttentry_pkey |  | fentryid |

---

## 其他方-多选基础资料表 t_conm_contpartother

- **表名称：** 其他方-多选基础资料表
- **表名：** t_conm_contpartother

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_contpartother_pkey |  | fpkid |
| 2 | idx_conm_contpartother_fid |  | fid |
