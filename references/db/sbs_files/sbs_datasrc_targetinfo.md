# 指标目标值信息-sbs_datasrc_targetinfo

## 指标目标值信息-主表 t_sbs_data_targetinfo

- **表名称：** 指标目标值信息-主表
- **表名：** t_sbs_data_targetinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fscopetype | 目标值范围类型 | varchar | 50 |  | √ | ' ' | 目标值范围类型,枚举: whole :按整体 dimension :按指标维度 |
| 2 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fdimensionkey | 维度标识 | varchar | 100 |  | √ | ' ' | 维度标识 |
| 4 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 5 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 6 | fquarter | 季度 | int4 | 32 |  | √ | 0 | 季度 |
| 7 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 8 | fvalue | 指标值 | numeric | 23 | 10 | √ | 0 | 指标值 |
| 9 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 10 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 11 | fmetricsid | 供应链指标 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |
| 12 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 13 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 14 | fperiodtype | 目标值周期类型 | varchar | 50 |  | √ | ' ' | 目标值周期类型,枚举: year :按年 quarter :按季度 month :按月 day :按天 |
| 15 | fdimensionval | 指标对象值 | varchar | 255 |  | √ | ' ' | 指标对象值 |
| 16 | fmonth | 月份 | int4 | 32 |  | √ | 0 | 月份 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_data_target_date |  | fbizdate |
| 2 | pk_sbs_data_targetinfo |  | ftpl_pkid |
| 3 | idx_sbs_data_target_m |  | fmetricsid |
