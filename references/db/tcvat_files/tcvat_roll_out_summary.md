# 进项税额转出台账单据-tcvat_roll_out_summary

## 进项税额转出台账单据-主表 t_tcvat_roll_out_summary

- **表名称：** 进项税额转出台账单据-主表
- **表名：** t_tcvat_roll_out_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fparentid | PID | int8 | 64 |  | √ | 0 | PID |
| 5 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 6 | fjzjtrolloutamount | 即征即退转出额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退转出额 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 10 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 |
| 11 | fdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申报金额 |
| 12 | fjzjt | 即征即退标识 | varchar | 30 |  | √ | ' ' | 即征即退标识,枚举: 0 :否 1 :是 2 :无法划分 |
| 13 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | finvoiceamount | 发票口径 | numeric | 23 | 10 | √ | 0.0000000000 | 发票口径 |
| 16 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 17 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 18 | faccountingamount | 会计口径 | numeric | 23 | 10 | √ | 0.0000000000 | 会计口径 |
| 19 | fdeclatype | 申报规则 | varchar | 30 |  | √ | ' ' | 申报规则,枚举: 1 :以会计口径申报 2 :以发票口径申报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_roll_out_summary_pkey |  | fid |
| 2 | idx_t_tcvat_roll_out_summary |  | forgid,ftaxperiod |
