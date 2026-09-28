# 完工结算差异单-sca_finishdiffbill

## 单据体-子表 t_sca_finishdiffbillentry

- **表名称：** 单据体-子表
- **表名：** t_sca_finishdiffbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanuorgid | fmanuorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fadjustnum | 成本调整单编码 | varchar | 60 |  | √ | ' ' | 成本调整单编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fadjustbill | 成本调整单id | int8 | 64 |  | √ | 0 | 成本调整单id |
| 10 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: 1 :材料耗用差异 2 :制造费耗用差异 3 :成本更新差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_finishdiffentry2 |  | fid |
| 2 | idx_sca_finishdiffentry |  | felementid,fsubelementid |
| 3 | t_sca_finishdiffbillentry_pkey |  | fentryid |

---

## 完工结算差异单-主表 t_sca_finishdiffbill

- **表名称：** 完工结算差异单-主表
- **表名：** t_sca_finishdiffbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fvoucher | fvoucher | varchar | 60 |  | √ | ' ' |  |
| 13 | fvouchernum | 凭证号 | varchar | 100 |  | √ | ' ' | 凭证号 |
| 14 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 15 | fdiffamount | 差异总额 | numeric | 23 | 10 | √ | 0.0000000000 | 差异总额 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsourcebillid | 来源单据 | int8 | 64 |  | √ | 0 | 来源单据 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 20 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fproallocgen | 在制 | varchar | 30 |  | √ | '0' | 在制 |
| 23 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_finishdiffbill_pkey |  | fid |
| 2 | idx_sca_finishdiffbill |  | fcostaccountid,fcostcenterid,fcostobjectid |
