# 费用暂估单-cal_costestimatebill

## 费用暂估单-关联追踪表 t_cal_costestimatebill_tc

- **表名称：** 费用暂估单-关联追踪表
- **表名：** t_cal_costestimatebill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costestimatebill_tc_tbill |  | ftbillid |
| 2 | idx_cal_costestimatebill_tc_tid |  | ftid |
| 3 | t_cal_costestimatebill_tc_pkey |  | fid |

---

## 分摊明细-子表 t_cal_esbillresultentry

- **表名称：** 分摊明细-子表
- **表名：** t_cal_esbillresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsharedetailamt | 本次分摊金额(单据) | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊金额(单据) |
| 2 | fexitemseq | 费用项目序号 | int8 | 64 |  | √ | 0 | 费用项目序号 |
| 3 | fsharedetailtaxamount | 本次分摊含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊含税金额 |
| 4 | fsharedetailamount | 本次分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsharedetailatype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fsharedetailasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fsharedetailtaxamt | 本次分摊含税金额(单据) | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊含税金额(单据) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fsharedetailexitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

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

## 分摊结果-子表 t_cal_costesbillresult

- **表名称：** 分摊结果-子表
- **表名：** t_cal_costesbillresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshareamt | 分摊总额(单据) | numeric | 23 | 10 | √ | 0.0000000000 | 分摊总额(单据) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcostdetailid | 成本记录明细 | int8 | 64 |  | √ | 0 | [核算成本记录明细 cal_costdetail](../cal_files/cal_costdetail.md) |
| 5 | fsharetaxamount | 分摊总含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊总含税金额 |
| 6 | fshareamount | 分摊总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊总金额 |
| 7 | festimatebillno | 暂估单编码 | varchar | 80 |  | √ | ' ' | 暂估单编码 |
| 8 | fcalentryid | 核算单分录id | int8 | 64 |  | √ | 0 | 核算单分录id |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fsharetaxamt | 分摊总含税金额(单据) | numeric | 23 | 10 | √ | 0.0000000000 | 分摊总含税金额(单据) |
| 11 | fisdirect | 是否直接生成 | bpchar | 1 |  | √ | '1' | 是否直接生成 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costesbillresult_pkey |  | fentryid |
| 2 | idx_cal_costesbillres_id |  | fid |

---

## 费用暂估单-反写记录表 t_cal_costestimatebill_wb

- **表名称：** 费用暂估单-反写记录表
- **表名：** t_cal_costestimatebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costestimatebill_wb_pkey |  | fentryid |
| 2 | idx_cal_costestimatebill_wb_fk |  | fid |

---

## 费用信息-子表 t_cal_costesbillexpense

- **表名称：** 费用信息-子表
- **表名：** t_cal_costesbillexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目编码 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | ftaxamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 4 | fintercostamt | 计成本金额 | numeric | 23 | 10 | √ | 0 | 计成本金额 |
| 5 | festimateamount | 分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊金额 |
| 6 | fasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | festimatetaxamount | 分摊含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊含税金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fasstacttype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 11 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | festimatestandard | 分摊标准 | varchar | 30 |  | √ | ' ' | 分摊标准,枚举: actualcost :实际成本 materialcost :材料成本 baseqty :基本数量 unitactualcost :单位实际成本 unitstandardcost :单位标准成本 standardcost :标准成本 unitmaterialcost :单位材料成本 unitfee :单位费用 fee :费用 taxamt :价税合计 loctaxamt :价税合计本位币 unitprocesscost :单位加工费 processcost :加工费 tax :税额 localtax :税额本位币 adjustamount :调整金额 totalsharefee :累计分摊费用 |
| 13 | frate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fexpensecurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costesbillexpense_pkey |  | fentryid |
| 2 | idx_cal_costesbillex_id |  | fid |

---

## 费用暂估单-主表 t_cal_costestimatebill

- **表名称：** 费用暂估单-主表
- **表名：** t_cal_costestimatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 C :已暂估 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fconvertmode | 汇率方式 | bpchar | 1 |  | √ | '1' | 汇率方式,枚举: 1 :直接汇率 2 :间接汇率 |
| 7 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | festimatedate | 暂估日期 | timestamp | 0 |  |  | null | 暂估日期 |
| 10 | fmatchruleid | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则（旧） cal_matchrule](../sbs_files/cal_matchrule.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fstandardcurrencyid | 分摊币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fexratetableid | 分摊汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fsharetypeid | 分摊类型 | int8 | 64 |  | √ | 0 | [核销类别（旧） cal_writeofftype](../sbs_files/cal_writeofftype.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costestimatebill_pkey |  | fid |
| 2 | idx_cal_costestim_billno |  | fbillno |

---

## 关联子实体-子表 t_cal_costesbillexpense_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cal_costesbillexpense_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costesbillexpense_lk_pkey |  | fpkid |
| 2 | idx_cal_costesbillexpense_lk_fk |  | fentryid |
