# 通用机打发票-eafc_inv_general

## 通用机打发票-主表 t_eafc_inv_general

- **表名称：** 通用机打发票-主表
- **表名：** t_eafc_inv_general

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 3 | fdrawer | 开票人 | varchar | 20 |  | √ | ' ' | 开票人 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fpayee | 收款人 | varchar | 20 |  | √ | ' ' | 收款人 |
| 6 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fexit | 出口 | varchar | 32 |  | √ | ' ' | 出口 |
| 8 | fplace | 发票所在地 | varchar | 32 |  | √ | ' ' | 发票所在地 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcheck_code | 校验码 | varchar | 32 |  | √ | ' ' | 校验码 |
| 13 | freviewer | 复核人 | varchar | 20 |  | √ | ' ' | 复核人 |
| 14 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 15 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 18 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 19 | ftime | 过路过桥发票时间 | varchar | 10 |  | √ | ' ' | 过路过桥发票时间 |
| 20 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 26 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 27 | ftotal_tax_amount | 合计税额 | numeric | 23 | 2 |  | null | 合计税额 |
| 28 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fbuyer_tax_no | 买方税号 | varchar | 20 |  | √ | ' ' | 买方税号 |
| 31 | fentrance | 入口 | varchar | 32 |  | √ | ' ' | 入口 |
| 32 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 34 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 35 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 36 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 37 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 38 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 39 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 40 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_general |  | fid |
