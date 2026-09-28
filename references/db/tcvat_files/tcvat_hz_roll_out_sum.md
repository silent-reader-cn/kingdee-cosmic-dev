# 总机构进项税额转出台账单据-tcvat_hz_roll_out_sum

## 总机构进项税额转出台账单据-主表 t_tcvat_hz_roll_out_sum

- **表名称：** 总机构进项税额转出台账单据-主表
- **表名：** t_tcvat_hz_roll_out_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjzjtrolloutamount | 即征即退转出额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退转出额 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申报金额 |
| 6 | fjzjt | 即征即退标识 | varchar | 30 |  | √ | ' ' | 即征即退标识,枚举: 0 :否 1 :是 2 :无法划分 |
| 7 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 11 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 12 | faccountingamount | 会计口径 | numeric | 23 | 10 | √ | 0.0000000000 | 会计口径 |
| 13 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | famountsum | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fparentid | PID | int8 | 64 |  | √ | 0 | PID |
| 17 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 18 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 2 :汇总 3 :被汇总 |
| 19 | fdescription | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 20 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 |
| 21 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 22 | finvoiceamount | 发票口径 | numeric | 23 | 10 | √ | 0.0000000000 | 发票口径 |
| 23 | fjzjtamount | 即征即退销售额 | numeric | 23 | 10 | √ | 0 | 即征即退销售额 |
| 24 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 25 | fdeclatype | 申报规则 | varchar | 30 |  | √ | ' ' | 申报规则,枚举: 1 :以会计口径申报 2 :以发票口径申报 |
| 26 | fsplitrate | 划分比例 | numeric | 23 | 10 | √ | 0 | 划分比例 |
| 27 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_roll_out_sum |  | fid |
| 2 | idx_tcvat_hz_roll_out_sum |  | forgid,fstartdate,fenddate |
