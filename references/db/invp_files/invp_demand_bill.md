# 库存计划需求单据-invp_demand_bill

## 库存计划需求单据-主表 t_invp_demand_bill

- **表名称：** 库存计划需求单据-主表
- **表名：** t_invp_demand_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrcbill | 需求单据 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 7 | flinenum | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 8 | fflexarea | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fbillentryid | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 10 | fdemandwarehouseid | 需求仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 11 | fbillid | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fsupplyorgid | fsupplyorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 需求单据编号 | varchar | 50 |  | √ | ' ' | 需求单据编号 |
| 15 | fplancalnum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_demand_bill |  | fid |
