# 飞机票-rim_inv_air

## 飞机票-主表 t_rim_inv_air

- **表名称：** 飞机票-主表
- **表名：** t_rim_inv_air

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finsurance_premium | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | finternational_flag | 国内国际标志 | varchar | 2 |  | √ | ' ' | 国内国际标志,枚举: 1 :国内 2 :国际 |
| 5 | ffilling_unit | 填开单位 | varchar | 100 |  | √ | ' ' | 填开单位 |
| 6 | fauthenticate_time | 抵扣时间 | timestamp | 0 |  |  | null | 抵扣时间 |
| 7 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 8 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 11 | fcarrier | 承运人 | varchar | 32 |  | √ | ' ' | 承运人 |
| 12 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 13 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 14 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 16 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | ffuel_surcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0.0000000000 | 燃油附加费 |
| 18 | fissue_date | 机票填开日期 | timestamp | 0 |  |  | null | 机票填开日期 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | feticket_no | 电子客票号码 | varchar | 32 |  | √ | ' ' | 电子客票号码 |
| 21 | fcustomer_name | 顾客姓名 | varchar | 32 |  | √ | ' ' | 顾客姓名 |
| 22 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 23 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 24 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fseat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | ftransport_deduction | 旅客运输抵扣 | varchar | 2 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 28 | finvoice_amount | 票价 | numeric | 23 | 10 | √ | 0.0000000000 | 票价 |
| 29 | fcustomer_id_no | 身份证号 | varchar | 25 |  | √ | ' ' | 身份证号 |
| 30 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fagent_code | 销售单位代码 | varchar | 32 |  | √ | ' ' | 销售单位代码 |
| 33 | fflight_num | 航班号 | varchar | 32 |  | √ | ' ' | 航班号 |
| 34 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 35 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fprint_num | 印刷序列号 | varchar | 32 |  | √ | ' ' | 印刷序列号 |
| 37 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 38 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 39 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | finvoice_date | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 41 | ftotal_tax_amount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 42 | fdestination | 目的地 | varchar | 32 |  | √ | ' ' | 目的地 |
| 43 | fother_amount | 其他税费 | numeric | 23 | 10 | √ | 0.0000000000 | 其他税费 |
| 44 | fairport_construction_fee | 机场建设费 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费 |
| 45 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fair_time | 乘机时间 | varchar | 10 |  | √ | ' ' | 乘机时间 |
| 47 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 48 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 49 | fendorsement | 签注 | varchar | 120 |  | √ | ' ' | 签注 |
| 50 | fplace_of_departure | 出发地 | varchar | 32 |  | √ | ' ' | 出发地 |
| 51 | fair_num | 机票编号 | varchar | 32 |  | √ | ' ' | 机票编号 |
| 52 | fticket_changes | 改签标识 | varchar | 4 |  | √ | ' ' | 改签标识,枚举: 1 :正常 2 :改签 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_air |  | fserial_no |
| 2 | idx_rim_inv_air_no |  | fprint_num,feticket_no |
| 3 | idx_rim_inv_air_taxorg |  | ftax_org,ftax_period,finvoice_date |
| 4 | pk_rim_inv_air |  | fid |

---

## 单据体-子表 t_rim_inv_air_item

- **表名称：** 单据体-子表
- **表名：** t_rim_inv_air_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentry_date | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 3 | fentry_carrier | 承运人 | varchar | 32 |  | √ | ' ' | 承运人 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentry_destination | 目的地 | varchar | 32 |  | √ | ' ' | 目的地 |
| 6 | fentry_time | 乘机时间 | varchar | 10 |  | √ | ' ' | 乘机时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
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
| 1 | idx_rim_inv_air_item_fk |  | fid |
| 2 | pk_rim_inv_air_item |  | fentryid |
