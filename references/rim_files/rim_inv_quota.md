# 定额发票-rim_inv_quota

## 定额发票-主表 t_rim_inv_quota

- **表名称：** 定额发票-主表
- **表名：** t_rim_inv_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fplace | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 8 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 9 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 10 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 11 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftotal_amount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 14 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 15 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 18 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 22 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 23 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 24 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 25 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 26 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 27 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_quota_taxorg |  | ftax_org |
| 2 | idx_rim_inv_quota_no |  | finvoice_code,finvoice_no |
| 3 | pk_rim_inv_quota |  | fid |
| 4 | idx_rim_inv_quota |  | fserial_no |
