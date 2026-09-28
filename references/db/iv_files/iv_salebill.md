# 销售发票单-iv_salebill

## 销售发票单-主表 t_iv_salebill

- **表名称：** 销售发票单-主表
- **表名：** t_iv_salebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fredorblue | 红蓝字 | varchar | 80 |  | √ | ' ' | 红蓝字,枚举: blue :蓝字 red :红字 |
| 4 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 5 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 11 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 12 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 开票备注 | varchar | 512 |  | √ | ' ' | 开票备注 |
| 17 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | '0' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从应收引入 5 :API生成 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_finarbill :财务应收单 im_saloutbill :销售出库单 sm_salorder :销售订单 iv_salebill :销售发票单 mpm_projinvapply :项目开票申请单 |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | foperateorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 26 | fbasecurrencyid | 本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | flocalamt | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 28 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 29 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 30 | foperatedeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 32 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 33 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 34 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 35 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 36 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | foperategroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 38 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | foperatemanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_salebill_sourcebillid |  | fsourcebillid |
| 2 | pk_t_iv_salebill |  | fid |
| 3 | idx_iv_salebill_bizdate |  | fbizdate |
| 4 | idx_iv_salebill_fbillno |  | fbillno |
| 5 | idx_iv_salebill_orgdate |  | forgid,fbizdate |
| 6 | idx_iv_salebill_asstact |  | fasstactid |

---

## 关联子实体-子表 t_iv_salebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_salebillentry_lk

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
| 1 | pk_iv_salebillentry_lk |  | fpkid |
| 2 | idx_iv_salebillentry_lk_fk |  | fentryid |

---

## 销售发票单-关联追踪表 t_iv_salebill_tc

- **表名称：** 销售发票单-关联追踪表
- **表名：** t_iv_salebill_tc

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
| 1 | pk_iv_salebill_tc |  | fid |
| 2 | idx_iv_salebill_tc_tbill |  | ftbillid |
| 3 | idx_iv_salebill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_iv_salebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_salebill_lk

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
| 1 | idx_iv_salebill_lk_fk |  | fid |
| 2 | pk_iv_salebill_lk |  | fpkid |

---

## 销售发票单-反写记录表 t_iv_salebill_wb

- **表名称：** 销售发票单-反写记录表
- **表名：** t_iv_salebill_wb

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
| 1 | idx_iv_salebill_wb_fk |  | fid |
| 2 | pk_iv_salebill_wb |  | fentryid |

---

## 明细-子表 t_iv_salebillentry

- **表名称：** 明细-子表
- **表名：** t_iv_salebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fe_srcbillentityid | 源单分录内码ID | int8 | 64 |  | √ | 0 | 源单分录内码ID |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 9 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 10 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 11 | fmaterialversionid | 物料/费用项目版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 12 | fe_red_quantity | 关联红字发票数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票数量 |
| 13 | fdelivercustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fe_red_basequantity | 关联红字发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票基本数量 |
| 15 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 pm_purorderbill :采购订单 |
| 16 | fe_amount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 17 | fe_reclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 18 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 19 | fexpenseitemid | 费用项目名称 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | fsrcbillid | 源单ID-废弃 | varchar | 255 |  | √ | ' ' | 源单ID-废弃 |
| 23 | facttaxunitprice | 实际含税单价-废弃 | numeric | 23 | 10 | √ | 0 | 实际含税单价-废弃 |
| 24 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 25 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 26 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 27 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 28 | fe_localamt | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 29 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 32 | fe_recamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 33 | fe_sourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_finarbill :财务应收单 im_saloutbill :销售出库单 sm_salorder :销售订单 iv_salebill :销售发票单 mpm_projinvapply :项目开票申请单 |
| 34 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 35 | fsrcbillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 36 | fe_srcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 37 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 38 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 39 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 41 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 42 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 43 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 44 | fe_materialname | fe_materialname | varchar | 255 |  | √ | ' ' |  |
| 45 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 46 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 47 | fe_remark | 备注说明 | varchar | 512 |  | √ | ' ' | 备注说明 |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 49 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 50 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 51 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 52 | factunitprice | 实际单价-废弃 | numeric | 23 | 10 | √ | 0 | 实际单价-废弃 |
| 53 | fe_tax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 54 | fsrcbilltypenum | 源单单据类型编码 | varchar | 255 |  | √ | ' ' | 源单单据类型编码 |
| 55 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 56 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 57 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 58 | finvoicecustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 59 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0 | 单位转换系数 |
| 60 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 61 | fmeasureunitid | 开票单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 62 | fsrcbillentityid | 源单分录内码ID-废弃 | varchar | 255 |  | √ | ' ' | 源单分录内码ID-废弃 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iv_salebillentry |  | fentryid |
| 2 | idx_iv_saleentry_corebill |  | fcorebillno,fcorebillentryseq |
| 3 | idx_iv_saleentry_srcbiilid |  | fe_srcbillid |
| 4 | idx_iv_saleentry_srcentryid |  | fe_srcbillentityid |
| 5 | idx_iv_saleentry_pid |  | fid |
| 6 | idx_iv_saleentry_sbillid |  | fsrcbillid |
