# 供应商经营信息-pm_supplierabnormalinfo

## 供应商经营信息-主表 t_pm_supplierabnormalinfo

- **表名称：** 供应商经营信息-主表
- **表名：** t_pm_supplierabnormalinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsuppliername | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 5 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 6 | fseqno | 序号 | varchar | 4 |  | √ | ' ' | 序号 |
| 7 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 8 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 9 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 11 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 12 | fdetail | 风险数量 | varchar | 255 |  | √ | ' ' | 风险数量 |
| 13 | ftype | 类型 | varchar | 24 |  | √ | ' ' | 类型 |
| 14 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 15 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 16 | fcompanyid | 公司ID | varchar | 128 |  | √ | ' ' | 公司ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_supplierabnormalinfo |  | ftpl_pkid |
| 2 | idx_pm_supabnoinfo_date |  | fbiztime |
| 3 | idx_pm_supabnoinfo_org |  | forgid |
