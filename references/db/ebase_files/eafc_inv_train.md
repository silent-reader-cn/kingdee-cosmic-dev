# 火车票-eafc_inv_train

## 火车票-主表 t_eafc_inv_train

- **表名称：** 火车票-主表
- **表名：** t_eafc_inv_train

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ftransport_deduction | 旅客运输抵扣 | varchar | 50 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | ftrain_num | 车次 | varchar | 16 |  | √ | ' ' | 车次 |
| 5 | fcustomer_id_no | 身份证号 | varchar | 25 |  | √ | ' ' | 身份证号 |
| 6 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fauthenticate_time | 抵扣时间 | timestamp | 0 |  |  | null | 抵扣时间 |
| 8 | ftrain_time | 乘车时间 | varchar | 10 |  | √ | ' ' | 乘车时间 |
| 9 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 10 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 2 |  | null | 可抵扣税额 |
| 13 | fsequence_no | 票号 | varchar | 32 |  | √ | ' ' | 票号 |
| 14 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstation_get_on | 上车站点 | varchar | 16 |  | √ | ' ' | 上车站点 |
| 17 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 18 | fpassenger_name | 乘客姓名 | varchar | 30 |  | √ | ' ' | 乘客姓名 |
| 19 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 22 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | ftax_rate | 税率 | numeric | 23 | 4 |  | null | 税率 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 29 | ftotal_tax_amount | 税额 | numeric | 23 | 2 |  | null | 税额 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | ftravel_date | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 32 | fstation_get_off | 下车站点 | varchar | 16 |  | √ | ' ' | 下车站点 |
| 33 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 35 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 36 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 37 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 38 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 39 | fseat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |
| 40 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_train |  | fid |
