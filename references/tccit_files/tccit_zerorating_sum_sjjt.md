# 不征税收入台账单据-tccit_zerorating_sum_sjjt

## 不征税收入台账单据-主表 t_tccit_zerorating_sjjt

- **表名称：** 不征税收入台账单据-主表
- **表名：** t_tccit_zerorating_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 5 | fpayregammount | 费用化支出金额 | numeric | 23 | 10 | √ | 0 | 费用化支出金额 |
| 6 | fincomedate | 取得日期 | timestamp | 0 |  |  | null | 取得日期 |
| 7 | fincomeregammount | 计入收益金额 | numeric | 23 | 10 | √ | 0 | 计入收益金额 |
| 8 | ftype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型,枚举: specialfund :专项用途财政性资金 other :其他 |
| 9 | fzeroratingamount | 其中：不征税收入 | numeric | 23 | 10 | √ | 0 | 其中：不征税收入 |
| 10 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 11 | ffiscalamount | 财政金额 | numeric | 23 | 10 | √ | 0 | 财政金额 |
| 12 | fbalanceregamount | 计入应税收入金额 | numeric | 23 | 10 | √ | 0 | 计入应税收入金额 |
| 13 | fzeroratinginamount | 不征税收入 | numeric | 23 | 10 | √ | 0 | 不征税收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_zerorating_sjjt |  | fid |
| 2 | idx_zero_org_qq_qz |  | forgid,fskssqq,fskssqz |
