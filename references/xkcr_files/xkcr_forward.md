# 结转年末数-xkcr_forward

## 结转年末数-主表 t_xkrpt_rptitemdata

- **表名称：** 结转年末数-主表
- **表名：** t_xkrpt_rptitemdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsystemid | facctsystemid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | 金额单位 xkbd_amountunit |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fshared | fshared | bpchar | 1 |  | √ | '0' |  |
| 7 | frptitemid | 项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 8 | felimtypeid | felimtypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 10 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 11 | fitemformulatype | fitemformulatype | bpchar | 1 |  | √ | ' ' |  |
| 12 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 13 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 14 | fformula | fformula | varchar | 2000 |  | √ | ' ' |  |
| 15 | frptdimension | frptdimension | text | 0 |  |  | ' ' |  |
| 16 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 17 | fdatadirect | fdatadirect | int4 | 32 |  | √ | 0 |  |
| 18 | fcycleid | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 19 | frpttype | 数据种类 | bpchar | 10 |  | √ | ' ' | 数据种类,枚举: 1 :合并数 |
| 20 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | ftranstypeid | ftranstypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rptitemdata |  | fid |
| 2 | idx_xkrpt_rptid_yearperiod |  | fyear,fperiod |
| 3 | idx_xkrpt_rptid_rptitemid |  | frptitemid |
