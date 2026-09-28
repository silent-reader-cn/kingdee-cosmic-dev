# 批号移动轨迹-bd_lotmovetrack

## 批号移动轨迹-主表 t_bd_lotmovetrack

- **表名称：** 批号移动轨迹-主表
- **表名：** t_bd_lotmovetrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flotidfield | 单据批号字段 | varchar | 100 |  | √ | ' ' | 单据批号字段 |
| 3 | fsrcwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 4 | fdescustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fbillentrytype | 单据分录类型 | varchar | 50 |  | √ | ' ' | 单据分录类型 |
| 6 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 7 | fdesbizorgid | 出库业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrcbizorgid | 入库业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 11 | fsrclocationid | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fsrcdeptid | 入库部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fdesdeptid | 出库部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fsrclotid | 原批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 17 | flotbillconfid | 批号单据规则 | int8 | 64 |  | √ | 0 | 批号单据配置 msmod_lotbillconf |
| 18 | fdeswarehouseid | 出库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 19 | fdseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 20 | fsrcsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fmovedirect | 移动方向 | varchar | 5 |  | √ | ' ' | 移动方向,枚举: A :来源 B :去向 |
| 22 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 23 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 24 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 25 | fbillentityid | 单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 26 | fdeslocationid | 出库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 27 | fsrclotnum | 原批号 | varchar | 100 |  | √ | ' ' | 原批号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_lotmovetrack_pkey |  | fid |
| 2 | idx_bd_lotmovetrack_billid |  | fbillid |
| 3 | idx_bd_lotmovetrack_lotid |  | flotid |
