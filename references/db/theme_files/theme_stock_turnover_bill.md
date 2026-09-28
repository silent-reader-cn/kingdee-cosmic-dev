# 存货周转分析表-theme_stock_turnover_bill

## 存货周转分析表-主表 t_theme_stock_turnover

- **表名称：** 存货周转分析表-主表
- **表名：** t_theme_stock_turnover

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbusinessincome | 营业成本 | numeric | 23 | 10 |  | null | 营业成本 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstockturnoverrate | 存货周转率（次/年） | numeric | 23 | 10 |  | null | 存货周转率（次/年） |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fstockbookbalance | 存货账面余额 | numeric | 23 | 10 |  | null | 存货账面余额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_stock_turnover_report |  | fipoorgld,freportdate |
| 2 | pk_theme_stock_turnover |  | fid |
