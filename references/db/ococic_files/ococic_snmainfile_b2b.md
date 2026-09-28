# 商品序列号-ococic_snmainfile_b2b

## 商品序列号-主表 t_ocdbd_snmainfile

- **表名称：** 商品序列号-主表
- **表名：** t_ocdbd_snmainfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelstockid | 渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fpackageno | 箱码 | varchar | 80 |  | √ | ' ' | 箱码 |
| 6 | fsalechannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | foutboxno | 外盒码 | varchar | 80 |  | √ | ' ' | 外盒码 |
| 9 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsnstatus | 序列号状态 | varchar | 1 |  | √ | '1' | 序列号状态,枚举: 1 :在途 2 :在库 3 :开单出库 4 :渠道出库 5 :退货出库 6 :废弃出库 |
| 12 | fcreatetype | 生成时机 | bpchar | 1 |  | √ | 'D' | 生成时机,枚举: D :自动生成 Y :预先生成 |
| 13 | fchannelstockstatusid | 渠道库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 14 | feffectivedate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 15 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 16 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 17 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | flotnum | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fchannellocationid | 渠道仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fscmsnid | ERP序列号ID | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 24 | flockstatus | 锁定状态 | bpchar | 1 |  | √ | '0' | 锁定状态,枚举: 0 :否 1 :是 |
| 25 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 26 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 28 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 29 | fauxsnt | 辅序列号2 | varchar | 80 |  | √ | ' ' | 辅序列号2 |
| 30 | flotid | 批号 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 31 | fchannelstocktypeid | 渠道库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 32 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 33 | fnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 34 | fauxsno | 辅序列号1 | varchar | 80 |  | √ | ' ' | 辅序列号1 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_snmainfile_lc |  | flotnum,fchannelid |
| 2 | idx_ocdbd_snmainfile_num |  | fnumber |
| 3 | idx_ocdbd_snmainfile_ao |  | fauxsno |
| 4 | pk_ocdbd_snmainfile |  | fid |
| 5 | idx_ocdbd_snmainfile_at |  | fauxsnt |
| 6 | idx_ocdbd_snmainfile_ics |  | fitemid,fchannelid,fsaleorgid |
