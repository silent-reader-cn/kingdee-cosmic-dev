# 返利预结算单-occpic_rebateprebudget

## 返利预结算明细-子表 t_occpic_rebatepbdgentry

- **表名称：** 返利预结算明细-子表
- **表名：** t_occpic_rebatepbdgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 3 | flocalhasbudgetamount | 累计结算金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计结算金额(本位币) |
| 4 | faperunitrebateamount | 预提单位返利 | numeric | 23 | 10 | √ | 0 | 预提单位返利 |
| 5 | fsaleorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 6 | flocalaccrualamount | 预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 预提金额(本位币) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fiteminfoid | 商品名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 10 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 11 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fusdhasbudgetamount | fusdhasbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 13 | frowstatus | 行状态 | bpchar | 1 |  | √ | 'C' | 行状态,枚举: C :未结算 F :部分结算 E :结算完成 |
| 14 | fprodcutlineid | fprodcutlineid | int8 | 64 |  | √ | 0 |  |
| 15 | fhasbudgetamount | 累计结算金额 | numeric | 23 | 10 | √ | 0 | 累计结算金额 |
| 16 | faccrualfixedamount | 累计预提金额 | numeric | 23 | 10 | √ | 0 | 累计预提金额 |
| 17 | fproconsignqty | 预结算数量 | numeric | 23 | 10 | √ | 0 | 预结算数量 |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fframecontractnumber | 框架合同编码 | varchar | 80 |  | √ | ' ' | 框架合同编码 |
| 20 | flocalrebateamount | 返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 返利金额(本位币) |
| 21 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 22 | faprofitrate | 预提返点率% | numeric | 23 | 10 | √ | 0 | 预提返点率% |
| 23 | fframecontractid | 框架合同ID | int8 | 64 |  | √ | 0 | 框架合同ID |
| 24 | fusdrebateamount | fusdrebateamount | numeric | 23 | 10 | √ | 0 |  |
| 25 | fproductid | 产品型号 | int8 | 64 |  | √ | 0 | [产品目录 bd_productsummary](../basedata_files/bd_productsummary.md) |
| 26 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 27 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 28 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 31 | fhasbudgetqty | 已结算数量 | numeric | 23 | 10 | √ | 0 | 已结算数量 |
| 32 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 33 | fbenefitcustomerid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 34 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 35 | fperunitrebateamount | 单位返利 | numeric | 23 | 10 | √ | 0 | 单位返利 |
| 36 | frepolicytgtgroup | 政策目标组号 | int4 | 32 |  | √ | 0 | 政策目标组号 |
| 37 | fjoinaccamount | 关联预提金额 | numeric | 23 | 10 | √ | 0 | 关联预提金额 |
| 38 | fusdhaspayamount | fusdhaspayamount | numeric | 23 | 10 | √ | 0 |  |
| 39 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fprosaleamount | 预结算金额 | numeric | 23 | 10 | √ | 0 | 预结算金额 |
| 41 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 42 | fjoinstaamount | 关联结算金额 | numeric | 23 | 10 | √ | 0 | 关联结算金额 |
| 43 | fadjustconsignqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 44 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 45 | fhaspayamount | 已支付金额 | numeric | 23 | 10 | √ | 0 | 已支付金额 |
| 46 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 47 | fbizdatastatus | 业务数据状态 | bpchar | 1 |  | √ | 'N' | 业务数据状态,枚举: N :正常 D :已删除 |
| 48 | fsaleamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 49 | fadjustsaleamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 50 | fjoinamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 51 | fsaleorderqty | 业务单据数量 | numeric | 23 | 10 | √ | 0 | 业务单据数量 |
| 52 | farrivaltime | 送达时间 | timestamp | 0 |  |  | null | 送达时间 |
| 53 | fafixedamount | 预提固定返利金额 | numeric | 23 | 10 | √ | 0 | 预提固定返利金额 |
| 54 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 58 | faccrualamount | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 59 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 60 | flocalaccrualfixedamount | 累计预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计预提金额(本位币) |
| 61 | factualunitrebate | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 62 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | [政策目标F7 ocdbd_rebatetargetf7](../occpic_files/ocdbd_rebatetargetf7.md) |

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

## 返利预结算单-反写记录表 t_occpic_rebateprebudget_wb

- **表名称：** 返利预结算单-反写记录表
- **表名：** t_occpic_rebateprebudget_wb

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
| 1 | pk_occpic_rebateprebudget_wb |  | fentryid |
| 2 | idx_occpic_rebateprebudget_wb_fk |  | fid |

---

## 关联子实体-子表 t_occpic_rebatepbdgentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_rebatepbdgentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassociatedqty_old | 关联数量_原始携带值 | numeric | 23 | 10 |  | null | 关联数量_原始携带值 |
| 2 | fhasbudgetqty_old | 已结算数量_原始携带值 | numeric | 23 | 10 |  | null | 已结算数量_原始携带值 |
| 3 | fhasbudgetqty | 已结算数量_确认携带值 | numeric | 23 | 10 |  | null | 已结算数量_确认携带值 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 7 | fassociatedqty | 关联数量_确认携带值 | numeric | 23 | 10 |  | null | 关联数量_确认携带值 |
| 8 | fhaspayamount_old | 已支付金额_原始携带值 | numeric | 23 | 10 |  | null | 已支付金额_原始携带值 |
| 9 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 10 | fhasbudgetamount_old | 累计结算金额_原始携带值 | numeric | 23 | 10 |  | null | 累计结算金额_原始携带值 |
| 11 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 12 | fhaspayamount | 已支付金额_确认携带值 | numeric | 23 | 10 |  | null | 已支付金额_确认携带值 |
| 13 | fhasbudgetamount | 累计结算金额_确认携带值 | numeric | 23 | 10 |  | null | 累计结算金额_确认携带值 |
| 14 | faccrualfixedamount_old | 累计预提金额_原始携带值 | numeric | 23 | 10 |  | null | 累计预提金额_原始携带值 |
| 15 | faccrualfixedamount | 累计预提金额_确认携带值 | numeric | 23 | 10 |  | null | 累计预提金额_确认携带值 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rebatepbdgentry_lk |  | fpkid |
| 2 | idx_occpic_rebatepbdgentry_lk_fk |  | fentryid |

---

## 商品销售属性-多选基础资料表 t_occpic_rebateprbd_sa

- **表名称：** 商品销售属性-多选基础资料表
- **表名：** t_occpic_rebateprbd_sa

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
| 1 | idx_occpic_rebateprbdsa_fbid |  | fid,fbasedataid |
| 2 | pk_occpic_rebateprbd_sa |  | fpkid |

---

## 返利预结算单-关联追踪表 t_occpic_rebateprebudget_tc

- **表名称：** 返利预结算单-关联追踪表
- **表名：** t_occpic_rebateprebudget_tc

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
| 1 | pk_occpic_rebateprebudget_tc |  | fid |
| 2 | idx_occpic_rebateprebudget_tc_tbill |  | ftbillid |
| 3 | idx_occpic_rebateprebudget_tc_tid |  | ftid |

---

## 返利预结算单-主表 t_occpic_rebateprebudget

- **表名称：** 返利预结算单-主表
- **表名：** t_occpic_rebateprebudget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalprecvyqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 3 | frpchannelfirstgroupid | 渠道一级分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 4 | frpcontractsubject | 签约主体 | int8 | 64 |  | √ | 0 | [合同主体 ocdbd_contparties](../ocdbd_files/ocdbd_contparties.md) |
| 5 | frebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | frprepresentofficeid | frprepresentofficeid | int8 | 64 |  | √ | 0 |  |
| 9 | fisbudgetfinish | 手工结算完成 | bpchar | 1 |  | √ | '0' | 手工结算完成 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | ftotallocaltax | 总税额(本位币) | numeric | 23 | 10 | √ | 0 | 总税额(本位币) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fversion | 版本号 | int8 | 64 |  | √ | 1 | 版本号 |
| 14 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 15 | frpenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | fname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 E :结算完成 F :部分结算 |
| 18 | ftotalsaleamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 19 | ftotalrbtamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | frpincentivesubtype | 激励子类型 | bpchar | 1 |  | √ | '0' | 激励子类型,枚举: B :Sell In C :Sell Out A :Sell Through |
| 22 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :手工新增 B :自动化计算 |
| 23 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | frebatetype | 计算公式(作废) | bpchar | 1 |  | √ | 'A' | 计算公式(作废),枚举: A :按金额比例返 B :按单位数量返 C :按固定金额返 |
| 25 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 26 | fladdertypeid | 政策类别 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 27 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | [返利政策F7 ocdbd_rebatepolicyf7](../occpic_files/ocdbd_rebatepolicyf7.md) |
| 28 | frpprecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcustomerid | 返利渠道（作废） | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 32 | frpdestcaculatetype | 判断依据(作废) | varchar | 20 |  | √ | ' ' | 判断依据(作废),枚举: totalamount :按金额 totalqty :按数量 |
| 33 | frpgoodsalepropertyid | frpgoodsalepropertyid | int8 | 64 |  | √ | 0 |  |
| 34 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 35 | faccrualformulaid | 预提计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 36 | frpbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'B' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 37 | frpareaid | frpareaid | int8 | 64 |  | √ | 0 |  |
| 38 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 39 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 40 | frppdestformulaid | frppdestformulaid | int8 | 64 |  | √ | 0 |  |
| 41 | ftotaltax | 总税额 | numeric | 23 | 10 | √ | 0 | 总税额 |
| 42 | fprebudgetorgid | 预结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 45 | frpchannelsecondgroupid | 渠道二级分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 46 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 47 | frpareadepid | frpareadepid | int8 | 64 |  | √ | 0 |  |
| 48 | frpincentivetype | 激励类型 | bpchar | 1 |  | √ | '0' | 激励类型,枚举: A :返利 B :价保 |
| 49 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 50 | fprebudgetdate | 预结算日期 | timestamp | 0 |  |  | null | 预结算日期 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | ftotallocalrebateamount | 总返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 总返利金额(本位币) |
| 53 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 54 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | frpbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 57 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 59 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 60 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 61 | frebatecustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 62 | ftotalbdgamount | 总已结算金额 | numeric | 23 | 10 | √ | 0 | 总已结算金额 |
| 63 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | [政策目标F7 ocdbd_rebatetargetf7](../occpic_files/ocdbd_rebatetargetf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebateprebudget_num |  | fbillno |
| 2 | pk_occpic_rebateprebudget |  | fid |
