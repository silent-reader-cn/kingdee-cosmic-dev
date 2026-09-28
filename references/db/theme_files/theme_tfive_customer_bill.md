# 收入前五大客户依赖分析表-theme_tfive_customer_bill

## 收入前五大客户依赖分析表-主表 t_theme_tfive_customer

- **表名称：** 收入前五大客户依赖分析表-主表
- **表名：** t_theme_tfive_customer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcustomer | 单位名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccounttype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :合计 |
| 8 | fratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 9 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 10 | fsalesrevenue | 销售收入 | numeric | 23 | 10 |  | null | 销售收入 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tfive_customer_report |  | freportdate,fipoorgld |
| 2 | pk_theme_tfive_customer |  | fid |
