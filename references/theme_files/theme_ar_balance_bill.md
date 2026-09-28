# 应收款余额变动分析表-theme_ar_balance_bill

## 应收款余额变动分析表-主表 t_theme_ar_balance_change

- **表名称：** 应收款余额变动分析表-主表
- **表名：** t_theme_ar_balance_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbaddebtavgrate | 坏账准备平均计提率（%） | numeric | 23 | 10 |  | null | 坏账准备平均计提率（%） |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbaddebt | 坏账准备 | numeric | 23 | 10 |  | null | 坏账准备 |
| 5 | farbookamount | 应收账款账面价值 | numeric | 23 | 10 |  | null | 应收账款账面价值 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbiratio | 应收账款余额占营业收入比例（%） | numeric | 23 | 10 |  | null | 应收账款余额占营业收入比例（%） |
| 8 | farbookbalance | 应收账款账面余额 | numeric | 23 | 10 |  | null | 应收账款账面余额 |
| 9 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 10 | farturnoverrate | 应收账款周转率（次/年） | numeric | 23 | 10 |  | null | 应收账款周转率（次/年） |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbusinessincome | 营业收入 | numeric | 23 | 10 |  | null | 营业收入 |
| 15 | farriseratio | 应收账款增长率（%） | numeric | 23 | 10 |  | null | 应收账款增长率（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_balance_change_report |  | fipoorgld,freportdate |
| 2 | pk_theme_ar_balance_change |  | fid |
