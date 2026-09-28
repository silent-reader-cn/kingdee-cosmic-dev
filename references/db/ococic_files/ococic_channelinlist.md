# 渠道库存初始化-ococic_channelinlist

## 渠道库存初始化-主表 t_ococic_channelinlist

- **表名称：** 渠道库存初始化-主表
- **表名：** t_ococic_channelinlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fpackageno | 箱码 | varchar | 80 |  | √ | ' ' | 箱码 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | foutboxno | 外盒码 | varchar | 80 |  | √ | ' ' | 外盒码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fwarehouseid | 渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 19 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 20 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 21 | fauxsnt | 辅序列号2 | varchar | 80 |  | √ | ' ' | 辅序列号2 |
| 22 | flocationid | 渠道仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 23 | finchannelid | 入库渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 24 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 26 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 27 | fauxsno | 辅序列号1 | varchar | 80 |  | √ | ' ' | 辅序列号1 |
| 28 | finaction | 入库场景 | bpchar | 1 |  | √ | ' ' | 入库场景,枚举: A :初始化 B :普通入库 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | finvstatus | 入库状态 | bpchar | 1 |  | √ | 'A' | 入库状态,枚举: A :未入库 B :已入库 |
| 31 | finstocktime | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_chlinlist_billno |  | fbillno |
| 2 | pk_ococic_channelinlist |  | fid |
