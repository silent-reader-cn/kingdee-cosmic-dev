# 资产卡片-fa_asset_card

## 入账时点财务信息-子表 t_fa_card_fininit

- **表名称：** 入账时点财务信息-子表
- **表名：** t_fa_card_fininit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0 | 净额 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0 | 进项税额 |
| 5 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0 | 累计折旧 |
| 6 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0 | 原币金额 |
| 9 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 10 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0 | 预计净残值 |
| 11 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 13 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0 | 资产原值 |
| 14 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0 | 净值 |
| 15 | fcurrencyrate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 16 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0 | 减值准备 |
| 17 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0 | 本年累计折旧 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_fininit_fid |  | fid |
| 2 | pk_fa_card_fininit |  | fentryid |

---

## 资产卡片-多语言表 t_fa_card_real_l

- **表名称：** 资产卡片-多语言表
- **表名：** t_fa_card_real_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 条码主档_资产_F7 bcmainfile_fa_f7 |
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

## 财务分录-子表 t_fa_card_fin

- **表名称：** 财务分录-子表
- **表名：** t_fa_card_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 4 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 5 | fyearorigvalchg | fyearorigvalchg | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdepredamount | 已折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 已折旧期间数 |
| 8 | fisdynamic | fisdynamic | bpchar | 1 |  | √ | '0' |  |
| 9 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fincomededuct | fincomededuct | bpchar | 1 |  | √ | '0' |  |
| 12 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 13 | ffincardid | 财务信息 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 14 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 15 | fmonthorigvalchg | fmonthorigvalchg | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | fbillstatus | varchar | 50 |  | √ | 'A' |  |
| 19 | fmonthdepre | fmonthdepre | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 21 | fmonthaccumdeprechg | fmonthaccumdeprechg | numeric | 19 | 6 | √ | 0 |  |
| 22 | fpreusingamount | 预计使用期间数/预计总工作量 | numeric | 19 | 6 | √ | 0.000000 | 预计使用期间数/预计总工作量 |
| 23 | fshowcurrency | 显示原币 | bpchar | 1 |  | √ | '0' | 显示原币 |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fnumber | fnumber | varchar | 100 |  |  | ' ' |  |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 29 | faddidepreamount | faddidepreamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 31 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 34 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 35 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 36 | fmonthdeprechg | fmonthdeprechg | numeric | 19 | 6 | √ | 0.000000 |  |
| 37 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 38 | fisneeddepre | fisneeddepre | bpchar | 1 |  | √ | '1' |  |
| 39 | fdeprerate | fdeprerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | 折旧方法 fa_depremethod |
| 42 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fworkloadunitid | fworkloadunitid | int8 | 64 |  | √ | 0 |  |
| 45 | frealcardid | 资产卡片基础资料 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 46 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 47 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 48 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0.000000 | 预计净残值 |
| 49 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 50 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 51 | fmonthworkload | fmonthworkload | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fdepredeptid | fdepredeptid | int8 | 64 |  | √ | 0 |  |
| 53 | fendperiodid | fendperiodid | int8 | 64 |  | √ | 0 |  |
| 54 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 55 | fcurrencyrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 56 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_cf_mainpage |  | fassetbookid,fclearperiodid |
| 2 | idx_fa_cf_realca |  | frealcardid |
| 3 | idx_fa_card_fin_fid |  | fid |
| 4 | idx_fincard_period |  | forg,fdepreuseid,fperiodid |
| 5 | idx_fincard_date |  | forg,fdepreuseid,ffinaccountdate,fnumber |
| 6 | idx_fincard_number |  | fnumber |
| 7 | idx_fa_biz_end_period |  | fbizperiodid,fendperiodid,forg,fdepreuseid,fnumber |
| 8 | t_fa_card_fin_pkey |  | fentryid |
| 9 | idx_fa_cf_forgid |  | forg,fdepreuseid,fendperiodid,fnumber |
| 10 | idx_fa_cf_fassetcat |  | fassetcatid,forg,fendperiodid |

---

## 资产卡片-关联追踪表 t_fa_card_real_tc

- **表名称：** 资产卡片-关联追踪表
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
| 6 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fassetqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 11 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
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

## 资产卡片-反写记录表 t_fa_card_real_wb

- **表名称：** 资产卡片-反写记录表
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

## 资产卡片-主表 t_fa_card_real

- **表名称：** 资产卡片-主表
- **表名：** t_fa_card_real

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourceentrysplitseq | 来源分录拆分序号 | int8 | 64 |  | √ | 0 | 来源分录拆分序号 |
| 3 | fpicturepath | 图片 | varchar | 255 |  |  | ' ' | 图片 |
| 4 | fsourceflag | 建卡方式 | varchar | 50 |  | √ | 'ADD' | 建卡方式,枚举: ADD :手工 PURCHASE :采购转固 INITIAL :初始化 IMPORT :导入 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 ENGINEERINGTRANS :工程转固 LEASECONTRACT :租赁合同 INVENTORYPROFIT :盘盈 INITLEASECONTRACT :初始化租赁合同 DATAASSET :数据资产 |
| 5 | fsrcbillentityname | 源单据标识 | varchar | 30 |  | √ | ' ' | 源单据标识 |
| 6 | fbarcoderecovery | 条形码回收 | bpchar | 1 |  | √ | ' ' | 条形码回收 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsourceentryid | 来源分录 | int8 | 64 |  | √ | 0 | 来源分录 |
| 9 | fheadusepersonid | 使用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 11 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 12 | fjustrealcard | 费用化资产 | bpchar | 1 |  | √ | '0' | 费用化资产 |
| 13 | fiscancel | fiscancel | bpchar | 1 |  | √ | '0' |  |
| 14 | fisstoraged | 在库资产 | bpchar | 1 |  | √ | '1' | 在库资产 |
| 15 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 18 | fbillnorecovery | 卡片编码回收 | bpchar | 1 |  | √ | ' ' | 卡片编码回收 |
| 19 | fbillno | 卡片编号 | varchar | 80 |  | √ | ' ' | 卡片编号 |
| 20 | foriginmethodid | 增减方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 23 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0 | 资产数量 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | finitchangeflag | finitchangeflag | int8 | 64 |  | √ | 0 |  |
| 29 | fisinitialcard | 初始化卡片 | bpchar | 1 |  | √ | '0' | 初始化卡片 |
| 30 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 33 | frealaccountdate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 34 | fismultidept | fismultidept | varchar | 1 |  | √ | ' ' |  |
| 35 | fmaterialgroupid | fmaterialgroupid | int8 | 64 |  | √ | 0 |  |
| 36 | fbizstatus | 业务状态 | varchar | 50 |  | √ | 'ADD' | 业务状态,枚举: ADD :新增中 READY :就绪 CHG :变更中 DEPRE :折旧中 CLEAR_ALL :完全清理中 CLEAR_PART :部分清理中 DISPATCH :调拨中 SPLIT :拆分中 DELETE :作废 TRANSFERING :移交中 DRAWBACKING :退库中 DEVALUE :减值中 DEPREADJUST :折旧调整中 COLLECTING :领用中 INVENTORY :盘点中 DIFFER :盘亏盘盈中 MERGING :合并中 |
| 37 | foriginaldata | 原始数据 | bpchar | 1 |  | √ | '0' | 原始数据 |
| 38 | fprice | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 39 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fmasterid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 43 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 44 | fnumberrecovery | 资产编码回收 | bpchar | 1 |  | √ | ' ' | 资产编码回收 |
| 45 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fassetname | 资产名称 | varchar | 100 |  |  | ' ' | 资产名称 |
| 48 | fusedate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fisfacility | 附属设备 | bpchar | 1 |  | √ | '0' | 附属设备 |
| 51 | fsourcebillnumber | 源单据编码 | varchar | 30 |  | √ | ' ' | 源单据编码 |
| 52 | fisbak | 备份卡片 | bpchar | 1 |  | √ | '0' | 备份卡片 |
| 53 | fmergedcard | 融合卡片 | bpchar | 1 |  | √ | '0' | 融合卡片 |

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
