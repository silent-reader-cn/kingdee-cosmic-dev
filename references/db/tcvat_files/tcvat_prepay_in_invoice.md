# 预缴项目进项发票-tcvat_prepay_in_invoice

## 预缴项目进项发票-主表 t_rim_invoice

- **表名称：** 预缴项目进项发票-主表
- **表名：** t_rim_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreset_deduction_purpose | fpreset_deduction_purpose | varchar | 2 |  | √ | ' ' |  |
| 3 | ftenant_no | ftenant_no | varchar | 30 |  | √ | ' ' |  |
| 4 | fcancel_select_type | fcancel_select_type | varchar | 2 |  | √ | ' ' |  |
| 5 | finternational_flag | finternational_flag | varchar | 2 |  | √ | ' ' |  |
| 6 | fcheck_result | fcheck_result | varchar | 50 |  | √ | ' ' |  |
| 7 | fauthenticate_time | fauthenticate_time | timestamp | 0 |  |  | null |  |
| 8 | ftax_period | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 9 | fdeduction_flag | fdeduction_flag | varchar | 50 |  | √ | ' ' |  |
| 10 | fmain_goods_name | fmain_goods_name | varchar | 200 |  | √ | ' ' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | feffective_tax_amount | feffective_tax_amount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fcompany_seal | fcompany_seal | varchar | 2 |  | √ | ' ' |  |
| 14 | fselect_time | fselect_time | timestamp | 0 |  |  | null |  |
| 15 | fnot_deductible_type | fnot_deductible_type | varchar | 2 |  | √ | ' ' |  |
| 16 | fresource | fresource | varchar | 50 |  | √ | ' ' |  |
| 17 | freal_transferdate | freal_transferdate | timestamp | 0 |  |  | null |  |
| 18 | fexpense_amount | fexpense_amount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fbillno | fbillno | varchar | 36 |  | √ | ' ' |  |
| 20 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 22 | fexpense_time | fexpense_time | timestamp | 0 |  |  | null |  |
| 23 | fdeduction_purpose | fdeduction_purpose | varchar | 50 |  | √ | ' ' |  |
| 24 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 25 | fauthenticate_flag | fauthenticate_flag | varchar | 50 |  | √ | ' ' |  |
| 26 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 27 | fcheck_times | fcheck_times | int4 | 32 |  | √ | 0 |  |
| 28 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 29 | fcheck_time | fcheck_time | timestamp | 0 |  |  | null |  |
| 30 | frollout_amount | frollout_amount | numeric | 23 | 10 | √ | 0 |  |
| 31 | fsaler_tax_no | 销方税号 | varchar | 30 |  | √ | ' ' | 销方税号 |
| 32 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 33 | fexpense_status | fexpense_status | varchar | 50 |  | √ | ' ' |  |
| 34 | fsource_area | fsource_area | varchar | 150 |  | √ | ' ' |  |
| 35 | foriginal_time | foriginal_time | timestamp | 0 |  |  | null |  |
| 36 | fisvoucher | fisvoucher | varchar | 2 |  | √ | ' ' |  |
| 37 | fcollect_type | fcollect_type | varchar | 2 |  | √ | ' ' |  |
| 38 | fproject | 项目 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |
| 39 | fsalelist_complete | fsalelist_complete | varchar | 10 |  | √ | ' ' |  |
| 40 | fis_revise | fis_revise | varchar | 50 |  | √ | ' ' |  |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | fbuyer_name | fbuyer_name | varchar | 150 |  | √ | ' ' |  |
| 43 | ftransport_deduction | ftransport_deduction | varchar | 2 |  | √ | ' ' |  |
| 44 | finvoice_amount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 45 | ftag | 发票标注 | varchar | 50 |  | √ | ' ' | 发票标注 |
| 46 | freceiver | freceiver | int8 | 64 |  | √ | 0 |  |
| 47 | faccount_time | faccount_time | timestamp | 0 |  |  | null |  |
| 48 | fvouch_no | fvouch_no | varchar | 500 |  | √ | ' ' |  |
| 49 | fmanage_status | fmanage_status | varchar | 50 |  | √ | ' ' |  |
| 50 | finvoice_status | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 7 :部分红冲 8 :全额红冲 6 :红字发票待确认 |
| 51 | fexpense_no | fexpense_no | varchar | 500 |  | √ | ' ' |  |
| 52 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 53 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 54 | fproxy_mark | fproxy_mark | varchar | 4 |  | √ | '0' |  |
| 55 | fsalelist_sumpage | fsalelist_sumpage | int4 | 32 |  | √ | 0 |  |
| 56 | faccount_date | faccount_date | timestamp | 0 |  |  | null |  |
| 57 | finvoice_info | finvoice_info | varchar | 50 |  | √ | ' ' |  |
| 58 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 59 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 60 | faws_serial_no | faws_serial_no | varchar | 36 |  | √ | ' ' |  |
| 61 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 62 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 63 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 64 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 65 | fbuyer_tax_no | fbuyer_tax_no | varchar | 30 |  | √ | ' ' |  |
| 66 | ftax_org | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 67 | fsaler_name | 销方名称 | varchar | 150 |  | √ | ' ' | 销方名称 |
| 68 | fcheck_status | fcheck_status | varchar | 50 |  | √ | ' ' |  |
| 69 | fcontinuous_no | fcontinuous_no | varchar | 2 |  | √ | ' ' |  |
| 70 | faudit_result | faudit_result | varchar | 2 |  | √ | '0' |  |
| 71 | foriginal_state | foriginal_state | varchar | 50 |  | √ | ' ' |  |
| 72 | fdest_area | fdest_area | varchar | 150 |  | √ | ' ' |  |
| 73 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 74 | frollout_remark | frollout_remark | varchar | 300 |  | √ | ' ' |  |
| 75 | faccount_tax_amount | faccount_tax_amount | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_code |  | finvoice_code,finvoice_no |
| 2 | idx_rim_invoice_org |  | forg_id |
| 3 | idx_rim_invoice_create |  | fcreatetime |
| 4 | idx_rim_invoice_type |  | finvoice_type |
| 5 | idx_rim_invoice_buyer |  | fbuyer_tax_no |
| 6 | pk_rim_invoice |  | fid |
| 7 | idx_rim_invoice |  | fserial_no |
| 8 | idx_rim_invoice_taxorg |  | ftax_org,fselect_time |
