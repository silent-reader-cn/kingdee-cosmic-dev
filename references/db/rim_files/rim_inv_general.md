# 通用机打发票-rim_inv_general

## 通用机打发票-主表 t_rim_inv_general

- **表名称：** 通用机打发票-主表
- **表名：** t_rim_inv_general

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 3 | fdrawer | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fpayee | 收款人 | varchar | 20 |  | √ | ' ' | 收款人 |
| 6 | fexit | 出口 | varchar | 32 |  | √ | ' ' | 出口 |
| 7 | fplace | 发票所在地 | varchar | 32 |  | √ | ' ' | 发票所在地 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcheck_code | 校验码 | varchar | 32 |  | √ | ' ' | 校验码 |
| 12 | freviewer | 复核人 | varchar | 20 |  | √ | ' ' | 复核人 |
| 13 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 14 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 15 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 17 | ftime | 过路过桥发票时间 | varchar | 10 |  | √ | ' ' | 过路过桥发票时间 |
| 18 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 21 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 22 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 25 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 26 | ftotal_tax_amount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 27 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fbuyer_tax_no | 买方税号 | varchar | 20 |  | √ | ' ' | 买方税号 |
| 30 | fentrance | 入口 | varchar | 32 |  | √ | ' ' | 入口 |
| 31 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 33 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 34 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 35 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 36 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 37 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 38 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_general |  | fid |
| 2 | idx_rim_inv_general |  | fserial_no |
| 3 | idx_rim_inv_general_no |  | finvoice_code,finvoice_no |
| 4 | idx_rim_inv_general_taxorg |  | ftax_org,finvoice_type |
