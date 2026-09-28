# 弥补以前年度亏损计算底稿单据-tccit_dg_b105060_sum

## 弥补以前年度亏损计算底稿单据-主表 t_tccit_dg_b105060_sum

- **表名称：** 弥补以前年度亏损计算底稿单据-主表
- **表名：** t_tccit_dg_b105060_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 亏损企业类型名称 | varchar | 50 |  | √ | ' ' | 亏损企业类型名称 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行 count :合计 |
| 5 | fflzcje | 分立转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分立转出金额 |
| 6 | fksdqnd | 亏损到期年度 | int8 | 64 |  | √ | 0 | 亏损到期年度 |
| 7 | fhappenyear | 发生年度 | int8 | 64 |  | √ | 0 | 发生年度 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 9 | fymbksje | 已弥补亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已弥补亏损金额 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fyjjznx | 预计结转年限（年） | int8 | 64 |  | √ | 0 | 预计结转年限（年） |
| 12 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 13 | fdnkjzyhndksje | 当年可结转以后年度亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年可结转以后年度亏损金额 |
| 14 | fsyjnsdmb | 使用境内所得弥补 | numeric | 23 | 10 | √ | 0.0000000000 | 使用境内所得弥补 |
| 15 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | flossmoney | 亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 亏损金额 |
| 17 | fbnkmbksje | 本年可弥补亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年可弥补亏损金额 |
| 18 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 19 | flossqiyetype | 亏损企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 20 | fnumber | 亏损企业编码 | varchar | 50 |  | √ | ' ' | 亏损企业编码 |
| 21 | flosstype | 亏损类型 | varchar | 50 |  | √ | ' ' | 亏损类型,枚举: jnsd :境内所得额亏损 zr :合并、分立转入亏损额 |
| 22 | fbillno | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |
| 23 | fsyjwsdmb | 使用境外所得弥补 | numeric | 23 | 10 | √ | 0.0000000000 | 使用境外所得弥补 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_dg_b105060_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_dg_b105060_sum |  | fid |
