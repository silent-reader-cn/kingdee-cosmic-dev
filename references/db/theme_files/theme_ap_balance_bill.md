# 应付款余额变动分析表-theme_ap_balance_bill

## 应付款余额变动分析表-主表 t_theme_ap_balance_change

- **表名称：** 应付款余额变动分析表-主表
- **表名：** t_theme_ap_balance_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fapbookbalancerate | 应付账款增长率(%) | numeric | 23 | 10 |  | null | 应付账款增长率(%) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | finventorybookbalarate | 存货增长率(%) | numeric | 23 | 10 |  | null | 存货增长率(%) |
| 6 | finventorybookbalance | 存货账面余额 | numeric | 23 | 10 |  | null | 存货账面余额 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fapbookbalance | 应付账款账面余额 | numeric | 23 | 10 |  | null | 应付账款账面余额 |
| 9 | foriginbuybalance | 原材料采购金额 | numeric | 23 | 10 |  | null | 原材料采购金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | foriginbuybalancerate | 应付账款占原材料当期采购金额比(%) | numeric | 23 | 10 |  | null | 应付账款占原材料当期采购金额比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_balance_change_report |  | freportdate,fipoorgld |
| 2 | pk_theme_ap_balance_change |  | fid |
