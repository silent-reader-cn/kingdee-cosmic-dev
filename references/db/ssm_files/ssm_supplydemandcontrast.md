# 供需即时对应-ssm_supplydemandcontrast

## 单据体-子表 t_ssm_supplyentry

- **表名称：** 单据体-子表
- **表名：** t_ssm_supplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fordersupplybaseqty | 供应基本数量 | numeric | 23 | 10 | √ | 0 | 供应基本数量 |
| 2 | fqtytocomplete | 预计完工数量 | numeric | 23 | 10 | √ | 0 | 预计完工数量 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 5 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsupplybillno | 供应单据编号 | varchar | 30 |  | √ | ' ' | 供应单据编号 |
| 7 | forderbaseqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 8 | fstorageqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 9 | fsupplybilltype | 供应来源 | varchar | 50 |  | √ | ' ' | 供应来源,枚举: 0 :重复生产工单 1 :即时库存 3 :生产工单 4 :委外工单 5 :采购订单 6 :滚动采购交货计划 7 :滚动采购预测计划 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fstarttime | 计划开工时间 | int4 | 32 |  | √ | '-1' | 计划开工时间 |
| 12 | fshift | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 13 | fbaseqtytocomplete | 预计完工基本数量 | numeric | 23 | 10 | √ | 0 | 预计完工基本数量 |
| 14 | fenddate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 15 | fyieldpercent | 成品率% | numeric | 23 | 2 | √ | 0 | 成品率% |
| 16 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 17 | fordersupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 18 | fprdunit | 业务单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fstartdate | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 20 | forderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 21 | fstoragebaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 22 | fendtime | 计划完工时间 | int4 | 32 |  | √ | '-1' | 计划完工时间 |
| 23 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_supplyentry |  | fentryid |
| 2 | idx_ssm_supplyentry_fk |  | fid |

---

## 供需即时对应-主表 t_ssm_supplydemandcontras

- **表名称：** 供需即时对应-主表
- **表名：** t_ssm_supplydemandcontras

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplybaseqty | 供应总数基本数量 | numeric | 23 | 10 | √ | 0 | 供应总数基本数量 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fneedqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 5 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fneeddate | 客户要货日期 | timestamp | 0 |  |  | null | 客户要货日期 |
| 9 | forigin | 需求类型 | varchar | 50 |  | √ | ' ' | 需求类型,枚举: 0 :预测 1 :交货 2 :发货 3 :合并 |
| 10 | fcompletedbaseqty | 已完成基本数量 | numeric | 23 | 10 | √ | 0 | 已完成基本数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 13 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 16 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fneedbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 18 | fneedtime | 客户要货时间 | int4 | 32 |  | √ | '-1' | 客户要货时间 |
| 19 | fplandeliverydate | 计划发货日期 | timestamp | 0 |  |  | null | 计划发货日期 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsupplyqty | 供应总数 | numeric | 23 | 10 | √ | 0 | 供应总数 |
| 22 | fduedate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 23 | fdemandtype | DemandTypeEnum | varchar | 50 |  | √ | ' ' | DemandTypeEnum,枚举: 0 :--标准销售订单 1 :--委托代销订单 2 :--标准销售计划协议 3 :--委托代销计划协议 4 :采购独立需求 5 :重复生产用料清单 6 :销售订单 7 :销售计划协议 8 :生产工单用料清单 9 :委外工单用料清单 |
| 24 | freleaseno | 发放号 | varchar | 50 |  | √ | ' ' | 发放号 |
| 25 | fcompletedqty | 已完成数量 | numeric | 23 | 10 | √ | 0 | 已完成数量 |
| 26 | freference | 参考值 | varchar | 50 |  | √ | ' ' | 参考值 |
| 27 | fbaseqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 28 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | funit | 业务单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fbilltype | 需求来源 | varchar | 50 |  | √ | ' ' | 需求来源 |
| 31 | fsupplystatus | 供应状态 | varchar | 50 |  | √ | ' ' | 供应状态,枚举: 0 :供应满足 1 :供应未满足 2 :供应剩余 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_supplydemandcontras_m0 |  | fbillno |
| 2 | pk_ssm_supplydemandcontras |  | fid |
