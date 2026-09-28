# 子要素总制造费用-sca_totalmfgfee

## 单据体-子表 t_sca_totalmfgfeeentry

- **表名称：** 单据体-子表
- **表名：** t_sca_totalmfgfeeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftotalproduce | 总制造费用 | numeric | 23 | 10 | √ | 0.0000000000 | 总制造费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_totalmfgfeeentry_pkey |  | fentryid |
| 2 | idx_sca_totalmfgfeeentry |  | fsubelementid,felementid |
| 3 | idx_sca_totalmfgfeeentry2 |  | fid |

---

## 子要素总制造费用-主表 t_sca_totalmfgfee

- **表名称：** 子要素总制造费用-主表
- **表名：** t_sca_totalmfgfee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 12 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 14 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_totalmfgfee_pkey |  | fid |
| 2 | idx_sca_totalmfgfee |  | forgid,fperiodid,fcostaccountid,fcostcenterid |
