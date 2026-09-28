# 进项转出发票登记列表-til_invoice_list

## 采集用户单据体-子表 t_rim_inv_collect_user

- **表名称：** 采集用户单据体-子表
- **表名：** t_rim_inv_collect_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frim_user | rim_user | int8 | 64 |  | √ | 0 | rim_user |
| 3 | fcollect_user_org | 采集人最后一次操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcollect_user | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_collect_user |  | fcollect_user,frim_user |
| 2 | pk_rim_inv_collect_user |  | fentryid |
| 3 | idx_rim_inv_collect_user_fk |  | fid |

---

## 采集组织单据体-子表 t_rim_inv_collect_org

- **表名称：** 采集组织单据体-子表
- **表名：** t_rim_inv_collect_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcollect_org_user | 当前组织最后一次操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcollect_org | 采集组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_collect_org_fk |  | fid |
| 2 | pk_rim_inv_collect_org |  | fentryid |
| 3 | idx_rim_inv_collect_org |  | fcollect_org |

---

## 进项转出发票登记列表-主表 t_rim_invoice

- **表名称：** 进项转出发票登记列表-主表
- **表名：** t_rim_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreset_deduction_purpose | 单据抵扣用途 | varchar | 2 |  | √ | ' ' | 单据抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fcancel_select_type | 撤销勾选类型 | varchar | 2 |  | √ | ' ' | 撤销勾选类型,枚举: 1 :手工撤销 2 :自动撤销 |
| 5 | finternational_flag | 国内国际标志 | varchar | 2 |  | √ | ' ' | 国内国际标志,枚举: 1 :国内 2 :国际 |
| 6 | fcheck_result | 查验结果 | varchar | 50 |  | √ | ' ' | 查验结果 |
| 7 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 8 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 9 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 10 | fmain_goods_name | 主要商品名片 | varchar | 200 |  | √ | ' ' | 主要商品名片 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 13 | fcompany_seal | 是否有公司印章 | varchar | 2 |  | √ | ' ' | 是否有公司印章,枚举: 0 :没有 1 :有 |
| 14 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 15 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 16 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 17 | freal_transferdate | 实际转出税期 | timestamp | 0 |  |  | null | 实际转出税期 |
| 18 | fexpense_amount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 19 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 20 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 22 | fexpense_time | 报销时间 | timestamp | 0 |  |  | null | 报销时间 |
| 23 | fdeduction_purpose | 抵扣用途 | varchar | 50 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fauthenticate_flag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 26 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 27 | fcheck_times | 查验次数 | int4 | 32 |  | √ | 0 | 查验次数 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fcheck_time | 查验时间 | timestamp | 0 |  |  | null | 查验时间 |
| 30 | frollout_amount | 转出税额 | numeric | 23 | 10 | √ | 0 | 转出税额 |
| 31 | fsaler_tax_no | 销方税号 | varchar | 30 |  | √ | ' ' | 销方税号 |
| 32 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 33 | fexpense_status | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :未用 30 :在用 60 :已用 65 :已入账 |
| 34 | fsource_area | 发票源地区 | varchar | 150 |  | √ | ' ' | 发票源地区 |
| 35 | foriginal_time | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 36 | fisvoucher | 生成凭证 | varchar | 2 |  | √ | ' ' | 生成凭证,枚举: 0 :否 1 :是 |
| 37 | fcollect_type | 采集方式 | varchar | 2 |  | √ | ' ' | 采集方式,枚举: 1 :手机拍照 2 :文件上传 3 :扫描仪 4 :扫码枪 5 :手工录入 9 :税盘 10 :excel引入 30 :批量导入 |
| 38 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 39 | fsalelist_complete | 清单标志 | varchar | 10 |  | √ | ' ' | 清单标志,枚举: 0 :清单完整 1 :非清单票 2 :清单不完整 3 :清单未上传 |
| 40 | fis_revise | 是否修改 | varchar | 50 |  | √ | ' ' | 是否修改,枚举: 0 :否 1 :是 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbuyer_name | 购方名称 | varchar | 150 |  | √ | ' ' | 购方名称 |
| 43 | ftransport_deduction | 旅客运输抵扣 | varchar | 2 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 44 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 45 | ftag | 发票标注 | varchar | 50 |  | √ | ' ' | 发票标注 |
| 46 | freceiver | 签收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | faccount_time | 入账时间 | timestamp | 0 |  |  | null | 入账时间 |
| 48 | fvouch_no | 凭证号 | varchar | 500 |  | √ | ' ' | 凭证号 |
| 49 | fmanage_status | 管理状态 | varchar | 50 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 50 | finvoice_status | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 7 :部分红冲 |
| 51 | fexpense_no | 报销单号 | varchar | 500 |  | √ | ' ' | 报销单号 |
| 52 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fproxy_mark | 代开标识 | varchar | 4 |  | √ | '0' | 代开标识,枚举: 0 :否 1 :是 |
| 55 | fsalelist_sumpage | 清单总页码数 | int4 | 32 |  | √ | 0 | 清单总页码数 |
| 56 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 57 | finvoice_info | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 ty_30 :海外发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 ch_4 :不查验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :预勾选 au_5 :勾选中 td_1 :旅客运输抵扣 mo_1 :已改 ty_21 :海关缴款书 ty_24 :火车票退票凭证 ty_25 :财政电子票据 ty_26 :全电普票 ty_27 :全电专票 st_7 :部分红冲 st_8 :全额红冲 st_4 :异常 |
| 58 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 59 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 60 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 61 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 62 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 63 | ftotal_tax_amount | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 64 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 65 | fbuyer_tax_no | 购方税号 | varchar | 30 |  | √ | ' ' | 购方税号 |
| 66 | ftax_org | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 67 | fsaler_name | 销方名称 | varchar | 150 |  | √ | ' ' | 销方名称 |
| 68 | fcheck_status | 查验状态 | varchar | 50 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 4 :不查验 |
| 69 | fcontinuous_no | 是否串号 | varchar | 2 |  | √ | ' ' | 是否串号,枚举: 0 :否 1 :是 |
| 70 | faudit_result | 审计状态 | varchar | 2 |  | √ | '0' | 审计状态,枚举: 0 :正常 1 :未处理 2 :已处理 |
| 71 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 72 | fdest_area | 目的地地区 | varchar | 150 |  | √ | ' ' | 目的地地区 |
| 73 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 74 | frollout_remark | 转出原因 | varchar | 300 |  | √ | ' ' | 转出原因 |
| 75 | faccount_tax_amount | 入账税额 | numeric | 23 | 10 | √ | 0 | 入账税额 |

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

---

## 进项转出发票登记列表-分表 t_rim_invoice_a

- **表名称：** 进项转出发票登记列表-分表
- **表名：** t_rim_invoice_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freal_output_amount | 实际转出税额 | numeric | 23 | 10 | √ | 0 | 实际转出税额 |
| 3 | foutput_type | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 2 :免税项目用 3 :集体福利、个人消费 4 :非正常损失 5 :简易计税方法征税项目用 6 :免抵退税办法不得抵扣的进项税额 8 :异常凭证转出进项税额 11 :其他 12 :开具红字专用发票信息表 - :- |
| 4 | foutput_signtype | 登记方式 | varchar | 30 |  | √ | ' ' | 登记方式,枚举: 1 :直接登记转出 2 :无法划分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_invoice_a |  | fid |
| 2 | idx_rim_invoice_out_type |  | foutput_type |

---

## 单据和凭证-子表 t_rim_reim_vouch_relation

- **表名称：** 单据和凭证-子表
- **表名：** t_rim_reim_vouch_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freim_resource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源 |
| 3 | freim_expense_type | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 4 | fvouch_vouchid | 凭证id | varchar | 50 |  | √ | ' ' | 凭证id |
| 5 | fvouch_account_date | 凭证会计属期 | timestamp | 0 |  |  | null | 凭证会计属期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freim_expense_num | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 8 | fvouch_resource | 凭证来源 | varchar | 50 |  | √ | ' ' | 凭证来源 |
| 9 | freim_expense_id | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 10 | fvouch_account_time | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 11 | freim_create_time | 单据关系创建时间 | timestamp | 0 |  |  | null | 单据关系创建时间 |
| 12 | freim_entityid | 单据实体标识 | varchar | 50 |  | √ | ' ' | 单据实体标识 |
| 13 | freim_status | 单据报销状态 | varchar | 50 |  | √ | ' ' | 单据报销状态,枚举: 1 :未用 30 :在用 60 :已用 65 :已入账 70 :已归档 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fvouch_vouch_no | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reim_vouch_relation_vo |  | fvouch_vouchid |
| 2 | idx_reim_vouch_relation_ex |  | freim_expense_id |
| 3 | pk_t_rim_reim_vouch_relation |  | fentryid |
| 4 | idx_reim_vouch_relation_fk |  | fid |
