# 现金账户余额-cas_cashbalance

## 现金账户余额-主表 t_cas_cashbalance

- **表名称：** 现金账户余额-主表
- **表名：** t_cas_cashbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebitamountloc | 借方金额本位币 | numeric | 23 | 10 | √ | 0 | 借方金额本位币 |
| 3 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdaybalanceloc | 期初余额本位币 | numeric | 23 | 10 | √ | 0 | 期初余额本位币 |
| 5 | fcashaccountid | 现金账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 6 | fcreditamount | 贷方金额 | numeric | 23 | 10 | √ | 0 | 贷方金额 |
| 7 | famount | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 8 | fdebitamount | 借方金额 | numeric | 23 | 10 | √ | 0 | 借方金额 |
| 9 | fdaytradeamount | 当天交易金额 | numeric | 23 | 10 | √ | 0 | 当天交易金额 |
| 10 | fdaybalance | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 11 | famountloc | 余额本位币 | numeric | 23 | 10 | √ | 0 | 余额本位币 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fdaytradenum | 当天交易笔数 | int4 | 32 |  |  | null | 当天交易笔数 |
| 15 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fcreditamountloc | 贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 贷方金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_cashbalance |  | fid |
