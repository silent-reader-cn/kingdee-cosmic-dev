# 通行费-rim_inv_toll

## 通行费-主表 t_rim_inv_toll

- **表名称：** 通行费-主表
- **表名：** t_rim_inv_toll

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fsaler_account | 卖方开户行及账号 | varchar | 150 |  | √ | ' ' | 卖方开户行及账号 |
| 5 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 6 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 7 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 8 | fmain_goods_name | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 11 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 12 | fcheck_code | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 13 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 14 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 15 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 16 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 18 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 19 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预抵扣 |
| 21 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsaler_address_phone | 卖方地址电话 | varchar | 120 |  | √ | ' ' | 卖方地址电话 |
| 24 | fproxy_saler_tax_no | 代开单位税号 | varchar | 30 |  | √ | ' ' | 代开单位税号 |
| 25 | fsaler_tax_no | 卖方税号 | varchar | 20 |  | √ | ' ' | 卖方税号 |
| 26 | fdelete | 可用状态 | varchar | 4 |  |  | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 27 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 28 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbuyer_name | 买方名称 | varchar | 120 |  | √ | ' ' | 买方名称 |
| 31 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 32 | finvoice_amount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 33 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 34 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 35 | fmachine_no | 机器编号 | varchar | 50 |  | √ | ' ' | 机器编号 |
| 36 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 37 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 38 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fproxy_mark | 代开标识 | varchar | 4 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 41 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 42 | fbuyer_account | 买方开户行及账号 | varchar | 150 |  | √ | ' ' | 买方开户行及账号 |
| 43 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 44 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 49 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 50 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 51 | fbuyer_address_phone | 买方地址电话 | varchar | 120 |  | √ | ' ' | 买方地址电话 |
| 52 | fbuyer_tax_no | 买方税号 | varchar | 20 |  | √ | ' ' | 买方税号 |
| 53 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 54 | ftype | 0-蓝字发票；1-红字发票 | varchar | 50 |  | √ | ' ' | 0-蓝字发票；1-红字发票,枚举: 0 :蓝字发票 1 :红字发票 |
| 55 | fsaler_name | 卖方名称 | varchar | 120 |  | √ | ' ' | 卖方名称 |
| 56 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 57 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 58 | foriginal_invoice_code | 原发票代码 | varchar | 32 |  | √ | ' ' | 原发票代码 |
| 59 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_toll_taxorg |  | ftax_org,ftax_period,fdeduction_purpose |
| 2 | pk_rim_inv_toll |  | fid |
| 3 | idx_rim_inv_toll |  | fserial_no |
| 4 | idx_rim_inv_toll_no |  | finvoice_code,finvoice_no |

---

## 单据体-子表 t_rim_inv_toll_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_toll_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscount_type | 折扣行 | varchar | 50 |  | √ | ' ' | 折扣行,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 3 | fstart_date | 通行起始日期 | timestamp | 0 |  |  | null | 通行起始日期 |
| 4 | fzerotaxrate_flag | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 5 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 6 | fversion_no | 商品编码版本号 | varchar | 16 |  | √ | ' ' | 商品编码版本号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fgoods_code | 商品编码 | varchar | 30 |  | √ | ' ' | 商品编码 |
| 9 | fveh_plate | 车牌号码 | varchar | 20 |  | √ | ' ' | 车牌号码 |
| 10 | fgoods_name | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 11 | fend_date | 通行结束日期 | timestamp | 0 |  |  | null | 通行结束日期 |
| 12 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 13 | fdetail_amount | 明细金额 | numeric | 23 | 10 | √ | 0.0000000000 | 明细金额 |
| 14 | fpreferential_policy | 优惠政策标识 | varchar | 50 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 15 | funit_price | 单价 | numeric | 30 | 18 | √ | 0 | 单价 |
| 16 | fspec_model | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 17 | fvat_exception | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理 |
| 18 | ftax_amount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_toll_item |  | fentryid |
| 2 | idx_rim_inv_toll_item_fk |  | fid |
