# 海关进口增值税专用缴款书抵扣明细单据-tcvat_customs_detail_bill

## 明细分录-子表 t_tcvat_customs_det_ent

- **表名称：** 明细分录-子表
- **表名：** t_tcvat_customs_det_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizdimensionfilter | 业务维度过滤条件 | varchar | 1050 |  | √ | ' ' | 业务维度过滤条件 |
| 3 | fbizdimensionfilter_tag | 业务维度过滤条件_详情 | text | 0 |  |  | null | 业务维度过滤条件_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_customs_det_ent |  | fentryid |

---

## 海关进口增值税专用缴款书抵扣明细单据-主表 t_tcvat_customs_detail

- **表名称：** 海关进口增值税专用缴款书抵扣明细单据-主表
- **表名：** t_tcvat_customs_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustom_declaration_no | 缴款书号码 | varchar | 50 |  | √ | ' ' | 缴款书号码 |
| 3 | finvoice_date | 日期 | timestamp | 0 |  |  | null | 日期 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotal_tax_amount | 税款金额合计 | numeric | 23 | 10 | √ | 0 | 税款金额合计 |
| 6 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 7 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 8 | fdept_name | 缴款单位一名称 | varchar | 80 |  | √ | ' ' | 缴款单位一名称 |
| 9 | fdatastatus | 数据状态 | varchar | 10 |  | √ | '1' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 10 | fsecond_dept_name | 缴款单位二名称 | varchar | 80 |  | √ | ' ' | 缴款单位二名称 |
| 11 | funit_price | 完税价格 | numeric | 23 | 10 | √ | 0 | 完税价格 |
| 12 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 13 | fsbbid | 底稿主表id | int8 | 64 |  | √ | 0 | 底稿主表id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_customs_detail |  | fid |
| 2 | idx_t_tcvat_cust_serialno |  | ftaxaccountserialno |
