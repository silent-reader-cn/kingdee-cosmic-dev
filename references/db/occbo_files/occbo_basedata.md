# 计划实际数-occbo_basedata

## 计划实际数-主表 t_occbo_basedata

- **表名称：** 计划实际数-主表
- **表名：** t_occbo_basedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsaleunitid | 销售计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | frowupdatebatchid | 行更新批次ID | int8 | 64 |  | √ | 0 | 行更新批次ID |
| 7 | fsrcbillentryseq | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatetype | 来源标识 | bpchar | 1 |  | √ | 'A' | 来源标识,枚举: A :取数规则生成 B :组合商品计算生成 |
| 11 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 15 | fsaleqty | 销售数量 | numeric | 23 | 10 | √ | 0 | 销售数量 |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fcombitemid | 组合商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 19 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 20 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 24 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 25 | fmonthname | 月份 | varchar | 80 |  | √ | ' ' | 月份 |
| 26 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 27 | fmainupdatebatchid | 主要更新批次ID | int8 | 64 |  | √ | 0 | 主要更新批次ID |
| 28 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 32 | fsrcbillentityid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_basedata_midci |  | fmonthname,fitemid,fdepartmentid,fchannelid,fispresent |
| 2 | pk_occbo_basedata |  | fid |
