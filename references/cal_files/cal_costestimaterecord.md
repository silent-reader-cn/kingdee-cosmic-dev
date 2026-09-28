# 费用暂估记录-cal_costestimaterecord

## 单据体-子表 t_cal_esbillresultentry

- **表名称：** 单据体-子表
- **表名：** t_cal_esbillresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsharedetailamt | 分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊金额 |
| 2 | fexitemseq | 费用项目序号 | int8 | 64 |  | √ | 0 | 费用项目序号 |
| 3 | fsharedetailtaxamount | fsharedetailtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fsharedetailamount | fsharedetailamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsharedetailatype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fsharedetailasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fsharedetailtaxamt | 分摊含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊含税金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fsharedetailexitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_esbillresultentry_pkey |  | fdetailid |
| 2 | idx_cal_esbillresen_entryid |  | fentryid |

---

## 费用暂估记录-主表 t_cal_costesbillresult

- **表名称：** 费用暂估记录-主表
- **表名：** t_cal_costesbillresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 费用暂估单id | int8 | 64 |  | √ | 0 | 费用暂估单id |
| 2 | fshareamt | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fcostdetailid | 成本记录明细 | int8 | 64 |  | √ | 0 | 核算成本记录明细 cal_costdetail |
| 5 | fsharetaxamount | fsharetaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fshareamount | fshareamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | festimatebillno | 暂估单编码 | varchar | 80 |  | √ | ' ' | 暂估单编码 |
| 8 | fcalentryid | 核算单分录id | int8 | 64 |  | √ | 0 | 核算单分录id |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fsharetaxamt | 含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 含税金额 |
| 11 | fisdirect | 是否直接生成 | bpchar | 1 |  | √ | '1' | 是否直接生成 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costesbillresult_pkey |  | fentryid |
| 2 | idx_cal_costesbillres_id |  | fid |
