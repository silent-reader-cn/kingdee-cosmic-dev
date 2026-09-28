# 二手车-rim_inv_usedcar

## 二手车-主表 t_rim_inv_usedcar

- **表名称：** 二手车-主表
- **表名：** t_rim_inv_usedcar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarket_address | 二手市场地址 | varchar | 120 |  | √ | ' ' | 二手市场地址 |
| 3 | fdrawer | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fsaler_address | 销方地址 | varchar | 120 |  | √ | ' ' | 销方地址 |
| 6 | fmarket_taxpayer_id | 二手市场税号 | varchar | 30 |  | √ | ' ' | 二手市场税号 |
| 7 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 8 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 9 | fdeduction_flag | 抵扣标识 | varchar | 2 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 12 | fsaler_phone_number | 销方电话 | varchar | 30 |  | √ | ' ' | 销方电话 |
| 13 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 14 | fcheck_code | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 15 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 16 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 17 | fbuyer_id_no | 购方组织代码/身份证号码 | varchar | 30 |  | √ | ' ' | 购方组织代码/身份证号码 |
| 18 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | ftotal_amount | 车价合计 | numeric | 23 | 10 | √ | 0.0000000000 | 车价合计 |
| 20 | fmarket_bank_accout | 二手市场开户银行帐号 | varchar | 100 |  | √ | ' ' | 二手市场开户银行帐号 |
| 21 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 |
| 22 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauction_taxpayer_id | 拍卖/经营税号 | varchar | 30 |  | √ | ' ' | 拍卖/经营税号 |
| 24 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预抵扣 |
| 25 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 26 | flicense_plate_number | 车牌照号 | varchar | 20 |  | √ | ' ' | 车牌照号 |
| 27 | fbuyer_address | 购方地址 | varchar | 120 |  | √ | ' ' | 购方地址 |
| 28 | fauction_name | 拍卖/经营名称 | varchar | 50 |  | √ | ' ' | 拍卖/经营名称 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fsaler_id_no | 销方组织代码/身份证号码 | varchar | 30 |  | √ | ' ' | 销方组织代码/身份证号码 |
| 31 | fregistration_number | 登记证号 | varchar | 30 |  | √ | ' ' | 登记证号 |
| 32 | fmarket_phone_number | 二手市场电话 | varchar | 30 |  | √ | ' ' | 二手市场电话 |
| 33 | fband_model | 厂牌型号 | varchar | 30 |  | √ | ' ' | 厂牌型号 |
| 34 | fauction_address | 拍卖/经营地址 | varchar | 120 |  | √ | ' ' | 拍卖/经营地址 |
| 35 | fauction_bank_accout | 拍卖/经营开户银行帐号 | varchar | 100 |  | √ | ' ' | 拍卖/经营开户银行帐号 |
| 36 | fdelete | 可用状态 | varchar | 4 |  |  | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 37 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 38 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 41 | fmarket_name | 二手市场单位 | varchar | 100 |  | √ | ' ' | 二手市场单位 |
| 42 | fmachine_no | 机器编码 | varchar | 50 |  | √ | ' ' | 机器编码 |
| 43 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 44 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 7 :部分红冲 4 :异常 |
| 45 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 48 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fvehicle_management_name | 转入地车辆管理所名称 | varchar | 50 |  | √ | ' ' | 转入地车辆管理所名称 |
| 51 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | finvoice_date | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 54 | fbuyer_phone_number | 购方电话 | varchar | 30 |  | √ | ' ' | 购方电话 |
| 55 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 56 | fvehicle_type | 车辆类型 | varchar | 30 |  | √ | ' ' | 车辆类型 |
| 57 | fvehicle_identification_no | 车辆识别代码/车驾号码 | varchar | 30 |  | √ | ' ' | 车辆识别代码/车驾号码 |
| 58 | fissuing_office | 开票单位 | varchar | 50 |  | √ | ' ' | 开票单位 |
| 59 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 60 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 61 | fauction_phone_number | 拍卖/经营电话 | varchar | 30 |  | √ | ' ' | 拍卖/经营电话 |
| 62 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 63 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_usedcar |  | fserial_no |
| 2 | idx_rim_inv_usedcar_no |  | finvoice_code,finvoice_no |
| 3 | pk_rim_inv_usedcar |  | fid |
| 4 | idx_rim_inv_usedcar_taxorg |  | ftax_org,ftax_period,fdeduction_purpose |
