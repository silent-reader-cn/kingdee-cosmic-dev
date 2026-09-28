# 分支即征即退进项税额明细-tcvat_fz_jzjtjxsemx

## 分支即征即退进项税额明细-主表 t_tcvat_fz_jzjtjxsemx

- **表名称：** 分支即征即退进项税额明细-主表
- **表名：** t_tcvat_fz_jzjtjxsemx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fhfbl | 划分比例 | numeric | 23 | 10 | √ | 0.0000000000 | 划分比例 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcurrentsigntaxamount | 本次标识税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次标识税额 |
| 6 | fvoucherno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 9 | fjzjtxse | 即征即退销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退销售额 |
| 10 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fconsumertype | 用途标识 | varchar | 30 |  | √ | ' ' | 用途标识,枚举: 5 :无法划分标识 4 :即征即退标识 |
| 12 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 15 :通行费电子发票 2 :电子专票 4 :纸质专票 |
| 13 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 15 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 16 | finvoicecode | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 17 | ftaxdeductionid | 抵扣台账ID | int8 | 64 |  | √ | 0 | 抵扣台账ID |
| 18 | finputauthid | 进项标示id | int8 | 64 |  | √ | 0 | 进项标示id |
| 19 | fdeductiontype | 抵扣类型 | varchar | 30 |  | √ | ' ' | 抵扣类型,枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 |
| 20 | fxsehe | 销售额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额合计 |
| 21 | fjzjsjxse | 即征即退进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退进项税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_jzjtjxsemx |  | forgid,fenddate,fstartdate |
| 2 | pk_tcvat_fz_jzjtjxsemx |  | fid |
