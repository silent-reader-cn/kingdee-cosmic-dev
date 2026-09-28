# 坏账准备单-ar_baddebtpreparebill_pro

## 坏账准备单-主表 t_ar_baddebtprepare

- **表名称：** 坏账准备单-主表
- **表名：** t_ar_baddebtprepare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcuraccruedamt | 本期末应计提金额 | numeric | 23 | 10 | √ | 0 | 本期末应计提金额 |
| 3 | faramtsum | 累计应收账款 | numeric | 23 | 10 | √ | 0 | 累计应收账款 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | frecoveramt | 本期坏账收回金额 | numeric | 23 | 10 | √ | 0 | 本期坏账收回金额 |
| 8 | frecamount | frecamount | numeric | 23 | 10 | √ | 0 |  |
| 9 | frecoverlocalamt | 本期坏账收回金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期坏账收回金额(本位币) |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | flastaccruedamt | 期初已计提金额 | numeric | 23 | 10 | √ | 0 | 期初已计提金额 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fstandardlocalamt | 坏账计提基数(本位币) | numeric | 23 | 10 | √ | 0 | 坏账计提基数(本位币) |
| 14 | fstandardamt | 坏账计提基数 | numeric | 23 | 10 | √ | 0 | 坏账计提基数 |
| 15 | fperiodid | 计提期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 16 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | faccrualpercent | faccrualpercent | numeric | 23 | 10 | √ | 0 |  |
| 20 | farlocalamtsum | 累计应收账款(本位币) | numeric | 23 | 10 | √ | 0 | 累计应收账款(本位币) |
| 21 | fauditadjustmentlocalamt | 审计调整金额(本位币) | numeric | 23 | 10 | √ | 0 | 审计调整金额(本位币) |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | freclocalamt | freclocalamt | numeric | 23 | 10 | √ | 0 |  |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 27 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 28 | fasstacttype | fasstacttype | varchar | 30 |  | √ | ' ' |  |
| 29 | foffsetamt | foffsetamt | numeric | 23 | 10 | √ | 0 |  |
| 30 | fcuraccruallocalamt | 本期计提坏账准备金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期计提坏账准备金额(本位币) |
| 31 | flosslocalamt | 本期坏账损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期坏账损失金额(本位币) |
| 32 | fquotation | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | flossamt | 本期坏账损失金额 | numeric | 23 | 10 | √ | 0 | 本期坏账损失金额 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fauditadjustmentamt | 审计调整金额 | numeric | 23 | 10 | √ | 0 | 审计调整金额 |
| 36 | flossamtsum | 累计坏账损失金额 | numeric | 23 | 10 | √ | 0 | 累计坏账损失金额 |
| 37 | fagingrange | fagingrange | varchar | 50 |  | √ | ' ' |  |
| 38 | fcuraccruedlocalamt | 本期末应计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期末应计提金额(本位币) |
| 39 | frecoverlocalamtsum | 累计坏账收回金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计坏账收回金额(本位币) |
| 40 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 quarter :季 semiannual :半年 year :年 |
| 41 | fisoffset | fisoffset | bpchar | 1 |  | √ | '0' |  |
| 42 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 43 | foffsetlocalamt | foffsetlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | flastaccruedlocalamt | 期初已计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 期初已计提金额(本位币) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fasstactid | fasstactid | int8 | 64 |  | √ | 0 |  |
| 48 | fsourcebilldate | fsourcebilldate | timestamp | 0 |  |  | null |  |
| 49 | faccrualmethod | faccrualmethod | varchar | 50 |  | √ | ' ' |  |
| 50 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 52 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 53 | faccrualobjid | faccrualobjid | int8 | 64 |  | √ | 0 |  |
| 54 | faccrualschemeid | faccrualschemeid | int8 | 64 |  | √ | 0 |  |
| 55 | flosslocalamtsum | 累计坏账损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计坏账损失金额(本位币) |
| 56 | frecoveramtsum | 累计坏账收回金额 | numeric | 23 | 10 | √ | 0 | 累计坏账收回金额 |
| 57 | fcuraccrualamt | 本期计提坏账准备金额 | numeric | 23 | 10 | √ | 0 | 本期计提坏账准备金额 |
| 58 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_bdp_faccrualdate |  | faccrualdate |
| 2 | idx_ar_bdp_fbillno |  | fbillno |
| 3 | idx_ar_bdp_org |  | forgid |
| 4 | pk_t_ar_baddebtprepare |  | fid |
| 5 | idx_ar_bdp_period_org |  | fperiodid,forgid |

---

## 计提明细单据体-子表 t_ar_baddebtprepareentry

- **表名称：** 计提明细单据体-子表
- **表名：** t_ar_baddebtprepareentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fcuraccruedamt | 本期末应计提金额 | numeric | 23 | 10 | √ | 0 | 本期末应计提金额 |
| 4 | faramtsum | 累计应收账款 | numeric | 23 | 10 | √ | 0 | 累计应收账款 |
| 5 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | foffsetamt | foffsetamt | numeric | 23 | 10 | √ | 0 |  |
| 8 | fcuraccruallocalamt | 本期计提坏账准备金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期计提坏账准备金额(本位币) |
| 9 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 10 | findividualreason | 个别认定原因 | varchar | 255 |  | √ | ' ' | 个别认定原因 |
| 11 | fotherbizclass | 业务分类 | varchar | 30 |  | √ | ' ' | 业务分类,枚举: oth_arap :其他应收 not_oth_arap : |
| 12 | flosslocalamt | 本期坏账损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期坏账损失金额(本位币) |
| 13 | frecoveramt | 本期坏账收回金额 | numeric | 23 | 10 | √ | 0 | 本期坏账收回金额 |
| 14 | flossamt | 本期坏账损失金额 | numeric | 23 | 10 | √ | 0 | 本期坏账损失金额 |
| 15 | frecamount | 暂估金额 | numeric | 23 | 10 | √ | 0 | 暂估金额 |
| 16 | frecoverlocalamt | 本期坏账收回金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期坏账收回金额(本位币) |
| 17 | flastaccruedamt | 期初已计提金额 | numeric | 23 | 10 | √ | 0 | 期初已计提金额 |
| 18 | fauditadjustmentamt | 审计调整金额 | numeric | 23 | 10 | √ | 0 | 审计调整金额 |
| 19 | flossamtsum | 累计坏账损失金额 | numeric | 23 | 10 | √ | 0 | 累计坏账损失金额 |
| 20 | fcuraccruedlocalamt | 本期末应计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期末应计提金额(本位币) |
| 21 | frecoverlocalamtsum | 累计坏账收回金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计坏账收回金额(本位币) |
| 22 | fstandardlocalamt | 坏账计提基数(本位币) | numeric | 23 | 10 | √ | 0 | 坏账计提基数(本位币) |
| 23 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 24 | fstandardamt | 坏账计提基数 | numeric | 23 | 10 | √ | 0 | 坏账计提基数 |
| 25 | foffsetlocalamt | foffsetlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 26 | flastaccruedlocalamt | 期初已计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 期初已计提金额(本位币) |
| 27 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 28 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fotheramt | 其他应收金额 | numeric | 23 | 10 | √ | 0 | 其他应收金额 |
| 30 | farlocalamtsum | 累计应收账款(本位币) | numeric | 23 | 10 | √ | 0 | 累计应收账款(本位币) |
| 31 | fotherlocalamt | 其他应收金额(本位币) | numeric | 23 | 10 | √ | 0 | 其他应收金额(本位币) |
| 32 | fotherbuslocalamt | 其他应收暂估金额(本位币) | numeric | 23 | 10 | √ | 0 | 其他应收暂估金额(本位币) |
| 33 | fbillsource | 计提单据来源 | varchar | 30 |  | √ | ' ' | 计提单据来源,枚举: ar_busbill :暂估应收单 other : |
| 34 | fotherbusamt | 其他应收暂估金额 | numeric | 23 | 10 | √ | 0 | 其他应收暂估金额 |
| 35 | fauditadjustmentlocalamt | 审计调整金额(本位币) | numeric | 23 | 10 | √ | 0 | 审计调整金额(本位币) |
| 36 | faccrualtype | 计提类型 | varchar | 30 |  | √ | ' ' | 计提类型,枚举: individual :个别认定 group :分组认定 aging :账龄分析法 |
| 37 | flosslocalamtsum | 累计坏账损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计坏账损失金额(本位币) |
| 38 | frecoveramtsum | 累计坏账收回金额 | numeric | 23 | 10 | √ | 0 | 累计坏账收回金额 |
| 39 | fcuraccrualamt | 本期计提坏账准备金额 | numeric | 23 | 10 | √ | 0 | 本期计提坏账准备金额 |
| 40 | freclocalamt | 暂估金额(本位币) | numeric | 23 | 10 | √ | 0 | 暂估金额(本位币) |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_bdpe_pid |  | fid |
| 2 | idx_ar_bdpe_srcidentryid |  | fsrcbillid |
| 3 | pk_t_ar_baddebtprepareentry |  | fentryid |

---

## 本期计提信息单据体-子表 t_ar_baddebtprecurentry

- **表名称：** 本期计提信息单据体-子表
- **表名：** t_ar_baddebtprecurentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstandardamt | 坏账计提基数 | numeric | 23 | 10 | √ | 0 | 坏账计提基数 |
| 3 | fsrcentryid | 计提明细行ID | int8 | 64 |  | √ | 0 | 计提明细行ID |
| 4 | fcuraccruedamt | 本期末应计提金额 | numeric | 23 | 10 | √ | 0 | 本期末应计提金额 |
| 5 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 8 | faccrualrate | 计提比率(%) | numeric | 23 | 10 | √ | 0 | 计提比率(%) |
| 9 | fotherbizclass | 业务分类 | varchar | 30 |  | √ | ' ' | 业务分类,枚举: oth_arap :其他应收 not_oth_arap : |
| 10 | fbillsource | 计提单据来源 | varchar | 30 |  | √ | ' ' | 计提单据来源,枚举: ar_busbill :暂估应收单 other : |
| 11 | fagingrange | 账龄区间 | varchar | 30 |  | √ | ' ' | 账龄区间 |
| 12 | fcuraccruedlocalamt | 本期末应计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期末应计提金额(本位币) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fstandardlocalamt | 坏账计提基数(本位币) | numeric | 23 | 10 | √ | 0 | 坏账计提基数(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtprecurentry |  | fentryid |
| 2 | idx_ar_bdpecur_pid |  | fid |
