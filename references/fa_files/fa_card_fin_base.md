# 财务卡片基础资料-fa_card_fin_base

## 财务卡片基础资料-分表 t_fa_card_fin_i

- **表名称：** 财务卡片基础资料-分表
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

## 财务卡片基础资料-主表 t_fa_card_fin

- **表名称：** 财务卡片基础资料-主表
- **表名：** t_fa_card_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 4 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 5 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fdepredamount | 已折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 已折旧期间数 |
| 8 | fisdynamic | 是否动态 | bpchar | 1 |  | √ | '0' | 是否动态 |
| 9 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fincomededuct | fincomededuct | bpchar | 1 |  | √ | '0' |  |
| 12 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 13 | ffincardid | ffincardid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 20 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 21 | fmonthaccumdeprechg | fmonthaccumdeprechg | numeric | 19 | 6 | √ | 0 |  |
| 22 | fpreusingamount | 预计使用期间数 | numeric | 19 | 6 | √ | 0.000000 | 预计使用期间数 |
| 23 | fshowcurrency | fshowcurrency | bpchar | 1 |  | √ | '0' |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fnumber | 资产编码 | varchar | 100 |  |  | ' ' | 资产编码 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 29 | faddidepreamount | 补提折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 补提折旧期间数 |
| 30 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 31 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fchangebillid | 折旧要素变更单 | int8 | 64 |  | √ | 0 | 折旧要素变更单 |
| 34 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 35 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 36 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 37 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 38 | fisneeddepre | 是否需要折旧 | bpchar | 1 |  | √ | '1' | 是否需要折旧 |
| 39 | fdeprerate | fdeprerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | 折旧方法 fa_depremethod |
| 42 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fworkloadunitid | fworkloadunitid | int8 | 64 |  | √ | 0 |  |
| 45 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 46 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 47 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 48 | fpreresidualval | 预计净残值 | numeric | 19 | 6 | √ | 0.000000 | 预计净残值 |
| 49 | fbasecurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 50 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 51 | fmonthworkload | 本期工作量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期工作量 |
| 52 | fdepredeptid | 折旧分摊部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
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
