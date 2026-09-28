# 可销量结果表操作日志-ococic_allotresultlog

## 可销量结果表操作日志-主表 t_ococic_allotresultlog

- **表名称：** 可销量结果表操作日志-主表
- **表名：** t_ococic_allotresultlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fupdatetype | 更新方式 | bpchar | 1 |  | √ | ' ' | 更新方式,枚举: A :累加更新可销量 B :覆盖更新可销量 C :占用可销量 D :释放可销量 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fsubentryid | 子分录主键 | int8 | 64 |  | √ | 0 | 子分录主键 |
| 7 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 8 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbillid | 单据主键 | int8 | 64 |  | √ | 0 | 单据主键 |
| 11 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 12 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fbaseqty | 操作数量(基本单位) | numeric | 23 | 10 | √ | 0 | 操作数量(基本单位) |
| 14 | fbillentity | 单据 | varchar | 80 |  | √ | ' ' | 单据,枚举: ococic_allotbill :可销量分配单 ocbsoc_saleorder :要货订单 |
| 15 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fentryid | 分录主键 | int8 | 64 |  | √ | 0 | 分录主键 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fallotresultid | 可销量分配表主键 | int8 | 64 |  | √ | 0 | 可销量分配表主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_allotresultlog_bill |  | fbillid,fentryid,fsubentryid |
| 2 | pk_ococic_allotresultlog |  | fid |
