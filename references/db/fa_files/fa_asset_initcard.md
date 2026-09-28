# 初始化资产卡片-fa_asset_initcard

## 入账时点财务信息-子表 t_fa_card_fininit

- **表名称：** 入账时点财务信息-子表
- **表名：** t_fa_card_fininit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0 | 净额 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0 | 进项税额 |
| 5 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0 | 累计折旧 |
| 6 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0 | 原币金额 |
| 9 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 10 | fdepredamount | 已折旧期间数 | numeric | 19 | 6 | √ | 0 | 已折旧期间数 |
| 11 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0 | 预计净残值 |
| 12 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 14 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0 | 资产原值 |
| 15 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0 | 净值 |
| 16 | fcurrencyrate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 17 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0 | 减值准备 |
| 18 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0 | 本年累计折旧 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_fininit |  | fentryid |
| 2 | idx_fa_card_fininit_fid |  | fid |

---

## 初始化资产卡片-多语言表 t_fa_card_real_l

- **表名称：** 初始化资产卡片-多语言表
- **表名：** t_fa_card_real_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetname | 资产名称 | varchar | 255 |  | √ | ' ' | 资产名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_l_pkey |  | fpkid |
| 2 | idx_fa_card_real_l |  | fid,flocaleid |

---

## 资产条码-多选基础资料表 t_fa_card_barcode

- **表名称：** 资产条码-多选基础资料表
- **表名：** t_fa_card_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产条码打印 barcm_barcodemainfile_fa](../barcm_files/barcm_barcodemainfile_fa.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_barcode |  | fpkid |
| 2 | idx_fa_card_bc_fdetail |  | fid |

---

## 财务分录-分表 t_fa_card_fin_i

- **表名称：** 财务分录-分表
- **表名：** t_fa_card_fin_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finitoriginalval | finitoriginalval | numeric | 23 | 10 | √ | '-1' |  |
| 3 | fcurusedday | 本期折旧天数 | numeric | 19 | 6 | √ | 0 | 本期折旧天数 |
| 4 | fusedday | 已折旧天数 | numeric | 19 | 6 | √ | 0 | 已折旧天数 |
| 5 | fusedaysum | 预计使用总天数 | numeric | 19 | 6 | √ | 0 | 预计使用总天数 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_card_fin_i |  | fentryid |

---

## 财务分录-子表 t_fa_card_fin

- **表名称：** 财务分录-子表
- **表名：** t_fa_card_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | flimitcalculate | 按照企业所得税法计算折旧限额 | bpchar | 1 |  | √ | '0' | 按照企业所得税法计算折旧限额 |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 5 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 6 | fyearorigvalchg | fyearorigvalchg | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdeprelimit | 税法折旧限额 | numeric | 19 | 6 | √ | 0 | 税法折旧限额 |
| 9 | fuseperiod | 使用年期间数 | numeric | 19 | 6 | √ | 0 | 使用年期间数 |
| 10 | fdepredamount | 已折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 已折旧期间数 |
| 11 | fisdynamic | fisdynamic | bpchar | 1 |  | √ | '0' |  |
| 12 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fisdyndepre | 切换动态算法 | bpchar | 1 |  | √ | '0' | 切换动态算法 |
| 15 | fincomededuct | fincomededuct | bpchar | 1 |  | √ | '0' |  |
| 16 | fissupplement | fissupplement | bpchar | 1 |  | √ | '0' |  |
| 17 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 18 | ffincardid | 财务信息 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 19 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 20 | fmonthorigvalchg | fmonthorigvalchg | numeric | 19 | 6 | √ | 0.000000 |  |
| 21 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 22 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 23 | fmaxrelvaluateamt | 重估最高限额 | numeric | 19 | 6 | √ | 0 | 重估最高限额 |
| 24 | fbillstatus | fbillstatus | varchar | 50 |  | √ | 'A' |  |
| 25 | fmonthdepre | fmonthdepre | numeric | 19 | 6 | √ | 0.000000 |  |
| 26 | frevaluationreserve | 重估准备金 | numeric | 19 | 6 | √ | 0 | 重估准备金 |
| 27 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 28 | fbeginyearamount | fbeginyearamount | numeric | 19 | 6 | √ | 0 |  |
| 29 | fmonthaccumdeprechg | fmonthaccumdeprechg | numeric | 19 | 6 | √ | 0 |  |
| 30 | fpreusingamount | 预计使用期间数/预计总工作量 | numeric | 19 | 6 | √ | 0.000000 | 预计使用期间数/预计总工作量 |
| 31 | fshowcurrency | 显示原币 | bpchar | 1 |  | √ | '0' | 显示原币 |
| 32 | frevalreservamor | 已摊销重估准备金 | numeric | 19 | 6 | √ | 0 | 已摊销重估准备金 |
| 33 | fisneerevaluate | fisneerevaluate | bpchar | 1 |  | √ | '0' |  |
| 34 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 35 | fnumber | fnumber | varchar | 100 |  |  | ' ' |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 38 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 39 | faddidepreamount | faddidepreamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 40 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 41 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 42 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 43 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 44 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 45 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 46 | fmonthdeprechg | fmonthdeprechg | numeric | 19 | 6 | √ | 0.000000 |  |
| 47 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 48 | fisneeddepre | fisneeddepre | bpchar | 1 |  | √ | '1' |  |
| 49 | fdeprerate | fdeprerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 51 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |
| 52 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 53 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 54 | fworkloadunitid | 工作量计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | frealcardid | 资产卡片基础资料 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 56 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 57 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 58 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0.000000 | 预计净残值 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 61 | fmonthworkload | fmonthworkload | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | fdepredeptid | fdepredeptid | int8 | 64 |  | √ | 0 |  |
| 63 | fendperiodid | fendperiodid | int8 | 64 |  | √ | 0 |  |
| 64 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 65 | frevalreservunamor | 未摊销重估准备金 | numeric | 19 | 6 | √ | 0 | 未摊销重估准备金 |
| 66 | fcurrencyrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 67 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_cf_mainpage |  | fassetbookid,fclearperiodid |
| 2 | idx_fa_card_fin_fid |  | fid |
| 3 | idx_fa_cf_realca |  | frealcardid |
| 4 | idx_fincard_period |  | forg,fdepreuseid,fperiodid |
| 5 | idx_fincard_date |  | forg,fdepreuseid,ffinaccountdate,fnumber |
| 6 | idx_fincard_number |  | fnumber |
| 7 | idx_fa_biz_end_period |  | fbizperiodid,fendperiodid,forg,fdepreuseid,fnumber |
| 8 | t_fa_card_fin_pkey |  | fentryid |
| 9 | idx_fa_cf_forgid |  | forg,fdepreuseid,fendperiodid,fnumber |
| 10 | idx_fa_cf_fassetcat |  | fassetcatid,forg,fendperiodid |

---

## 初始化资产卡片-关联追踪表 t_fa_card_real_tc

- **表名称：** 初始化资产卡片-关联追踪表
- **表名：** t_fa_card_real_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_fa_card_real_tc_tbill |  | ftbillid |
| 2 | t_fa_card_real_tc_pkey |  | fid |
| 3 | idx_fa_card_rtc_sbid |  | fsbillid |
| 4 | idx_fa_card_real_tc_tid |  | ftid |

---

## 附属设备分录-子表 t_fa_facility

- **表名称：** 附属设备分录-子表
- **表名：** t_fa_facility

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fregisterdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 6 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fassetqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 11 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_facility_pkey |  | fentryid |
| 2 | idx_fa_fac_fseq |  | fseq |

---

## 关联子实体-子表 t_fa_card_real_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_card_real_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fassetqty | fassetqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fassetqty_old | fassetqty_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_lk_pkey |  | fpkid |
| 2 | idx_fa_card_rlk_entryid |  | fid |

---

## 折旧分摊信息-子表 t_fa_card_split_entry

- **表名称：** 折旧分摊信息-子表
- **表名：** t_fa_card_split_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsplitinfo | 折旧分摊信息 | varchar | 4000 |  | √ | ' ' | 折旧分摊信息 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fpercent | 分摊比例(%) | numeric | 19 | 6 | √ | 0 | 分摊比例(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_split_entry |  | fdetailid |
| 2 | idx_fa_card_split_entry_feid |  | fentryid |

---

## 折旧分摊信息-多语言表 t_fa_card_split_entry_l

- **表名称：** 折旧分摊信息-多语言表
- **表名：** t_fa_card_split_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsplitinfo | 折旧分摊信息 | varchar | 4000 |  | √ | ' ' | 折旧分摊信息 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_split_entry_l |  | fpkid |
| 2 | idx_fa_card_sp_entry_l_fid |  | fdetailid,flocaleid |

---

## 初始化资产卡片-反写记录表 t_fa_card_real_wb

- **表名称：** 初始化资产卡片-反写记录表
- **表名：** t_fa_card_real_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | bpchar | 1 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_rwb_sbid |  | fsbillid |
| 2 | t_fa_card_real_wb_pkey |  | fentryid |

---

## 初始化资产卡片-主表 t_fa_card_real

- **表名称：** 初始化资产卡片-主表
- **表名：** t_fa_card_real

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourceentrysplitseq | 来源分录拆分序号 | int8 | 64 |  | √ | 0 | 来源分录拆分序号 |
| 3 | fisoperatelease | 经营租赁使用权资产 | bpchar | 1 |  | √ | '0' | 经营租赁使用权资产 |
| 4 | fpicturepath | 图片 | varchar | 255 |  |  | ' ' | 图片 |
| 5 | fsourceflag | 建卡方式 | varchar | 50 |  | √ | 'ADD' | 建卡方式,枚举: ADD :手工 PURCHASE :采购转固 INITIAL :初始化 IMPORT :导入 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 ENGINEERINGTRANS :工程转固 LEASECONTRACT :租赁合同 INVENTORYPROFIT :盘盈 INITLEASECONTRACT :初始化租赁合同 DATAASSET :数据资产 |
| 6 | fsrcbillentityname | 源单据标识 | varchar | 30 |  | √ | ' ' | 源单据标识 |
| 7 | fbarcoderecovery | 条形码回收 | bpchar | 1 |  | √ | ' ' | 条形码回收 |
| 8 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsourceentryid | 来源分录 | int8 | 64 |  | √ | 0 | 来源分录 |
| 10 | fheadusepersonid | 使用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 12 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 13 | fjustrealcard | 费用化资产 | bpchar | 1 |  | √ | '0' | 费用化资产 |
| 14 | fiscancel | fiscancel | bpchar | 1 |  | √ | '0' |  |
| 15 | fisstoraged | 在库资产 | bpchar | 1 |  | √ | '1' | 在库资产 |
| 16 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 19 | fbillnorecovery | 卡片编码回收 | bpchar | 1 |  | √ | ' ' | 卡片编码回收 |
| 20 | fbillno | 卡片编号 | varchar | 80 |  | √ | ' ' | 卡片编号 |
| 21 | foriginmethodid | 增减方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 24 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0 | 资产数量 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 30 | finitchangeflag | finitchangeflag | int8 | 64 |  | √ | 0 |  |
| 31 | fisinitialcard | 初始化卡片 | bpchar | 1 |  | √ | '0' | 初始化卡片 |
| 32 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 35 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 36 | frealaccountdate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 37 | fismultidept | fismultidept | varchar | 1 |  | √ | ' ' |  |
| 38 | fmaterialgroupid | fmaterialgroupid | int8 | 64 |  | √ | 0 |  |
| 39 | fbizstatus | 业务状态 | varchar | 50 |  | √ | 'ADD' | 业务状态,枚举: ADD :新增中 READY :就绪 CHG :变更中 DEPRE :折旧中 CLEAR_ALL :完全清理中 CLEAR_PART :部分清理中 DISPATCH :调拨中 SPLIT :拆分中 DELETE :作废 TRANSFERING :移交中 DRAWBACKING :退库中 DEVALUE :减值中 DEPREADJUST :折旧调整中 COLLECTING :领用中 INVENTORY :盘点中 DIFFER :盘亏盘盈中 CLEARAPPLYING :清理申请中 MERGING :合并中 REVALUATING :重估中 REVAL_MORTIZING :重估摊销中 COST_ALLOCATING :费用分摊中 |
| 40 | foriginaldata | 原始数据 | bpchar | 1 |  | √ | '0' | 原始数据 |
| 41 | fprice | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 42 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 43 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fmasterid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 47 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 48 | fnumberrecovery | 资产编码回收 | bpchar | 1 |  | √ | ' ' | 资产编码回收 |
| 49 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fassetname | 资产名称 | varchar | 255 |  |  | ' ' | 资产名称 |
| 52 | fusedate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fisfacility | 附属设备 | bpchar | 1 |  | √ | '0' | 附属设备 |
| 55 | fsourcebillnumber | 源单据编码 | varchar | 30 |  | √ | ' ' | 源单据编码 |
| 56 | fisbak | 备份卡片 | bpchar | 1 |  | √ | '0' | 备份卡片 |
| 57 | fmergedcard | 融合卡片 | bpchar | 1 |  | √ | '0' | 融合卡片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_pkey |  | fid |
| 2 | idx_fa_carrea_fnumber |  | fnumber |
| 3 | idx_fa_carrea_billno |  | fbillno |
| 4 | idx_fa_carrea_fmaster |  | fmasterid |
| 5 | idx_fa_carrea_fuseid |  | fheadusepersonid |
| 6 | idx_fa_carrea_faccdate |  | fassetunitid,fisbak,frealaccountdate,fnumber |
| 7 | idx_fa_carrea_fbarcode |  | fbarcode |
| 8 | idx_fa_carrea_ini_sel |  | foriginaldata,fassetunitid,fisinitialcard,fnumber |
| 9 | idx_fa_carrea_org |  | forgid,fisbak,fnumber |
