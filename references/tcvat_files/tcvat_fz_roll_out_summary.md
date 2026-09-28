# 分支进项税额转出台账单据-tcvat_fz_roll_out_summary

## 分支进项税额转出台账单据-主表 t_tcvat_fz_rolloutsummary

- **表名称：** 分支进项税额转出台账单据-主表
- **表名：** t_tcvat_fz_rolloutsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fparentid | PID | int8 | 64 |  | √ | 0 | PID |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | fjzjtrolloutamount | 即征即退转出额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退转出额 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdescription | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 9 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 |
| 10 | fdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申报金额 |
| 11 | fjzjt | 即征即退标识 | varchar | 30 |  | √ | ' ' | 即征即退标识,枚举: 0 :否 1 :是 2 :无法划分 |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 16 | finvoiceamount | 发票口径 | numeric | 23 | 10 | √ | 0.0000000000 | 发票口径 |
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
| 1 | idx_tcvat_fz_rolloutsummary |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_fz_rolloutsummary |  | fid |
