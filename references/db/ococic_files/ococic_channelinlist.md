# 渠道库存初始化-ococic_channelinlist

## 渠道库存初始化-主表 t_ococic_channelinlist

- **表名称：** 渠道库存初始化-主表
- **表名：** t_ococic_channelinlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fpackageno | 箱码 | varchar | 80 |  | √ | ' ' | 箱码 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | foutboxno | 外盒码 | varchar | 80 |  | √ | ' ' | 外盒码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 19 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 20 | fauxsnt | 辅序列号2 | varchar | 80 |  | √ | ' ' | 辅序列号2 |
| 21 | finchannelid | 入库渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 22 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 23 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 24 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 25 | fauxsno | 辅序列号1 | varchar | 80 |  | √ | ' ' | 辅序列号1 |
| 26 | finaction | 入库场景 | bpchar | 1 |  | √ | ' ' | 入库场景,枚举: A :初始化 B :普通入库 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | finvstatus | 入库状态 | bpchar | 1 |  | √ | 'A' | 入库状态,枚举: A :未入库 B :已入库 |
| 29 | finstocktime | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_chlinlist_billno |  | fbillno |
| 2 | pk_ococic_channelinlist |  | fid |
