# 市场费用申请单分录-ocmem_mcostapply_entry

## 执行人-多选基础资料表 t_ocmem_executor

- **表名称：** 执行人-多选基础资料表
- **表名：** t_ocmem_executor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_executor_fbid |  | fentryid,fbasedataid |
| 2 | pk_ocmem_executor |  | fpkid |

---

## 市场费用申请单分录-分表 t_ocmem_mcost_applye_p

- **表名称：** 市场费用申请单分录-分表
- **表名：** t_ocmem_mcost_applye_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryexecutestatus | 行执行状态 | bpchar | 1 |  | √ | ' ' | 行执行状态,枚举: A :未执行 B :已执行 C :执行中 D :无需执行 |
| 3 | fbudgetitemid | fbudgetitemid | int8 | 64 |  | √ | 0 |  |
| 4 | fexecuteresult | fexecuteresult | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbudgetchlclassid | fbudgetchlclassid | int8 | 64 |  | √ | 0 |  |
| 6 | flocalamtunapproved | flocalamtunapproved | numeric | 23 | 10 | √ | 0 |  |
| 7 | flocalamtapproved | flocalamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 8 | flocalaccreimamont | flocalaccreimamont | numeric | 23 | 10 | √ | 0 |  |
| 9 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fbudgetitemclassid | fbudgetitemclassid | int8 | 64 |  | √ | 0 |  |
| 11 | faccoutqty | faccoutqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fbudgetbalanceid | fbudgetbalanceid | int8 | 64 |  | √ | 0 |  |
| 13 | ftargetbudget | ftargetbudget | numeric | 23 | 10 | √ | 0 |  |
| 14 | flocaladvicereduceamt | flocaladvicereduceamt | numeric | 23 | 10 | √ | 0 |  |
| 15 | flocalamount | flocalamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | flocallinkreimamont | flocallinkreimamont | numeric | 23 | 10 | √ | 0 |  |
| 17 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 18 | flinkoutbaseqty | flinkoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | flinkoutqty | flinkoutqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fentrysupervisestatus | 行督查状态 | bpchar | 1 |  | √ | 'A' | 行督查状态,枚举: A :未督查 B :已督查 C :督查中 D :无需督查 |
| 21 | flinklocalamtapproved | flinklocalamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 22 | faccreimamont | faccreimamont | numeric | 23 | 10 | √ | 0 |  |
| 23 | flinkreimamont | flinkreimamont | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsuperviseresult | fsuperviseresult | bpchar | 1 |  | √ | ' ' |  |
| 25 | fadvicereduceamount | fadvicereduceamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fbudget | fbudget | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_applye_p |  | fentryid |
| 2 | idx_ocmem_mcostapplyep_fid |  | fid |

---

## 市场费用申请单分录-主表 t_ocmem_mcost_applye

- **表名称：** 市场费用申请单分录-主表
- **表名：** t_ocmem_mcost_applye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据 | int8 | 64 |  | √ | 0 | [市场费用申请单基础资料 ocmem_marketcost_applybd](../ocmem_files/ocmem_marketcost_applybd.md) |
| 2 | fentrywriteoffname | fentrywriteoffname | varchar | 80 |  | √ | ' ' |  |
| 3 | freachrate | 达成率（%） | numeric | 23 | 10 | √ | 0 | 达成率（%） |
| 4 | famtapproved | 已核准金额 | numeric | 23 | 10 | √ | 0 | 已核准金额 |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 7 | fmeasurementunitid | fmeasurementunitid | int8 | 64 |  | √ | 0 |  |
| 8 | fiteminfoid | 产品名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | fshopid | 门店 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | famtunapproved | 未核准金额 | numeric | 23 | 10 | √ | 0 | 未核准金额 |
| 11 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | ffeecashtypeid | ffeecashtypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 16 | fentryexpensetypeid | fentryexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 18 | fshoptypeid | fshoptypeid | int8 | 64 |  | √ | 0 |  |
| 19 | fcostamount | 成本金额 | numeric | 23 | 10 | √ | 0 | 成本金额 |
| 20 | fbaseverifiedqty | fbaseverifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | faccborwamount | faccborwamount | numeric | 23 | 10 | √ | 0 |  |
| 22 | fplansaleqty | 预计销量 | numeric | 23 | 10 | √ | 0 | 预计销量 |
| 23 | flossrate | 损耗率（%） | numeric | 23 | 10 | √ | 0 | 损耗率（%） |
| 24 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 25 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fentryenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 28 | ftotalqty | ftotalqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 30 | frefundamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 31 | famount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 32 | foriginalamt | foriginalamt | numeric | 23 | 10 | √ | 0 |  |
| 33 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 34 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 35 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | fentrybegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 37 | ffinalamt | ffinalamt | numeric | 23 | 10 | √ | 0 |  |
| 38 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | 'A' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 39 | fdisplayarea | 陈列面积 | varchar | 100 |  | √ | ' ' | 陈列面积 |
| 40 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | flinkamtapproved | flinkamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 42 | fcontractpoint | 合同点数（%） | numeric | 23 | 10 | √ | 0 | 合同点数（%） |
| 43 | foldshopid | 原门店 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 44 | fentryaccountid | fentryaccountid | int8 | 64 |  | √ | 0 |  |
| 45 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 46 | fisexecuted | 是否已执行 | bpchar | 1 |  | √ | '0' | 是否已执行 |
| 47 | flinklocalborwamount | flinklocalborwamount | numeric | 23 | 10 | √ | 0 |  |
| 48 | facclocalborwamount | facclocalborwamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 50 | foriginalqty | foriginalqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fentrywriteoffid | fentrywriteoffid | int8 | 64 |  | √ | 0 |  |
| 52 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 53 | fcostprice | 成本单价 | numeric | 23 | 10 | √ | 0 | 成本单价 |
| 54 | fverifiedqty | fverifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | factualsaleqty | 实际销量 | numeric | 23 | 10 | √ | 0 | 实际销量 |
| 56 | fentrychannelid | fentrychannelid | int8 | 64 |  | √ | 0 |  |
| 57 | flinkborwamount | flinkborwamount | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_applye |  | fentryid |
| 2 | idx_ocmem_mcae_fid |  | fid |
| 3 | idx_ocmem_mcae_item |  | fiteminfoid |
| 4 | idx_ocmem_mcae_fshop |  | fshopid |
| 5 | idx_ocmem_mcae_oshop |  | foldshopid |
