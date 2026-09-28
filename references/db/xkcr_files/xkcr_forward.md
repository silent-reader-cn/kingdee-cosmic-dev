# 结转年末数-xkcr_forward

## 结转年末数-主表 t_xkrpt_rptitemdata

- **表名称：** 结转年末数-主表
- **表名：** t_xkrpt_rptitemdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftext | ftext | varchar | 2000 |  | √ | ' ' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 5 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fitemformulatype | fitemformulatype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 9 | fformula | fformula | varchar | 2000 |  | √ | ' ' |  |
| 10 | fdatadirect | fdatadirect | int4 | 32 |  | √ | 0 |  |
| 11 | ftranstypeid | ftranstypeid | int8 | 64 |  | √ | 0 |  |
| 12 | facctsystemid | facctsystemid | int8 | 64 |  | √ | 0 |  |
| 13 | fshared | fshared | bpchar | 1 |  | √ | '0' |  |
| 14 | frptitemid | 项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 15 | felimtypeid | felimtypeid | int8 | 64 |  | √ | 0 |  |
| 16 | fbookid | fbookid | int8 | 64 |  | √ | 0 |  |
| 17 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 18 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 19 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 20 | frptdimension | 项目维度 | varchar | 2000 |  |  | null | 项目维度 |
| 21 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 22 | fcycleid | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 23 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 24 | frpttype | 数据种类 | varchar | 10 |  | √ | ' ' | 数据种类,枚举: 1 :合并数 |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
