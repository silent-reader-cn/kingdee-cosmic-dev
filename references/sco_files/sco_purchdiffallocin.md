# 差异分配单（在制）-sco_purchdiffallocin

## 差异明细信息-子表 t_sco_purchdiffallocentry

- **表名称：** 差异明细信息-子表
- **表名：** t_sco_purchdiffallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | funjoindiffamt | 未吸收费用 | numeric | 23 | 10 | √ | 0 | 未吸收费用 |
| 4 | ffalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 5 | fmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 6 | forddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 7 | freservediffx | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 8 | freservediffw | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 9 | freservediffy | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 10 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: 1 :未结算 2 :已结算 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 13 | famount | 差异合计 | numeric | 23 | 10 | √ | 0 | 差异合计 |
| 14 | fmadeupamt | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 15 | ftransferamount | 转出金额(无意义删除 | numeric | 23 | 10 | √ | 0 | 转出金额(无意义删除 |
| 16 | finvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 17 | fotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 18 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 19 | ffeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 20 | fstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 21 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 22 | fdifamount | fdifamount | numeric | 23 | 10 | √ | 0 |  |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fbalanceamount | 待转余额 | numeric | 23 | 10 | √ | 0 | 待转余额 |
| 25 | fweighvalue | fweighvalue | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_purchdiffallocentry |  | fentryid |
| 2 | idx_sco_purchdiffallocentry |  | fcostobjectid,felementid,fsubelementid |
| 3 | idx_sco_purchdiffallocentry2 |  | fid |

---

## 来源单据-子表 t_sco_purdiffacsrcentry

- **表名称：** 来源单据-子表
- **表名：** t_sco_purdiffacsrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 3 | fsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 00 :差异归集单 01 :差异分配单 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_purdiffacsrcentry |  | fentryid |
| 2 | idx_sco_purdiffacsrcentry |  | fid |

---

## 差异分配单（在制）-主表 t_sco_purchdiffalloc

- **表名称：** 差异分配单（在制）-主表
- **表名：** t_sco_purchdiffalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifftotal | 差异总额 | numeric | 23 | 10 | √ | 0 | 差异总额 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbiztype | 分配单类型 | varchar | 30 |  | √ | ' ' | 分配单类型,枚举: 00 :完工 01 :在制 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbecostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 11 | fcalcschemeid | fcalcschemeid | int8 | 64 |  | √ | 0 |  |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 14 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 15 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 24 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fcostobjbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :未结算 B :已结算 |
| 27 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: G :订单价差 H :发票价差 K :费用价差 M :标准成本变更差异 P :材料耗用差异 Q :制造费用差异 R :未吸收费用差异 S :成本更新差异 T :其他差异 C :跌价差异 |
| 28 | fmaincostobjectid | 主成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 29 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_purchdiffalloc_fkeycol |  | fkeycol |
| 2 | pk_sco_purchdiffalloc |  | fid |
| 3 | idx_sco_purchdiffalloc |  | forgid,fperiodid,fcostaccountid,fcostcenterid |

---

## 子项物料-子表 t_sco_lastdiffmaterial

- **表名称：** 子项物料-子表
- **表名：** t_sco_lastdiffmaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flastmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | fweightvalue | 比值 | numeric | 23 | 10 | √ | 0 | 比值 |
| 3 | flastauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fadjamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | flastversionid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_lastdiffmaterial |  | fdetailid |
| 2 | idx_sco_lastdiffmaterial |  | fentryid,fseq |
