# 采购申请重复申请-pm_purapplyrepeatdata

## 采购申请重复申请-主表 t_pm_purapplyrepeat

- **表名称：** 采购申请重复申请-主表
- **表名：** t_pm_purapplyrepeat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 5 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 6 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fbillinfo | 重复申请编码-行号 | varchar | 255 |  | √ | ' ' | 重复申请编码-行号 |
| 9 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 10 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 11 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 12 | fentryrow | 分录行 | int4 | 32 |  | √ | 0 | 分录行 |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 15 | fbillno | 单据编码 | varchar | 64 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplyrepeat_date |  | fbiztime |
| 2 | pk_pm_purapplyrepeat |  | ftpl_pkid |
| 3 | idx_pm_purapplyrepeat_org |  | forgid |
