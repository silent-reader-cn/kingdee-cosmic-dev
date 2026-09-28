# ASN数据记录-amccsa_asndata

## ASN数据记录-主表 t_amccsa_asndata

- **表名称：** ASN数据记录-主表
- **表名：** t_amccsa_asndata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsaleunit | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fauxiliaryproperties | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fcusreferencevalue | 客户参考值 | varchar | 50 |  | √ | ' ' | 客户参考值 |
| 9 | fcuspurchaseorder | 客户采购订单号 | varchar | 50 |  | √ | ' ' | 客户采购订单号 |
| 10 | faccumdeliqty | 累计发货数量 | numeric | 23 | 10 | √ | 0 | 累计发货数量 |
| 11 | fyearmodel | 年份型号 | varchar | 50 |  | √ | ' ' | 年份型号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 15 | fsaloutbillid | 单据编号 | int8 | 64 |  | √ | 0 | 销售出库单 im_saloutbill |
| 16 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | freqschedulerelease | 滚动交货计划发放号 | varchar | 50 |  | √ | ' ' | 滚动交货计划发放号 |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_asndata |  | fid |
| 2 | idx_t_amccsa_asndata_join |  | fbillno,fmaterialcode,fauxiliaryproperties |

---

## 物料明细-多语言表 t_amccsa_asndatadetail_l

- **表名称：** 物料明细-多语言表
- **表名：** t_amccsa_asndatadetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | freceiveaddress | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_asndd_l_fid |  | fentryid |
| 2 | pk_t_amccsa_asndatadetail_l |  | fpkid |

---

## 物料明细-子表 t_amccsa_asndatadetail

- **表名称：** 物料明细-子表
- **表名：** t_amccsa_asndatadetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliveryaddress | 交货地点 | varchar | 255 |  |  | null | 交货地点 |
| 3 | fdeliofsaleqty | 发货数量 | numeric | 23 | 10 | √ | 0 | 发货数量 |
| 4 | fdemandreference | 需求参考值 | varchar | 50 |  | √ | ' ' | 需求参考值 |
| 5 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 6 | fsaleunit | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fauxiliaryproperties | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 12 | fdeliverytime | 到货时间 | int8 | 64 |  | √ | 0 | 到货时间 |
| 13 | fdeliveryway | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 14 | freqschdentryid | 交货计划行ID | int8 | 64 |  | √ | 0 | 交货计划行ID |
| 15 | fdeliofbaseqty | 发货数量 | numeric | 23 | 10 | √ | 0 | 发货数量 |
| 16 | fdemandtime | 需求时间 | int8 | 64 |  | √ | 0 | 需求时间 |
| 17 | fshipdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 18 | fdeliverydate | 到货日期 | timestamp | 0 |  |  | null | 到货日期 |
| 19 | fshiptime | 发货时间 | int8 | 64 |  | √ | 0 | 发货时间 |
| 20 | freceivecontactid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 21 | fdateunit | 日期单位 | varchar | 8 |  | √ | ' ' | 日期单位,枚举: D :日 W :周 M :月 Q :季 Y :年 |
| 22 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 23 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | freceiveaddress | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_asndatadetail |  | fentryid |
| 2 | idx_t_amccsa_asndatadetail_fid |  | fid |
