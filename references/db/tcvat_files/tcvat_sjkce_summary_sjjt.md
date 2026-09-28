# 计提扣除底稿实际扣除额-tcvat_sjkce_summary_sjjt

## 计提扣除底稿实际扣除额-主表 t_tcvat_sjkce_summ_sjjt

- **表名称：** 计提扣除底稿实际扣除额-主表
- **表名：** t_tcvat_sjkce_summ_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fendamount | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |
| 4 | fbeginamount | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 5 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 6 | fnotaxamount | 免税销售额 | numeric | 23 | 10 | √ | 0 | 免税销售额 |
| 7 | fdifftypeid | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 8 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fjzjtsumamount | 服务、不动产和无形资产的计税合计 | numeric | 23 | 10 | √ | 0 | 服务、不动产和无形资产的计税合计 |
| 11 | frulecheckbox | 规则分录开关 | varchar | 50 |  | √ | ' ' | 规则分录开关,枚举: minswitch :“价税合计销售额”和“本期应扣除金额”取孰小值 equalsjkce :等于“本期实际扣除额” |
| 12 | fjzjtdeductamount | 即征即退实际扣除额 | numeric | 23 | 10 | √ | 0 | 即征即退实际扣除额 |
| 13 | fdeductamount | 本期实际扣除额 | numeric | 23 | 10 | √ | 0 | 本期实际扣除额 |
| 14 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 15 | fpredeductamount | 本期应扣除额 | numeric | 23 | 10 | √ | 0 | 本期应扣除额 |
| 16 | fjzjtynse | 即征即退应纳税额 | numeric | 23 | 10 | √ | 0 | 即征即退应纳税额 |
| 17 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 18 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 19 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 20 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 21 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_sjkce_summ_sjjt1 |  | forgid,ftaxperiod |
| 2 | pk_tcvat_sjkce_summ_sjjt |  | fid |
