# 采购退料率信息-pm_data_purrefundinfo

## 采购退料率信息-主表 t_pm_data_purrefundinfo

- **表名称：** 采购退料率信息-主表
- **表名：** t_pm_data_purrefundinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finredqty | 采购入库红单数量 | numeric | 23 | 4 | √ | 0 | 采购入库红单数量 |
| 2 | frecblueqty | 收料蓝单数量 | numeric | 23 | 4 | √ | 0 | 收料蓝单数量 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 4 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgnumber | 库存组织编码 | varchar | 100 |  | √ | ' ' | 库存组织编码 |
| 8 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 9 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 10 | frecredqty | 收料红单数量 | numeric | 23 | 4 | √ | 0 | 收料红单数量 |
| 11 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fbizorgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 13 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 14 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 15 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | finblueqty | 采购入库蓝单数量 | numeric | 23 | 4 | √ | 0 | 采购入库蓝单数量 |
| 17 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 18 | fprovidersuppliernumber | 订货供应商编码 | varchar | 100 |  | √ | ' ' | 订货供应商编码 |
| 19 | fbizorgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 20 | fprovidersuppliername | 订货供应商名称 | varchar | 255 |  | √ | ' ' | 订货供应商名称 |
| 21 | forgname | 库存组织名称 | varchar | 255 |  | √ | ' ' | 库存组织名称 |
| 22 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 23 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_data_purrefnd_date |  | fbiztime |
| 2 | pk_pm_data_purrefundinfo |  | ftpl_pkid |
| 3 | idx_pm_data_purrefnd_org |  | fbizorgid,fprovidersupplier |
