# 机动车票-eafc_inv_motor

## 机动车票-主表 t_eafc_inv_motor

- **表名称：** 机动车票-主表
- **表名：** t_eafc_inv_motor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fdrawer | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fsaler_address | 卖方地址 | varchar | 150 |  | √ | ' ' | 卖方地址 |
| 5 | fsaler_account | 卖方银行账号 | varchar | 150 |  | √ | ' ' | 卖方银行账号 |
| 6 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 7 | fimport_certificate | 进口证明书号 | varchar | 32 |  | √ | ' ' | 进口证明书号 |
| 8 | fcommodity_inspection_num | 商检单号 | varchar | 32 |  | √ | ' ' | 商检单号 |
| 9 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 10 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 2 |  | null | 可抵扣税额 |
| 13 | flimite_people | 限乘人数 | int8 | 64 |  |  | null | 限乘人数 |
| 14 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 15 | fengine_num | 发动机编号 | varchar | 60 |  | √ | ' ' | 发动机编号 |
| 16 | fcheck_code | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 17 | fnot_deductible_type | 不抵扣原因 | varchar | 50 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 18 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fsaler_phone | 卖方电话号码 | varchar | 30 |  | √ | ' ' | 卖方电话号码 |
| 22 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 24 | fdeduction_purpose | 抵扣用途 | varchar | 50 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fauthenticate_flag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预抵扣 |
| 27 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 28 | fvehicle_identification_code | 车辆识别代码 | varchar | 32 |  | √ | ' ' | 车辆识别代码 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fproxy_saler_tax_no | 代开单位税号 | varchar | 20 |  | √ | ' ' | 代开单位税号 |
| 31 | fsaler_tax_no | 卖方税号 | varchar | 20 |  | √ | ' ' | 卖方税号 |
| 32 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 33 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 34 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 35 | fbrand_model | 厂牌型号 | varchar | 80 |  | √ | ' ' | 厂牌型号 |
| 36 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fover_tax_code | 完税凭证号码 | varchar | 20 |  | √ | ' ' | 完税凭证号码 |
| 38 | ftax_authority_code | 税务机关代码 | varchar | 50 |  | √ | ' ' | 税务机关代码 |
| 39 | fbuyer_name | 买方名称 | varchar | 120 |  | √ | ' ' | 买方名称 |
| 40 | fproxy_saler_name | 代开单位名称 | varchar | 120 |  | √ | ' ' | 代开单位名称 |
| 41 | finvoice_amount | 不含税金额 | numeric | 23 | 2 |  | null | 不含税金额 |
| 42 | finvalid_date | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 43 | fmachine_no | 机器编号 | varchar | 30 |  | √ | ' ' | 机器编号 |
| 44 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 45 | fcertificate_num | 合格证号 | varchar | 32 |  | √ | ' ' | 合格证号 |
| 46 | fmanage_status | 管理状态 | varchar | 50 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 47 | finvoice_status | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 48 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fproxy_mark | 代开标识 | varchar | 50 |  | √ | ' ' | 代开标识,枚举: 0 :否 1 :是 |
| 51 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 52 | fbuyer_cardno | 买方身份证号/组织机构代码 | varchar | 100 |  | √ | ' ' | 买方身份证号/组织机构代码 |
| 53 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 55 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 56 | ftax_authority_name | 税务机关名称 | varchar | 50 |  | √ | ' ' | 税务机关名称 |
| 57 | ftax_rate | 税率 | numeric | 23 | 6 |  | null | 税率 |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 60 | ftotal_tax_amount | 合计税额 | numeric | 23 | 2 |  | null | 合计税额 |
| 61 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 62 | fvehicle_type | 车辆类型 | varchar | 30 |  | √ | ' ' | 车辆类型 |
| 63 | ftotal_ton | 吨位 | varchar | 50 |  | √ | ' ' | 吨位 |
| 64 | fbuyer_tax_no | 买方税号 | varchar | 20 |  | √ | ' ' | 买方税号 |
| 65 | fsaler_bank_name | 销方开户银行 | varchar | 50 |  | √ | ' ' | 销方开户银行 |
| 66 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 67 | fsaler_name | 卖方名称 | varchar | 120 |  | √ | ' ' | 卖方名称 |
| 68 | fproducing_area | 产地 | varchar | 30 |  | √ | ' ' | 产地 |
| 69 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 70 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 71 | foriginal_invoice_code | 原发票代码 | varchar | 32 |  | √ | ' ' | 原发票代码 |
| 72 | foriginal_invoice_no | 原发票号码 | varchar | 32 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_motor |  | fid |
