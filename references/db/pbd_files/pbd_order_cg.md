# 电商订单_晨光-pbd_order_cg

## 电商订单_晨光-主表 t_mal_order_cg

- **表名称：** 电商订单_晨光-主表
- **表名：** t_mal_order_cg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubmitstate | 预占确认状态 | bpchar | 1 |  | √ | ' ' | 预占确认状态,枚举: 0 :未确认预占 1 :确认预占 |
| 3 | fmarkid | 开票唯一标志 | varchar | 255 |  | √ | ' ' | 开票唯一标志 |
| 4 | forderid | 子订单号 | varchar | 80 |  | √ | ' ' | 子订单号 |
| 5 | finvoicetaxamount | 发票价税合计 | numeric | 23 | 10 | √ | 0 | 发票价税合计 |
| 6 | fporderid | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 7 | finvoiceaddress | 发票下载地址 | varchar | 1000 |  | √ | ' ' | 发票下载地址 |
| 8 | finvoicestate | 开票状态 | bpchar | 1 |  | √ | ' ' | 开票状态,枚举: 1 :待申请 2 :待审核 3 :驳回 4 :部分开票成功 5 :待出票 6 :开票成功 7 :处理中 8 :开票失败 9 :取消开票成功 |
| 9 | finvoicetax | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 12 | finvoiceresult | 开票结果 | varchar | 255 |  | √ | ' ' | 开票结果 |
| 13 | finvoicecode | 发票代码 | varchar | 80 |  | √ | ' ' | 发票代码 |
| 14 | ffreight | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 15 | fordernakedamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 16 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fordertaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | forderstate | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: 0 :取消 1 :有效 |
| 20 | fstate | 物流状态 | varchar | 2 |  | √ | ' ' | 物流状态,枚举: 0 :新建 1 :妥投 -1 :拒收 4 :退换货中 5 :发货 |
| 21 | finvoicetype | 发票类型 | bpchar | 10 |  | √ | ' ' | 发票类型,枚举: 1 :增值税发票 2 :普通发票 |
| 22 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 23 | finvoicetaxrate | 发票税率(%) | numeric | 23 | 10 | √ | 0 | 发票税率(%) |
| 24 | finvoiceid | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 25 | forderamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_order_cg |  | fid |
| 2 | idx_mal_order_cg_forderid |  | forderid |

---

## 单据体-子表 t_mal_orderentry_cg

- **表名称：** 单据体-子表
- **表名：** t_mal_orderentry_cg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0 | 数量 |
| 3 | ftaxamount | 商品税额 | numeric | 23 | 10 | √ | 0 | 商品税额 |
| 4 | fnakedamount | 商品裸价 | numeric | 23 | 10 | √ | 0 | 商品裸价 |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 电商商品 pbd_mallgoods |
| 6 | ftaxrate | 商品税率 | numeric | 19 | 6 | √ | 0 | 商品税率 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fprice | 商品单价 | numeric | 23 | 10 | √ | 0 | 商品单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_entry_cg_fgoodsid |  | fgoodsid |
| 2 | idx_mal_entry_cg_fid_fseq |  | fid,fseq |
| 3 | pk_t_mal_orderentry_cg |  | fentryid |
