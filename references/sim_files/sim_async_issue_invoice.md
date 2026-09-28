# 异步开票临时表-sim_async_issue_invoice

## 异步开票临时表-主表 t_sim_async_issue_invoice

- **表名称：** 异步开票临时表-主表
- **表名：** t_sim_async_issue_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fquerycount | 查询次数 | int4 | 32 |  | √ | 0 | 查询次数 |
| 4 | fissuechannel | 开票方式 | varchar | 30 |  | √ | ' ' | 开票方式,枚举: ly :联云托管 hbhx :河北航信托管 |
| 5 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_async_issue_invoice |  | fid |
| 2 | idx_async_invoice_orderno |  | forderno |
| 3 | idx_async_invoice_createtime |  | fcreatedate |
