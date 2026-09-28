# 坏账准备单（废弃）（废弃）-ar_baddebtpreparebill

## 坏账准备单（废弃）（废弃）-主表 t_ar_baddebtprepare

- **表名称：** 坏账准备单（废弃）（废弃）-主表
- **表名：** t_ar_baddebtprepare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcuraccruedamt | 本期应计提金额 | numeric | 23 | 10 | √ | 0 | 本期应计提金额 |
| 3 | faramtsum | faramtsum | numeric | 23 | 10 | √ | 0 |  |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | frecoveramt | frecoveramt | numeric | 23 | 10 | √ | 0 |  |
| 8 | frecamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 9 | frecoverlocalamt | frecoverlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | flastaccruedamt | 累计已计提金额 | numeric | 23 | 10 | √ | 0 | 累计已计提金额 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fstandardlocalamt | 基准金额(本位币) | numeric | 23 | 10 | √ | 0 | 基准金额(本位币) |
| 14 | fstandardamt | 基准金额 | numeric | 23 | 10 | √ | 0 | 基准金额 |
| 15 | fperiodid | 计提期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 16 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_finarbill :财务应收单 ar_busbill :暂估应收单 ar_revcfmbill :收入确认单 ap_paidbill :期初预付单 cas_paybill :付款处理 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | faccrualpercent | 计提比率(%) | numeric | 23 | 10 | √ | 0 | 计提比率(%) |
| 20 | farlocalamtsum | farlocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 21 | fauditadjustmentlocalamt | fauditadjustmentlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 22 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 23 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 24 | freclocalamt | 应收金额(本位币) | numeric | 23 | 10 | √ | 0 | 应收金额(本位币) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisperiod | fisperiod | bpchar | 1 |  | √ | '0' |  |
| 27 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 28 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 29 | foffsetamt | 被抵消金额 | numeric | 23 | 10 | √ | 0 | 被抵消金额 |
| 30 | fcuraccruallocalamt | 本期计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期计提金额(本位币) |
| 31 | flosslocalamt | 损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 损失金额(本位币) |
| 32 | fquotation | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | flossamt | 损失金额 | numeric | 23 | 10 | √ | 0 | 损失金额 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fauditadjustmentamt | fauditadjustmentamt | numeric | 23 | 10 | √ | 0 |  |
| 36 | flossamtsum | flossamtsum | numeric | 23 | 10 | √ | 0 |  |
| 37 | fagingrange | 账龄区间 | varchar | 50 |  | √ | ' ' | 账龄区间 |
| 38 | fcuraccruedlocalamt | 本期应计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期应计提金额(本位币) |
| 39 | frecoverlocalamtsum | frecoverlocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 40 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 quarter :季 semiannual :半年 year :年 |
| 41 | fisoffset | 已被抵消 | bpchar | 1 |  | √ | '0' | 已被抵消 |
| 42 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 43 | foffsetlocalamt | 被抵消金额(本位币) | numeric | 23 | 10 | √ | 0 | 被抵消金额(本位币) |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | flastaccruedlocalamt | 累计已计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计已计提金额(本位币) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 48 | fsourcebilldate | 源单日期 | timestamp | 0 |  |  | null | 源单日期 |
| 49 | faccrualmethod | 计提方法 | varchar | 50 |  | √ | ' ' | 计提方法,枚举: aging :账龄分析法 individual :个别认定法 |
| 50 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 52 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 53 | faccrualobjid | 计提对象 | int8 | 64 |  | √ | 0 | 计提对象 ar_accrualentityobj |
| 54 | faccrualschemeid | 计提方案 | int8 | 64 |  | √ | 0 | 计提方案（废弃） ar_baddebtaccrualplan |
| 55 | flosslocalamtsum | flosslocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 56 | frecoveramtsum | frecoveramtsum | numeric | 23 | 10 | √ | 0 |  |
| 57 | fcuraccrualamt | 本期计提金额 | numeric | 23 | 10 | √ | 0 | 本期计提金额 |
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

## 单据体-子表 t_ar_baddebtprepareentry

- **表名称：** 单据体-子表
- **表名：** t_ar_baddebtprepareentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 3 | fcuraccruedamt | 本期应计提金额 | numeric | 23 | 10 | √ | 0 | 本期应计提金额 |
| 4 | faramtsum | faramtsum | numeric | 23 | 10 | √ | 0 |  |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | foffsetamt | 被抵消金额 | numeric | 23 | 10 | √ | 0 | 被抵消金额 |
| 8 | fcuraccruallocalamt | 本期计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期计提金额(本位币) |
| 9 | fasstacttype | fasstacttype | varchar | 30 |  | √ | ' ' |  |
| 10 | findividualreason | findividualreason | varchar | 255 |  | √ | ' ' |  |
| 11 | fotherbizclass | fotherbizclass | varchar | 30 |  | √ | ' ' |  |
| 12 | flosslocalamt | 损失金额(本位币) | numeric | 23 | 10 | √ | 0 | 损失金额(本位币) |
| 13 | frecoveramt | frecoveramt | numeric | 23 | 10 | √ | 0 |  |
| 14 | flossamt | 损失金额 | numeric | 23 | 10 | √ | 0 | 损失金额 |
| 15 | frecamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 16 | frecoverlocalamt | frecoverlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 17 | flastaccruedamt | 累计已计提金额 | numeric | 23 | 10 | √ | 0 | 累计已计提金额 |
| 18 | fauditadjustmentamt | fauditadjustmentamt | numeric | 23 | 10 | √ | 0 |  |
| 19 | flossamtsum | flossamtsum | numeric | 23 | 10 | √ | 0 |  |
| 20 | fcuraccruedlocalamt | 本期应计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 本期应计提金额(本位币) |
| 21 | frecoverlocalamtsum | frecoverlocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 22 | fstandardlocalamt | 基准金额(本位币) | numeric | 23 | 10 | √ | 0 | 基准金额(本位币) |
| 23 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 24 | fstandardamt | 基准金额 | numeric | 23 | 10 | √ | 0 | 基准金额 |
| 25 | foffsetlocalamt | 被抵消金额(本位币) | numeric | 23 | 10 | √ | 0 | 被抵消金额(本位币) |
| 26 | flastaccruedlocalamt | 累计已计提金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计已计提金额(本位币) |
| 27 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 28 | fasstactid | fasstactid | int8 | 64 |  | √ | 0 |  |
| 29 | fotheramt | fotheramt | numeric | 23 | 10 | √ | 0 |  |
| 30 | farlocalamtsum | farlocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 31 | fotherlocalamt | fotherlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 32 | fotherbuslocalamt | fotherbuslocalamt | numeric | 23 | 10 | √ | 0 |  |
| 33 | fbillsource | fbillsource | varchar | 30 |  | √ | ' ' |  |
| 34 | fotherbusamt | fotherbusamt | numeric | 23 | 10 | √ | 0 |  |
| 35 | fauditadjustmentlocalamt | fauditadjustmentlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 36 | faccrualtype | faccrualtype | varchar | 30 |  | √ | ' ' |  |
| 37 | flosslocalamtsum | flosslocalamtsum | numeric | 23 | 10 | √ | 0 |  |
| 38 | frecoveramtsum | frecoveramtsum | numeric | 23 | 10 | √ | 0 |  |
| 39 | fcuraccrualamt | 本期计提金额 | numeric | 23 | 10 | √ | 0 | 本期计提金额 |
| 40 | freclocalamt | 应收金额(本位币) | numeric | 23 | 10 | √ | 0 | 应收金额(本位币) |
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
