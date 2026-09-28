# 进项税额转出台账单据-tcvat_roll_out_summary

## 进项税额转出台账单据-主表 t_tcvat_roll_out_summary

- **表名称：** 进项税额转出台账单据-主表
- **表名：** t_tcvat_roll_out_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 4 | fjzjtrolloutamount | 即征即退转出额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退转出额 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 8 | fdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申报金额 |
| 9 | fjzjt | 即征即退标识 | varchar | 30 |  | √ | ' ' | 即征即退标识,枚举: 0 :否 1 :是 2 :无法划分 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 13 | faccountingamount | 会计口径 | numeric | 23 | 10 | √ | 0.0000000000 | 会计口径 |
| 14 | famountsum | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 15 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fparentid | PID | int8 | 64 |  | √ | 0 | PID |
| 18 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 19 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fdescription | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 21 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 9 :纳税检查调减进项税 10 :上期留抵税额抵减欠税 11 :上期留抵税额退税 12 :异常凭证转出进项税额 |
| 22 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 23 | finvoiceamount | 发票口径 | numeric | 23 | 10 | √ | 0.0000000000 | 发票口径 |
| 24 | fjzjtamount | 即征即退销售额 | numeric | 23 | 10 | √ | 0 | 即征即退销售额 |
| 25 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 26 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 27 | fdeclatype | 申报规则 | varchar | 30 |  | √ | ' ' | 申报规则,枚举: 1 :以会计口径申报 2 :以发票口径申报 |
| 28 | fsplitrate | 划分比例 | numeric | 23 | 10 | √ | 0 | 划分比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_roll_out_summary_pkey |  | fid |
| 2 | idx_t_tcvat_roll_out_summary |  | forgid,ftaxperiod |
