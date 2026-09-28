# 订单拣货-ocbsoc_deliveryorder

## 拣货明细信息-子表 t_ocbsoc_deliveryentry_o

- **表名称：** 拣货明细信息-子表
- **表名：** t_ocbsoc_deliveryentry_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 价格合计 | numeric | 23 | 10 | √ | 0 | 价格合计 |
| 3 | fapprovebaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 4 | forderbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 5 | forderdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | forderid | 订单Id | int8 | 64 |  | √ | 0 | 订单Id |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fapproveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 13 | forderdetailid | 订单交付行Id | int8 | 64 |  | √ | 0 | 订单交付行Id |
| 14 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 15 | forderentryid | 订单分录Id | int8 | 64 |  | √ | 0 | 订单分录Id |
| 16 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 17 | fdeliveryqty | 拣货数量 | numeric | 23 | 10 | √ | 0 | 拣货数量 |
| 18 | forderstatus | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货 E :已发货 F :已完成 |
| 19 | fiscontrolorderqty | 数量可调配 | bpchar | 1 |  | √ | '0' | 数量可调配 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fdeliverybaseqty | 拣货基本数量 | numeric | 23 | 10 | √ | 0 | 拣货基本数量 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_deliveryentry_o |  | fentryid |
| 2 | idx_ocbsoc_delientry_o_fid |  | fid |
| 3 | idx_ocbsoc_delientry_o_edid |  | forderid,forderentryid,forderdetailid |
| 4 | idx_ocbsoc_delientry_o_obno |  | forderbillno |

---

## 拣货汇总信息-子表 t_ocbsoc_deliveryentry

- **表名称：** 拣货汇总信息-子表
- **表名：** t_ocbsoc_deliveryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovebaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapproveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 10 | fgroupkey | 汇总key值 | varchar | 500 |  | √ | ' ' | 汇总key值 |
| 11 | fdeliveryqty | 拣货数量 | numeric | 23 | 10 | √ | 0 | 拣货数量 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fdeliverybaseqty | 拣货基本数量 | numeric | 23 | 10 | √ | 0 | 拣货基本数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_deliveryentry |  | fentryid |
| 2 | idx_ocbsoc_deliveryentry_fid |  | fid |

---

## 订单拣货-主表 t_ocbsoc_deliveryorder

- **表名称：** 订单拣货-主表
- **表名：** t_ocbsoc_deliveryorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已拣货 |
| 4 | fprintstatus | 打印状态 | bpchar | 1 |  | √ | '0' | 打印状态,枚举: 0 :未打印 1 :已打印 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fselecttype | 拣货方式 | varchar | 10 |  | √ | '1' | 拣货方式,枚举: 1 :车辆 2 :部门 |
| 7 | fdeliverydate | 配送日期 | timestamp | 0 |  |  | null | 配送日期 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | faudittime | 拣货时间 | timestamp | 0 |  |  | null | 拣货时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fenddate | 订单拣选范围.结束 | timestamp | 0 |  |  | null | 订单拣选范围.结束 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fprintcount | 打印次数 | int4 | 32 |  | √ | 0 | 打印次数 |
| 15 | fstartdate | 订单拣选范围.开始 | timestamp | 0 |  |  | null | 订单拣选范围.开始 |
| 16 | fdeliverymanid | 配送员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fprintuserid | 打印人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fprintdate | 打印时间 | timestamp | 0 |  |  | null | 打印时间 |
| 19 | fdeliveryway | 配送方式 | varchar | 20 |  | √ | ' ' | 配送方式,枚举: A :物流发货 B :车辆配送 C :客户自提 |
| 20 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fvehicleid | 配送车辆 | int8 | 64 |  | √ | 0 | [车辆信息 ocdbd_vehicle](../ococic_files/ocdbd_vehicle.md) |
| 23 | fauditorid | 拣货人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_deliveryorder_bno |  | fbillno |
| 2 | pk_ocbsoc_deliveryorder |  | fid |
