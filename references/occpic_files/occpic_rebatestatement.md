# 返利结算单-occpic_rebatestatement

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

## 返利结算明细-子表 t_occpic_rebatestmentry

- **表名称：** 返利结算明细-子表
- **表名：** t_occpic_rebatestmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fbenefitcustomerid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fcontractid | 框架合同ID | int8 | 64 |  | √ | 0 | 框架合同ID |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fechncustomerid | 返利客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | fiteminfoid | 商品名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | favailablebalance | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 11 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 12 | fperunitrebateamount | 单位返利 | numeric | 23 | 10 | √ | 0 | 单位返利 |
| 13 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 14 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 15 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fprodcutlineid | fprodcutlineid | int8 | 64 |  | √ | 0 |  |
| 17 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 19 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 20 | fhasbudgetamount | 已兑付金额 | numeric | 23 | 10 | √ | 0 | 已兑付金额 |
| 21 | fsaleamount | 销售金额 | numeric | 23 | 10 | √ | 0 | 销售金额 |
| 22 | fsourceorderid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 23 | fsourceorderentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 24 | foccupyamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 25 | farrivaltime | 送达时间 | timestamp | 0 |  |  | null | 送达时间 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fframecontractnumber | 框架合同编码 | varchar | 80 |  | √ | ' ' | 框架合同编码 |
| 28 | fpropayunitprice | 已支付单位价保 | numeric | 23 | 10 | √ | 0 | 已支付单位价保 |
| 29 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fadjuststatementqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 33 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 34 | fscunitrbamount | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 35 | fproductid | 产品型号 | int8 | 64 |  | √ | 0 | 产品目录 bd_productsummary |
| 36 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 37 | fpurorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 38 | fstatementqty | 结算数量 | numeric | 23 | 10 | √ | 0 | 结算数量 |
| 39 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 40 | fadjuststunitprice | 调整单位返利 | numeric | 23 | 10 | √ | 0 | 调整单位返利 |
| 41 | fsourceorderno | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 42 | fsrcbilltype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型 |
| 43 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | factualunitrebate | 实际单位返利 | numeric | 23 | 10 | √ | 0 | 实际单位返利 |
| 46 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 政策目标F7 ocdbd_rebatetargetf7 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
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

---

## 返利结算单-主表 t_occpic_rebatestatement

- **表名称：** 返利结算单-主表
- **表名：** t_occpic_rebatestatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelsecondgroupid | 渠道二级分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 3 | ftotalrebamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 4 | fsalesattrsid | fsalesattrsid | int8 | 64 |  | √ | 0 |  |
| 5 | fchncustomerid | 返利客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 7 | ftotalstateqty | 总结算数量 | numeric | 23 | 10 | √ | 0 | 总结算数量 |
| 8 | fchannelfirstgroupid | 渠道一级分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 9 | fdestcaculatetype | 判断依据 | varchar | 20 |  | √ | ' ' | 判断依据,枚举: totalamount :按金额 totalqty :按数量 |
| 10 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fstatementdate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 16 | fstatementorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 19 | fstmcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fofficeid | fofficeid | int8 | 64 |  | √ | 0 |  |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fidentify | 单据名称 | varchar | 80 |  | √ | ' ' | 单据名称 |
| 23 | fisbatchsettle | 批量结算 | bpchar | 1 |  | √ | '0' | 批量结算 |
| 24 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fincentivetype | 激励类型 | bpchar | 1 |  | √ | 'A' | 激励类型,枚举: A :返利 B :价保 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 30 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fpaytype | 支付方式 | bpchar | 1 |  | √ | 'A' | 支付方式,枚举: A :开红票 B :下单抵扣 |
| 33 | fcontractsubjectid | 签约主体 | int8 | 64 |  | √ | 0 | 合同主体 ocdbd_contparties |
| 34 | fincentivesubtype | 激励子类型 | bpchar | 1 |  | √ | 'A' | 激励子类型,枚举: B :SI C :SO A :ST |
| 35 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 36 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 37 | fbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'B' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 38 | frebatetype | 资金池类型 | bpchar | 1 |  | √ | 'A' | 资金池类型,枚举: A :品牌商 B :渠道商 |
| 39 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 40 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | 返利政策F7 ocdbd_rebatepolicyf7 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | faccountid | 激励账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 43 | fcustomerid | 返利渠道（作废） | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 44 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestatement_num |  | fbillno |
| 2 | pk_occpic_rebatestatement |  | fid |
