# 未吸收费用差异单-sca_unabsorbdiff

## 未吸收费用差异单-主表 t_sca_unabsorbdiff

- **表名称：** 未吸收费用差异单-主表
- **表名：** t_sca_unabsorbdiff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fdifftotal | 差异总额 | numeric | 23 | 10 | √ | 0.0000000000 | 差异总额 |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fvouchernum | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fadjustbill | 成本调整单id | int8 | 64 |  | √ | 0 | 成本调整单id |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdifftype | 差异类型 | varchar | 30 |  | √ | '0' | 差异类型,枚举: 4 :未吸收差异 3 :成本更新差异 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcarrynumid | fcarrynumid | varchar | 60 |  | √ | ' ' |  |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 18 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 19 | fadjustnum | 成本调整单编号 | varchar | 60 |  | √ | ' ' | 成本调整单编号 |
| 20 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fproallocgen | 在制 | varchar | 30 |  | √ | '0' | 在制 |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_unabsorbdiff_pkey |  | fid |
| 2 | index_sca_unabsorbdiff |  | forgid,fperiodid,fcostaccountid,fcostcenterid |

---

## 单据体-子表 t_sca_unabsorbdiffentry

- **表名称：** 单据体-子表
- **表名：** t_sca_unabsorbdiffentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_unabsorbdiffentry |  | felementid,fsubelementid |
| 2 | t_sca_unabsorbdiffentry_pkey |  | fentryid |
| 3 | idx_sca_unabsorbdiffentry2 |  | fid |
