# 增值税普通发票-rim_inv_ordinary

## 增值税普通发票-主表 t_rim_inv_ordinary

- **表名称：** 增值税普通发票-主表
- **表名：** t_rim_inv_ordinary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 4 | fsaler_account | 销方帐号 | varchar | 150 |  | √ | ' ' | 销方帐号 |
| 5 | fauthenticate_time | 抵扣时间 | timestamp | 0 |  |  | null | 抵扣时间 |
| 6 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 7 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 8 | fmain_goods_name | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 11 | fcheck_code | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 12 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 13 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 14 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 16 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fsaler_address_phone | 销方地址电话 | varchar | 150 |  | √ | ' ' | 销方地址电话 |
| 20 | fproxy_saler_tax_no | 代开单位税号 | varchar | 30 |  | √ | ' ' | 代开单位税号 |
| 21 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 22 | fdelete | 可用状态 | varchar | 4 |  |  | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 23 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 24 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 27 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 28 | ftransport_deduction | 旅客运输抵扣 | varchar | 2 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 29 | finvoice_amount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 30 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 31 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 32 | fmachine_no | 机器编号 | varchar | 50 |  | √ | ' ' | 机器编号 |
| 33 | fpurchase_ticket | 农产品发票类型 | varchar | 2 |  | √ | '0' | 农产品发票类型,枚举: 0 :空 1 :收购票 2 :销售票 |
| 34 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 35 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fproxy_mark | 代开标识 | varchar | 4 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 38 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 39 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 40 | fbuyer_account | 购方银行帐号 | varchar | 150 |  | √ | ' ' | 购方银行帐号 |
| 41 | favail_deduct | 可扣除额 | numeric | 23 | 10 | √ | 0 | 可扣除额 |
| 42 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 43 | ftotal_deduct | 累计扣除额 | numeric | 23 | 10 | √ | 0 | 累计扣除额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 46 | fsplit | 分包标识 | varchar | 50 |  | √ | ' ' | 分包标识,枚举: |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 49 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 50 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 51 | fbuyer_address_phone | 购方地址电话 | varchar | 150 |  | √ | ' ' | 购方地址电话 |
| 52 | fcurrent_deduct | 本次扣除额 | numeric | 23 | 10 | √ | 0 | 本次扣除额 |
| 53 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 54 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 56 | ftype | 0-蓝字发票；1-红字发票 | varchar | 2 |  | √ | ' ' | 0-蓝字发票；1-红字发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 57 | fremain_deduct | 剩余扣除额 | numeric | 23 | 10 | √ | 0 | 剩余扣除额 |
| 58 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 59 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 60 | foriginal_invoice_code | 原发票代码 | varchar | 32 |  | √ | ' ' | 原发票代码 |
| 61 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_ordinary_no |  | finvoice_code,finvoice_no |
| 2 | idx_rim_inv_ordinary_taxorg |  | ftax_org,ftax_period |
| 3 | pk_rim_inv_ordinary |  | fid |
| 4 | idx_rim_inv_ordinary |  | fbillno |
| 5 | idx_rim_inv_ordinary_serial |  | fserial_no |

---

## 单据体-子表 t_rim_inv_ordinary_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_ordinary_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscount_type | 折扣行 | varchar | 50 |  | √ | ' ' | 折扣行,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 3 | fzerotaxrate_flag | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | fversion_no | 商品编码版本号 | varchar | 16 |  | √ | ' ' | 商品编码版本号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgoods_code | 商品编码 | varchar | 30 |  | √ | ' ' | 商品编码 |
| 8 | fgoods_name | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 9 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 10 | fwriteoffqty | 已核销数量 | numeric | 23 | 10 | √ | 0 | 已核销数量 |
| 11 | fdetail_amount | 明细金额 | numeric | 23 | 10 | √ | 0.0000000000 | 明细金额 |
| 12 | fpreferential_policy | 优惠政策标识 | varchar | 50 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 13 | funit_price | 单价 | numeric | 30 | 18 | √ | 0 | 单价 |
| 14 | fspec_model | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 15 | fvat_exception | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理 |
| 16 | funwriteoffqty | 未核销数量 | numeric | 23 | 10 | √ | 0 | 未核销数量 |
| 17 | ftax_amount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_ordinary_item_code |  | fgoods_code |
| 2 | idx_rim_inv_ordinary_item_fk |  | fid |
| 3 | pk_rim_inv_ordinary_item |  | fentryid |
