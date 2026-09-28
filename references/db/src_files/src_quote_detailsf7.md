# 议价详情F7-src_quote_detailsf7

## 议价详情F7-主表 t_src_quote_details

- **表名称：** 议价详情F7-主表
- **表名：** t_src_quote_details

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 2 | fnegotiatedate | 议价时间 | timestamp | 0 |  |  | null | 议价时间 |
| 3 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 4 | fentrystatus | 议标状态 | bpchar | 1 |  | √ | ' ' | 议标状态,枚举: A :未响应 B :已响应 |
| 5 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) 16 :议价(15) 17 :议价(16) 18 :议价(17) 19 :议价(18) 20 :议价(19) 21 :议价(20) 22 :议价(21) 23 :议价(22) 24 :议价(23) 25 :议价(24) 26 :议价(25) 27 :议价(26) 28 :议价(27) 29 :议价(28) 30 :议价(29) 31 :补价(1) 32 :补价(2) 33 :补价(3) 34 :补价(4) 35 :补价(5) |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fnegotiatetype | 议价方式 | bpchar | 1 |  | √ | ' ' | 议价方式,枚举: 1 :线上议价 2 :线下议价(标的) 3 :线下议价(标段) |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_quote_details_fid |  | fid |
| 2 | pk_src_quote_details |  | fentryid |
| 3 | idx_src_quote_details_sup |  | fsupplierid |
