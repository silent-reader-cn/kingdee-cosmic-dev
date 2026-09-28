# 进项发票-tcvat_invoice_auth

## 进项发票-主表 t_tdm_invoice_input

- **表名称：** 进项发票-主表
- **表名：** t_tdm_invoice_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 3 | fdrawer | 开票人 | varchar | 100 |  | √ | ' ' | 开票人 |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 2 | √ | 0.00 | 价税合计 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finputstatus | 进项状态 | varchar | 30 |  | √ | ' ' | 进项状态,枚举: unauth :未认证 authed :已认证 unauth_overtime :逾期未认证 |
| 7 | fbuyeraccount | 购方银行帐号 | varchar | 100 |  | √ | ' ' | 购方银行帐号 |
| 8 | fbuyeraddressphone | 购方地址电话 | varchar | 300 |  | √ | ' ' | 购方地址电话 |
| 9 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsaleraddressphone | 销方地址电话 | varchar | 300 |  | √ | ' ' | 销方地址电话 |
| 12 | fsaleraccount | 销方银行帐号 | varchar | 300 |  | √ | ' ' | 销方银行帐号 |
| 13 | fmachineno | 机器编号 | varchar | 100 |  | √ | ' ' | 机器编号 |
| 14 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 15 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 16 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 17 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fsalertaxno | 销方税号 | varchar | 100 |  | √ | ' ' | 销方税号 |
| 20 | ftaxamount | 合计税额 | numeric | 23 | 2 | √ | 0.00 | 合计税额 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fusedjzjtse | fusedjzjtse | numeric | 23 | 2 | √ | 0.00 |  |
| 24 | flastrolloutuser | flastrolloutuser | int8 | 64 |  | √ | 0 |  |
| 25 | flastrollouttime | flastrollouttime | timestamp | 0 |  |  | null |  |
| 26 | fjzjtamount | 即征即退税额 | numeric | 23 | 2 | √ | 0.00 | 即征即退税额 |
| 27 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 30 | fpayee | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 31 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fscanauthenticatetime | 扫描认证时间 | timestamp | 0 |  |  | null | 扫描认证时间 |
| 34 | fselecttime | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 35 | freviewer | 复核人 | varchar | 100 |  | √ | ' ' | 复核人 |
| 36 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 37 | fmaingoodsname | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 38 | fbuyertaxno | 购方税号 | varchar | 100 |  | √ | ' ' | 购方税号 |
| 39 | fremark | 备注 | varchar | 480 |  | √ | ' ' | 备注 |
| 40 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fregisterstatus | fregisterstatus | varchar | 30 |  | √ | ' ' |  |
| 44 | fremainamount | 可转出金额 | numeric | 23 | 2 | √ | 0.00 | 可转出金额 |
| 45 | fexportamount | 出口税额 | numeric | 23 | 2 | √ | 0.00 | 出口税额 |
| 46 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 15 :通行费发票 |
| 47 | frolloutamount | 已转出金额 | numeric | 23 | 2 | √ | 0.00 | 已转出金额 |
| 48 | finvoiceamount | 合计金额 | numeric | 23 | 2 | √ | 0.00 | 合计金额 |
| 49 | fproxymark | 代开标识代开标识 | varchar | 30 |  | √ | ' ' | 代开标识代开标识,枚举: 0 :默认 1 :代开 |
| 50 | fusedckse | fusedckse | numeric | 23 | 2 | √ | 0.00 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_invoice_input |  | fbillno |
| 2 | t_tdm_invoice_input_pkey |  | fid |
| 3 | idx_t_tdm_invoice_input2 |  | fselectauthenticatetime,ftaxperiod,forgid |
