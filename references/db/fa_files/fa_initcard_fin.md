# 财务卡片初始化-fa_initcard_fin

## 财务卡片初始化-分表 t_fa_card_fin_i

- **表名称：** 财务卡片初始化-分表
- **表名：** t_fa_card_fin_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finitoriginalval | 初始资产原值 | numeric | 23 | 10 | √ | '-1' | 初始资产原值 |
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

## 财务卡片初始化-主表 t_fa_card_fin

- **表名称：** 财务卡片初始化-主表
- **表名：** t_fa_card_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 关联资产卡片id | int8 | 64 |  | √ | 0 | 关联资产卡片id |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | flimitcalculate | 按照企业所得税法计算折旧限额 | bpchar | 1 |  | √ | '0' | 按照企业所得税法计算折旧限额 |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 5 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 6 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fdeprelimit | 税法折旧限额 | numeric | 19 | 6 | √ | 0 | 税法折旧限额 |
| 9 | fuseperiod | 使用年期间数 | numeric | 19 | 6 | √ | 0 | 使用年期间数 |
| 10 | fdepredamount | 已折旧期间 | numeric | 19 | 6 | √ | 0.000000 | 已折旧期间 |
| 11 | fisdynamic | 是否动态 | bpchar | 1 |  | √ | '0' | 是否动态 |
| 12 | forg | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fisdyndepre | fisdyndepre | bpchar | 1 |  | √ | '0' |  |
| 15 | fincomededuct | fincomededuct | bpchar | 1 |  | √ | '0' |  |
| 16 | fissupplement | 是否中途补录 | bpchar | 1 |  | √ | '0' | 是否中途补录 |
| 17 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 18 | ffincardid | ffincardid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 21 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 22 | fclearperiodid | 清理期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | fmaxrelvaluateamt | 重估最高限额 | numeric | 19 | 6 | √ | 0 | 重估最高限额 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 26 | frevaluationreserve | 重估准备金 | numeric | 19 | 6 | √ | 0 | 重估准备金 |
| 27 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 28 | fbeginyearamount | 年初折旧金额 | numeric | 19 | 6 | √ | 0 | 年初折旧金额 |
| 29 | fmonthaccumdeprechg | 本期累计折旧变动 | numeric | 19 | 6 | √ | 0 | 本期累计折旧变动 |
| 30 | fpreusingamount | 预计使用期间 | numeric | 19 | 6 | √ | 0.000000 | 预计使用期间 |
| 31 | fshowcurrency | 显示原币 | bpchar | 1 |  | √ | '0' | 显示原币 |
| 32 | frevalreservamor | 已摊销重估准备金 | numeric | 19 | 6 | √ | 0 | 已摊销重估准备金 |
| 33 | fisneerevaluate | fisneerevaluate | bpchar | 1 |  | √ | '0' |  |
| 34 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 35 | fnumber | 资产编码 | varchar | 100 |  |  | ' ' | 资产编码 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 39 | faddidepreamount | 补提折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 补提折旧期间数 |
| 40 | foriginalamount | 原币原值 | numeric | 19 | 6 | √ | 0.000000 | 原币原值 |
| 41 | ffinaccountdate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 44 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 45 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 46 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 47 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 48 | fisneeddepre | 是否需要折旧 | bpchar | 1 |  | √ | '1' | 是否需要折旧 |
| 49 | fdeprerate | 本期折旧率 | numeric | 23 | 10 | √ | 0.0000000000 | 本期折旧率 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |
| 52 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fworkloadunitid | 工作量计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 56 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 57 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 58 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0.000000 | 预计净残值 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 61 | fmonthworkload | 本期工作量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期工作量 |
| 62 | fdepredeptid | 折旧分摊部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 64 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 65 | frevalreservunamor | 未摊销重估准备金 | numeric | 19 | 6 | √ | 0 | 未摊销重估准备金 |
| 66 | fcurrencyrate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 67 | fcurrencyid | 原币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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

## 关联子实体-子表 t_fa_card_fin_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_card_fin_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_fin_lk_fid |  | fid |
| 2 | t_fa_card_fin_lk_pkey |  | fpkid |

---

## 财务卡片初始化-反写记录表 t_fa_card_fin_wb

- **表名称：** 财务卡片初始化-反写记录表
- **表名：** t_fa_card_fin_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
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
| 1 | t_fa_card_fin_wb_pkey |  | fentryid |
| 2 | idx_fa_card_fin_wb_fid |  | fid |

---

## 财务卡片初始化-关联追踪表 t_fa_card_fin_tc

- **表名称：** 财务卡片初始化-关联追踪表
- **表名：** t_fa_card_fin_tc

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
| 1 | idx_fa_card_fin_tc_tbill |  | ftbillid |
| 2 | t_fa_card_fin_tc_pkey |  | fid |
| 3 | idx_fa_card_fin_tc_tid |  | ftid |
| 4 | idx_fa_card_fin_tc_fsbillid |  | fsbillid |
| 5 | idx_fa_card_fin_tc_ftbillid |  | ftbillid |
