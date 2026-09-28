# 负卖占用记录-ococic_occupyrecords

## 负卖占用记录-主表 t_ococic_occupyrecords

- **表名称：** 负卖占用记录-主表
- **表名：** t_ococic_occupyrecords

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 占用需求数量 | numeric | 23 | 10 | √ | 0 | 占用需求数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fcreatetime | 占用日期 | timestamp | 0 |  |  | null | 占用日期 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 8 | fipaddress | 操作IP地址 | varchar | 80 |  | √ | ' ' | 操作IP地址 |
| 9 | factualqty | 实际占用数量 | numeric | 23 | 10 | √ | 0 | 实际占用数量 |
| 10 | fpolicyid | 负卖政策ID | int8 | 64 |  | √ | 0 | 负卖政策ID |
| 11 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 12 | fpolicyentryid | 负卖政策分录ID | int8 | 64 |  | √ | 0 | 负卖政策分录ID |
| 13 | fbrandid | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 14 | factualbaseqty | 实际占用基本数量 | numeric | 23 | 10 | √ | 0 | 实际占用基本数量 |
| 15 | ftype | 占用类型 | bpchar | 1 |  | √ | '0' | 占用类型,枚举: 0 :占货 1 :释放 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillentryid | 占用单据分录ID | int8 | 64 |  | √ | 0 | 占用单据分录ID |
| 18 | fbillid | 占用单据ID | int8 | 64 |  | √ | 0 | 占用单据ID |
| 19 | fbillentityid | 占用单据名称 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fbaseqty | 占用基本数量 | numeric | 23 | 10 | √ | 0 | 占用基本数量 |
| 22 | fbillno | 占用单据编码 | varchar | 80 |  | √ | ' ' | 占用单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_occupyrecords |  | fid |
| 2 | idx_ococic_occupyrec_no |  | fbillno |
