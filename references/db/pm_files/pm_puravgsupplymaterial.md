# 采购平均供货周期-pm_puravgsupplymaterial

## 采购平均供货周期-主表 t_pm_puravgsupplymaterial

- **表名称：** 采购平均供货周期-主表
- **表名：** t_pm_puravgsupplymaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 2 | fprovidersupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgnumber | 采购组织编码 | varchar | 100 |  | √ | ' ' | 采购组织编码 |
| 6 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 7 | frecduration | 收货间隔天数 | numeric | 23 | 4 | √ | 0 | 收货间隔天数 |
| 8 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 9 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 11 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 12 | fbillentryid | 订单分录ID | int8 | 64 |  | √ | 0 | 订单分录ID |
| 13 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 14 | fprovidersuppliernumber | 订货供应商编码 | varchar | 100 |  | √ | ' ' | 订货供应商编码 |
| 15 | fprovidersuppliername | 订货供应商名称 | varchar | 255 |  | √ | ' ' | 订货供应商名称 |
| 16 | forgname | 采购组织名称 | varchar | 255 |  | √ | ' ' | 采购组织名称 |
| 17 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 18 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puravgmat_date |  | fbiztime |
| 2 | pk_pm_puravgsupplymaterial |  | ftpl_pkid |
| 3 | idx_pm_puravgmat_org |  | forgid,fprovidersupplier |
