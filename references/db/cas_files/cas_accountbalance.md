# 银行账户余额-cas_accountbalance

## 银行账户余额-主表 t_cas_accountbalance

- **表名称：** 银行账户余额-主表
- **表名：** t_cas_accountbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankaccountid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 3 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fdebitamountloc | 借方金额本位币 | numeric | 23 | 10 | √ | 0 | 借方金额本位币 |
| 5 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdaybalanceloc | 期初余额本位币 | numeric | 23 | 10 | √ | 0 | 期初余额本位币 |
| 7 | fcreditamount | 贷方金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方金额 |
| 8 | famount | 余额 | numeric | 23 | 10 | √ | 0.0000000000 | 余额 |
| 9 | fdebitamount | 借方金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方金额 |
| 10 | fdaytradeamount | 当天交易金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当天交易金额 |
| 11 | fdaybalance | 期初余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额 |
| 12 | famountloc | 余额本位币 | numeric | 23 | 10 | √ | 0 | 余额本位币 |
| 13 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fdaytradenum | 当天交易笔数 | int8 | 64 |  | √ | 0 | 当天交易笔数 |
| 16 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fcreditamountloc | 贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 贷方金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_accountbalance |  | fid |
