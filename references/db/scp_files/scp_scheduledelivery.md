# 交货计划-scp_scheduledelivery

## 交货计划-主表 t_pur_deliveryschedule

- **表名称：** 交货计划-主表
- **表名：** t_pur_deliveryschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplierlinkid | 业务员 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 10 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 15 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 16 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_deliveryschedule |  | fid |
| 2 | idx_pur_ds_fsupplierid |  | fsupplierid |
| 3 | idx_pur_ds_fbillno |  | fbillno |
| 4 | idx_pur_ds_fbizpartnerid |  | fbilldate,fbizpartnerid |

---

## 交货计划-反写记录表 t_pur_deliveryschedule_wb

- **表名称：** 交货计划-反写记录表
- **表名：** t_pur_deliveryschedule_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_deliveryschedule_wb |  | fentryid |
| 2 | idx_pur_deliveryschedule_wb_fk |  | fid |

---

## 交货计划-多语言表 t_pur_deliveryschedule_l

- **表名称：** 交货计划-多语言表
- **表名：** t_pur_deliveryschedule_l

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
| 1 | idx_pur_deliveryschedule_l_fid |  | fid,flocaleid |
| 2 | pk_pur_deliveryschedule_l |  | fpkid |

---

## 交货计划-关联追踪表 t_pur_deliveryschedule_tc

- **表名称：** 交货计划-关联追踪表
- **表名：** t_pur_deliveryschedule_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_deliveryschedule_tc |  | fid |
| 2 | idx_pur_deliveryschedule_tc_tbill |  | ftbillid |
| 3 | idx_pur_deliveryschedule_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pur_deliveryschentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_deliveryschentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpromiseqty | 确认数量_确认携带值 | numeric | 23 | 10 |  | null | 确认数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpromiseqty_old | 确认数量_原始携带值 | numeric | 23 | 10 |  | null | 确认数量_原始携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_deliveryschentry_lk_fk |  | fentryid |
| 2 | pk_pur_deliveryschentry_lk |  | fpkid |

---

## 交货计划分录-子表 t_pur_deliveryschentry

- **表名称：** 交货计划分录-子表
- **表名：** t_pur_deliveryschentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | frelateoutstockbasicqty | 关联发货基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货基本数量 |
| 5 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | frowcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | festimateddeliverydate | 预计发货日期 | timestamp | 0 |  |  | null | 预计发货日期 |
| 10 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 13 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fsrcentryseq | 来源单据分录行号 | int8 | 64 |  | √ | 0 | 来源单据分录行号 |
| 15 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 17 | fsupplierremark | 供应商反馈 | varchar | 512 |  | √ | ' ' | 供应商反馈 |
| 18 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 19 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 20 | frowcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fpromisedate | 确认到货日期 | timestamp | 0 |  |  | null | 确认到货日期 |
| 24 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fispresent | fispresent | bpchar | 1 |  | √ | ' ' |  |
| 27 | fsumoutstockbaseqty | 已发货基本数量 | numeric | 23 | 10 | √ | 0 | 已发货基本数量 |
| 28 | fdeliverydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 29 | frelateoutstockqty | 关联发货数量 | numeric | 23 | 10 | √ | 0 | 关联发货数量 |
| 30 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fismeets | 是否满足 | bpchar | 1 |  | √ | ' ' | 是否满足 |
| 32 | fpromisestatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :待重新确认 D :待采购方确认 |
| 33 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 34 | fsumoutstockqty | 已发货数量 | numeric | 23 | 10 | √ | 0 | 已发货数量 |
| 35 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 36 | frowmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 37 | fpromiseqty | 确认数量 | numeric | 23 | 10 | √ | 0 | 确认数量 |
| 38 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 39 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 40 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 41 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 44 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 45 | fpromisebasicqty | 确认基本数量 | numeric | 23 | 10 | √ | 0 | 确认基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_deliveryschentry |  | fentryid |
| 2 | idx_pur_dsentry_fmaterialid |  | fmaterialid |
| 3 | idx_pur_dsrentry_fid_fseq |  | fid,fseq |
