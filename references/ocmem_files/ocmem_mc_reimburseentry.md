# 报销单的报销分录-ocmem_mc_reimburseentry

## 报销单的报销分录-主表 t_ocmem_mc_reimentry

- **表名称：** 报销单的报销分录-主表
- **表名：** t_ocmem_mc_reimentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrywriteoffname | fentrywriteoffname | varchar | 80 |  | √ | ' ' |  |
| 3 | freachrate | freachrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | famtapproved | 核准金额 | numeric | 23 | 10 | √ | 0 | 核准金额 |
| 5 | fsourceid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 6 | fsourceentryid | 来源单据分录id | varchar | 100 |  | √ | ' ' | 来源单据分录id |
| 7 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fiteminfoid | 产品名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fshopid | 门店名称 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | famtunapproved | 未核准金额 | numeric | 23 | 10 | √ | 0 | 未核准金额 |
| 12 | famtapply | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 13 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | ffeecashtypeid | ffeecashtypeid | int8 | 64 |  | √ | 0 |  |
| 16 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 18 | fentryexpensetypeid | fentryexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 19 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 20 | fshoptypeid | fshoptypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fcostamount | 成本金额 | numeric | 23 | 10 | √ | 0 | 成本金额 |
| 22 | fplansaleqty | 预计销量 | numeric | 23 | 10 | √ | 0 | 预计销量 |
| 23 | flossrate | 损耗率（%） | numeric | 23 | 10 | √ | 0 | 损耗率（%） |
| 24 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 25 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 28 | famount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 29 | foriginalamt | foriginalamt | numeric | 23 | 10 | √ | 0 |  |
| 30 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 31 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 32 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | ffinalamt | ffinalamt | numeric | 23 | 10 | √ | 0 |  |
| 34 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | ' ' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 35 | fdisplayarea | 陈列面积 | varchar | 100 |  | √ | ' ' | 陈列面积 |
| 36 | fcontractpoint | 合同点数（%） | numeric | 23 | 10 | √ | 0 | 合同点数（%） |
| 37 | foldshopid | 原门店 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 38 | fentryaccountid | fentryaccountid | int8 | 64 |  | √ | 0 |  |
| 39 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 40 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 41 | foriginalqty | foriginalqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | frowparentexpenseid | frowparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 43 | fentrywriteoffid | fentrywriteoffid | int8 | 64 |  | √ | 0 |  |
| 44 | frowexpensetypeid | frowexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 45 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 46 | fcostprice | 成本单价 | numeric | 23 | 10 | √ | 0 | 成本单价 |
| 47 | fverifiedqty | fverifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 48 | factualsaleqty | 实际销量 | numeric | 23 | 10 | √ | 0 | 实际销量 |
| 49 | fentrychannelid | fentrychannelid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mcre_fseid |  | fsourceentryid |
| 2 | pk_ocmem_mc_reimentry |  | fentryid |
| 3 | idx_ocmem_mcre_itemid |  | fiteminfoid |
| 4 | idx_ocmem_mcre_ospid |  | foldshopid |
| 5 | idx_ocmem_mcre_fid |  | fid |
| 6 | idx_ocmem_mcre_fsid |  | fsourceid |
