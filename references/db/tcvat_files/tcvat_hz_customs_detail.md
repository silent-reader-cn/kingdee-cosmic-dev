# 总机构海关缴款书明细单据-tcvat_hz_customs_detail

## 总机构海关缴款书明细单据-主表 t_tcvat_hz_customs_detail

- **表名称：** 总机构海关缴款书明细单据-主表
- **表名：** t_tcvat_hz_customs_detail

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
| 9 | fsecond_dept_name | 缴款单位二名称 | varchar | 80 |  | √ | ' ' | 缴款单位二名称 |
| 10 | ftype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 3 :被汇总 2 :汇总 |
| 11 | funit_price | 完税价格 | numeric | 23 | 10 |  | null | 完税价格 |
| 12 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 13 | fdeductiontype | 抵扣类型 | varchar | 50 |  | √ | ' ' | 抵扣类型,枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 21 :海关进口增值税专用缴款书 |
| 14 | fsuborg | 分支机构组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_hz_custom_serialno |  | ftaxaccountserialno |
| 2 | pk_tcvat_hz_customs_detail |  | fid |
