# 利率上限波动率曲面-md_intratevol

## 金融工具-子表 t_md_ratevol_ft

- **表名称：** 金融工具-子表
- **表名：** t_md_ratevol_ft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 期限 | varchar | 50 |  | √ | ' ' | 期限 |
| 3 | ffinparvoldif | 波动率差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 波动率差(%) |
| 4 | fstrike | 执行价格(%) | numeric | 23 | 10 | √ | 0.0000000000 | 执行价格(%) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparstrike | 平价执行价格(%) | numeric | 23 | 10 | √ | 0.0000000000 | 平价执行价格(%) |
| 7 | fzerorate | 零息利率 | numeric | 23 | 10 | √ | 0.0000000000 | 零息利率 |
| 8 | fpremium | 期权费 | numeric | 23 | 10 | √ | 0.0000000000 | 期权费 |
| 9 | ffinstrikedif | 执行价差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 执行价差(%) |
| 10 | fpremiumsource | 期权费获取来源 | varchar | 30 |  | √ | ' ' | 期权费获取来源,枚举: Bloomberg :彭博 Reuters :路透 Wind :万得 Handle :手工 |
| 11 | ffintool | 金融工具 | varchar | 80 |  | √ | ' ' | 金融工具 |
| 12 | fparvolsource | 波动率获取来源 | varchar | 30 |  | √ | ' ' | 波动率获取来源,枚举: Bloomberg :彭博 Reuters :路透 Wind :万得 Handle :手工 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | faddpoint | 点数 | int8 | 64 |  | √ | 0 | 点数 |
| 15 | fparvol | 波动率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 波动率(%) |
| 16 | fstrikesource | 执行价格获取来源 | varchar | 30 |  | √ | ' ' | 执行价格获取来源,枚举: Bloomberg :彭博 Reuters :路透 Wind :万得 Handle :手工 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_ratevol_ft_id |  | fid,fentryid |
| 2 | pk_t_md_ratevol_ft |  | fentryid |

---

## 日历-多选基础资料表 t_md_intratevol_wc

- **表名称：** 日历-多选基础资料表
- **表名：** t_md_intratevol_wc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作日历 tbd_workcalendar](../fbd_files/tbd_workcalendar.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_intratevol_wc |  | fpkid |
| 2 | idx_md_intratevol_wc_fid |  | fid |

---

## 利率上限波动率曲面-多语言表 t_md_intratevol_l

- **表名称：** 利率上限波动率曲面-多语言表
- **表名：** t_md_intratevol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_intratevol_l |  | fpkid |
| 2 | idx_md_intratevol_l_id |  | fid,flocaleid |

---

## 利率上限波动率曲面-主表 t_md_intratevol

- **表名称：** 利率上限波动率曲面-主表
- **表名：** t_md_intratevol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarketid | 市场 | int8 | 64 |  | √ | 0 | [市场信息 tbd_marketinfo](../fbd_files/tbd_marketinfo.md) |
| 3 | fnameprice | 名义本金（万元） | int8 | 64 |  | √ | 0 | 名义本金（万元） |
| 4 | fpoint | 执行价格数量 | int4 | 32 |  | √ | 0 | 执行价格数量 |
| 5 | fisfixedvol | 是否固定波动率差 | bpchar | 1 |  | √ | ' ' | 是否固定波动率差 |
| 6 | fpriceruleid | 定价规则 | int8 | 64 |  | √ | 0 | [定价规则 md_pricerule](../fbd_files/md_pricerule.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | ftermend | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fdateadjustmethod | 日期调整方式 | varchar | 30 |  | √ | ' ' | 日期调整方式,枚举: forward :向前 ad_forward :调整向前 backward :向后 ad_backward :调整向后 no_adjust :不调整 |
| 13 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fstrikedif | 执行价差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 执行价差(%) |
| 19 | friskfactors | 风险因子 | varchar | 30 |  | √ | ' ' | 风险因子,枚举: intratevol :利率上限波动率 intrateatm :Caplet Volatility |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fisfixedprice | 是否固定行权价差 | bpchar | 1 |  | √ | ' ' | 是否固定行权价差 |
| 22 | finsertmethod | 插值方法 | varchar | 30 |  | √ | ' ' | 插值方法,枚举: linear :线性 cubicspline :三次样条 |
| 23 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: intrateceil :利率上限波动率曲面 |
| 24 | fatmpricecol | ATM行权价列数 | int8 | 64 |  | √ | 0 | ATM行权价列数 |
| 25 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Actual/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 26 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 27 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 28 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | ftimeinterval | 期限 | varchar | 30 |  | √ | ' ' | 期限,枚举: 1y :一年 6m :半年 3m :季度 1m :一月 |
| 30 | ftermstart | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fisatmprice | 是否使用ATM行权价 | bpchar | 1 |  | √ | ' ' | 是否使用ATM行权价 |
| 33 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: yield :收益率曲线 bond volatility :债券波动率曲面 rate quote :汇率报价 rate ceil volatility :汇率上限波动率曲面 forex volatility :外汇波动率曲面 |
| 34 | frefdate | 参照日期 | timestamp | 0 |  |  | null | 参照日期 |
| 35 | frefindexid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 36 | fparvoldif | 波动率差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 波动率差(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_intratevol |  | fid |
| 2 | idx_intratevol_bb |  | fbillno |

---

## 结构-子表 t_md_ratevol_st

- **表名称：** 结构-子表
- **表名：** t_md_ratevol_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fimpliedvol | 隐含波动率 | numeric | 19 | 6 | √ | 0.000000 | 隐含波动率 |
| 3 | fenddate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 4 | fstructpoint | 点数 | int8 | 64 |  | √ | 0 | 点数 |
| 5 | fstructstrike | 执行价格 | numeric | 19 | 6 | √ | 0.000000 | 执行价格 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_ratevol_st |  | fentryid |
| 2 | idx_md_ratevol_st_id_entid |  | fid |
