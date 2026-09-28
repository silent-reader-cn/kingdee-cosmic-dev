# 差异分配单（完工）-sca_purchdiffalloc

## 子项物料-子表 t_sca_lastdiffmaterial

- **表名称：** 子项物料-子表
- **表名：** t_sca_lastdiffmaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flastmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fweightvalue | 比值 | numeric | 23 | 10 | √ | 0.0000000000 | 比值 |
| 3 | flastauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fadjamount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | flastversionid | 版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_lastdiffmaterial |  | fdetailid |
| 2 | idx_sca_lastdiffmaterial |  | fentryid,fseq |

---

## 来源单据-子表 t_sca_purdiffacsrcentry

- **表名称：** 来源单据-子表
- **表名：** t_sca_purdiffacsrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 3 | fsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 00 :差异归集单 01 :差异分配单 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_purdiffacsrcentry |  | fentryid |
| 2 | idx_sca_purdiffacsrcentry |  | fid |

---

## 差异明细信息-子表 t_sca_purchdiffallocentry

- **表名称：** 差异明细信息-子表
- **表名：** t_sca_purchdiffallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: 1 :未结算 2 :已结算 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | ftransferamount | 转出金额(无意义删除 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额(无意义删除 |
| 9 | fdifamount | fdifamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fbalanceamount | 待转余额 | numeric | 23 | 10 | √ | 0.0000000000 | 待转余额 |
| 12 | fweighvalue | fweighvalue | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_purchdiffallocentry_pkey |  | fentryid |
| 2 | idx_sca_purchdiffallocentry |  | fcostobjectid,felementid,fsubelementid |
| 3 | idx_sca_purchdiffallocentry2 |  | fid |

---

## 差异分配单（完工）-主表 t_sca_purchdiffalloc

- **表名称：** 差异分配单（完工）-主表
- **表名：** t_sca_purchdiffalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifftotal | 差异总额 | numeric | 23 | 10 | √ | 0.0000000000 | 差异总额 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 00 :完工 01 :在制 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbecostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 10 | fcalcschemeid | fcalcschemeid | int8 | 64 |  | √ | 0 |  |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 16 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 20 | fvouchernum | 凭证字号 | varchar | 60 |  | √ | ' ' | 凭证字号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fcostobjbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :未结算 B :已结算 |
| 23 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: G :订单价差 H :发票价差 K :费用价差 M :标准成本变更差异 P :材料耗用差异 Q :制造费用差异 R :未吸收费用差异 S :成本更新差异 T :其他差异 C :跌价差异 |
| 24 | fmaincostobjectid | 主成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 25 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fkeycol | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_purchdiffalloc_pkey |  | fid |
| 2 | idx_sca_purchdiffalloc_fkeycol |  | fkeycol |
| 3 | idx_sca_purchdiffalloc |  | forgid,fperiodid,fcostaccountid,fcostcenterid |
