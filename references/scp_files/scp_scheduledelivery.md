# 交货计划-scp_scheduledelivery

## 交货计划-主表 t_pur_deliveryschedule

- **表名称：** 交货计划-主表
- **表名：** t_pur_deliveryschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplierlinkid | 业务员 | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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

## 交货计划分录-子表 t_pur_deliveryschentry

- **表名称：** 交货计划分录-子表
- **表名：** t_pur_deliveryschentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | frelateoutstockbasicqty | 关联发货基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货基本数量 |
| 5 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | frowcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | festimateddeliverydate | 预计发货日期 | timestamp | 0 |  |  | null | 预计发货日期 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 12 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 13 | fsrcentryseq | 来源单据分录行号 | int8 | 64 |  | √ | 0 | 来源单据分录行号 |
| 14 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 16 | fsupplierremark | 供应商反馈 | varchar | 512 |  | √ | ' ' | 供应商反馈 |
| 17 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 18 | frowcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 20 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fpromisedate | 确认到货日期 | timestamp | 0 |  |  | null | 确认到货日期 |
| 22 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fispresent | fispresent | bpchar | 1 |  | √ | ' ' |  |
| 25 | fsumoutstockbaseqty | 已发货基本数量 | numeric | 23 | 10 | √ | 0 | 已发货基本数量 |
| 26 | fdeliverydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 27 | frelateoutstockqty | 关联发货数量 | numeric | 23 | 10 | √ | 0 | 关联发货数量 |
| 28 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 29 | fismeets | 是否满足 | bpchar | 1 |  | √ | ' ' | 是否满足 |
| 30 | fpromisestatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :待重新确认 D :待采购方确认 |
| 31 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 32 | fsumoutstockqty | 已发货数量 | numeric | 23 | 10 | √ | 0 | 已发货数量 |
| 33 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 34 | frowmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 35 | fpromiseqty | 确认数量 | numeric | 23 | 10 | √ | 0 | 确认数量 |
| 36 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 37 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 40 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 41 | fpromisebasicqty | 确认基本数量 | numeric | 23 | 10 | √ | 0 | 确认基本数量 |

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
