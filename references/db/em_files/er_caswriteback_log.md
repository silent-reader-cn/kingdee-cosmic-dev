# 反写日志-er_caswriteback_log

## 反写日志-主表 t_er_caswriteback_log

- **表名称：** 反写日志-主表
- **表名：** t_er_caswriteback_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatetype | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | frequestparam | 请求参数 | text | 0 |  |  | null | 请求参数 |
| 5 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 6 | frequestparam_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_caswriteback_log |  | fid |
| 2 | index_er_writeback_billtype |  | fbilltype |
