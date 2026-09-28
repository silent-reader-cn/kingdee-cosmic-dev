# 返利结算单-occpic_rebatestatement

## 关联子实体-子表 t_occpic_rebatestmentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_rebatestmentry_lk

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
| 1 | idx_occpic_rebatestmentry_lk_fk |  | fentryid |
| 2 | pk_occpic_rebatestmentry_lk |  | fpkid |

---

## 关联子实体-子表 t_occpic_rebatestatement_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_rebatestatement_lk

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
| 1 | pk_occpic_rebatestatement_lk |  | fpkid |
| 2 | idx_occpic_rebatestatement_lk_fk |  | fid |

---

## 返利结算单-主表 t_occpic_rebatestatement

- **表名称：** 返利结算单-主表
- **表名：** t_occpic_rebatestatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesattrsid | fsalesattrsid | int8 | 64 |  | √ | 0 |  |
| 3 | fchncustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | ftotalstateqty | 总结算数量 | numeric | 23 | 10 | √ | 0 | 总结算数量 |
| 5 | frebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 6 | fdestcaculatetype | 判断依据 | varchar | 20 |  | √ | ' ' | 判断依据,枚举: totalamount :按金额 totalqty :按数量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fofficeid | fofficeid | int8 | 64 |  | √ | 0 |  |
| 12 | ftotallocaltax | 总税额(本位币) | numeric | 23 | 10 | √ | 0 | 总税额(本位币) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fisbatchsettle | 批量结算 | bpchar | 1 |  | √ | '0' | 批量结算 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fincentivetype | 激励类型 | bpchar | 1 |  | √ | 'A' | 激励类型,枚举: A :返利 B :价保 |
| 17 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 20 | fbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'B' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 21 | frebatetype | 资金池类型 | bpchar | 1 |  | √ | 'A' | 资金池类型,枚举: A :品牌商 B :渠道商 |
| 22 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 23 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | [返利政策F7 ocdbd_rebatepolicyf7](../occpic_files/ocdbd_rebatepolicyf7.md) |
| 24 | ftotalapprovedamt | 总已使用核销金额 | numeric | 23 | 10 | √ | 0 | 总已使用核销金额 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | faccountid | 返利账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 27 | fcustomerid | 返利渠道（作废） | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | fchannelsecondgroupid | 渠道二级分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 30 | ftotalrebamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 31 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 32 | fchannelfirstgroupid | 渠道一级分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 33 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 34 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 35 | ftotaltax | 总税额 | numeric | 23 | 10 | √ | 0 | 总税额 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fstatementdate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 38 | fstatementorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 41 | fstmcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fidentify | 单据名称 | varchar | 80 |  | √ | ' ' | 单据名称 |
| 43 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | ftotallocalrebateamount | 总返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 总返利金额(本位币) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 48 | fpaytype | 兑付方式 | bpchar | 1 |  | √ | 'A' | 兑付方式,枚举: A :应收账款红冲 B :上账资金池 |
| 49 | fcontractsubjectid | 签约主体 | int8 | 64 |  | √ | 0 | [合同主体 ocdbd_contparties](../ocdbd_files/ocdbd_contparties.md) |
| 50 | fincentivesubtype | 激励子类型 | bpchar | 1 |  | √ | 'A' | 激励子类型,枚举: B :SI C :SO A :ST |
| 51 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 53 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestatement_num |  | fbillno |
| 2 | pk_occpic_rebatestatement |  | fid |

---

## 返利结算单-反写记录表 t_occpic_rebatestatement_wb

- **表名称：** 返利结算单-反写记录表
- **表名：** t_occpic_rebatestatement_wb

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
| 1 | idx_occpic_rebatestatement_wb_fk |  | fid |
| 2 | pk_occpic_rebatestatement_wb |  | fentryid |

---

## 预算汇总-子表 t_occpic_rebatestm_see

- **表名称：** 预算汇总-子表
- **表名：** t_occpic_rebatestm_see

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsmemchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | fsmemdepartmentid | 预算承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsmemprovinceid | 预算省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsmemitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 7 | fsmemchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fsmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 9 | fsmemregionid | 预算大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsmemitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 11 | fsfeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 12 | fsmemyearid | 预算年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 13 | fsrebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestmsee_fid |  | fid |
| 2 | pk_occpic_rebatestm_see |  | fentryid |

---

## 返利结算明细-子表 t_occpic_rebatestmentry

- **表名称：** 返利结算明细-子表
- **表名：** t_occpic_rebatestmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fiteminfoid | 商品名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 5 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 6 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 7 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fprodcutlineid | fprodcutlineid | int8 | 64 |  | √ | 0 |  |
| 9 | fmemitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 10 | ftotalaccamount | 累计补提金额 | numeric | 23 | 10 | √ | 0 | 累计补提金额 |
| 11 | fhasbudgetamount | 已兑付金额 | numeric | 23 | 10 | √ | 0 | 已兑付金额 |
| 12 | faccrualfixedamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 13 | fsourceorderid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 14 | fmemregionid | 预算大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | foccupyamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fframecontractnumber | 框架合同编码 | varchar | 80 |  | √ | ' ' | 框架合同编码 |
| 18 | fpropayunitprice | 已支付单位价保 | numeric | 23 | 10 | √ | 0 | 已支付单位价保 |
| 19 | flocalrebateamount | 返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 返利金额(本位币) |
| 20 | fadjuststatementqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 21 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 22 | fscunitrbamount | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 23 | fproductid | 产品型号 | int8 | 64 |  | √ | 0 | [产品目录 bd_productsummary](../basedata_files/bd_productsummary.md) |
| 24 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 25 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 26 | fstatementqty | 结算数量 | numeric | 23 | 10 | √ | 0 | 结算数量 |
| 27 | fadjuststunitprice | 调整单位返利 | numeric | 23 | 10 | √ | 0 | 调整单位返利 |
| 28 | fsourceorderno | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 29 | fsrcbilltype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型 |
| 30 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fapprovedamt | 已使用核销金额 | numeric | 23 | 10 | √ | 0 | 已使用核销金额 |
| 33 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 34 | fmemdepartmentid | 预算承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fbenefitcustomerid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 37 | fcontractid | 框架合同ID | int8 | 64 |  | √ | 0 | 框架合同ID |
| 38 | fechncustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 39 | favailablebalance | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 40 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 41 | fperunitrebateamount | 单位返利 | numeric | 23 | 10 | √ | 0 | 单位返利 |
| 42 | fjoinaccamount | 关联补提金额 | numeric | 23 | 10 | √ | 0 | 关联补提金额 |
| 43 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 45 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 46 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 47 | fsaleamount | 销售金额 | numeric | 23 | 10 | √ | 0 | 销售金额 |
| 48 | fmemitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 49 | fmemprovinceid | 预算省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fsourceorderentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 51 | flocalaccrualdifamount | 未关联金额(本位币) | numeric | 23 | 10 | √ | 0 | 未关联金额(本位币) |
| 52 | farrivaltime | 送达时间 | timestamp | 0 |  |  | null | 送达时间 |
| 53 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fmemchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 57 | fmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 58 | fmemchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 59 | fpurorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 60 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 61 | faccrualdifamount | 未关联金额 | numeric | 23 | 10 | √ | 0 | 未关联金额 |
| 62 | fmemyearid | 预算年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 63 | flocalaccrualfixedamount | 已关联金额(本位币) | numeric | 23 | 10 | √ | 0 | 已关联金额(本位币) |
| 64 | factualunitrebate | 实际单位返利 | numeric | 23 | 10 | √ | 0 | 实际单位返利 |
| 65 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | [政策目标F7 ocdbd_rebatetargetf7](../occpic_files/ocdbd_rebatetargetf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestmentry_fid |  | fid |
| 2 | pk_occpic_rebatestmentry |  | fentryid |

---

## 商品销售属性-多选基础资料表 t_occpic_rebatestm_sa

- **表名称：** 商品销售属性-多选基础资料表
- **表名：** t_occpic_rebatestm_sa

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestmsa_fbid |  | fid,fbasedataid |
| 2 | pk_occpic_rebatestm_sa |  | fpkid |

---

## 返利结算单-关联追踪表 t_occpic_rebatestatement_tc

- **表名称：** 返利结算单-关联追踪表
- **表名：** t_occpic_rebatestatement_tc

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
| 1 | pk_occpic_rebatestatement_tc |  | fid |
| 2 | idx_occpic_rebatestatement_tc_tid |  | ftid |
| 3 | idx_occpic_rebatestatement_tc_tbill |  | ftbillid |
