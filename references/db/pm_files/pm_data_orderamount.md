# 采购订单金额信息-pm_data_orderamount

## 采购订单金额信息-主表 t_pm_data_orderamount

- **表名称：** 采购订单金额信息-主表
- **表名：** t_pm_data_orderamount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | foverdueamount | 逾期金额 | numeric | 23 | 10 | √ | 0 | 逾期金额 |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 7 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 8 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 9 | fnotreceiveqty | 未收货数量 | numeric | 23 | 10 | √ | 0 | 未收货数量 |
| 10 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 12 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 13 | fcuramountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 14 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 15 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_data_odm_date |  | fbiztime |
| 2 | idx_pm_data_odm_org |  | forgid,fprovidersupplier |
| 3 | pk_pm_data_orderamount |  | ftpl_pkid |
