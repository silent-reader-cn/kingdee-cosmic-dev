# 上市公司财报披露日期-dfa_market_company_pdate

## 上市公司财报披露日期-主表 t_dfa_marketcompany_pdate

- **表名称：** 上市公司财报披露日期-主表
- **表名：** t_dfa_marketcompany_pdate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fstock_name | 证券名称 | varchar | 50 |  | √ | ' ' | 证券名称 |
| 4 | fstock_code | 证券代码 | varchar | 50 |  | √ | ' ' | 证券代码 |
| 5 | factual_public_date | 实际披露日期 | timestamp | 0 |  |  | null | 实际披露日期 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcompany_name | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 8 | fplan_public_date | 计划披露日期 | timestamp | 0 |  |  | null | 计划披露日期 |
| 9 | fmarket_date | 首发上市日期 | timestamp | 0 |  |  | null | 首发上市日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_marketcompany_pdate |  | fid |
| 2 | idx_dfa_marketcompany_pdate |  | fstock_code |
