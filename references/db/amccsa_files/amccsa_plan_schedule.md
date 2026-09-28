# 客户预测计划-amccsa_plan_schedule

## 客户预测计划-主表 t_amccsa_planschedule

- **表名称：** 客户预测计划-主表
- **表名：** t_amccsa_planschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastreceivedqty | 上次接收数量 | numeric | 23 | 10 | √ | 0 | 上次接收数量 |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fenddatetime | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 5 | fauxiliaryproperties | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fcuspurchaseorder | 客户采购订单号 | varchar | 50 |  | √ | ' ' | 客户采购订单号 |
| 7 | fyearmodel | 年份型号 | varchar | 50 |  | √ | ' ' | 年份型号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsaleunit2 | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | flastdeliverydate | 上次发货日期 | timestamp | 0 |  |  | null | 上次发货日期 |
| 12 | flastreceiveddate | 上次接收日期 | timestamp | 0 |  |  | null | 上次接收日期 |
| 13 | frelease | 发放号 | varchar | 50 |  | √ | ' ' | 发放号 |
| 14 | fcusmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 15 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fnumentrytype | 数量录入方式 | varchar | 8 |  | √ | ' ' | 数量录入方式,枚举: 0 :累计值 1 :净值 |
| 18 | fsaleplanagreement | 销售计划协议 | varchar | 50 |  | √ | ' ' | 销售计划协议 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fprodorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsdpcode | SDP代码 | int8 | 64 |  | √ | 0 | [SDP代码 amccsa_sdpcode](../amccsa_files/amccsa_sdpcode.md) |
| 24 | fnumbertype | 数量类型 | varchar | 8 |  | √ | ' ' | 数量类型,枚举: 0 :累计值 1 :净值 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fbaseunit2 | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fcusreferencevalue | 客户参考值 | varchar | 50 |  | √ | ' ' | 客户参考值 |
| 28 | flastasn | 上次提前发运通知单 | varchar | 50 |  | √ | ' ' | 上次提前发运通知单 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 31 | fmaterielname | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 32 | fpriorcumdate | 前期累计截止日 | timestamp | 0 |  |  | null | 前期累计截止日 |
| 33 | fsoldto | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 34 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 35 | fisaccumulation | 累计制 | bpchar | 1 |  | √ | '0' | 累计制 |
| 36 | fstartdatetime | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 37 | fplandatetype | 计划日期类型 | varchar | 8 |  | √ | ' ' | 计划日期类型,枚举: 0 :以到货日期为准 1 :以发货日期为准 |
| 38 | fdaysdelivery | 运输天数 | int4 | 32 |  | √ | 0 | 运输天数 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fshipto | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 41 | fpriorcumreq | 前期累计需求量 | numeric | 23 | 10 | √ | 0 | 前期累计需求量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_ps_bill |  | fsaleplanagreement,flineno,frelease |
| 2 | pk_t_amccsa_planschedule |  | fid |

---

## 单据体-子表 t_amccsa_plansch_detail

- **表名称：** 单据体-子表
- **表名：** t_amccsa_plansch_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleqty | 销售数量 | numeric | 23 | 10 | √ | 0 | 销售数量 |
| 3 | fsaleunit | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdeliverydate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 6 | fdeliverydatetime | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 7 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdatefield | 到货日期 | timestamp | 0 |  |  | null | 到货日期 |
| 11 | fmodifydatefield | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |
| 12 | fdateunit | 日期单位 | varchar | 8 |  | √ | ' ' | 日期单位,枚举: D :日 W :周 M :月 Q :季 Y :年 |
| 13 | fshipdatetime | 到货日期 | timestamp | 0 |  |  | null | 到货日期 |
| 14 | freference | 参考值 | varchar | 50 |  | √ | ' ' | 参考值 |
| 15 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_ps_de_fid |  | fid |
| 2 | pk_t_amccsa_plansch_detail |  | fentryid |
