# 渠道即时库存-ococic_channelinvacc

## 渠道即时库存-主表 t_ococic_channelinvacc

- **表名称：** 渠道即时库存-主表
- **表名：** t_ococic_channelinvacc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelstockid | 渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 3 | fupdatekey | 库存更新维度 | varchar | 512 |  | √ | ' ' | 库存更新维度 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 7 | fstockqty | 库存单位数量 | numeric | 23 | 10 | √ | 0 | 库存单位数量 |
| 8 | fsalechannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexceptionhandling | 异常处理 | bpchar | 1 |  | √ | ' ' | 异常处理,枚举: A :库存调减 B :库存调增 |
| 13 | fabnormalstatus | 异常状态 | bpchar | 1 |  | √ | ' ' | 异常状态,枚举: A :正常 B :异常 |
| 14 | fchannelstockstatusid | 渠道库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 15 | feffectivedate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 16 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 17 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 18 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fassistunitid | 主辅单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | flotnum | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 23 | fstockunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fchannellocationid | 渠道仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 28 | fsaleorgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 30 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 31 | flotid | 批号Id | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 32 | fchannelstocktypeid | 渠道库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 33 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 34 | fassistqty | 主辅助单位数量 | numeric | 23 | 10 | √ | 0 | 主辅助单位数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_channelinvacc_cis |  | fchannelid,fitemid,fsaleorgid |
| 2 | idx_ococic_channelinvacc_lc |  | flotnum,fchannelid |
| 3 | pk_ococic_channelinvacc |  | fid |
| 4 | idx_ococic_channelinvacc_ukey |  | fupdatekey |
