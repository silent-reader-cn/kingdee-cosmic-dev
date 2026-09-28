# 库存红蓝单信息-pm_data_purinbillinfo

## 库存红蓝单信息-主表 t_pm_data_purinbillinfo

- **表名称：** 库存红蓝单信息-主表
- **表名：** t_pm_data_purinbillinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 6 | fredqty | 红单数量 | numeric | 23 | 10 | √ | 0 | 红单数量 |
| 7 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 8 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 9 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 11 | fblueqty | 蓝单数量 | numeric | 23 | 10 | √ | 0 | 蓝单数量 |
| 12 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 13 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 14 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_data_purinbillinfo |  | ftpl_pkid |
| 2 | idx_pm_data_pib_date |  | fbiztime |
| 3 | idx_pm_data_pib_org |  | forgid,fprovidersupplier |
