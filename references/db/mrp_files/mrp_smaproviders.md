# 缺料供应单据-mrp_smaproviders

## 缺料供应单据-主表 t_mrp_smaproviders

- **表名称：** 缺料供应单据-主表
- **表名：** t_mrp_smaproviders

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistock | 是否库存数据 | bpchar | 1 |  | √ | '0' | 是否库存数据 |
| 3 | fbasecansupplyqty | 基本可用供应 | numeric | 23 | 10 | √ | 0 | 基本可用供应 |
| 4 | fmaterialid | 物料(主档) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 6 | flocation | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 7 | fbillentryseq | 供应单据分录行号 | int4 | 32 |  | √ | 0 | 供应单据分录行号 |
| 8 | fbilldate | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 9 | fcalculateid | 本次计算id | varchar | 50 |  | √ | ' ' | 本次计算id |
| 10 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fsupplyorgunitid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 13 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 14 | fprojectnumber | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fbasereservedqty | 基本预留数量 | numeric | 23 | 10 | √ | 0 | 基本预留数量 |
| 16 | fsmaid | 缺料分析单据id | int8 | 64 |  | √ | 0 | 缺料分析单据id |
| 17 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 18 | fsupplypriority | 供应优先级 | int4 | 32 |  | √ | 0 | 供应优先级 |
| 19 | fauxprop | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fsupplyentityid | 供应单据实体标识 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 21 | fowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbillnumber | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 23 | fbaseallreserveqty | 基本综合预留数量 | numeric | 23 | 10 | √ | 0 | 基本综合预留数量 |
| 24 | fbillentryid | 供应单据分录ID | int8 | 64 |  | √ | 0 | 供应单据分录ID |
| 25 | fbillid | 供应单据ID | int8 | 64 |  | √ | 0 | 供应单据ID |
| 26 | fbaseqty | 基本分配数量 | numeric | 23 | 10 | √ | 0 | 基本分配数量 |
| 27 | fbaseallqty | 基本单位总供给数量 | numeric | 23 | 10 | √ | 0 | 基本单位总供给数量 |
| 28 | fbilltype | 供应单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_smaproviders |  | fmaterialid,fsupplypriority |
| 2 | pk_mrp_smaproviders |  | fid |
