# 海关缴款书-rim_inv_custom

## 单据体-子表 t_rim_inv_custom_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_custom_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | forder_number | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 4 | ftaxno_info | 税号信息 | varchar | 30 |  | √ | ' ' | 税号信息 |
| 5 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 6 | funit_price | 完税价格 | numeric | 23 | 10 | √ | 0 | 完税价格 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftax_amount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fitem_source | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源 |
| 11 | fgoods_name | 货物名称 | varchar | 100 |  | √ | ' ' | 货物名称 |
| 12 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_custom_item |  | fentryid |
| 2 | idx_rim_inv_custom_item_fk |  | fid |

---

## 海关缴款书-主表 t_rim_inv_custom

- **表名称：** 海关缴款书-主表
- **表名：** t_rim_inv_custom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 4 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 5 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdelivery_no | 提运单号 | varchar | 50 |  | √ | ' ' | 提运单号 |
| 8 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 9 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 10 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 11 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 12 | fdeclare_no | 报关单编号 | varchar | 50 |  | √ | ' ' | 报关单编号 |
| 13 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 14 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmode_trade | 贸易方式 | varchar | 50 |  | √ | ' ' | 贸易方式 |
| 16 | fcode_collection_treasury | 收款国库代码 | varchar | 50 |  | √ | ' ' | 收款国库代码 |
| 17 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 18 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :已抵扣 |
| 20 | fcustom_declaration_no | 缴款书号码 | varchar | 50 |  | √ | ' ' | 缴款书号码 |
| 21 | fpay_limit_date | 缴款期限 | varchar | 30 |  | √ | ' ' | 缴款期限 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fcustoms_name | 进口口岸名称 | varchar | 30 |  | √ | ' ' | 进口口岸名称 |
| 24 | fdeal_goods_no | 提/装货单号 | varchar | 50 |  | √ | ' ' | 提/装货单号 |
| 25 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 26 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 27 | fsecond_dept_tax_no | 缴款单位二税号 | varchar | 50 |  | √ | ' ' | 缴款单位二税号 |
| 28 | fdept_bank | 缴款单位开户银行 | varchar | 58 |  | √ | ' ' | 缴款单位开户银行 |
| 29 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdept_account | 缴款单位账号 | varchar | 50 |  | √ | ' ' | 缴款单位账号 |
| 32 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 33 | fpurchase_ticket | 农产品发票类型 | varchar | 2 |  | √ | '0' | 农产品发票类型,枚举: 0 :空 1 :收购票 2 :销售票 |
| 34 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fapply_dept_no | 申请单位编号 | varchar | 50 |  | √ | ' ' | 申请单位编号 |
| 37 | fsecond_dept_name | 缴款单位二名称 | varchar | 80 |  | √ | ' ' | 缴款单位二名称 |
| 38 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 39 | fcontract_no | 合同批文号 | varchar | 50 |  | √ | ' ' | 合同批文号 |
| 40 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 43 | ftrans_tool_no | 运输工具号 | varchar | 50 |  | √ | ' ' | 运输工具号 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | finvoice_date | 日期 | timestamp | 0 |  |  | null | 日期 |
| 46 | ftotal_tax_amount | 税款金额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 税款金额合计 |
| 47 | fdept_tax_no | 缴款单位一税号 | varchar | 36 |  | √ | ' ' | 缴款单位一税号 |
| 48 | fdata_source | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源 |
| 49 | fdept_name | 缴款单位一名称 | varchar | 80 |  | √ | ' ' | 缴款单位一名称 |
| 50 | fget_office | 收入机关 | varchar | 50 |  | √ | ' ' | 收入机关 |
| 51 | fbudget_account_code | 预算科目代码 | varchar | 50 |  | √ | ' ' | 预算科目代码 |
| 52 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 54 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 55 | fport_code | 进口口岸代码 | varchar | 30 |  | √ | ' ' | 进口口岸代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rim_inv_custom_taxorg |  | ftax_org,ftax_period |
| 2 | pk_rim_inv_custom |  | fid |
| 3 | idx_t_rim_inv_custom_no |  | fcustom_declaration_no |
| 4 | idx_t_rim_inv_custom |  | fserial_no |
