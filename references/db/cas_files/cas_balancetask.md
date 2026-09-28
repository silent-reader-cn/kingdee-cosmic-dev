# 日记账余额任务-cas_balancetask

## 日记账余额任务-主表 t_cas_balancetask

- **表名称：** 日记账余额任务-主表
- **表名：** t_cas_balancetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankaccountid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | fdebitamountloc | 借方金额本位币 | numeric | 23 | 10 | √ | 0 | 借方金额本位币 |
| 4 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: add :新增 delete :删除 |
| 7 | fcreditamount | 贷方金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方金额 |
| 8 | fdebitamount | 借方金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方金额 |
| 9 | fjournaltype | 日记账类型 | varchar | 50 |  | √ | ' ' | 日记账类型,枚举: bank :银行日记账 cash :现金日记账 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | ferrormessage | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 13 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: 0 :待执行 1 :执行中 2 :执行成功 3 :执行失败 |
| 14 | ferrormessage_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
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
| 1 | pk_t_cas_balancetask |  | fid |
| 2 | idx_cas_bt_fbalancetask |  | ftaskstatus |
