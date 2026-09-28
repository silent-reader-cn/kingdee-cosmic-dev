# 财务卡片初始化-fa_initcard_fin

## 财务卡片初始化-分表 t_fa_card_fin_i

- **表名称：** 财务卡片初始化-分表
- **表名：** t_fa_card_fin_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finitoriginalval | 初始资产原值 | numeric | 23 | 10 | √ | '-1' | 初始资产原值 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
| 3 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 4 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 5 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fdepredamount | 已折旧期间 | numeric | 19 | 6 | √ | 0.000000 | 已折旧期间 |
| 8 | fisdynamic | 是否动态 | bpchar | 1 |  | √ | '0' | 是否动态 |
| 9 | forg | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fincomededuct | fincomededuct | bpchar | 1 |  | √ | '0' |  |
| 12 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 13 | ffincardid | ffincardid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fclearperiodid | 清理期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 20 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 21 | fmonthaccumdeprechg | 本期累计折旧变动 | numeric | 19 | 6 | √ | 0 | 本期累计折旧变动 |
| 22 | fpreusingamount | 预计使用期间 | numeric | 19 | 6 | √ | 0.000000 | 预计使用期间 |
| 23 | fshowcurrency | 显示原币 | bpchar | 1 |  | √ | '0' | 显示原币 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fnumber | 资产编码 | varchar | 100 |  |  | ' ' | 资产编码 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 29 | faddidepreamount | 补提折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 补提折旧期间数 |
| 30 | foriginalamount | 原币原值 | numeric | 19 | 6 | √ | 0.000000 | 原币原值 |
| 31 | ffinaccountdate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 34 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 35 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 36 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 37 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 38 | fisneeddepre | 是否需要折旧 | bpchar | 1 |  | √ | '1' | 是否需要折旧 |
| 39 | fdeprerate | 本期折旧率 | numeric | 23 | 10 | √ | 0.0000000000 | 本期折旧率 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | 折旧方法 fa_depremethod |
| 42 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fworkloadunitid | 工作量计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 45 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 46 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 47 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 48 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0.000000 | 预计净残值 |
| 49 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 50 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 51 | fmonthworkload | 本期工作量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期工作量 |
| 52 | fdepredeptid | 折旧分摊部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 54 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 55 | fcurrencyrate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 56 | fcurrencyid | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 1 | t_fa_card_fin_lk_pkey |  | fpkid |
| 2 | idx_fa_card_fin_lk_fid |  | fid |

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
| 1 | idx_fa_card_fin_wb_fid |  | fid |
| 2 | t_fa_card_fin_wb_pkey |  | fentryid |

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
