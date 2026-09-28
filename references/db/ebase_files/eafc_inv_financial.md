# 财政电子票据-eafc_inv_financial

## 明细-子表 t_eafc_inv_fin_item

- **表名称：** 明细-子表
- **表名：** t_eafc_inv_fin_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fitem_name | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 3 | fitem_remark | 项目备注 | varchar | 200 |  | √ | ' ' | 项目备注 |
| 4 | fitem_std | 标准 | numeric | 23 | 2 |  | null | 标准 |
| 5 | fitem_code | 项目编码 | varchar | 30 |  | √ | ' ' | 项目编码 |
| 6 | fitem_amount | 金额 | numeric | 23 | 2 |  | null | 金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fitem_quantity | 数量 | int8 | 64 |  |  | null | 数量 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 10 | fitem_unit | 单位 | varchar | 30 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_fin_item |  | fentryid |
| 2 | idx_eafc_inv_fin_item_fk |  | fid |

---

## 财政电子票据-主表 t_eafc_inv_financial

- **表名称：** 财政电子票据-主表
- **表名：** t_eafc_inv_financial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbiz_code | 业务流水号 | varchar | 32 |  | √ | ' ' | 业务流水号 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | finvoicing_party_code | 开票单位代码 | varchar | 30 |  | √ | ' ' | 开票单位代码 |
| 5 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 6 | finvoice_name | 电子票据名称 | varchar | 100 |  | √ | ' ' | 电子票据名称 |
| 7 | finvoice_time | 开票时间 | timestamp | 0 |  |  | null | 开票时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finvoicing_party_name | 开票单位名称 | varchar | 100 |  | √ | ' ' | 开票单位名称 |
| 12 | fcheck_code | 校验码 | varchar | 10 |  | √ | ' ' | 校验码 |
| 13 | fpayer_party_code | 交款人代码 | varchar | 30 |  | √ | ' ' | 交款人代码 |
| 14 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 15 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 18 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 19 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | ftotal_amount | 总金额 | numeric | 23 | 2 |  | null | 总金额 |
| 22 | fhandling_person | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 26 | finvoice_code | 电子票据代码 | varchar | 32 |  | √ | ' ' | 电子票据代码 |
| 27 | frelated_invoice_code | 红票票据代码 | varchar | 12 |  | √ | ' ' | 红票票据代码 |
| 28 | fpayer_party_name | 交款人名称 | varchar | 200 |  | √ | ' ' | 交款人名称 |
| 29 | finvoice_no | 电子票据号码 | varchar | 32 |  | √ | ' ' | 电子票据号码 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fpay_mode | 交款方式 | varchar | 50 |  | √ | ' ' | 交款方式,枚举: |
| 32 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 34 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 35 | fpayer_party_type | 交款人类型 | varchar | 50 |  | √ | ' ' | 交款人类型,枚举: |
| 36 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 37 | fchecker | 复核人 | varchar | 20 |  | √ | ' ' | 复核人 |
| 38 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 39 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 40 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 41 | frelated_invoice_no | 红票票据号码 | varchar | 10 |  | √ | ' ' | 红票票据号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_financial |  | fid |

---

## 辅助明细-子表 t_eafc_inv_fin_itema

- **表名称：** 辅助明细-子表
- **表名：** t_eafc_inv_fin_itema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | faux_item_name | 收费明细项目名称 | varchar | 100 |  | √ | ' ' | 收费明细项目名称 |
| 3 | faux_item_related_name | 对应项目名称 | varchar | 100 |  | √ | ' ' | 对应项目名称 |
| 4 | faux_item_unit | 收费明细项目单位 | varchar | 30 |  | √ | ' ' | 收费明细项目单位 |
| 5 | faux_item_amount | 收费明细项目金额 | numeric | 23 | 2 |  | null | 收费明细项目金额 |
| 6 | faux_item_related_code | 对应项目编码 | varchar | 30 |  | √ | ' ' | 对应项目编码 |
| 7 | faux_item_std | 收费明细项目标准 | numeric | 23 | 2 |  | null | 收费明细项目标准 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | faux_item_code | 收费明细项目编码 | varchar | 30 |  | √ | ' ' | 收费明细项目编码 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | faux_item_remark | 收费明细项目备注 | varchar | 200 |  | √ | ' ' | 收费明细项目备注 |
| 12 | faux_item_quantity | 收费明细项目数量 | int8 | 64 |  |  | null | 收费明细项目数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_fin_itema |  | fentryid |
| 2 | idx_eafc_inv_fin_itema_fk |  | fid |
