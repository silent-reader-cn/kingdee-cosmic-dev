# 增值税普通发票-tdm_input_plain_invoice

## 发票明细-子表 t_tdm_speinvoice_item

- **表名称：** 发票明细-子表
- **表名：** t_tdm_speinvoice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fzerotaxrateflag | 零税率标识 | varchar | 30 |  | √ | ' ' | 零税率标识,枚举: 0 :非零税率 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | fdiscounttype | 折扣类型 | varchar | 30 |  | √ | ' ' | 折扣类型,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailamount | 明细金额(不含税) | numeric | 23 | 10 | √ | 0.0000000000 | 明细金额(不含税) |
| 8 | fpreferentialpolicy | 优惠政策标识 | varchar | 30 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 9 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fgoodscode | 商品编码 | varchar | 100 |  | √ | ' ' | 商品编码 |
| 11 | fgoodsname | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 12 | fspecmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 13 | fversionno | 商品编码版本号 | varchar | 100 |  | √ | ' ' | 商品编码版本号 |
| 14 | fvatexception | 增值税特殊管理 | varchar | 100 |  | √ | ' ' | 增值税特殊管理 |
| 15 | fcount | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | funit | 单位 | varchar | 100 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_speinvoice_item_pkey |  | fentryid |
| 2 | idx_t_tdm_speinvoice_item |  | fid |
| 3 | idx_t_tdm_speinvoice_item2 |  | fgoodscode |

---

## 增值税普通发票-主表 t_tdm_input_plain_invoice

- **表名称：** 增值税普通发票-主表
- **表名：** t_tdm_input_plain_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 3 | fdrawer | 开票人 | varchar | 60 |  | √ | ' ' | 开票人 |
| 4 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 7 | fbuyeraccount | 购方银行帐号 | varchar | 300 |  | √ | ' ' | 购方银行帐号 |
| 8 | fbuyeraddressphone | 购方地址电话 | varchar | 300 |  | √ | ' ' | 购方地址电话 |
| 9 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsaleraddressphone | 销方地址电话 | varchar | 300 |  | √ | ' ' | 销方地址电话 |
| 12 | fsaleraccount | 销方银行帐号 | varchar | 300 |  | √ | ' ' | 销方银行帐号 |
| 13 | fmachineno | 机器编号 | varchar | 100 |  | √ | ' ' | 机器编号 |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 15 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 16 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 17 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fsalertaxno | 销方税号 | varchar | 40 |  | √ | ' ' | 销方税号 |
| 20 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 21 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | foriginalinvoiceno | 原发票号码 | varchar | 16 |  | √ | ' ' | 原发票号码 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 26 | foriginalinvoicecode | 原发票代码 | varchar | 24 |  | √ | ' ' | 原发票代码 |
| 27 | fjzjtamount | 即征即退税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退税额 |
| 28 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 29 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fauthenticatedate | 认证日期 | timestamp | 0 |  |  | null | 认证日期 |
| 32 | faccountsperiod | 记账期间 | varchar | 50 |  | √ | ' ' | 记账期间 |
| 33 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 34 | fpayee | 收款人 | varchar | 60 |  | √ | ' ' | 收款人 |
| 35 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 36 | faccountssign | 记账标识 | varchar | 30 |  | √ | ' ' | 记账标识,枚举: 是 :是 否 :否 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fopentype | 开票类型 | varchar | 30 |  | √ | ' ' | 开票类型,枚举: 0 :蓝字发票 1 :红字发票 |
| 39 | freviewer | 复核人 | varchar | 60 |  | √ | ' ' | 复核人 |
| 40 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 41 | fmaingoodsname | 主要商品名称 | varchar | 400 |  | √ | ' ' | 主要商品名称 |
| 42 | fbuyertaxno | 购方税号 | varchar | 40 |  | √ | ' ' | 购方税号 |
| 43 | fremark | 备注 | varchar | 480 |  | √ | ' ' | 备注 |
| 44 | ftaxperiod | 所属税期 | varchar | 20 |  | √ | ' ' | 所属税期 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fexportamount | 出口税额 | numeric | 23 | 10 | √ | 0.0000000000 | 出口税额 |
| 48 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 1 :电子普票 3 :纸质普票 5 :普通卷票 |
| 49 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 50 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_input_plain_invoice_pkey |  | fid |
| 2 | idx_tdm_input_plain_invoice |  | forgid,ftaxperiod |
