# 失败自动重开记录-sim_fail_auto_issue

## 失败自动重开记录-主表 t_sim_fail_auto_issue

- **表名称：** 失败自动重开记录-主表
- **表名：** t_sim_fail_auto_issue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | ffailreason | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 4 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fail_auto_issue_createdate |  | fcreatedate |
| 2 | pk_t_sim_fail_auto_issue |  | fid |
| 3 | idx_fail_auto_issue_orderno |  | forderno |
