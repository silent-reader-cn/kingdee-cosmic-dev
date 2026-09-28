# 同步发票台账-rim_down_account

## 同步发票台账-主表 t_rim_down_account

- **表名称：** 同步发票台账-主表
- **表名：** t_rim_down_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffpy_serial_no | 发票云发票流水号 | varchar | 36 |  | √ | ' ' | 发票云发票流水号 |
| 3 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 4 | fbatch_no | 批次号 | varchar | 36 |  | √ | ' ' | 批次号 |
| 5 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 6 | finvoice_status | 发票状态 | varchar | 2 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 7 :部分红冲 |
| 7 | ftax_period | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 8 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | feffective_tax_amount | 有效税额 | numeric | 23 | 10 | √ | 0 | 有效税额 |
| 11 | fstatus | 处理状态 | varchar | 2 |  | √ | ' ' | 处理状态,枚举: 1 :处理成功 2 :已下载表头待查验 3 :超出初始的日期不处理 4 :进项下载缺少抵扣数据 5 :进销项已下载 6 :查验失败 |
| 12 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 13 | fdata_type | 数据类型 | varchar | 2 |  | √ | ' ' | 数据类型,枚举: 1 :进项 2 :销项 |
| 14 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 15 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 16 | ftax_amount | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 17 | fdeduction_purpose | 抵扣用途 | varchar | 2 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 |
| 18 | fauthenticate_flag | 认证状态 | varchar | 2 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :已勾选 2 :勾选认证 3 :扫描认证 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 21 | finvoice_code | 发票代码 | varchar | 30 |  | √ | ' ' | 发票代码 |
| 22 | finvoice_no | 发票号码 | varchar | 30 |  | √ | ' ' | 发票号码 |
| 23 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 24 | fselect_authenticate_time | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 25 | fscan_authenticate_time | 扫描认证时间 | timestamp | 0 |  |  | null | 扫描认证时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_down_account_date |  | finvoice_date |
| 2 | idx_rim_down_account |  | fbatch_no |
| 3 | idx_rim_down_account_org |  | forg |
| 4 | pk_rim_down_account |  | fid |
| 5 | idx_rim_down_account2 |  | fstatus |
| 6 | idx_rim_downaccount_createtime |  | fcreatetime |
| 7 | idx_rim_down_accoun_serial_no |  | fserial_no |
