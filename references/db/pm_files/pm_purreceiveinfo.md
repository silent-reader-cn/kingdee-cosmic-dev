# 收料通知信息-pm_purreceiveinfo

## 收料通知信息-主表 t_pm_data_purreceiveinfo

- **表名称：** 收料通知信息-主表
- **表名：** t_pm_data_purreceiveinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconcessionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 2 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 7 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 8 | fcheckqty | 检查接收数量 | numeric | 23 | 10 | √ | 0 | 检查接收数量 |
| 9 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 10 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 12 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 13 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 14 | fdamageqty | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 15 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 16 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 17 | fchecktotalqty | 检查总数量 | numeric | 23 | 10 | √ | 0 | 检查总数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_data_prv_date |  | fbiztime |
| 2 | pk_pm_data_purreceiveinfo |  | ftpl_pkid |
| 3 | idx_pm_data_prv_org |  | forgid,fprovidersupplier |
