# 全电发票-rim_inv_electric

## 全电发票-主表 t_rim_inv_electric

- **表名称：** 全电发票-主表
- **表名：** t_rim_inv_electric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 5 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 6 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 7 | fmain_goods_name | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | feffective_tax_amount | 有效税额 | numeric | 23 | 10 | √ | 0 | 有效税额 |
| 10 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 11 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 12 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 13 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 14 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 16 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 17 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fproxy_saler_tax_no | 代开单位税号 | varchar | 30 |  | √ | ' ' | 代开单位税号 |
| 21 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 22 | fdelete | 可用状态 | varchar | 4 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 23 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 24 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 27 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 28 | finvoice_amount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 29 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 30 | fmachine_no | fmachine_no | varchar | 50 |  | √ | ' ' |  |
| 31 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 32 | fpurchase_ticket | 农产品发票类型 | varchar | 2 |  | √ | '0' | 农产品发票类型,枚举: 0 :空 1 :收购票 2 :销售票 |
| 33 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 34 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fproxy_mark | 代开标识 | varchar | 4 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 37 | freviewer | freviewer | varchar | 50 |  | √ | ' ' |  |
| 38 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 39 | favail_deduct | 可扣除额 | numeric | 23 | 10 | √ | 0 | 可扣除额 |
| 40 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 41 | ftotal_deduct | 累计扣除额 | numeric | 23 | 10 | √ | 0 | 累计扣除额 |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 44 | fsplit | fsplit | varchar | 50 |  | √ | ' ' |  |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 47 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 48 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 49 | fcurrent_deduct | 本次扣除额 | numeric | 23 | 10 | √ | 0 | 本次扣除额 |
| 50 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 51 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 53 | ftype | 0-蓝字发票；1-红字发票 | varchar | 50 |  | √ | ' ' | 0-蓝字发票；1-红字发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 54 | fremain_deduct | 剩余扣除额 | numeric | 23 | 10 | √ | 0 | 剩余扣除额 |
| 55 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 56 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 57 | foriginal_invoice_code | foriginal_invoice_code | varchar | 32 |  | √ | ' ' |  |
| 58 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_electric_serial |  | fserial_no |
| 2 | pk_rim_inv_electric |  | fid |
| 3 | idx_rim_inv_electric_no |  | finvoice_no |
| 4 | idx_rim_inv_electric_taxorg |  | ftax_org |

---

## 单据体-子表 t_rim_inv_electric_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_electric_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscount_type | 折扣行 | varchar | 50 |  | √ | ' ' | 折扣行,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 3 | fzerotaxrate_flag | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | fversion_no | 商品编码版本号 | varchar | 16 |  | √ | ' ' | 商品编码版本号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgoods_code | 商品编码 | varchar | 30 |  | √ | ' ' | 商品编码 |
| 8 | fgoods_name | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 9 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fwriteoffqty | 已核销数量 | numeric | 23 | 10 | √ | 0 | 已核销数量 |
| 11 | fdetail_amount | 明细金额 | numeric | 23 | 10 | √ | 0 | 明细金额 |
| 12 | fpreferential_policy | 优惠政策标识 | varchar | 50 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 13 | funit_price | 单价 | numeric | 30 | 18 | √ | 0 | 单价 |
| 14 | fspec_model | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 15 | fvat_exception | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理 |
| 16 | funwriteoffqty | 未核销数量 | numeric | 23 | 10 | √ | 0 | 未核销数量 |
| 17 | ftax_amount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_electric |  | fid |
| 2 | pk_t_rim_inv_electric_item |  | fentryid |
