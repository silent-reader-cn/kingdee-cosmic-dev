# 电商订单_SN-pbd_order_sn

## 单据体-子表 t_mal_orderentry_sn

- **表名称：** 单据体-子表
- **表名：** t_mal_orderentry_sn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 3 | ftaxamount | 商品税额 | numeric | 23 | 10 | √ | 0.0000000000 | 商品税额 |
| 4 | fnakedamount | 商品裸价 | numeric | 23 | 10 | √ | 0.0000000000 | 商品裸价 |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [电商商品 pbd_mallgoods](../pbd_files/pbd_mallgoods.md) |
| 6 | ftaxrate | 商品税率 | numeric | 19 | 6 | √ | 0.000000 | 商品税率 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fprice | 商品单价 | numeric | 23 | 10 | √ | 0.0000000000 | 商品单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_entry_sn_fid_fseq |  | fid,fseq |
| 2 | idx_mal_entry_sn_fgoodsid |  | fgoodsid |
| 3 | pk_t_mal_orderentry_sn |  | fentryid |

---

## 电商订单_SN-主表 t_mal_order_sn

- **表名称：** 电商订单_SN-主表
- **表名：** t_mal_order_sn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubmitstate | 预占确认状态 | bpchar | 1 |  | √ | ' ' | 预占确认状态,枚举: 0 :未确认预占 1 :确认预占 |
| 3 | fmarkid | 开票唯一标志 | varchar | 255 |  | √ | ' ' | 开票唯一标志 |
| 4 | forderid | 子订单号 | varchar | 80 |  | √ | ' ' | 子订单号 |
| 5 | finvoicetaxamount | 发票价税合计 | numeric | 19 | 6 | √ | 0.000000 | 发票价税合计 |
| 6 | fporderid | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 7 | finvoiceaddress | 发票下载地址 | varchar | 1000 |  | √ | ' ' | 发票下载地址 |
| 8 | finvoicestate | 开票状态 | bpchar | 1 |  | √ | ' ' | 开票状态,枚举: 1 :待申请 5 :待出票 6 :开票成功 8 :开票失败 |
| 9 | finvoicetax | 发票税额 | numeric | 19 | 6 | √ | 0.000000 | 发票税额 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 12 | finvoiceresult | 开票结果 | varchar | 255 |  | √ | ' ' | 开票结果 |
| 13 | finvoicecode | 发票代码 | varchar | 80 |  | √ | ' ' | 发票代码 |
| 14 | ffreight | 运费 | numeric | 19 | 6 | √ | 0.000000 | 运费 |
| 15 | fordernakedamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 16 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fordertaxamount | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 19 | forderstate | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: 1 :审核中 2 :待发货 3 :待收货或待服务 4 :已完成或已服务 5 :已取消 6 :已退货 7 :待处理 8 :审核不通过，订单已取消 9 :待支付 |
| 20 | finvoicetype | 发票类型 | bpchar | 10 |  | √ | ' ' | 发票类型,枚举: 2 :普票 4 :电子发票 6 :增票 |
| 21 | finvoiceamount | 发票金额 | numeric | 19 | 6 | √ | 0.000000 | 发票金额 |
| 22 | finvoicetaxrate | 发票税率(%) | numeric | 19 | 6 | √ | 0.000000 | 发票税率(%) |
| 23 | finvoiceid | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 24 | forderamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 25 | fsuborderstate | 子订单状态码 | bpchar | 1 |  | √ | ' ' | 子订单状态码,枚举: 1 :审核中 2 :待发货 3 :待收货或待服务 4 :已完成或已服务 5 :已取消 6 :已退货 7 :待处理 8 :审核不通过，订单已取消 9 :待支付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_order_sn |  | fid |
| 2 | idx_mal_order_sn_forderid |  | forderid |
