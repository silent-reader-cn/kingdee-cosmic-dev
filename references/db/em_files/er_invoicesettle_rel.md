# 开票申请与结算单映射-er_invoicesettle_rel

## 开票申请与结算单映射-主表 t_er_invoicesettle_rel

- **表名称：** 开票申请与结算单映射-主表
- **表名：** t_er_invoicesettle_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fserviceitem | 服务项目 | varchar | 50 |  | √ | ' ' | 服务项目 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fsettleid | 结算id | int8 | 64 |  | √ | 0 | 结算id |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftotalamount | 结算金额（含税） | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额（含税） |
| 9 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fsystemtaxrate | 系统税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 系统税率（%） |
| 11 | fsettleformid | 结算单formid | varchar | 30 |  | √ | ' ' | 结算单formid |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | finvoicebillno | 开票申请单号 | varchar | 100 |  | √ | ' ' | 开票申请单号 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fallorderbaseid | 订单总表 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 17 | finvoiceid | 开票id | int8 | 64 |  | √ | 0 | 开票id |
| 18 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_settleid |  | fsettleid |
| 2 | t_er_invoicesettle_rel_pkey |  | fid |
| 3 | index_rel_allorderid |  | fallorderbaseid |
| 4 | index_invoiceid |  | finvoiceid |
