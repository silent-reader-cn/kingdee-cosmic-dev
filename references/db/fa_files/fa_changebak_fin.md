# 财务卡片变更备份-fa_changebak_fin

## 财务卡片变更备份-主表 t_fa_changebak_fin

- **表名称：** 财务卡片变更备份-主表
- **表名：** t_fa_changebak_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnetamount | 净额 | numeric | 23 | 10 | √ | 0.0000000000 | 净额 |
| 3 | fincometax | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 4 | faccumdepre | 累计折旧 | numeric | 23 | 10 | √ | 0.0000000000 | 累计折旧 |
| 5 | fyearorigvalchg | 本年原值变动 | numeric | 23 | 10 | √ | 0.0000000000 | 本年原值变动 |
| 6 | foriginalamount | 原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币金额 |
| 7 | fdepredamount | 已折旧期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 已折旧期间数 |
| 8 | ffinaccountdate | 财务入账日期 | timestamp | 0 |  |  | null | 财务入账日期 |
| 9 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 10 | fchangebillid | 折旧要素变更单 | int8 | 64 |  | √ | 0 | 折旧要素变更单 |
| 11 | faddupyeardepre | 本年累计折旧 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计折旧 |
| 12 | fdecval | 减值准备 | numeric | 23 | 10 | √ | 0.0000000000 | 减值准备 |
| 13 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 14 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 15 | fisneeddepre | 是否需要折旧 | bpchar | 1 |  | √ | '1' | 是否需要折旧 |
| 16 | fmonthorigvalchg | 本期原值变动 | numeric | 23 | 10 | √ | 0.0000000000 | 本期原值变动 |
| 17 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |
| 18 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 19 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 20 | fcardid | 卡片id | int8 | 64 |  | √ | 0 | 卡片id |
| 21 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 22 | fpreusingamount | 预计使用期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 预计使用期间数 |
| 23 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 24 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 25 | fpreresidualval | 预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 预计净残值 |
| 26 | foriginalval | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 27 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 28 | fnetworth | 净值 | numeric | 23 | 10 | √ | 0.0000000000 | 净值 |
| 29 | fcurrencyrate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 30 | fnumber | 资产编码 | varchar | 100 |  | √ | ' ' | 资产编码 |
| 31 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chgback_fin_frealcardid |  | frealcardid |
| 2 | t_fa_changebak_fin_pkey |  | fid |
