# 全电发票-eafc_inv_electric

## 全电发票-主表 t_eafc_inv_electric

- **表名称：** 全电发票-主表
- **表名：** t_eafc_inv_electric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fdrawer | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 4 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 5 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 6 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 7 | fmain_goods_name | 主要商品名称 | varchar | 120 |  | √ | ' ' | 主要商品名称 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | feffective_tax_amount | 有效税额 | numeric | 23 | 2 |  | null | 有效税额 |
| 10 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 11 | fnot_deductible_type | 不抵扣原因 | varchar | 50 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 12 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 15 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 17 | fdeduction_purpose | 抵扣用途 | varchar | 50 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauthenticate_flag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fproxy_saler_tax_no | 代开单位税号 | varchar | 20 |  | √ | ' ' | 代开单位税号 |
| 22 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 23 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 24 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 25 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 28 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 29 | finvoice_amount | 合计金额 | numeric | 23 | 2 |  | null | 合计金额 |
| 30 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 31 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 32 | fmanage_status | 管理状态 | varchar | 50 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 33 | finvoice_status | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 34 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fproxy_mark | 代开标识 | varchar | 50 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 37 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 38 | favail_deduct | 可扣除额 | numeric | 23 | 2 |  | null | 可扣除额 |
| 39 | ftotal_deduct | 累计扣除额 | numeric | 23 | 2 |  | null | 累计扣除额 |
| 40 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 44 | ftotal_tax_amount | 合计税额 | numeric | 23 | 2 |  | null | 合计税额 |
| 45 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 46 | fcurrent_deduct | 本次扣除额 | numeric | 23 | 2 |  | null | 本次扣除额 |
| 47 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 48 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 50 | ftype | 0-蓝字发票；1-红字发票 | varchar | 50 |  | √ | ' ' | 0-蓝字发票；1-红字发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 51 | fremain_deduct | 剩余扣除额 | numeric | 23 | 2 |  | null | 剩余扣除额 |
| 52 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 53 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 54 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_electric |  | fid |

---

## 单据体-子表 t_eafc_inv_electric_item

- **表名称：** 单据体-子表
- **表名：** t_eafc_inv_electric_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fdiscount_type | 折扣行 | varchar | 50 |  | √ | ' ' | 折扣行,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 3 | fzerotaxrate_flag | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | ftax_rate | 税率 | numeric | 23 | 4 |  | null | 税率 |
| 5 | fversion_no | 商品编码版本号 | varchar | 16 |  | √ | ' ' | 商品编码版本号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgoods_code | 商品编码 | varchar | 30 |  | √ | ' ' | 商品编码 |
| 8 | fgoods_name | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 9 | fnum | 数量 | numeric | 23 | 2 |  | null | 数量 |
| 10 | fdetail_amount | 明细金额 | numeric | 23 | 2 |  | null | 明细金额 |
| 11 | fpreferential_policy | 优惠政策标识 | varchar | 50 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 12 | funit_price | 单价 | numeric | 23 | 2 |  | null | 单价 |
| 13 | fspec_model | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 14 | fvat_exception | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理 |
| 15 | ftax_amount | 税额 | numeric | 23 | 2 |  | null | 税额 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 17 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_inv_electric_item_fk |  | fid |
| 2 | pk_eafc_inv_electric_item |  | fentryid |
