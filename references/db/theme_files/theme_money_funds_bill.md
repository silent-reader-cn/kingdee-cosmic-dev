# 货币资金结构分析表-theme_money_funds_bill

## 货币资金结构分析表-主表 t_theme_money_funds

- **表名称：** 货币资金结构分析表-主表
- **表名：** t_theme_money_funds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fothermonetarycapital | 其他货币资金 | numeric | 23 | 10 |  | null | 其他货币资金 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbankdeposit | 银行存款 | numeric | 23 | 10 |  | null | 银行存款 |
| 6 | fperiodendratio | 比上期末(%) | numeric | 23 | 10 |  | null | 比上期末(%) |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fbankdepositratio | 银行存款占比(%) | numeric | 23 | 10 |  | null | 银行存款占比(%) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 11 | fothercapitalrati | 其他货币资金占比(%) | numeric | 23 | 10 |  | null | 其他货币资金占比(%) |
| 12 | fcash | 库存现金 | numeric | 23 | 10 |  | null | 库存现金 |
| 13 | frestrictedfundsratio | 其中：受限资金占比(%) | numeric | 23 | 10 |  | null | 其中：受限资金占比(%) |
| 14 | famountto | 合计 | numeric | 23 | 10 |  | null | 合计 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcashrate | 库存现金占比(%) | numeric | 23 | 10 |  | null | 库存现金占比(%) |
| 17 | frestrictedfunds | 其中：受限资金 | numeric | 23 | 10 |  | null | 其中：受限资金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_money_funds |  | fid |
| 2 | idx_money_funds_report |  | fipoorgld,freportdate |
