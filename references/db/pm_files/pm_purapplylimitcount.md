# 采购申请超量申请-pm_purapplylimitcount

## 采购申请超量申请-主表 t_pm_purapplylimitcount

- **表名称：** 采购申请超量申请-主表
- **表名：** t_pm_purapplylimitcount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 物料ID | int8 | 64 |  | √ | 0 | 物料ID |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 6 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 7 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 10 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 11 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 12 | fentryrow | 分录行 | int4 | 32 |  | √ | 0 | 分录行 |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | fmonth | 月份 | varchar | 24 |  | √ | ' ' | 月份 |
| 15 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 16 | fmaterialnumber | 物料编码 | varchar | 255 |  | √ | ' ' | 物料编码 |
| 17 | flinkrelativeratio | 环比 | numeric | 23 | 6 | √ | 0 | 环比 |
| 18 | fbillno | 单据编码 | varchar | 64 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplylimitcount_date |  | fbiztime,forgid,fmaterialid |
| 2 | pk_pm_purapplylimitcount |  | ftpl_pkid |
