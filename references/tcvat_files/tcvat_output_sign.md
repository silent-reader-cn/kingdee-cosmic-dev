# 销项发票标识-tcvat_output_sign

## 销项发票标识-主表 t_tdm_invoice_output

- **表名称：** 销项发票标识-主表
- **表名：** t_tdm_invoice_output

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 3 | fdrawer | fdrawer | varchar | 100 |  | √ | ' ' |  |
| 4 | fpayee | fpayee | varchar | 100 |  | √ | ' ' |  |
| 5 | fcheckcode | fcheckcode | varchar | 100 |  | √ | ' ' |  |
| 6 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 7 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbuyeraccount | fbuyeraccount | varchar | 100 |  | √ | ' ' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fsaleraddressphone | fsaleraddressphone | varchar | 200 |  | √ | ' ' |  |
| 13 | fsaleraccount | fsaleraccount | varchar | 200 |  | √ | ' ' |  |
| 14 | fmachineno | fmachineno | varchar | 100 |  | √ | ' ' |  |
| 15 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 16 | fsgfp | fsgfp | varchar | 30 |  | √ | ' ' |  |
| 17 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 18 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 19 | freviewer | freviewer | varchar | 100 |  | √ | ' ' |  |
| 20 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 21 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 22 | fbillno | fbillno | varchar | 60 |  | √ | ' ' |  |
| 23 | fsalertaxno | fsalertaxno | varchar | 100 |  | √ | ' ' |  |
| 24 | fbuyertaxno | 购方税号 | varchar | 100 |  | √ | ' ' | 购方税号 |
| 25 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 26 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 27 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 28 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 29 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 31 | foriginalinvoiceno | foriginalinvoiceno | varchar | 100 |  | √ | ' ' |  |
| 32 | fpdfurl | fpdfurl | varchar | 600 |  | √ | ' ' |  |
| 33 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 34 | fsourcesys | fsourcesys | varchar | 50 |  | √ | ' ' |  |
| 35 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 1 :增值税电子普通发票 3 :增值税纸质普通发票 4 :增值税专用发票 |
| 36 | finvoicetype | finvoicetype | varchar | 30 |  | √ | ' ' |  |
| 37 | foriginalinvoicecode | foriginalinvoicecode | varchar | 100 |  | √ | ' ' |  |
| 38 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 39 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 40 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 41 | fproxymark | fproxymark | varchar | 30 |  | √ | ' ' |  |
| 42 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_invoice_output |  | fbillno |
| 2 | t_tdm_invoice_output_pkey |  | fid |
| 3 | idx_t_tdm_invoice_output_org |  | forgid,finvoicedate |
