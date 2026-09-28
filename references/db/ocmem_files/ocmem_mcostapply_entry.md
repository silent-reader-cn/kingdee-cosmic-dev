# 市场费用申请单分录-ocmem_mcostapply_entry

## 市场费用申请单分录-主表 t_ocmem_mcost_applye

- **表名称：** 市场费用申请单分录-主表
- **表名：** t_ocmem_mcost_applye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据 | int8 | 64 |  | √ | 0 | 市场费用申请单基础资料 ocmem_marketcost_applybd |
| 2 | fentrywriteoffname | fentrywriteoffname | varchar | 80 |  | √ | ' ' |  |
| 3 | freachrate | 达成率（%） | numeric | 23 | 10 | √ | 0 | 达成率（%） |
| 4 | famtapproved | 已核准金额 | numeric | 23 | 10 | √ | 0 | 已核准金额 |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 7 | fiteminfoid | 产品名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 8 | fshopid | 门店 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | famtunapproved | 未核准金额 | numeric | 23 | 10 | √ | 0 | 未核准金额 |
| 10 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | ffeecashtypeid | ffeecashtypeid | int8 | 64 |  | √ | 0 |  |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 15 | fentryexpensetypeid | fentryexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 16 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 17 | fshoptypeid | fshoptypeid | int8 | 64 |  | √ | 0 |  |
| 18 | fcostamount | 成本金额 | numeric | 23 | 10 | √ | 0 | 成本金额 |
| 19 | fplansaleqty | 预计销量 | numeric | 23 | 10 | √ | 0 | 预计销量 |
| 20 | flossrate | 损耗率（%） | numeric | 23 | 10 | √ | 0 | 损耗率（%） |
| 21 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 22 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fentryenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 25 | ftotalqty | ftotalqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 27 | frefundamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 28 | famount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 29 | foriginalamt | foriginalamt | numeric | 23 | 10 | √ | 0 |  |
| 30 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 31 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 32 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fentrybegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 34 | ffinalamt | ffinalamt | numeric | 23 | 10 | √ | 0 |  |
| 35 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | 'A' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 36 | fdisplayarea | 陈列面积 | varchar | 100 |  | √ | ' ' | 陈列面积 |
| 37 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fcontractpoint | 合同点数（%） | numeric | 23 | 10 | √ | 0 | 合同点数（%） |
| 39 | foldshopid | 原门店 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 40 | fentryaccountid | fentryaccountid | int8 | 64 |  | √ | 0 |  |
| 41 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 42 | fisexecuted | 是否已执行 | bpchar | 1 |  | √ | '0' | 是否已执行 |
| 43 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 44 | foriginalqty | foriginalqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fentrywriteoffid | fentrywriteoffid | int8 | 64 |  | √ | 0 |  |
| 46 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 47 | fcostprice | 成本单价 | numeric | 23 | 10 | √ | 0 | 成本单价 |
| 48 | fverifiedqty | fverifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | factualsaleqty | 实际销量 | numeric | 23 | 10 | √ | 0 | 实际销量 |
| 50 | fentrychannelid | fentrychannelid | int8 | 64 |  | √ | 0 |  |

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

---

## 执行人-多选基础资料表 t_ocmem_executor

- **表名称：** 执行人-多选基础资料表
- **表名：** t_ocmem_executor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
