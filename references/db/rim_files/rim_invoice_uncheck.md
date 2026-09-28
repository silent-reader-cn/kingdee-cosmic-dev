# 待查验发票列表-rim_invoice_uncheck

## 待查验发票列表-主表 t_rim_invoice_uncheck

- **表名称：** 待查验发票列表-主表
- **表名：** t_rim_invoice_uncheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | ffile_name | 文件名 | varchar | 200 |  | √ | ' ' | 文件名 |
| 4 | fcheck_result | 查验结果 | varchar | 50 |  | √ | ' ' | 查验结果 |
| 5 | finvoice_detail_tag | 发票明细_详情 | text | 0 |  |  | null | 发票明细_详情 |
| 6 | finvoice_detail | 发票明细 | varchar | 255 |  | √ | ' ' | 发票明细 |
| 7 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 8 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 9 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 10 | fcompany_seal | 是否有公司印章 | varchar | 2 |  | √ | ' ' | 是否有公司印章,枚举: 0 :没有 1 :有 |
| 11 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 12 | fcheck_code | 验证码 | varchar | 30 |  | √ | ' ' | 验证码 |
| 13 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 14 | fpage_no | 对于文件页码 | int4 | 32 |  | √ | 0 | 对于文件页码 |
| 15 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: 9 :税盘 10 :滴滴 11 :云票儿 |
| 16 | fexpense_amount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 17 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 19 | fexpense_time | 报销时间 | timestamp | 0 |  |  | null | 报销时间 |
| 20 | fdeduction_purpose | 抵扣用途 | varchar | 50 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 |
| 21 | fauthenticate_flag | 认证标志 | varchar | 2 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :旅客运输抵扣 |
| 22 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 23 | fcheck_times | 查验次数 | int4 | 32 |  | √ | 0 | 查验次数 |
| 24 | fcheck_time | 查验时间 | timestamp | 0 |  |  | null | 查验时间 |
| 25 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 26 | fdelete | 可用状态 | varchar | 2 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 27 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 28 | fsource_area | 发票源地区 | varchar | 150 |  | √ | ' ' | 发票源地区 |
| 29 | fcollect_type | 采集方式 | varchar | 10 |  | √ | ' ' | 采集方式,枚举: 1 :手机拍照 2 :文件上传 3 :扫描仪 4 :扫码枪 5 :手工录入 9 :税盘 |
| 30 | fis_revise | 是否修改 | varchar | 50 |  | √ | ' ' | 是否修改,枚举: 0 :否 1 :是 |
| 31 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 32 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 33 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 34 | faccount_time | 入账时间 | timestamp | 0 |  |  | null | 入账时间 |
| 35 | fvouch_no | 凭证号 | varchar | 500 |  | √ | ' ' | 凭证号 |
| 36 | fmanage_status | 管理状态 | varchar | 50 |  | √ | ' ' | 管理状态,枚举: |
| 37 | fexpense_no | 报销单号 | varchar | 500 |  | √ | ' ' | 报销单号 |
| 38 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 39 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 42 | finvoice_info | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :已抵扣 mo_1 :已改 |
| 43 | finvoice_date | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 44 | ftotal_tax_amount | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 45 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 46 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 47 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 48 | fcheck_status | 查验状态 | varchar | 2 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 |
| 49 | fcontinuous_no | 是否串号 | varchar | 2 |  | √ | ' ' | 是否串号,枚举: 0 :否 1 :是 |
| 50 | fdest_area | 目的地地区 | varchar | 150 |  | √ | ' ' | 目的地地区 |
| 51 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_uncheck_no |  | fserial_no |
| 2 | pk_rim_invoice_uncheck |  | fid |
| 3 | idx_rim_invoice_uncheck |  | ftenant_no,finvoice_code,finvoice_no |
