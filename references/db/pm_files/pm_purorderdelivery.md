# 采购订单交期风险信息-pm_purorderdelivery

## 采购订单交期风险信息-主表 t_pm_purorderdelivery

- **表名称：** 采购订单交期风险信息-主表
- **表名：** t_pm_purorderdelivery

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 4 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 5 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 6 | fexpectleadtime | 预计提前期（天） | numeric | 23 | 6 | √ | 0 | 预计提前期（天） |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 9 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 10 | forderleadtime | 订单提前期（天） | numeric | 23 | 6 | √ | 0 | 订单提前期（天） |
| 11 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 12 | fentryrow | 分录行 | int4 | 32 |  | √ | 0 | 分录行 |
| 13 | forgname | forgname | varchar | 255 |  | √ | ' ' |  |
| 14 | fmaterialnumber | 物料编码 | varchar | 255 |  | √ | ' ' | 物料编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorderdelivery_date |  | fbiztime |
| 2 | pk_pm_purorderdelivery |  | ftpl_pkid |
