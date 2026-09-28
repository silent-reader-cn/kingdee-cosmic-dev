# 总机构进项待抵扣台账单据-tcvat_hz_wait_deduct_sum

## 总机构进项待抵扣台账单据-主表 t_tcvat_hz_waitdeduct_sum

- **表名称：** 总机构进项待抵扣台账单据-主表
- **表名：** t_tcvat_hz_waitdeduct_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 9 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 11 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 12 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 13 | fdeductiontype | 抵扣类型 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tcvat_bizdef |
| 14 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_waitdeduct_sum |  | fid |
| 2 | idx_tcvat_hz_waitdeduct_sum |  | forgid,fstartdate,fenddate |
