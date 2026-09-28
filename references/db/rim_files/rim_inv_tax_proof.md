# 完税证明-rim_inv_tax_proof

## 完税证明-主表 t_rim_inv_tax_proof

- **表名称：** 完税证明-主表
- **表名：** t_rim_inv_tax_proof

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyer_name | 购买方名称 | varchar | 120 |  | √ | ' ' | 购买方名称 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 8 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 9 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 10 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ftotal_amount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 13 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 14 | ftax_authority_name | 税务机关 | varchar | 100 |  | √ | ' ' | 税务机关 |
| 15 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbuyer_tax_no | 购买方税号 | varchar | 20 |  | √ | ' ' | 购买方税号 |
| 20 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 22 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 23 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 24 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 25 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | ftax_paid_proof_no | 完税证明号码 | varchar | 20 |  | √ | ' ' | 完税证明号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_tax_proof |  | fid |
| 2 | idx_rim_inv_tax_proof |  | fserial_no |
| 3 | idx_rim_inv_tax_proof_taxorg |  | ftax_org,finvoice_date |
| 4 | idx_rim_inv_tax_proof_no |  | ftax_paid_proof_no |
