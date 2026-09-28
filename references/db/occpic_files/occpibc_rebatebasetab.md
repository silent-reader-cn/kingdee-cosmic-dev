# 返利数据底表-occpibc_rebatebasetab

## 返利数据底表-主表 t_occpic_rebatebasetab

- **表名称：** 返利数据底表-主表
- **表名：** t_occpic_rebatebasetab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | foperatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fata | 送达时间 | timestamp | 0 |  |  | null | 送达时间 |
| 6 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 7 | fproductnoid | 产品编码 | int8 | 64 |  | √ | 0 | [产品目录 bd_productsummary](../basedata_files/bd_productsummary.md) |
| 8 | frowupdatebatchid | 行更新批次ID | int8 | 64 |  | √ | 0 | 行更新批次ID |
| 9 | fsrcbillentryseq | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 10 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsignentityid | 签约主体 | int8 | 64 |  | √ | 0 | [合同主体 ocdbd_contparties](../ocdbd_files/ocdbd_contparties.md) |
| 12 | forderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 13 | fdeliveryamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 14 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fsrcbillentity | 来源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 18 | frepofficeid | frepofficeid | int8 | 64 |  | √ | 0 |  |
| 19 | fqtytype | 数量类型 | bpchar | 1 |  | √ | 'A' | 数量类型,枚举: A :sell through B :sell in C :sell out |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fserialno | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 25 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fcontractno | 合同/PO号 | varchar | 80 |  | √ | ' ' | 合同/PO号 |
| 29 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 30 | fpod | 来源单据日期 | timestamp | 0 |  |  | null | 来源单据日期 |
| 31 | fmainupdatebatchid | 主要更新批次ID | int8 | 64 |  | √ | 0 | 主要更新批次ID |
| 32 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsettlecustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 35 | flinetypeid | 商品属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 36 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fcustomerid | 返利渠道（作废） | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 38 | fbizdatatypeid | 业务数据类型 | int8 | 64 |  | √ | 0 | [业务数据类型 ocdbd_bizdatatype](../occpic_files/ocdbd_bizdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatebasetab_bid |  | fmainupdatebatchid,frowupdatebatchid |
| 2 | idx_occpic_rebatebasetab_sno |  | fserialno |
| 3 | idx_occpic_rebatebasetab_sid |  | fsrcbillid,fmainupdatebatchid |
| 4 | pk_occpic_rebatebasetab |  | fid |
