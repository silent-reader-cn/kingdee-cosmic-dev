# 一般纳税人计提减税台账汇总单据-tcvat_tax_reduce_sum_sjjt

## 一般纳税人计提减税台账汇总单据-主表 t_tcvat_tax_redu_sum_sjjt

- **表名称：** 一般纳税人计提减税台账汇总单据-主表
- **表名：** t_tcvat_tax_redu_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | funiquekey | 减免税数据分组标识 | varchar | 250 |  | √ | ' ' | 减免税数据分组标识 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 9 | fbqfse | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |
| 10 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fqcye | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 14 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 15 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 16 | fbqydjse | 本期应抵减税额 | numeric | 23 | 10 | √ | 0 | 本期应抵减税额 |
| 17 | fqmye | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |
| 18 | fbqsjdjse | 本期实际抵减税额 | numeric | 23 | 10 | √ | 0 | 本期实际抵减税额 |
| 19 | fewbhxh | 二维表行序号 | varchar | 50 |  | √ | ' ' | 二维表行序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tax_redu_sum_serialno |  | forgid,ftaxperiod |
| 2 | pk_tcvat_tax_redu_sum_sjjt |  | fid |
