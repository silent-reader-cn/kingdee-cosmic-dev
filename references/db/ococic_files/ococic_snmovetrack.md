# 商品序列号移动轨迹-ococic_snmovetrack

## 商品序列号移动轨迹-主表 t_ocdbd_snmovetrack

- **表名称：** 商品序列号移动轨迹-主表
- **表名：** t_ocdbd_snmovetrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcchannelid | 来源渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 3 | fsrcchannellocationid | 来源渠道仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 4 | fsrcchannelstockid | 来源渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fsrcstocktypeid | 来源渠道库存类型 | int8 | 64 |  | √ | 0 | 渠道库存类型 ococic_stocktype |
| 7 | fsrcsaleorgid | 来源销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fsrcsalechannelid | 来源销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fsrckeepertype | 来源保管者类型 | varchar | 36 |  | √ | ' ' | 来源保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 12 | fdestchannelid | 去向渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fdestsaleorgid | 去向销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsnmainfileid | 序列号主档 | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |
| 15 | fsrcownerid | 来源货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fsrckeeperid | 来源保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fdestchannellocationid | 去向渠道仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 20 | fsrcstockstatusid | 来源渠道库存状态 | int8 | 64 |  | √ | 0 | 渠道库存状态 ococic_stockstatus |
| 21 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 22 | fmovedirect | 移动方向 | bpchar | 1 |  | √ | 'A' | 移动方向,枚举: A :来源 B :去向 |
| 23 | fsrcownertype | 来源货主类型 | varchar | 36 |  | √ | ' ' | 来源货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 24 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 25 | fmovedate | 移动日期 | timestamp | 0 |  |  | null | 移动日期 |
| 26 | fdestchannelstockid | 去向渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 27 | fdestsalechannelid | 去向销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 28 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 29 | fbillentityid | 单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_snmovetrack_sn |  | fsnmainfileid |
| 2 | pk_ocdbd_snmovetrack |  | fid |
| 3 | idx_ocdbd_snmovetrack_beid |  | fbillid,fbillentryid |
