# 渠道库存上报-ococic_inventoryreport

## 子单据体-子表 t_ococic_invenreport_sn

- **表名称：** 子单据体-子表
- **表名：** t_ococic_invenreport_sn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fserialid | 序列号ID | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 6 | fserialcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_invenreportsn_eid |  | fentryid |
| 2 | pk_ococic_invenreport_sn |  | fdetailid |

---

## 渠道库存上报-主表 t_ococic_inven_report

- **表名称：** 渠道库存上报-主表
- **表名：** t_ococic_inven_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | freportchannelid | 上报渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | freportdate | 上报日期 | timestamp | 0 |  |  | null | 上报日期 |
| 10 | finway | 入库方向 | bpchar | 1 |  | √ | '1' | 入库方向,枚举: 1 :正向 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_stockreport_no |  | fbillno |
| 2 | pk_ococic_inven_report |  | fid |

---

## 单据体-子表 t_ococic_invenreport_e

- **表名称：** 单据体-子表
- **表名：** t_ococic_invenreport_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 渠道库存状态 ococic_stockstatus |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 8 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | 渠道库存类型 ococic_stocktype |
| 9 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 10 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 |
| 11 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 12 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | flotnumberid | 批号ID | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 |
| 18 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 19 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 20 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 21 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 22 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fbaseqty | 基本计量单位数量 | numeric | 23 | 10 | √ | 0 | 基本计量单位数量 |
| 24 | fassistqty | 辅助计量单位数量 | numeric | 23 | 10 | √ | 0 | 辅助计量单位数量 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_invenreport_e |  | fentryid |
| 2 | idx_ococic_inven_reporte_fid |  | fid |
