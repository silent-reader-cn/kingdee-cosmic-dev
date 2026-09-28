# 收入计划单-ar_revcfmplanbill

## 收入计划单-反写记录表 t_ar_revcfmplanbill_wb

- **表名称：** 收入计划单-反写记录表
- **表名：** t_ar_revcfmplanbill_wb

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
| 1 | idx_ar_revcfmplanbill_wb_fk |  | fid |
| 2 | pk_ar_revcfmplanbill_wb |  | fentryid |

---

## 关联子实体-子表 t_ar_revcfmplanbillplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_revcfmplanbillplan_lk

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
| 1 | pk_ar_revcfmplanbillplan_lk |  | fpkid |
| 2 | idx_ar_revcfmplanbillplan_lk_fk |  | fentryid |

---

## 收入计划单-关联追踪表 t_ar_revcfmplanbill_tc

- **表名称：** 收入计划单-关联追踪表
- **表名：** t_ar_revcfmplanbill_tc

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
| 1 | idx_ar_revcfmplanbill_tc_tid |  | ftid |
| 2 | pk_ar_revcfmplanbill_tc |  | fid |
| 3 | idx_ar_revcfmplanbill_tc_tbill |  | ftbillid |

---

## 子单据体-子表 t_ar_revcfmplanbillchange

- **表名称：** 子单据体-子表
- **表名：** t_ar_revcfmplanbillchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fs_change_user | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fs_change_time | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 3 | fs_amount_old | 变更前金额 | numeric | 23 | 10 | √ | 0 | 变更前金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fs_tax_old | 变更前税额 | numeric | 23 | 10 | √ | 0 | 变更前税额 |
| 6 | fs_discountmode_old | 变更前折扣方式 | varchar | 30 |  | √ | ' ' | 变更前折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 7 | fs_quantity | 变更后数量 | numeric | 23 | 10 | √ | 0 | 变更后数量 |
| 8 | fs_taxunitprice_old | 变更前含税单价 | numeric | 23 | 10 | √ | 0 | 变更前含税单价 |
| 9 | fs_materialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fs_enddate | 变更后结束日期 | timestamp | 0 |  |  | null | 变更后结束日期 |
| 12 | fs_unitprice | 变更后单价 | numeric | 23 | 10 | √ | 0 | 变更后单价 |
| 13 | fs_amount | 变更后金额 | numeric | 23 | 10 | √ | 0 | 变更后金额 |
| 14 | fs_change_reason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 15 | fs_unitprice_old | 变更前单价 | numeric | 23 | 10 | √ | 0 | 变更前单价 |
| 16 | fs_taxunitprice | 变更后含税单价 | numeric | 23 | 10 | √ | 0 | 变更后含税单价 |
| 17 | fs_taxrateid_old | 变更前税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fs_discountamount | 变更后折扣额 | numeric | 23 | 10 | √ | 0 | 变更后折扣额 |
| 19 | fs_recamount_old | 变更前价税合计 | numeric | 23 | 10 | √ | 0 | 变更前价税合计 |
| 20 | fs_discountmode | 变更后折扣方式 | varchar | 30 |  | √ | ' ' | 变更后折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 21 | fs_projectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fs_taxrateid | 变更后税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 23 | fs_recamount | 变更后价税合计 | numeric | 23 | 10 | √ | 0 | 变更后价税合计 |
| 24 | fs_discountrate | 变更后单位折扣(率) | numeric | 23 | 10 | √ | 0 | 变更后单位折扣(率) |
| 25 | fs_discountamount_old | 变更前折扣额 | numeric | 23 | 10 | √ | 0 | 变更前折扣额 |
| 26 | fs_quantity_old | 变更前数量 | numeric | 23 | 10 | √ | 0 | 变更前数量 |
| 27 | fs_discountrate_old | 变更前单位折扣(率) | numeric | 23 | 10 | √ | 0 | 变更前单位折扣(率) |
| 28 | fs_enddate_old | 变更前结束日期 | timestamp | 0 |  |  | null | 变更前结束日期 |
| 29 | fs_tax | 变更后税额 | numeric | 23 | 10 | √ | 0 | 变更后税额 |
| 30 | fs_conbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_revcfmplanbillchange |  | fdetailid |
| 2 | idx_ar_rcvplan_pid |  | fentryid |

---

## 收入计划单-主表 t_ar_revcfmplanbill

- **表名称：** 收入计划单-主表
- **表名：** t_ar_revcfmplanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 5 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 10 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 13 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | fsourcebillno | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 |
| 20 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_invoice :增值税发票 ar_finarbill :财务应收单 ap_finapbill :财务应付单 im_saloutbill :销售出库单 ar_busbill :暂估应收单 sm_salorder :销售订单 conm_salcontract :销售合同 ar_revcfmbill :收入成本确认单 mpm_projsaleconf :项目销售服务确认单 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fasstactid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 29 | fisincludetax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 30 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 31 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 32 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 33 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 35 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 38 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 39 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_revcfmplanbill_org |  | forgid,fbizdate |
| 2 | idx_ar_revcfmplanbill_billno |  | fbillno |
| 3 | idx_ar_revcfmplanbill_bizdate |  | fbizdate |
| 4 | pk_t_ar_revcfmplanbill |  | fid |

---

## 关联子实体-子表 t_ar_revcfmplanbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_revcfmplanbill_lk

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
| 1 | pk_ar_revcfmplanbill_lk |  | fpkid |
| 2 | idx_ar_revcfmplanbill_lk_fk |  | fid |

---

## 明细-子表 t_ar_revcfmplanbillentry

- **表名称：** 明细-子表
- **表名：** t_ar_revcfmplanbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 3 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fhandlekey | 操作标识 | varchar | 50 |  | √ | ' ' | 操作标识 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fconfirmedlocalamt | 已确认金额（本位币） | numeric | 23 | 10 | √ | 0 | 已确认金额（本位币） |
| 8 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fsharerectotal | 已分摊价税合计 | numeric | 23 | 10 | √ | 0 | 已分摊价税合计 |
| 14 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 15 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 17 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 18 | frowstatus | 行状态 | varchar | 5 |  | √ | ' ' | 行状态,枚举: A :已生效 B :未生效 C :已冲回 |
| 19 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 20 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 21 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 23 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 25 | frevcfmruleid | 收入分摊规则 | int8 | 64 |  | √ | 0 | 收入分摊规则 ar_revcfmrule |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 28 | fsharedperiodid | fsharedperiodid | int8 | 64 |  | √ | 0 |  |
| 29 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 30 | facttaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 31 | fconfirmedexcludingtax | 已确认金额 | numeric | 23 | 10 | √ | 0 | 已确认金额 |
| 32 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 33 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 34 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 35 | fsharerecamount | 已分摊金额 | numeric | 23 | 10 | √ | 0 | 已分摊金额 |
| 36 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 37 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 38 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0 | 单位转换系数 |
| 39 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 40 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fsharerectax | 已分摊税额 | numeric | 23 | 10 | √ | 0 | 已分摊税额 |
| 44 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_revcfmplanbillentry |  | fentryid |
| 2 | idx_ar_revcfmplanbillentry_fid |  | fid |

---

## 收入计划-子表 t_ar_revcfmplanbillplan

- **表名称：** 收入计划-子表
- **表名：** t_ar_revcfmplanbillplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fwritebacknum | 确认次数 | int4 | 32 |  | √ | 0 | 确认次数 |
| 4 | frevcfmruleid | 收入分摊规则 | int8 | 64 |  | √ | 0 | 收入分摊规则 ar_revcfmrule |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 6 | fwriteoff | 冲回 | bpchar | 1 |  | √ | '0' | 冲回 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fconfirnstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :未确认 B :已确认 C :已关闭 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fgenerationtype | 生成方式 | bpchar | 1 |  | √ | ' ' | 生成方式,枚举: 0 :系统生成 1 :手工生成 |
| 11 | fshareperiodid | 分摊期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 12 | fexcludingtaxamount | 本期金额 | numeric | 23 | 10 | √ | 0 | 本期金额 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | ftaxlocal | 本期税额（本位币） | numeric | 23 | 10 | √ | 0 | 本期税额（本位币） |
| 15 | flocalamt | 本期金额（本位币） | numeric | 23 | 10 | √ | 0 | 本期金额（本位币） |
| 16 | fwritedoff | 被冲回 | bpchar | 1 |  | √ | '0' | 被冲回 |
| 17 | fbillentryid | 明细ID | int8 | 64 |  | √ | 0 | 明细ID |
| 18 | ftax | 本期税额 | numeric | 23 | 10 | √ | 0 | 本期税额 |
| 19 | fperiodtaxamount | 本期价税合计 | numeric | 23 | 10 | √ | 0 | 本期价税合计 |
| 20 | freclocalamt | 本期价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 本期价税合计（本位币） |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_revcfmplanbillplan |  | fentryid |
| 2 | idx_ar_revcfmplanbillplan_fid |  | fid |

---

## 关联子实体-子表 t_ar_revcfmplanbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_revcfmplanbillentry_lk

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
| 1 | pk_ar_revcfmplanbillentry_lk |  | fpkid |
| 2 | idx_ar_revcfmplanbillentry_lk_fk |  | fentryid |
