# 销项发票明细表-tcvat_sim_vatinvoice_item

## 销项发票明细表-主表 t_sim_vatinvoice_item

- **表名称：** 销项发票明细表-主表
- **表名：** t_sim_vatinvoice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 发票主表id | int8 | 64 |  | √ | 0 | 发票主表id |
| 2 | fsimplegoodsname | fsimplegoodsname | varchar | 50 |  | √ | ' ' |  |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: |
| 4 | fdiscountrate | fdiscountrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | frowtype | frowtype | varchar | 30 |  | √ | ' ' |  |
| 6 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 8 | fspmc | fspmc | int8 | 64 |  | √ | 0 |  |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fitemremainredtax | fitemremainredtax | numeric | 23 | 10 | √ | 0 |  |
| 11 | fnum | fnum | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 13 | fwriteoffqty | fwriteoffqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | funitprice | funitprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 16 | fgoodsname | 商品名称 | varchar | 128 |  | √ | ' ' | 商品名称 |
| 17 | fbillsourceid | fbillsourceid | varchar | 50 |  | √ | ' ' |  |
| 18 | fitemremainredamount | fitemremainredamount | numeric | 23 | 10 | √ | 0 |  |
| 19 | foriginalinvoiceitemid | foriginalinvoiceitemid | int8 | 64 |  | √ | 0 |  |
| 20 | fzzstsgl | fzzstsgl | varchar | 2000 |  | √ | ' ' |  |
| 21 | fuserinputgoodsname | fuserinputgoodsname | varchar | 128 |  | √ | ' ' |  |
| 22 | fspbm | fspbm | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | ftaxflag | ftaxflag | varchar | 8 |  | √ | ' ' |  |
| 25 | fzerotaxmark | fzerotaxmark | varchar | 8 |  | √ | ' ' |  |
| 26 | ftaxpremark | ftaxpremark | varchar | 16 |  | √ | ' ' |  |
| 27 | ftaxunitprice | ftaxunitprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fgoodscode | fgoodscode | varchar | 50 |  | √ | ' ' |  |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 31 | fzxbm | fzxbm | varchar | 128 |  | √ | ' ' |  |
| 32 | fvehplate | fvehplate | varchar | 50 |  | √ | ' ' |  |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | funit | funit | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_vatinvoice_item |  | fentryid |
| 2 | idx_vatinvo_item_fgoodscode |  | fgoodscode |
| 3 | idx_sim_vatinvoice_item_fk |  | fid |
