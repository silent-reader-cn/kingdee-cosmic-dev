# 排产订单-mrp_pls_order

## 排产订单-主表 t_mrp_proschedule_order

- **表名称：** 排产订单-主表
- **表名：** t_mrp_proschedule_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductyieldrate | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 3 | fordernum | 订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单数量 |
| 4 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 7 | fplanstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 8 | fsourceentity | 来源单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 10 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 11 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 12 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 15 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 16 | fplanfinishdate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fplanner | 计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbomdatetime | 展开BOM时间 | timestamp | 0 |  |  | null | 展开BOM时间 |
| 20 | fplanorderbillno | 来源订单编号 | varchar | 30 |  | √ | ' ' | 来源订单编号 |
| 21 | fbom | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 22 | fplanpreparedate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 23 | fproductyieldnum | 成品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 成品数量 |
| 24 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fattribute | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性 |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 27 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_proschedule_order |  | fbillno |
| 2 | pk_t_mrp_proschedule_order |  | fid |
