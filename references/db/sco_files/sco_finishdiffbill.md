# 完工结算差异单-sco_finishdiffbill

## 完工结算差异单-主表 t_sco_finishdiffbill

- **表名称：** 完工结算差异单-主表
- **表名：** t_sco_finishdiffbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fdiffamount | 差异总额 | numeric | 23 | 10 | √ | 0 | 差异总额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fvoucher | fvoucher | varchar | 255 |  | √ | ' ' |  |
| 18 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsourcebillid | 来源单据 | int8 | 64 |  | √ | 0 | 来源单据 |
| 21 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 22 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fproallocgen | 期末成本计算生成 | varchar | 30 |  | √ | '0' | 期末成本计算生成 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_finishdiffbill |  | fid |
| 2 | idx_sco_finishdiffbill |  | fcostaccountid,fcostcenterid,fcostobjectid |

---

## 单据体-子表 t_sco_finishdiffbillentry

- **表名称：** 单据体-子表
- **表名：** t_sco_finishdiffbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanuorgid | fmanuorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fadjustnum | 成本调整单编码 | varchar | 80 |  | √ | ' ' | 成本调整单编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fadjustbill | 成本调整单id | int8 | 64 |  | √ | 0 | 成本调整单id |
| 10 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: 1 :材料耗用差异 2 :制造费用差异 3 :成本更新差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_finishdiffentry2 |  | fid |
| 2 | idx_sco_finishdiffentry |  | felementid,fsubelementid |
| 3 | pk_sco_finishdiffbillentry |  | fentryid |
