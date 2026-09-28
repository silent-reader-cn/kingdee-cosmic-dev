# 一般纳税人计提进项税额转出台账单据-tcvat_roll_out_sum_sjjt

## 一般纳税人计提进项税额转出台账单据-主表 t_tcvat_roll_out_sum_sjjt

- **表名称：** 一般纳税人计提进项税额转出台账单据-主表
- **表名：** t_tcvat_roll_out_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 4 | ftaxperioddate | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 5 | fjzjtrolloutamount | 即征即退转出额 | numeric | 23 | 10 | √ | 0 | 即征即退转出额 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 9 | fdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0 | 申报金额 |
| 10 | fjzjt | 即征即退标识 | varchar | 50 |  | √ | ' ' | 即征即退标识,枚举: 0 :否 1 :是 2 :无法划分 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 14 | faccountingamount | 转出税额 | numeric | 23 | 10 | √ | 0 | 转出税额 |
| 15 | famountsum | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 16 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | PID | int8 | 64 |  | √ | 0 | PID |
| 19 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 20 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 21 | fdescription | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 22 | frollouttype | 进项转出类型 | varchar | 50 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 9 :纳税检查调减进项税 10 :上期留抵税额抵减欠税 11 :上期留抵税额退税 12 :异常凭证转出进项税额 |
| 23 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 24 | finvoiceamount | 发票口径 | numeric | 23 | 10 | √ | 0 | 发票口径 |
| 25 | fjzjtamount | 即征即退销售额 | numeric | 23 | 10 | √ | 0 | 即征即退销售额 |
| 26 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 27 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 28 | fdeclatype | 申报规则 | varchar | 50 |  | √ | ' ' | 申报规则,枚举: 1 :以会计口径申报 2 :以发票口径申报 |
| 29 | fsplitrate | 划分比例 | numeric | 23 | 10 | √ | 0 | 划分比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_roll_out_sum_serialno |  | forgid,ftaxperiod |
| 2 | pk_tcvat_roll_out_sum_sjjt |  | fid |
