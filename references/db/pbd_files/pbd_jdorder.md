# 京东订单-pbd_jdorder

## 单据体-子表 t_mal_jdorderentry

- **表名称：** 单据体-子表
- **表名：** t_mal_jdorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0 | 数量 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fjdprice | 京东价 | numeric | 23 | 10 | √ | 0 | 京东价 |
| 6 | ftotalprice | 含费价格 | numeric | 23 | 10 | √ | 0 | 含费价格 |
| 7 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_jdorderentry |  | fentryid |
| 2 | idx_mal_jdorderentry_fid_fseq |  | fid,fseq |
| 3 | idx_mal_jdorderentry_fgoodsid |  | fgoodsid |

---

## 京东订单-主表 t_mal_jdorder

- **表名称：** 京东订单-主表
- **表名：** t_mal_jdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaddress | 发票下载地址 | varchar | 1000 |  | √ | ' ' | 发票下载地址 |
| 3 | fmarkid | 开票唯一标志 | varchar | 255 |  | √ | ' ' | 开票唯一标志 |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fjdstate | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: 0 :新建 1 :妥投 2 :拒收 3 :妥投 |
| 6 | finvoicetaxamount | 发票价税合计 | numeric | 19 | 6 | √ | 0 | 发票价税合计 |
| 7 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | finvoicestate | 开票状态 | bpchar | 1 |  | √ | ' ' | 开票状态,枚举: 1 :待申请 2 :待审核 3 :驳回 4 :部分开票成功 5 :待出票 6 :开票成功 7 :处理中 8 :开票失败 9 :取消开票成功 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvoicetax | 发票税额 | numeric | 19 | 6 | √ | 0 | 发票税额 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 13 | fjdorderid | 京东订单号 | varchar | 80 |  | √ | ' ' | 京东订单号 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | finvoiceresult | 开票结果 | varchar | 255 |  | √ | ' ' | 开票结果 |
| 18 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 19 | fpaycodeid | 付款识别码 | varchar | 80 |  | √ | ' ' | 付款识别码 |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | finvoicecode | 发票代码 | varchar | 80 |  | √ | ' ' | 发票代码 |
| 22 | fjdchildorderstatus | 京东状态 | varchar | 2 |  | √ | ' ' | 京东状态,枚举: 1 :新单 2 :等待支付 3 :等待支付确认 4 :延迟付款确认 5 :订单暂停 6 :店长最终审核 7 :等待打印 8 :等待出库 9 :等待打包 10 :等待发货 11 :自提途中 12 :上门提货 13 :自提退货 14 :确认自提 16 :等待确认收货 17 :配送退货 18 :货到付款确认 19 :已完成 21 :收款确认 22 :锁定 29 :等待三方出库 30 :等待三方发货 31 :等待三方发货完成 0 :其他 |
| 23 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0 | 价税合计 |
| 24 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 26 | ffreight | 运费 | numeric | 19 | 6 | √ | 0 | 运费 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 29 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fjdorderstate | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: 0 :取消 1 :有效 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 34 | finvoicetype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: 2 :增值税专用发票 3 :增值税电子普通发票 1 :普票 |
| 35 | ftax | 税额 | numeric | 19 | 6 | √ | 0 | 税额 |
| 36 | finvoiceamount | 发票金额 | numeric | 19 | 6 | √ | 0 | 发票金额 |
| 37 | finvoiceid | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 38 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fnumber | 京东子订单号 | varchar | 80 |  | √ | ' ' | 京东子订单号 |
| 40 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_jdorder_master |  | fmasterid |
| 2 | pk_mal_jdorder |  | fid |
| 3 | idx_mal_jdorder_number |  | fnumber |
| 4 | idx_t_mal_jdorder_createorg |  | fcreateorgid |
| 5 | idx_mal_jdorder_fjdorderid |  | fjdorderid |

---

## 京东订单-多语言表 t_mal_jdorder_l

- **表名称：** 京东订单-多语言表
- **表名：** t_mal_jdorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_jdorder_l_fid |  | fid,flocaleid |
| 2 | pk_mal_jdorder_l |  | fpkid |

---

## 京东订单-使用范围表 t_mal_jdorder_u

- **表名称：** 京东订单-使用范围表
- **表名：** t_mal_jdorder_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_jdorder_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mal_jdorder_u_uo |  | fuseorgid |

---

## 京东订单-使用范围位图表 t_mal_jdorder_m

- **表名称：** 京东订单-使用范围位图表
- **表名：** t_mal_jdorder_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_jdorder_m |  | forgid |
