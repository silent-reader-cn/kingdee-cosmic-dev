# 发票台账历史数据表-er_invoiceinforptbill

## 发票台账历史数据表-主表 t_er_invoiceinforptbill

- **表名称：** 发票台账历史数据表-主表
- **表名：** t_er_invoiceinforptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | finvoicefromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 5 | fmakeoutcompname | 开票公司 | varchar | 255 |  |  | ' ' | 开票公司 |
| 6 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 7 | finvoicetocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 8 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | foffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 10 | fpassengername | 旅客 | varchar | 255 |  |  | ' ' | 旅客 |
| 11 | foffsetamount | 可抵扣金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣金额 |
| 12 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 |
| 13 | fgoodsname | 发票内容 | varchar | 255 |  |  | ' ' | 发票内容 |
| 14 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 15 | finvoicecode | 发票代码 | varchar | 255 |  |  | ' ' | 发票代码 |
| 16 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 17 | fbuyername | 收票公司 | varchar | 255 |  |  | ' ' | 收票公司 |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  |  | ' ' | 发票号码 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fbilltype | 单据类型 | varchar | 255 |  |  | ' ' | 单据类型,枚举: er_dailyreimbursebill :费用报销单 er_tripreimbursebill :差旅报销单 er_invoiceorderbill :开票申请单 er_publicreimbursebill :对公报销单 er_checkingpaybill :商旅付款申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_invoiceinforptbill_pkey |  | fid |
| 2 | idx_er_t_er_invoiceinforptbill |  | finvoicetype,fbilltype |
