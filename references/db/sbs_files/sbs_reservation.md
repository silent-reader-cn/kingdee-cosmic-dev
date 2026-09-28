# 预留记录（旧）-sbs_reservation

## 预留记录（旧）-主表 t_sbs_reservation

- **表名称：** 预留记录（旧）-主表
- **表名：** t_sbs_reservation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freservebaseqty | 预留基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留基本数量 |
| 3 | flotnumber | 批号编码 | varchar | 100 |  | √ | ' ' | 批号编码 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | freservetype | 预留类型 | bpchar | 1 |  | √ | '0' | 预留类型,枚举: 0 :单据类预留 1 :对象预留 |
| 6 | fdemandformid | 需求单据类型 | varchar | 100 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fsupplydate | 供给日期 | timestamp | 0 |  |  | null | 供给日期 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | freserveenddate | 预留到期日 | timestamp | 0 |  |  | null | 预留到期日 |
| 11 | fdemandunit2nd | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fdemandunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | freservereleaseqty | 基本预留释放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本预留释放数量 |
| 14 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 15 | fdemandunit3rd | fdemandunit3rd | int8 | 64 |  | √ | 0 |  |
| 16 | fdemandseq | 需求行号 | int8 | 64 |  | √ | 0 | 需求行号 |
| 17 | fsupplyentryid | 供应单内码 | varchar | 100 |  | √ | ' ' | 供应单内码 |
| 18 | fsupplystocklocid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 19 | fdemandid | 需求单内码 | varchar | 100 |  | √ | ' ' | 需求单内码 |
| 20 | fdemanbasedunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbillentry | 单据体标识 | varchar | 100 |  | √ | ' ' | 单据体标识 |
| 23 | freserveqty | 预留数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留数量 |
| 24 | freserveunit2ndqty | 预留辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留辅助数量 |
| 25 | freserveoperateid | 预留业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 26 | fsupplybillid | 供应单内码 | varchar | 100 |  | √ | ' ' | 供应单内码 |
| 27 | fdemandnumber | 需求单号 | varchar | 100 |  | √ | ' ' | 需求单号 |
| 28 | fdemandentryid | 需求单分录内码 | varchar | 100 |  | √ | ' ' | 需求单分录内码 |
| 29 | fsupplybillnumber | 供应单号 | varchar | 100 |  | √ | ' ' | 供应单号 |
| 30 | fdemandunit2ndqty | 需求辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求辅助数量 |
| 31 | fsupplystockid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 32 | freserveprctype | 预留产生类型 | bpchar | 1 |  | √ | '0' | 预留产生类型,枚举: 0 :自动预留 1 :手工预留 |
| 33 | freserveunit3rdqty | freserveunit3rdqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | freveredeptid | 预留部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | freservetime | 预留日期 | timestamp | 0 |  |  | null | 预留日期 |
| 36 | freservecustid | 预留客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 37 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求数量 |
| 38 | fdemandunit3rdqty | fdemandunit3rdqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fsupplylotid | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 41 | fsupplyformid | 供应单据类型 | varchar | 100 |  | √ | ' ' | 业务对象 bos_objecttype |
| 42 | fdemandbaseunitqty | 需求基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_rstn_fdmid |  | fdemandformid |
| 2 | t_sbs_reservation_pkey |  | fid |
