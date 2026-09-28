# 辅助账余额(包含未过账原币)-ds_assistbalance_1f

## 辅助账余额(包含未过账原币)-主表 t_ds_assistbalance_1f

- **表名称：** 辅助账余额(包含未过账原币)-主表
- **表名：** t_ds_assistbalance_1f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fendbalancelocal | 期末余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额本位币 |
| 3 | fdebitfor | 本期借方发生原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方发生原币 |
| 4 | fcreditlocal | 本期贷方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方本位币 |
| 5 | fbeginbalancerpt | 期初余额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额报告币 |
| 6 | fassistgrpid2 | 辅助账ID | varchar | 100 |  | √ | ' ' | 辅助账ID |
| 7 | fbeginbalancelocal | 初始余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 初始余额本位币 |
| 8 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |
| 9 | fcreditrpt | 本期贷方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方报告币 |
| 10 | fcreditqty | 本期贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方数量 |
| 11 | fendbalancerpt | 期末余额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额报告币 |
| 12 | fassistgrpid | 辅助账核算项目组合 | varchar | 400 |  | √ | ' ' | 辅助账核算项目组合 |
| 13 | fbeginqty | 期初数量余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量余额 |
| 14 | fyeardebitrpt | 本年累计借方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方报告币 |
| 15 | fyeardebitqty | 本年累计借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方数量 |
| 16 | fyearcreditfor | 本年累计贷方原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方原币 |
| 17 | fyeardebitlocal | 本年累计借方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方本位币 |
| 18 | forgunitid | 公司 | varchar | 100 |  | √ | ' ' | 公司 |
| 19 | fmonthpnlfor | 本期损益发生额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额原币 |
| 20 | fperiodid | 期间 | varchar | 100 |  | √ | ' ' | 期间 |
| 21 | fbeginbalancefor | 初始余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 初始余额原币 |
| 22 | fbizkey | 业务联查关键字 | varchar | 400 |  | √ | ' ' | 业务联查关键字 |
| 23 | fyearpnlrpt | 本年损益发生额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额报告币 |
| 24 | fbaltype | 余额类型 | varchar | 30 |  |  | ' ' | 余额类型,枚举: 1 :保存后余额 5 :过账后余额 |
| 25 | fyearcreditrpt | 本年累计贷方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方报告币 |
| 26 | fyearcreditqty | 本年累计贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方数量 |
| 27 | fdebitlocal | 本期借方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方本位币 |
| 28 | faccountid2 | 科目ID | varchar | 100 |  | √ | ' ' | 科目ID |
| 29 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 30 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | 来源系统 ds_srcsys |
| 31 | fyearpnlfor | 本年损益发生额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额原币 |
| 32 | fendqty | 期末数量余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末数量余额 |
| 33 | fdetailcount | 本期发生次数 | int8 | 64 |  | √ | 0 | 本期发生次数 |
| 34 | fyearpnllocal | 本年损益发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年损益发生额本位币 |
| 35 | fmonthpnlrpt | 本期损益发生额报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额报告币 |
| 36 | fyeardebitfor | 本年累计借方原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方原币 |
| 37 | fdebitrpt | 本期借方报告币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方报告币 |
| 38 | fdebitqty | 本期借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期借方数量 |
| 39 | fyearcreditlocal | 本年累计贷方本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方本位币 |
| 40 | fendbalancefor | 期末余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额原币 |
| 41 | fcreditfor | 本期贷方发生原币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期贷方发生原币 |
| 42 | fmonthpnllocal | 本期损益发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期损益发生额本位币 |
| 43 | fcurrencyid | 币别 | varchar | 100 |  | √ | ' ' | 币别 |
| 44 | faccountid | 科目 | varchar | 100 |  | √ | ' ' | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_assistbalance_1f_key |  | faccountid,fcurrencyid,forgunitid,fperiodid |
| 2 | idx_ds_assistbalance_1f_soid |  | fsoid |
| 3 | t_ds_assistbalance_1f_pkey |  | fid |
