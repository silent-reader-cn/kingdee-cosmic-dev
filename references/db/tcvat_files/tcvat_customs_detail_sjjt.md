# 一般纳税人计提海关进口缴款书明细单据-tcvat_customs_detail_sjjt

## 一般纳税人计提海关进口缴款书明细单据-主表 t_tcvat_customs_detail_jt

- **表名称：** 一般纳税人计提海关进口缴款书明细单据-主表
- **表名：** t_tcvat_customs_detail_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdept_name | 缴款单位一名称 | varchar | 80 |  | √ | ' ' | 缴款单位一名称 |
| 3 | fsecond_dept_name | 缴款单位二名称 | varchar | 80 |  | √ | ' ' | 缴款单位二名称 |
| 4 | fcustom_declaration_no | 缴款书号码 | varchar | 50 |  | √ | ' ' | 缴款书号码 |
| 5 | finvoice_date | 日期 | timestamp | 0 |  |  | null | 日期 |
| 6 | funit_price | 完税价格 | numeric | 23 | 10 | √ | 0 | 完税价格 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftotal_tax_amount | 税款金额合计 | numeric | 23 | 10 | √ | 0 | 税款金额合计 |
| 9 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 10 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 11 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_customs_detail_serialno |  | ftaxaccountserialno |
| 2 | pk_tcvat_customs_detail_jt |  | fid |
