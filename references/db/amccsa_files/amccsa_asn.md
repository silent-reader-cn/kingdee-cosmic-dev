# 提前发运通知单-amccsa_asn

## 提前发运通知单-反写记录表 t_amccsa_asn_wb

- **表名称：** 提前发运通知单-反写记录表
- **表名：** t_amccsa_asn_wb

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
| 1 | pk_amccsa_asn_wb |  | fentryid |
| 2 | idx_amccsa_asn_wb_fk |  | fid |

---

## 需求明细-子表 t_amccsa_asndetailsub

- **表名称：** 需求明细-子表
- **表名：** t_amccsa_asndetailsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdeliveryaddress | fdeliveryaddress | varchar | 255 |  |  | null |  |
| 2 | fdeliofsaleqty | 发货数量 | numeric | 23 | 10 | √ | 0 | 发货数量 |
| 3 | fdemandreference | 需求参考值 | varchar | 50 |  | √ | ' ' | 需求参考值 |
| 4 | fdeliofbaseqty | 发货基本数量 | numeric | 23 | 10 | √ | 0 | 发货基本数量 |
| 5 | flotnumber | flotnumber | varchar | 50 |  | √ | ' ' |  |
| 6 | fdemandtime | 需求时间 | int8 | 64 |  | √ | 0 | 需求时间 |
| 7 | fsaleunit | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fauxiliaryproperties | fauxiliaryproperties | int8 | 64 |  | √ | 0 |  |
| 10 | fshipdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 11 | fdeliverydate | 到货日期 | timestamp | 0 |  |  | null | 到货日期 |
| 12 | fmaterielid | fmaterielid | int8 | 64 |  | √ | 0 |  |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 15 | fshiptime | 发货时间 | int8 | 64 |  | √ | 0 | 发货时间 |
| 16 | fdeliverytime | 到货时间 | int8 | 64 |  | √ | 0 | 到货时间 |
| 17 | freceivecontactid | freceivecontactid | int8 | 64 |  | √ | 0 |  |
| 18 | fdateunit | 日期单位 | varchar | 8 |  | √ | ' ' | 日期单位,枚举: D :日 W :周 M :月 Q :季 Y :年 |
| 19 | fexpirydate | fexpirydate | timestamp | 0 |  |  | null |  |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 22 | fdeliveryway | fdeliveryway | int8 | 64 |  | √ | 0 |  |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | freceiveaddress | freceiveaddress | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_asnsub_entryid |  | fentryid |
| 2 | pk_t_amccsa_asndetailsub |  | fdetailid |

---

## 出库明细-子表 t_amccsa_asnstocksub

- **表名称：** 出库明细-子表
- **表名：** t_amccsa_asnstocksub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fdeliveryaddress | 交货地点 | varchar | 255 |  |  | null | 交货地点 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fauxiliaryproperties | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | freceivecontactid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 9 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 10 | fsaloutentryid | 出库单行id | int8 | 64 |  | √ | 0 | 出库单行id |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 13 | fdeliveryway | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | freceiveaddress | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_asnstocksub |  | fdetailid |
| 2 | idx_t_amccsa_asnssub_entryid |  | fentryid |

---

## 出库明细-多语言表 t_amccsa_asnstocksub_l

- **表名称：** 出库明细-多语言表
- **表名：** t_amccsa_asnstocksub_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | freceiveaddress | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_asnss_l_fid |  | fdetailid |
| 2 | pk_t_amccsa_asnstocksub_l |  | fpkid |

---

## 提前发运通知单-关联追踪表 t_amccsa_asn_tc

- **表名称：** 提前发运通知单-关联追踪表
- **表名：** t_amccsa_asn_tc

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
| 1 | pk_amccsa_asn_tc |  | fid |
| 2 | idx_amccsa_asn_tc_tbill |  | ftbillid |
| 3 | idx_amccsa_asn_tc_tid |  | ftid |

---

## 提前发运通知单-主表 t_amccsa_asn

- **表名称：** 提前发运通知单-主表
- **表名：** t_amccsa_asn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexcepteddeliverydate | 预计收货日期 | timestamp | 0 |  |  | null | 预计收货日期 |
| 9 | foutdate | 出库日期 | timestamp | 0 |  |  | null | 出库日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsendtime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 12 | fshiptoid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 13 | fsendstatus | 发送状态 | bpchar | 1 |  | √ | ' ' | 发送状态,枚举: A :未发送 B :已发送 C :发送失败 D :发送成功 E :已提取 |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fsaleoutbillid | 销售出库单 | int8 | 64 |  | √ | 0 | 销售出库单 im_saloutbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_asn |  | fid |
| 2 | idx_t_amccsa_asn |  | fsaleoutbillid |

---

## 关联子实体-子表 t_amccsa_asndetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_amccsa_asndetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_amccsa_asndetail_lk_fk |  | fentryid |
| 2 | pk_amccsa_asndetail_lk |  | fpkid |

---

## 协议物料信息-子表 t_amccsa_asndetail

- **表名称：** 协议物料信息-子表
- **表名：** t_amccsa_asndetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 4 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 7 | fsaleunit | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fauxiliaryproperties | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fcusreferencevalue | 客户参考值 | varchar | 50 |  | √ | ' ' | 客户参考值 |
| 11 | fcuspurchaseorder | 客户采购订单号 | varchar | 50 |  | √ | ' ' | 客户采购订单号 |
| 12 | faccumdeliqty | 累计发货数量 | numeric | 23 | 10 | √ | 0 | 累计发货数量 |
| 13 | fyearmodel | 年份型号 | varchar | 50 |  | √ | ' ' | 年份型号 |
| 14 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 15 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 16 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 17 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 18 | fcusmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 22 | freqschedulerelease | 发货计划发放号 | varchar | 50 |  | √ | ' ' | 发货计划发放号 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_asndetail |  | fentryid |
| 2 | idx_t_amccsa_asndetail_fid |  | fid |
