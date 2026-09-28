# 旅客运输-rim_inv_transport

## 旅客运输-主表 t_rim_inv_transport

- **表名称：** 旅客运输-主表
- **表名：** t_rim_inv_transport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransport_deduction | 旅客运输抵扣 | varchar | 2 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | finsurance_premium | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 5 | ftrain_num | 车次 | varchar | 16 |  | √ | ' ' | 车次 |
| 6 | fcustomer_id_no | 身份证号 | varchar | 25 |  | √ | ' ' | 身份证号 |
| 7 | fauthenticate_time | 抵扣时间 | timestamp | 0 |  |  | null | 抵扣时间 |
| 8 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 9 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 12 | fsequence_no | 印刷序号 | varchar | 32 |  | √ | ' ' | 印刷序号 |
| 13 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fstation_get_on | 上车站点 | varchar | 16 |  | √ | ' ' | 上车站点 |
| 16 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 17 | fpassenger_name | 乘客姓名 | varchar | 30 |  | √ | ' ' | 乘客姓名 |
| 18 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 19 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 20 | ftime | 乘车时间 | varchar | 10 |  | √ | ' ' | 乘车时间 |
| 21 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | ftotal_amount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 24 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 25 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | ftax_rate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | finvoice_date | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 29 | ftotal_tax_amount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 31 | fcurrency | 币别 | varchar | 10 |  | √ | ' ' | 币别 |
| 32 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fstation_get_off | 下车站点 | varchar | 16 |  | √ | ' ' | 下车站点 |
| 35 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 37 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 38 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 39 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 40 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 41 | fseat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_transport_no |  | finvoice_code,finvoice_no |
| 2 | idx_rim_inv_transport_taxorg |  | ftax_org,ftax_period,finvoice_date |
| 3 | idx_rim_inv_transport |  | fserial_no |
| 4 | pk_rim_inv_transport |  | fid |
