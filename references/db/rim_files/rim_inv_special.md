# 增值税专用发票-rim_inv_special

## 单据体-子表 t_rim_inv_special_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_special_item

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
| 1 | idx_rim_inv_special_item_fk |  | fid |
| 2 | pk_rim_inv_special_item |  | fentryid |
| 3 | idx_rim_inv_special_item_code |  | fgoods_code |

---

## 增值税专用发票-主表 t_rim_inv_special

- **表名称：** 增值税专用发票-主表
- **表名：** t_rim_inv_special

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fsaler_account | 销方银行帐号 | varchar | 150 |  | √ | ' ' | 销方银行帐号 |
| 5 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 6 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 7 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 8 | fmain_goods_name | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 11 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 12 | fcheck_code | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 13 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 14 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 15 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 16 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 18 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 19 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 |
| 21 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsaler_address_phone | 销方地址电话 | varchar | 150 |  | √ | ' ' | 销方地址电话 |
| 24 | fproxy_saler_tax_no | 代开单位税号 | varchar | 30 |  | √ | ' ' | 代开单位税号 |
| 25 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 26 | fdelete | 可用状态 | varchar | 4 |  |  | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 27 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 28 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 31 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 32 | finvoice_amount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 33 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 34 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 35 | fmachine_no | 机器编号 | varchar | 50 |  | √ | ' ' | 机器编号 |
| 36 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 37 | fpurchase_ticket | 农产品发票类型 | varchar | 2 |  | √ | '0' | 农产品发票类型,枚举: 0 :空 1 :收购票 2 :销售票 |
| 38 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 39 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fproxy_mark | 代开标识 | varchar | 4 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 42 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 43 | fbuyer_account | 购方银行帐号 | varchar | 150 |  | √ | ' ' | 购方银行帐号 |
| 44 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 45 | favail_deduct | 可扣除额 | numeric | 23 | 10 | √ | 0 | 可扣除额 |
| 46 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 47 | ftotal_deduct | 累计扣除额 | numeric | 23 | 10 | √ | 0 | 累计扣除额 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 50 | fsplit | 分包标识 | varchar | 50 |  | √ | ' ' | 分包标识,枚举: |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 53 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 54 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 55 | fbuyer_address_phone | 购方地址电话 | varchar | 150 |  | √ | ' ' | 购方地址电话 |
| 56 | fcurrent_deduct | 本次扣除额 | numeric | 23 | 10 | √ | 0 | 本次扣除额 |
| 57 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 58 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 59 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 60 | ftype | 0-蓝字发票；1-红字发票 | varchar | 50 |  | √ | ' ' | 0-蓝字发票；1-红字发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 61 | fremain_deduct | 剩余扣除额 | numeric | 23 | 10 | √ | 0 | 剩余扣除额 |
| 62 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 63 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 64 | foriginal_invoice_code | 原发票代码 | varchar | 32 |  | √ | ' ' | 原发票代码 |
| 65 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_special |  | fid |
| 2 | idx_rim_inv_special |  | fserial_no |
| 3 | idx_rim_inv_special_no |  | finvoice_code,finvoice_no |
| 4 | idx_rim_inv_special_taxorg |  | ftax_org,ftax_period,fdeduction_purpose |
