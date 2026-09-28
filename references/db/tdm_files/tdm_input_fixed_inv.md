# 定额发票-tdm_input_fixed_inv

## 定额发票-主表 t_tdm_input_fixed_inv

- **表名称：** 定额发票-主表
- **表名：** t_tdm_input_fixed_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fplace | 发票所在地 | varchar | 40 |  | √ | ' ' | 发票所在地 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fticketcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 11 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 14 :定额发票 |
| 15 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 16 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 17 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 18 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 19 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 20 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsalertaxno | 销方税号 | varchar | 64 |  | √ | ' ' | 销方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_fixed_inv |  | forg,finvoicecode,finvoiceno |
| 2 | t_tdm_input_fixed_inv_pkey |  | fid |
