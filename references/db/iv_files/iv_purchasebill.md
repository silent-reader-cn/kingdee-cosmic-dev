# 采购发票单-iv_purchasebill

## 采购发票单-主表 t_iv_purchasebill

- **表名称：** 采购发票单-主表
- **表名：** t_iv_purchasebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisinputtaxded | 进项税抵扣 | bpchar | 1 |  | √ | ' ' | 进项税抵扣 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fredorblue | 红蓝字 | varchar | 80 |  | √ | ' ' | 红蓝字,枚举: blue :蓝字 red :红字 |
| 5 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 6 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 12 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 13 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 14 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 16 | fscmbilltype | 供应链单据标识 | varchar | 30 |  | √ | ' ' | 供应链单据标识,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 sfc_processsettlebill :工序结算单 |
| 17 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fremark | 开票备注 | varchar | 512 |  | √ | ' ' | 开票备注 |
| 20 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | '0' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从应付引入 5 :API生成 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_finapbill :财务应付单 iv_purchasebill :采购发票单 pm_purorderbill :采购订单 im_purinbill :采购入库单 |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | foperateorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 29 | fbasecurrencyid | 本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | flocalamt | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 31 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 32 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | foperatedeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 35 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 36 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 38 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 39 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | foperategroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 41 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | foperatemanid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_pur_fbillno |  | fbillno |
| 2 | idx_iv_pur_bizdate |  | fbizdate |
| 3 | idx_iv_pur_orgdate |  | forgid,fbizdate |
| 4 | idx_iv_pur_sourcebillid |  | fsourcebillid |
| 5 | pk_t_iv_purchasebill |  | fid |
| 6 | idx_iv_pur_asstact |  | fasstactid |

---

## 采购发票单-反写记录表 t_iv_purchasebill_wb

- **表名称：** 采购发票单-反写记录表
- **表名：** t_iv_purchasebill_wb

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
| 1 | idx_iv_purchasebill_wb_fk |  | fid |
| 2 | pk_iv_purchasebill_wb |  | fentryid |

---

## 关联子实体-子表 t_iv_purchasebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_purchasebill_lk

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
| 1 | pk_iv_purchasebill_lk |  | fpkid |
| 2 | idx_iv_purchasebill_lk_fk |  | fid |

---

## 明细-子表 t_iv_purchasebillentry

- **表名称：** 明细-子表
- **表名：** t_iv_purchasebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fe_srcbillentityid | 源单分录内码ID | int8 | 64 |  | √ | 0 | 源单分录内码ID |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 10 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 12 | finvoicesupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fmaterialversionid | 物料/费用项目版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | fe_red_quantity | 关联红字发票数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票数量 |
| 15 | fe_red_basequantity | 关联红字发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票基本数量 |
| 16 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 sm_salorder :销售订单 |
| 17 | fe_amount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 18 | fe_reclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 19 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 20 | fexpenseitemid | 费用项目名称 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 21 | fscmentryid | 供应链单据分录ID | int8 | 64 |  | √ | 0 | 供应链单据分录ID |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 23 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 24 | fsrcbillid | 源单ID-废弃 | varchar | 255 |  | √ | ' ' | 源单ID-废弃 |
| 25 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 26 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 27 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 28 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 29 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 30 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 31 | fe_localamt | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 32 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 35 | fe_recamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 36 | fe_sourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_finapbill :财务应付单 iv_purchasebill :采购发票单 pm_purorderbill :采购订单 im_purinbill :采购入库单 |
| 37 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 38 | fsrcbillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 39 | fe_srcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 40 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 41 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 42 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 43 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 44 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 46 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 47 | fe_materialname | fe_materialname | varchar | 255 |  | √ | ' ' |  |
| 48 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 49 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 50 | fe_remark | 备注说明 | varchar | 512 |  | √ | ' ' | 备注说明 |
| 51 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 52 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 53 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 54 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 55 | fe_tax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 56 | fsrcbilltypenum | 源单单据类型编码 | varchar | 255 |  | √ | ' ' | 源单单据类型编码 |
| 57 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 58 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 59 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 60 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0 | 单位转换系数 |
| 61 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 62 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 63 | fmeasureunitid | 开票单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 64 | fsrcbillentityid | 源单分录内码ID-废弃 | varchar | 255 |  | √ | ' ' | 源单分录内码ID-废弃 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_purentry_srcbiilid |  | fe_srcbillid |
| 2 | idx_iv_purentry_corebill |  | fcorebillno,fcorebillentryseq |
| 3 | idx_iv_purentry_srcentryid |  | fe_srcbillentityid |
| 4 | pk_t_iv_purchasebillentry |  | fentryid |
| 5 | idx_iv_purentry_pid |  | fid |
| 6 | idx_iv_purentry_sourcebillid |  | fsrcbillid |

---

## 关联子实体-子表 t_iv_purchasebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_purchasebillentry_lk

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
| 1 | pk_iv_purchasebillentry_lk |  | fpkid |
| 2 | idx_iv_purchasebillentry_lk_fk |  | fentryid |

---

## 采购发票单-关联追踪表 t_iv_purchasebill_tc

- **表名称：** 采购发票单-关联追踪表
- **表名：** t_iv_purchasebill_tc

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
| 1 | pk_iv_purchasebill_tc |  | fid |
| 2 | idx_iv_purchasebill_tc_tid |  | ftid |
| 3 | idx_iv_purchasebill_tc_tbill |  | ftbillid |
