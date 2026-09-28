# 清理单详情基础资料-fa_cleardetail_base

## 清理单详情基础资料-主表 t_fa_clrbillentry_d

- **表名称：** 清理单详情基础资料-主表
- **表名：** t_fa_clrbillentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 清理单 | int8 | 64 |  | √ | 0 | [清理单基础资料 fa_clearbill_base](../fa_files/fa_clearbill_base.md) |
| 2 | faddupdepre | 清理累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 清理累计折旧 |
| 3 | fnetamount | fnetamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 4 | fclearloss | fclearloss | numeric | 19 | 6 | √ | 0 |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fcleancurrency | fcleancurrency | int8 | 64 |  | √ | 0 |  |
| 7 | fclearrevenue | fclearrevenue | numeric | 19 | 6 | √ | 0 |  |
| 8 | fdepredamount | fdepredamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 9 | fisclearall | fisclearall | bpchar | 1 |  | √ | '1' |  |
| 10 | fisadjustdepre | fisadjustdepre | bpchar | 1 |  | √ | 0 |  |
| 11 | fclearrate | fclearrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fclearmethod | fclearmethod | varchar | 8 |  | √ | ' ' |  |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fdecval | fdecval | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | floctaxamountentry | floctaxamountentry | numeric | 19 | 6 | √ | 0 |  |
| 16 | ffincardid | ffincardid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 清理单号 | varchar | 30 |  | √ | ' ' | 清理单号 |
| 18 | fclearfare | 清理费用 | numeric | 19 | 6 | √ | 0.000000 | 清理费用 |
| 19 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 20 | flocclearfare | flocclearfare | numeric | 19 | 6 | √ | 0 |  |
| 21 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 22 | ftaxamount | ftaxamount | numeric | 19 | 6 | √ | 0 |  |
| 23 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 24 | fclearincome | 清理收入 | numeric | 19 | 6 | √ | 0.000000 | 清理收入 |
| 25 | frevaluationreserve | frevaluationreserve | numeric | 19 | 6 | √ | 0 |  |
| 26 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量 |
| 27 | fcompfieldsv | fcompfieldsv | varchar | 200 |  | √ | ' ' |  |
| 28 | fassetvalue | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 29 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 30 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 31 | fclearqty | 清理数量 | numeric | 19 | 6 | √ | 0.000000 | 清理数量 |
| 32 | fpreresidualval | fpreresidualval | numeric | 19 | 6 | √ | 0.000000 |  |
| 33 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | flocclearincome | flocclearincome | numeric | 19 | 6 | √ | 0 |  |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fcurrencyrate | fcurrencyrate | numeric | 19 | 6 | √ | 0 |  |
| 37 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fentrysid | 主键 | int8 | 64 |  | √ | 0 | 主键 |
| 39 | fnetval | fnetval | numeric | 19 | 6 | √ | 0.000000 |  |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | fmonthadjustdepreforcur | fmonthadjustdepreforcur | numeric | 19 | 6 | √ | 0 |  |
| 42 | fassetnumber | 资产编码 | varchar | 100 |  | √ | ' ' | 资产编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentrysid | fentrysid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_clrbillentry_d |  | fentrysid |
| 2 | idx_fa_clrbillentry_d_fid |  | fid |
| 3 | idx_fa_clrbilent_d_fentryid |  | fentryid |
