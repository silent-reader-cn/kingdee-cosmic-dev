# 毛利率波动分析表-theme_gross_margin_bill

## 毛利率波动分析表-主表 t_theme_gross_margin

- **表名称：** 毛利率波动分析表-主表
- **表名：** t_theme_gross_margin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgrossmargin | 毛利率（%） | numeric | 23 | 10 |  | null | 毛利率（%） |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostsales | 主营业务成本 | numeric | 23 | 10 |  | null | 主营业务成本 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fsalesrevenue | 主营业务收入 | numeric | 23 | 10 |  | null | 主营业务收入 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_gross_margin |  | fid |
| 2 | idx_gross_margin_report |  | freportdate,fipoorgld |
