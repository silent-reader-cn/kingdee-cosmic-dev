# 销项发票-tdm_invoice_output

## 销项发票-主表 t_tdm_invoice_output

- **表名称：** 销项发票-主表
- **表名：** t_tdm_invoice_output

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 3 | fdrawer | 开票人 | varchar | 100 |  | √ | ' ' | 开票人 |
| 4 | fpayee | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 5 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 6 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 7 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbuyeraccount | 购方银行帐号 | varchar | 100 |  | √ | ' ' | 购方银行帐号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsaleraddressphone | 销方地址电话 | varchar | 200 |  | √ | ' ' | 销方地址电话 |
| 13 | fsaleraccount | 销方银行帐号 | varchar | 200 |  | √ | ' ' | 销方银行帐号 |
| 14 | fmachineno | 机器编号 | varchar | 100 |  | √ | ' ' | 机器编号 |
| 15 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 16 | fsgfp | 收购发票标志 | varchar | 30 |  | √ | ' ' | 收购发票标志,枚举: 0 :其他增值税普通发票 1 :农产品销售发票 2 :农产品收购发票 |
| 17 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 18 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 19 | freviewer | 复核人 | varchar | 100 |  | √ | ' ' | 复核人 |
| 20 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 21 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fsalertaxno | 销方税号 | varchar | 100 |  | √ | ' ' | 销方税号 |
| 24 | fbuyertaxno | 购方税号 | varchar | 100 |  | √ | ' ' | 购方税号 |
| 25 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 26 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fprojectid | 项目名称 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 29 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | foriginalinvoiceno | 原发票号码 | varchar | 100 |  | √ | ' ' | 原发票号码 |
| 32 | fpdfurl | pdf下载地址 | varchar | 600 |  | √ | ' ' | pdf下载地址 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 35 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 1 :增值税电子普通发票 3 :增值税纸质普通发票 4 :增值税专用发票 |
| 36 | finvoicetype | 红蓝发票 | varchar | 30 |  | √ | ' ' | 红蓝发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 37 | foriginalinvoicecode | 原发票代码 | varchar | 100 |  | √ | ' ' | 原发票代码 |
| 38 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 39 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 40 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 41 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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

---

## 单据体-子表 t_tdm_invoiceoutput_item

- **表名称：** 单据体-子表
- **表名：** t_tdm_invoiceoutput_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fzerotaxrateflag | 零税率标识 | varchar | 30 |  | √ | ' ' | 零税率标识,枚举: 0 :非零税率 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | fdiscounttype | 折扣类型 | varchar | 30 |  | √ | ' ' | 折扣类型,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 5 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 6 | fhsbz | 含税标志 | varchar | 30 |  | √ | ' ' | 含税标志,枚举: 0 :不含税 1 :含税 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 9 | fpreferentialpolicy | 优惠政策标识 | varchar | 30 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 10 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fgoodscode | 商品编码 | varchar | 100 |  | √ | ' ' | 商品编码 |
| 12 | fgoodsname | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 13 | fspecmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 14 | fversionno | 商品编码版本号 | varchar | 100 |  | √ | ' ' | 商品编码版本号 |
| 15 | fvatexception | 增值税特殊管理 | varchar | 100 |  | √ | ' ' | 增值税特殊管理 |
| 16 | fzxbm | 自行编码 | varchar | 100 |  | √ | ' ' | 自行编码 |
| 17 | fcount | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | funit | 单位 | varchar | 100 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxrate |  | ftaxrate |
| 2 | t_tdm_invoiceoutput_item_pkey |  | fentryid |
| 3 | idx_t_tdm_invoiceoutput_item |  | fid |
