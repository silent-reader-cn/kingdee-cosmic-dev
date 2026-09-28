# 坏账信息-sm_datasrc_baddebt

## 坏账信息-主表 t_sm_data_baddebt

- **表名称：** 坏账信息-主表
- **表名：** t_sm_data_baddebt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbadamount | 累计坏账总额 | numeric | 28 | 10 | √ | 0 | 累计坏账总额 |
| 5 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 7 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 8 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 9 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 10 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 11 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 12 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 13 | faramount | 累计应收总额 | numeric | 28 | 10 | √ | 0 | 累计应收总额 |
| 14 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 15 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 16 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 17 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_data_baddebt |  | ftpl_pkid |
| 2 | idx_sm_data_baddebt_date |  | fbizdate |
| 3 | idx_sm_data_baddebt_org |  | forgid,fcustomerid |
