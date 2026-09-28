# 总机构差额扣除本期实际扣除台账单据-tcvat_hz_sjkce_summary

## 总机构差额扣除本期实际扣除台账单据-主表 t_tcvat_hz_sjkce_summary

- **表名称：** 总机构差额扣除本期实际扣除台账单据-主表
- **表名：** t_tcvat_hz_sjkce_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendamount | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |
| 3 | fbeginamount | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 4 | fnotaxamount | 免税销售额 | numeric | 23 | 10 | √ | 0 | 免税销售额 |
| 5 | fdifftypeid | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 6 | fserialno | 流水号 | varchar | 200 |  | √ | ' ' | 流水号 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fjzjtsumamount | 服务、不动产和无形资产的计税合计 | numeric | 23 | 10 | √ | 0 | 服务、不动产和无形资产的计税合计 |
| 9 | frulecheckbox | 规则分录开关 | varchar | 50 |  | √ | ' ' | 规则分录开关,枚举: minswitch :“价税合计销售额”和“本期应扣除金额”取孰小值 equalsjkce :等于“本期实际扣除额” |
| 10 | fjzjtdeductamount | 即征即退实际扣除额 | numeric | 23 | 10 | √ | 0 | 即征即退实际扣除额 |
| 11 | fdeductamount | 本期实际扣除额 | numeric | 23 | 10 | √ | 0 | 本期实际扣除额 |
| 12 | fpredeductamount | 本期应扣除额 | numeric | 23 | 10 | √ | 0 | 本期应扣除额 |
| 13 | fjzjtynse | 即征即退应纳税额 | numeric | 23 | 10 | √ | 0 | 即征即退应纳税额 |
| 14 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 15 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 16 | fdeadline | 缴纳期限 | varchar | 200 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 17 | ftaxpayertype | 纳税人类型 | varchar | 200 |  | √ | ' ' | 纳税人类型 |
| 18 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 19 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 20 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_sjkce_summary |  | fid |
