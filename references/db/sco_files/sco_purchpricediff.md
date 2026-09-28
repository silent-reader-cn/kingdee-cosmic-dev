# 差异归集单-sco_purchpricediff

## 单据体-子表 t_sco_purchpriceentry

- **表名称：** 单据体-子表
- **表名：** t_sco_purchpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fintoamount | 转入金额 | numeric | 23 | 10 | √ | 0 | 转入金额 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fintostatus | 转入状态 | varchar | 30 |  | √ | ' ' | 转入状态,枚举: 0 :未转入 1 :部分转入 2 :完全转入 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 11 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 12 | flastintoamt | 最后转入金额 | numeric | 23 | 10 | √ | 0 | 最后转入金额 |
| 13 | flastperiod | 最后转入期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fadjustamt | 差异金额 | numeric | 23 | 10 | √ | 0 | 差异金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_purchpriceentry |  | fentryid |
| 2 | idx_sco_purchpriceet |  | felementid,fsubelementid,fcostcenterid |
| 3 | idx_sco_purchpriceet2 |  | fid |

---

## 差异归集单-主表 t_sco_purchpricediff

- **表名称：** 差异归集单-主表
- **表名：** t_sco_purchpricediff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 0 :手工录入 1 :内部系统导入 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreatetype | 创建类型 | varchar | 30 |  | √ | ' ' | 创建类型,枚举: G :订单价差 H :发票价差 K :费用价差 A :其他差异 B :材料耗用差异 C :制造费用差异 D :在产品成本变更差异 E :未吸收费用差异 F :标准成本变更差异 |
| 12 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 15 | fcostadjustnum | 成本调整单号 | varchar | 80 |  | √ | ' ' | 成本调整单号 |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsrcbilltypeid | fsrcbilltypeid | int8 | 64 |  | √ | 0 |  |
| 20 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_purchpricediff |  | forgid,fcostaccountid |
| 2 | pk_sco_purchpricediff |  | fid |
