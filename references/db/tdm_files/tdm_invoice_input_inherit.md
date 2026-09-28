# 增值税专用发票_继承(到票)-tdm_invoice_input_inherit

## 专业发票明细-子表 t_tdm_speinvoice_item

- **表名称：** 专业发票明细-子表
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

## 增值税专用发票_继承(到票)-分表 t_tdm_invoice_input_a

- **表名称：** 增值税专用发票_继承(到票)-分表
- **表名：** t_tdm_invoice_input_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 3 | finvoicearriveder | 到票人 | varchar | 50 |  | √ | ' ' | 到票人 |
| 4 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 5 | freceiptdate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 6 | foriginalinvoiceno | 原发票号码 | varchar | 100 |  | √ | ' ' | 原发票号码 |
| 7 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 8 | finvoicearrivedstatus | 到票状态 | varchar | 50 |  | √ | ' ' | 到票状态,枚举: 0 :未到票 1 :已到票 |
| 9 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 10 | freceipter | 签收人 | varchar | 50 |  | √ | ' ' | 签收人 |
| 11 | fcertstatus | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未认证 1 :勾选认证 2 :扫描认证 |
| 12 | fselectresult | 勾选结果 | varchar | 50 |  | √ | ' ' | 勾选结果,枚举: 0 :- 1 :抵扣 2 :不抵扣 |
| 13 | fopentype | 开票类型 | varchar | 30 |  | √ | ' ' | 开票类型,枚举: 0 :蓝字发票 1 :红字发票 |
| 14 | foriginalinvoicecode | 原发票代码 | varchar | 100 |  | √ | ' ' | 原发票代码 |
| 15 | fauthdate | 认证日期 | timestamp | 0 |  |  | null | 认证日期 |
| 16 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 17 | fsignstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: 0 :未签收 1 :已签收 |
| 18 | fselectstatus | 勾选状态 | varchar | 50 |  | √ | ' ' | 勾选状态,枚举: 1 :已勾选 0 :未勾选 |
| 19 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 20 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 21 | finvoicearriveddate | 到票日期 | timestamp | 0 |  |  | null | 到票日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_invoice_input_a_pkey |  | fid |
| 2 | idx_tdm_invoice_input_a |  | foriginalinvoicecode,foriginalinvoiceno |
| 3 | idx_tdm_invoice_input_a2 |  | fbaseinvoicetype |

---

## 增值税专用发票_继承(到票)-主表 t_tdm_invoice_input

- **表名称：** 增值税专用发票_继承(到票)-主表
- **表名：** t_tdm_invoice_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 3 | fdrawer | 开票人 | varchar | 100 |  | √ | ' ' | 开票人 |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 2 | √ | 0.00 | 价税合计 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finputstatus | finputstatus | varchar | 30 |  | √ | ' ' |  |
| 7 | fbuyeraccount | 购方银行帐号 | varchar | 100 |  | √ | ' ' | 购方银行帐号 |
| 8 | fbuyeraddressphone | 购方地址电话 | varchar | 300 |  | √ | ' ' | 购方地址电话 |
| 9 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :未认证 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsaleraddressphone | 销方地址电话 | varchar | 300 |  | √ | ' ' | 销方地址电话 |
| 12 | fsaleraccount | 销方银行帐号 | varchar | 300 |  | √ | ' ' | 销方银行帐号 |
| 13 | fmachineno | 机器编号 | varchar | 100 |  | √ | ' ' | 机器编号 |
| 14 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 15 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 16 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 17 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fsalertaxno | 销方税号 | varchar | 100 |  | √ | ' ' | 销方税号 |
| 20 | ftaxamount | 合计税额 | numeric | 23 | 2 | √ | 0.00 | 合计税额 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fusedjzjtse | fusedjzjtse | numeric | 23 | 2 | √ | 0.00 |  |
| 24 | flastrolloutuser | flastrolloutuser | int8 | 64 |  | √ | 0 |  |
| 25 | flastrollouttime | flastrollouttime | timestamp | 0 |  |  | null |  |
| 26 | fjzjtamount | 即征即退税额 | numeric | 23 | 2 | √ | 0.00 | 即征即退税额 |
| 27 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 30 | fpayee | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 31 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fscanauthenticatetime | 扫描认证时间 | timestamp | 0 |  |  | null | 扫描认证时间 |
| 34 | fselecttime | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 35 | freviewer | 复核人 | varchar | 100 |  | √ | ' ' | 复核人 |
| 36 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 37 | fmaingoodsname | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 38 | fbuyertaxno | 购方税号 | varchar | 100 |  | √ | ' ' | 购方税号 |
| 39 | fremark | 备注 | varchar | 480 |  | √ | ' ' | 备注 |
| 40 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fregisterstatus | fregisterstatus | varchar | 30 |  | √ | ' ' |  |
| 44 | fremainamount | fremainamount | numeric | 23 | 2 | √ | 0.00 |  |
| 45 | fexportamount | 出口税额 | numeric | 23 | 2 | √ | 0.00 | 出口税额 |
| 46 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 2 :电子专票 4 :纸质专票 |
| 47 | frolloutamount | frolloutamount | numeric | 23 | 2 | √ | 0.00 |  |
| 48 | finvoiceamount | 合计金额 | numeric | 23 | 2 | √ | 0.00 | 合计金额 |
| 49 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |
| 50 | fusedckse | fusedckse | numeric | 23 | 2 | √ | 0.00 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_invoice_input |  | fbillno |
| 2 | t_tdm_invoice_input_pkey |  | fid |
| 3 | idx_t_tdm_invoice_input2 |  | fselectauthenticatetime,ftaxperiod,forgid |
