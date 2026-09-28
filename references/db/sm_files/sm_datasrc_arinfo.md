# 应收信息-sm_datasrc_arinfo

## 应收信息-主表 t_sm_data_arinfo

- **表名称：** 应收信息-主表
- **表名：** t_sm_data_arinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 5 | foveraramount | 逾期应收金额 | numeric | 28 | 10 | √ | 0 | 逾期应收金额 |
| 6 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 7 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 8 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 9 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 10 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 11 | faramount | 应收款余额 | numeric | 28 | 10 | √ | 0 | 应收款余额 |
| 12 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 13 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_data_arinfo_org |  | forgid,fcustomerid |
| 2 | pk_sm_data_arinfo |  | ftpl_pkid |
