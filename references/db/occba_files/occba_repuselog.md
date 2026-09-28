# 货补使用记录-occba_repuselog

## 货补使用记录-主表 t_occba_repuselog

- **表名称：** 货补使用记录-主表
- **表名：** t_occba_repuselog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frepsaleorgid | 货补销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fusebilldepartmentid | 使用单据部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fyearid | 年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 8 | freppoolid | 货补池 | int8 | 64 |  | √ | 0 | [货补池表 occba_replenishment](../occba_files/occba_replenishment.md) |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | frepdepartmentid | 货补所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | frepuseunitid | 货补使用单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | frepsettleorgid | 货补结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbillno | 使用单据编号 | varchar | 80 |  | √ | ' ' | 使用单据编号 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | frepuseamount | 货补使用金额 | numeric | 23 | 10 | √ | 0 | 货补使用金额 |
| 16 | frepsettlecustomerid | 货补结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fitemclassid | 产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 18 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 19 | frepsettlechannelid | 货补结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 20 | frepaccountid | 货补账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 21 | fbillentryid | 使用单据分录ID | int8 | 64 |  | √ | 0 | 使用单据分录ID |
| 22 | fusebillid | 使用单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 23 | fbillid | 使用单据ID | int8 | 64 |  | √ | 0 | 使用单据ID |
| 24 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 25 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | frepuseqty | 货补使用数量 | numeric | 23 | 10 | √ | 0 | 货补使用数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_repuselog_item |  | fitemid |
| 2 | pk_t_occba_repuselog |  | fid |
