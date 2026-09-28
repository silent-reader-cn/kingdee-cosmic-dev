# 用料发货通知-scp_moduledelivery

## 用料发货通知-多语言表 t_pur_moduledelivery_l

- **表名称：** 用料发货通知-多语言表
- **表名：** t_pur_moduledelivery_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_moduledelivery_l |  | fpkid |
| 2 | idx_pur_moduledelivery_l_fid |  | fid,flocaleid |

---

## 分录信息-子表 t_pur_moduledeliveryentry

- **表名称：** 分录信息-子表
- **表名：** t_pur_moduledeliveryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelrecieptqty | 关联确认收货数量 | numeric | 23 | 10 | √ | 0 | 关联确认收货数量 |
| 3 | fcomrecieptqty | 已确认收货数量 | numeric | 23 | 10 | √ | 0 | 已确认收货数量 |
| 4 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 5 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 6 | fsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 7 | fmainbillentryseq | 核心单据分录序号 | varchar | 20 |  | √ | ' ' | 核心单据分录序号 |
| 8 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 10 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 13 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 15 | fsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 16 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 17 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 19 | freclocationid | 收货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fsumrecieptbaseqty | 关联确认收货基本数量 | numeric | 23 | 10 | √ | 0 | 关联确认收货基本数量 |
| 22 | fcomrecieptbaseqty | 已确认收货基本数量 | numeric | 23 | 10 | √ | 0 | 已确认收货基本数量 |
| 23 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 24 | fpurorgid | 发出方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | freldeliverqty | 关联确认发货数量 | numeric | 23 | 10 | √ | 0 | 关联确认发货数量 |
| 26 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 28 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fwarehouseid | 发出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 32 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 33 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 34 | freldeliverbaseqty | 关联确认发货基本数量 | numeric | 23 | 10 | √ | 0 | 关联确认发货基本数量 |
| 35 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 36 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 37 | frecwarehouselocid | 收货仓位 | varchar | 50 |  | √ | '0' | 收货仓位 |
| 38 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 39 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 40 | frecwarehouse | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 44 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_moddeventry_fmatid |  | fmaterialid |
| 2 | idx_pur_moddeventry_fid_fseq |  | fid,fseq |
| 3 | pk_t_pur_moduledeliveryentry |  | fentryid |

---

## 用料发货通知-主表 t_pur_moduledelivery

- **表名称：** 用料发货通知-主表
- **表名：** t_pur_moduledelivery

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 7 | forgid | 调入方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | foutsupplierid | 调出供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fbizpartnerid | 调入供应商.商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 12 | fsupplierid | 调入供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 1 :材料直送 2 :直接调拨 3 :分步调拨 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | foutorgid | 调出方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fpersonid | 采购方联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 20 | foutbizpartnerid | 调出供应商.商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 21 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_moduledel_fbilldate |  | fbilldate |
| 2 | pk_t_pur_moduledelivery |  | fid |
| 3 | idx_pur_moduledelivery_fbillno |  | fbillno |
| 4 | idx_pur_moduledelivery_fbizid |  | fbizpartnerid |
