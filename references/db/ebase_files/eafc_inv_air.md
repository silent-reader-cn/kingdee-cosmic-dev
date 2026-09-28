# 飞机票-eafc_inv_air

## 单据体-子表 t_eafc_inv_air_item

- **表名称：** 单据体-子表
- **表名：** t_eafc_inv_air_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fentry_date | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 3 | fentry_carrier | 承运人 | varchar | 32 |  | √ | ' ' | 承运人 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentry_destination | 目的地 | varchar | 32 |  | √ | ' ' | 目的地 |
| 6 | fentry_time | 乘机时间 | varchar | 10 |  | √ | ' ' | 乘机时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 8 | fentry_flight_num | 航班号 | varchar | 32 |  | √ | ' ' | 航班号 |
| 9 | fentry_departure | 出发地 | varchar | 32 |  | √ | ' ' | 出发地 |
| 10 | fentry_seat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_inv_air_item_fk |  | fid |
| 2 | pk_eafc_inv_air_item |  | fentryid |

---

## 飞机票-主表 t_eafc_inv_air

- **表名称：** 飞机票-主表
- **表名：** t_eafc_inv_air

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | finsurance_premium | 保险费 | numeric | 23 | 2 |  | null | 保险费 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | finternational_flag | 国内国际标志 | varchar | 50 |  | √ | ' ' | 国内国际标志,枚举: 1 :国内 2 :国际 |
| 5 | ffilling_unit | 填开单位 | varchar | 100 |  | √ | ' ' | 填开单位 |
| 6 | fauthenticate_time | 抵扣时间 | timestamp | 0 |  |  | null | 抵扣时间 |
| 7 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 8 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 2 |  | null | 可抵扣税额 |
| 11 | fcarrier | 承运人 | varchar | 32 |  | √ | ' ' | 承运人 |
| 12 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 15 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | ffuel_surcharge | 燃油附加费 | numeric | 23 | 2 |  | null | 燃油附加费 |
| 19 | fissue_date | 机票填开日期 | timestamp | 0 |  |  | null | 机票填开日期 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | feticket_no | 电子客票号码 | varchar | 32 |  | √ | ' ' | 电子客票号码 |
| 22 | fcustomer_name | 顾客姓名 | varchar | 32 |  | √ | ' ' | 顾客姓名 |
| 23 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 24 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 25 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fseat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |
| 27 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | ftransport_deduction | 旅客运输抵扣 | varchar | 50 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 29 | finvoice_amount | 票价 | numeric | 23 | 2 |  | null | 票价 |
| 30 | fcustomer_id_no | 身份证号 | varchar | 25 |  | √ | ' ' | 身份证号 |
| 31 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 32 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fagent_code | 销售单位代码 | varchar | 32 |  | √ | ' ' | 销售单位代码 |
| 35 | fflight_num | 航班号 | varchar | 32 |  | √ | ' ' | 航班号 |
| 36 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 38 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 39 | fprint_num | 印刷序列号 | varchar | 32 |  | √ | ' ' | 印刷序列号 |
| 40 | ftax_rate | 税率 | numeric | 23 | 4 |  | null | 税率 |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | finvoice_date | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 43 | ftotal_tax_amount | 税额 | numeric | 23 | 2 |  | null | 税额 |
| 44 | fdestination | 目的地 | varchar | 32 |  | √ | ' ' | 目的地 |
| 45 | fother_amount | 其他税费 | numeric | 23 | 2 |  | null | 其他税费 |
| 46 | fairport_construction_fee | 机场建设费 | numeric | 23 | 2 |  | null | 机场建设费 |
| 47 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fair_time | 乘机时间 | varchar | 10 |  | √ | ' ' | 乘机时间 |
| 49 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 50 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 51 | fendorsement | 签注 | varchar | 64 |  | √ | ' ' | 签注 |
| 52 | fplace_of_departure | 出发地 | varchar | 32 |  | √ | ' ' | 出发地 |
| 53 | fair_num | 机票编号 | varchar | 32 |  | √ | ' ' | 机票编号 |
| 54 | fticket_changes | 改签标识 | varchar | 50 |  | √ | ' ' | 改签标识,枚举: 1 :正常 2 :改签 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_air |  | fid |
