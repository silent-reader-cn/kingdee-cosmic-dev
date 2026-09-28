# 委外调拨平台日志-om_transferplatformlog

## 委外调拨平台日志-主表 t_om_transferlog

- **表名称：** 委外调拨平台日志-主表
- **表名：** t_om_transferlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstockno | 委外用料清单编号 | varchar | 50 |  | √ | ' ' | 委外用料清单编号 |
| 3 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fproductid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fstockid | 用料清单id | int8 | 64 |  | √ | 0 | 用料清单id |
| 9 | fprdqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 10 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 11 | fprdbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | forderentryid | 委外工单分录f7 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_transferlog_sid |  | fstockid |
| 2 | pk_t_om_transferlog |  | fid |
| 3 | idx_om_transferlog_sno |  | fstockno |

---

## 分录-子表 t_om_transferlogentry

- **表名称：** 分录-子表
- **表名：** t_om_transferlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 3 | facttransbaseqty | 应调基本数量 | numeric | 23 | 10 | √ | 0 | 应调基本数量 |
| 4 | foldunissueqty | 变更前未领数量 | numeric | 23 | 10 | √ | 0 | 变更前未领数量 |
| 5 | fsupplierinvqty | 供应商库存分配数量 | numeric | 23 | 10 | √ | 0 | 供应商库存分配数量 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | freqtransbaseqty | 需调基本数量 | numeric | 23 | 10 | √ | 0 | 需调基本数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | facttransqty | 应调数量 | numeric | 23 | 10 | √ | 0 | 应调数量 |
| 10 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | frectransqty | 本次建议调拨数量 | numeric | 23 | 10 | √ | 0 | 本次建议调拨数量 |
| 12 | foldbaseunissueqty | 变更前未领基本数量 | numeric | 23 | 10 | √ | 0 | 变更前未领基本数量 |
| 13 | foldbasedemandqty | 变更前需求基本数量 | numeric | 23 | 10 | √ | 0 | 变更前需求基本数量 |
| 14 | fnewdemandqty | 变更后需求数量 | numeric | 23 | 10 | √ | 0 | 变更后需求数量 |
| 15 | factissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fchildbaseunitid | 子项基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | freqtransqty | 需调数量 | numeric | 23 | 10 | √ | 0 | 需调数量 |
| 20 | frectransbaseqty | 本次建议调拨基本数量 | numeric | 23 | 10 | √ | 0 | 本次建议调拨基本数量 |
| 21 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 22 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 23 | fnewuseratio | 变更后使用比例 | numeric | 23 | 10 | √ | 0 | 变更后使用比例 |
| 24 | folduseratio | 变更前使用比例 | numeric | 23 | 10 | √ | 0 | 变更前使用比例 |
| 25 | folddemandqty | 变更前需求数量 | numeric | 23 | 10 | √ | 0 | 变更前需求数量 |
| 26 | fstockentryid | 委外用料清单分录f7 | int8 | 64 |  | √ | 0 | [委外用料清单分录f7 om_mftstockf7](../om_files/om_mftstockf7.md) |
| 27 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 28 | fnewbasedemandqty | 变更后需求基本数量 | numeric | 23 | 10 | √ | 0 | 变更后需求基本数量 |
| 29 | fbaseactissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 30 | fnewbaseunissueqty | 变更后未领基本数量 | numeric | 23 | 10 | √ | 0 | 变更后未领基本数量 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fnewunissueqty | 变更后未领数量 | numeric | 23 | 10 | √ | 0 | 变更后未领数量 |
| 33 | fsupplierinvbaseqty | 供应商库存分配基本数量 | numeric | 23 | 10 | √ | 0 | 供应商库存分配基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_om_transferlogentry |  | fentryid |
| 2 | idx_om_transferlogentry_fid |  | fid |
