# 返利预结算单-occpic_rebateprebudget

## 返利预结算明细-子表 t_occpic_rebatepbdgentry

- **表名称：** 返利预结算明细-子表
- **表名：** t_occpic_rebatepbdgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | fhasbudgetqty | 已结算数量 | numeric | 23 | 10 | √ | 0 | 已结算数量 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fbenefitcustomerid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 7 | fsaleorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fiteminfoid | 商品名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 11 | fperunitrebateamount | 单位返利 | numeric | 23 | 10 | √ | 0 | 单位返利 |
| 12 | frepolicytgtgroup | 政策目标组号 | int4 | 32 |  | √ | 0 | 政策目标组号 |
| 13 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 14 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 15 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fusdhasbudgetamount | fusdhasbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 17 | fusdhaspayamount | fusdhaspayamount | numeric | 23 | 10 | √ | 0 |  |
| 18 | frowstatus | 行状态 | bpchar | 1 |  | √ | 'C' | 行状态,枚举: C :未结算 F :部分结算 E :结算完成 |
| 19 | fprodcutlineid | fprodcutlineid | int8 | 64 |  | √ | 0 |  |
| 20 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fprosaleamount | 预结算金额 | numeric | 23 | 10 | √ | 0 | 预结算金额 |
| 22 | fadjustconsignqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 23 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 24 | fhaspayamount | 已支付金额 | numeric | 23 | 10 | √ | 0 | 已支付金额 |
| 25 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 26 | fhasbudgetamount | 已结算金额 | numeric | 23 | 10 | √ | 0 | 已结算金额 |
| 27 | fsaleamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 28 | fproconsignqty | 预结算数量 | numeric | 23 | 10 | √ | 0 | 预结算数量 |
| 29 | fadjustsaleamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 30 | fsaleorderqty | 业务单据数量 | numeric | 23 | 10 | √ | 0 | 业务单据数量 |
| 31 | farrivaltime | 送达时间 | timestamp | 0 |  |  | null | 送达时间 |
| 32 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fframecontractnumber | 框架合同编码 | varchar | 80 |  | √ | ' ' | 框架合同编码 |
| 34 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 38 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 39 | fframecontractid | 框架合同ID | int8 | 64 |  | √ | 0 | 框架合同ID |
| 40 | fusdrebateamount | fusdrebateamount | numeric | 23 | 10 | √ | 0 |  |
| 41 | fproductid | 产品型号 | int8 | 64 |  | √ | 0 | 产品目录 bd_productsummary |
| 42 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 43 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 44 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | factualunitrebate | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 47 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 政策目标F7 ocdbd_rebatetargetf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatepbdgentry_fid |  | fid |
| 2 | pk_occpic_rebatepbdgentry |  | fentryid |

---

## 商品销售属性-多选基础资料表 t_occpic_rebateprbd_sa

- **表名称：** 商品销售属性-多选基础资料表
- **表名：** t_occpic_rebateprbd_sa

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
| 1 | idx_occpic_rebateprbdsa_fbid |  | fid,fbasedataid |
| 2 | pk_occpic_rebateprbd_sa |  | fpkid |

---

## 返利预结算单-主表 t_occpic_rebateprebudget

- **表名称：** 返利预结算单-主表
- **表名：** t_occpic_rebateprebudget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalprecvyqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 3 | frpchannelfirstgroupid | 渠道一级分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 4 | frpcontractsubject | 签约主体 | int8 | 64 |  | √ | 0 | 合同主体 ocdbd_contparties |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | frprepresentofficeid | frprepresentofficeid | int8 | 64 |  | √ | 0 |  |
| 7 | fisbudgetfinish | 手工结算完成 | bpchar | 1 |  | √ | '0' | 手工结算完成 |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fversion | 版本号 | int8 | 64 |  | √ | 1 | 版本号 |
| 10 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 11 | frpenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 E :结算完成 F :部分结算 |
| 14 | ftotalsaleamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 15 | ftotalrbtamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | frpincentivesubtype | 激励子类型 | bpchar | 1 |  | √ | '0' | 激励子类型,枚举: B :Sell In C :Sell Out A :Sell Through |
| 18 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :手工新增 B :自动化计算 |
| 19 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | frebatetype | 计算公式(作废) | bpchar | 1 |  | √ | 'A' | 计算公式(作废),枚举: A :按金额比例返 B :按单位数量返 C :按固定金额返 |
| 21 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 22 | fladdertypeid | 政策类别 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 23 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | 返利政策F7 ocdbd_rebatepolicyf7 |
| 24 | frpprecurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fcustomerid | 返利渠道（作废） | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 28 | frpdestcaculatetype | 判断依据(作废) | varchar | 20 |  | √ | ' ' | 判断依据(作废),枚举: totalamount :按金额 totalqty :按数量 |
| 29 | frpgoodsalepropertyid | frpgoodsalepropertyid | int8 | 64 |  | √ | 0 |  |
| 30 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 31 | frpbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'B' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 32 | frpareaid | frpareaid | int8 | 64 |  | √ | 0 |  |
| 33 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 34 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 35 | frppdestformulaid | frppdestformulaid | int8 | 64 |  | √ | 0 |  |
| 36 | fprebudgetorgid | 预结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 39 | frpchannelsecondgroupid | 渠道二级分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 40 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 41 | frpareadepid | frpareadepid | int8 | 64 |  | √ | 0 |  |
| 42 | frpincentivetype | 激励类型 | bpchar | 1 |  | √ | '0' | 激励类型,枚举: A :返利 B :价保 |
| 43 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 44 | fprebudgetdate | 预结算日期 | timestamp | 0 |  |  | null | 预结算日期 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 47 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | frpbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 50 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 51 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 52 | frebatecustomerid | 返利客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 53 | ftotalbdgamount | 总已结算金额 | numeric | 23 | 10 | √ | 0 | 总已结算金额 |
| 54 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 政策目标F7 ocdbd_rebatetargetf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebateprebudget_num |  | fbillno |
| 2 | pk_occpic_rebateprebudget |  | fid |
