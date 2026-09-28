# 营业收入分析表-theme_co_income_bill

## 营业收入分析表-主表 t_theme_co_income

- **表名称：** 营业收入分析表-主表
- **表名：** t_theme_co_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fothercoincomeratio | 其他业务收入占比 | numeric | 23 | 10 |  | null | 其他业务收入占比 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fothercoincome | 其他业务收入 | numeric | 23 | 10 |  | null | 其他业务收入 |
| 6 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 7 | fmaincoincome | 主营业务收入 | numeric | 23 | 10 |  | null | 主营业务收入 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 10 | fmainbusinessincomeratio | 主营业务收入占比 | numeric | 23 | 10 |  | null | 主营业务收入占比 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcoincomegrowthrate | 营业收入增长率（%） | numeric | 23 | 10 |  | null | 营业收入增长率（%） |
| 13 | fcoincometotal | 营业收入合计 | numeric | 23 | 10 |  | null | 营业收入合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_co_income |  | fid |
| 2 | idx_co_income_report |  | freportdate,fipoorgld |
