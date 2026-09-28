# 需求供应分配记录-mrp_smasupplyallot

## 需求供应分配记录-主表 t_mrp_smasupplyallot

- **表名称：** 需求供应分配记录-主表
- **表名：** t_mrp_smasupplyallot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistock | 是否库存数据 | bpchar | 1 |  | √ | '0' | 是否库存数据 |
| 3 | fbasecansupplyqty | 当前基本供应 | numeric | 23 | 10 | √ | 0 | 当前基本供应 |
| 4 | fcalseq | 处理顺序 | int4 | 32 |  | √ | 0 | 处理顺序 |
| 5 | forderbillno | 订单编码 | varchar | 50 |  | √ | ' ' | 订单编码 |
| 6 | fmaterialid | 物料(主档) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fpriorityweight | 供应权重 | int4 | 32 |  | √ | 0 | 供应权重 |
| 9 | flocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | fbillentryseq | 供应单据分录行号 | int8 | 64 |  | √ | 0 | 供应单据分录行号 |
| 11 | fsubentryid | 子项明细行id | int8 | 64 |  | √ | 0 | 子项明细行id |
| 12 | fcalculateid | 本次计算id | varchar | 50 |  | √ | ' ' | 本次计算id |
| 13 | fbilldate | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 14 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fsupplyorgunitid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fprovidersid | 供应单据id | int8 | 64 |  | √ | 0 | 供应单据id |
| 17 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 18 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 19 | fsubitembillno | 子项单据编码 | varchar | 50 |  | √ | ' ' | 子项单据编码 |
| 20 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 21 | forderseq | 订单行号 | varchar | 50 |  | √ | ' ' | 订单行号 |
| 22 | fprojectnumber | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fbasereservedqty | 当前预留数量 | numeric | 23 | 10 | √ | 0 | 当前预留数量 |
| 24 | fsmaid | 缺料分析单据id | int8 | 64 |  | √ | 0 | 缺料分析单据id |
| 25 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | fsupplypriority | 供应优先级 | int8 | 64 |  | √ | 0 | 供应优先级 |
| 27 | fauxprop | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | fsubitemseq | 子项单据行号 | int4 | 32 |  | √ | 0 | 子项单据行号 |
| 29 | fsupplyentityid | 供应单据实体标识 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 30 | fowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fbillnumber | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 32 | fbaseallreserveqty | 基本综合预留数量 | numeric | 23 | 10 | √ | 0 | 基本综合预留数量 |
| 33 | fbillentryid | 供应单据分录ID | int8 | 64 |  | √ | 0 | 供应单据分录ID |
| 34 | fbillid | 供应单据ID | int8 | 64 |  | √ | 0 | 供应单据ID |
| 35 | fbaseqty | 基本分配数量 | numeric | 23 | 10 | √ | 0 | 基本分配数量 |
| 36 | fbaseallqty | 基本单位总供给数量 | numeric | 23 | 10 | √ | 0 | 基本单位总供给数量 |
| 37 | fbilltype | 供应单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 38 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smasupplyallot |  | fid |
| 2 | idx_mrp_smasupplyallot |  | forderbillno,fmaterialid |
