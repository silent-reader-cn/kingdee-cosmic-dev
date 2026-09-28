# 渠道批号主档移动轨迹-ococic_lotmovetrack

## 渠道批号主档移动轨迹-主表 t_ocdbd_lotmovetrack

- **表名称：** 渠道批号主档移动轨迹-主表
- **表名：** t_ocdbd_lotmovetrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fsrcchannelid | 来源渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fsrclocationid | 来源仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 5 | fdeschannelid | 去向渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fsrcwarehouseid | 来源仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 9 | fsrcsalechannelid | 来源销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fdeswarehouseid | 去向仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | fmovedirect | 移动方向 | bpchar | 1 |  | √ | ' ' | 移动方向,枚举: A :来源 B :去向 |
| 13 | flotid | 批号主档id | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 14 | fbillentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 15 | fmovedate | 移动日期 | timestamp | 0 |  |  | null | 移动日期 |
| 16 | fdestsalechannelid | 去向销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 17 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 18 | fbillentityid | 单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 19 | fdeslocationid | 去向仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_lotmovetrack_beid |  | fbillid,fbillentityid |
| 2 | pk_ocdbd_lotmovetrack |  | fid |
| 3 | idx_ocdbd_lotmovetrack_lid |  | flotid |
