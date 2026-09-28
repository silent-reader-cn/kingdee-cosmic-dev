# 货补流水异常备份-occba_suprecord_bak

## 货补流水异常备份-主表 t_occba_suprcd_bak

- **表名称：** 货补流水异常备份-主表
- **表名：** t_occba_suprcd_bak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentity | 来源单据标识 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fupdatetype | 更新事务 | bpchar | 1 |  | √ | ' ' | 更新事务,枚举: A :报销结算 D :订单占用 E :订单释放 C :订单审核扣减 B :余额调整 F :订单反审核释放 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fafterqty | 更新后可用数量 | numeric | 23 | 10 | √ | 0 | 更新后可用数量 |
| 10 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 11 | fsupplementno | 原货补池编码 | varchar | 80 |  | √ | ' ' | 原货补池编码 |
| 12 | fcreatedate | 流水发生时间 | timestamp | 0 |  |  | null | 流水发生时间 |
| 13 | fupdateqty | 变动数量 | numeric | 23 | 10 | √ | 0 | 变动数量 |
| 14 | fbeforeqty | 更新前可用数量 | numeric | 23 | 10 | √ | 0 | 更新前可用数量 |
| 15 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 16 | fsourcebillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_suprcd_bak |  | fid |
| 2 | idx_occba_suprcdbak_sid |  | fsupplementno |
