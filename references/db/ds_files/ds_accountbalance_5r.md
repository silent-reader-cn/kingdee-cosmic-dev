# 科目余额(过账报告币)-ds_accountbalance_5r

## 科目余额(过账报告币)-主表 t_ds_accountbalance_5r

- **表名称：** 科目余额(过账报告币)-主表
- **表名：** t_ds_accountbalance_5r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fendbalancelocal | 期末余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额本位币 |
| 3 | fdebitfor | 本期借方发生原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方发生原币 |
| 4 | fcreditlocal | 本期贷方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方本位币 |
| 5 | fbeginbalancerpt | 期初余额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额报告币 |
| 6 | fbeginbalancelocal | 初始余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 初始余额本位币 |
| 7 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |
| 8 | fcreditrpt | 本期贷方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方报告币 |
| 9 | fcreditqty | 本期贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方数量 |
| 10 | fendbalancerpt | 期末余额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额报告币 |
| 11 | fbeginqty | 期初数量余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量余额 |
| 12 | fyeardebitrpt | 本年累计借方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方报告币 |
| 13 | fyeardebitqty | 本年累计借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方数量 |
| 14 | fyearcreditfor | 本年累计贷方原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方原币 |
| 15 | fyeardebitlocal | 本年累计借方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方本位币 |
| 16 | forgunitid | 公司 | varchar | 100 |  | √ | ' ' | 公司 |
| 17 | fmonthpnlfor | 本期损益发生额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额原币 |
| 18 | fperiodid | 期间 | varchar | 100 |  | √ | ' ' | 期间 |
| 19 | fbeginbalancefor | 初始余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 初始余额原币 |
| 20 | fbizkey | 业务联查关键字 | varchar | 400 |  |  | ' ' | 业务联查关键字 |
| 21 | fyearpnlrpt | 本年损益发生额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额报告币 |
| 22 | fbaltype | 余额类型 | varchar | 30 |  | √ | ' ' | 余额类型,枚举: 1 :保存后余额 5 :过账后余额 |
| 23 | fyearcreditrpt | 本年累计贷方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方报告币 |
| 24 | fyearcreditqty | 本年累计贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方数量 |
| 25 | fdebitlocal | 本期借方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方本位币 |
| 26 | faccountid2 | 科目ID | varchar | 100 |  | √ | ' ' | 科目ID |
| 27 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 28 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | [来源系统 ds_srcsys](../ds_files/ds_srcsys.md) |
| 29 | fyearpnlfor | 本年损益发生额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额原币 |
| 30 | fendqty | 期末数量余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末数量余额 |
| 31 | fdetailcount | 本期发生次数 | int8 | 64 |  | √ | 0 | 本期发生次数 |
| 32 | fyearpnllocal | 本年损益发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额本位币 |
| 33 | fmonthpnlrpt | 本期损益发生额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额报告币 |
| 34 | fyeardebitfor | 本年累计借方原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方原币 |
| 35 | fdebitrpt | 本期借方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方报告币 |
| 36 | fdebitqty | 本期借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方数量 |
| 37 | fyearcreditlocal | 本年累计贷方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方本位币 |
| 38 | fendbalancefor | 期末余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额原币 |
| 39 | fcreditfor | 本期贷方发生原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方发生原币 |
| 40 | fmonthpnllocal | 本期损益发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额本位币 |
| 41 | fcurrencyid | 币种 | varchar | 100 |  | √ | ' ' | 币种 |
| 42 | faccountid | 科目 | varchar | 100 |  | √ | ' ' | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_accountbalance_5r_soid |  | fsoid |
| 2 | idx_ds_accountbalance_5r_key |  | faccountid,fcurrencyid,forgunitid,fperiodid |
| 3 | t_ds_accountbalance_5r_pkey |  | fid |
