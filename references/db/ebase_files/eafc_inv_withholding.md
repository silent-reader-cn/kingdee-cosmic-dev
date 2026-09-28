# 代扣代缴税收凭证-eafc_inv_withholding

## 单据体-子表 t_eafc_inv_withhold_item

- **表名称：** 单据体-子表
- **表名：** t_eafc_inv_withhold_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fitem_name | 品目名称 | varchar | 50 |  | √ | ' ' | 品目名称 |
| 3 | fstart_date | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 4 | finput_date | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 实缴金额 | numeric | 23 | 10 |  | null | 实缴金额 |
| 7 | ftax_type | 税种 | int8 | 64 |  |  | null | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 9 | forigin_code | 原凭证号 | varchar | 50 |  | √ | ' ' | 原凭证号 |
| 10 | fend_date | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_withhold_item |  | fentryid |
| 2 | idx_eafc_inv_withhold_item_fk |  | fid |

---

## 代扣代缴税收凭证-主表 t_eafc_inv_withholding

- **表名称：** 代扣代缴税收凭证-主表
- **表名：** t_eafc_inv_withholding

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ftax_no | 纳税人识别号 | varchar | 30 |  | √ | ' ' | 纳税人识别号 |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | ftextfield | 填票人 | varchar | 50 |  | √ | ' ' | 填票人 |
| 6 | ftax_code | 凭证编号 | varchar | 50 |  | √ | ' ' | 凭证编号 |
| 7 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 12 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftotal_amount | 金额合计 | numeric | 23 | 10 |  | null | 金额合计 |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdatefield | 填发日期 | timestamp | 0 |  |  | null | 填发日期 |
| 20 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 22 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 23 | fperiod | 扣款属期 | timestamp | 0 |  |  | null | 扣款属期 |
| 24 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 26 | ftax_office | 税务机关 | varchar | 100 |  | √ | ' ' | 税务机关 |
| 27 | ftaxpayer_no | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_withholding |  | fid |
