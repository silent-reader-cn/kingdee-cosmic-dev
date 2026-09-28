# 分片配置详情表-bos_cbs_shard_detail

## 分片配置详情表-主表 t_cbs_shard_detail

- **表名称：** 分片配置详情表-主表
- **表名：** t_cbs_shard_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 配置名 | varchar | 300 |  | √ | ' ' | 配置名 |
| 3 | fparentfield | 父表关联字段 | varchar | 50 |  |  | ' ' | 父表关联字段 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fshardproperties | 分片属性 | varchar | 300 |  |  | ' ' | 分片属性 |
| 6 | fjoinfield | 关联字段 | varchar | 50 |  |  | ' ' | 关联字段 |
| 7 | fentitynumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 8 | fatrribute | 类型属性 | varchar | 50 |  |  | ' ' | 类型属性 |
| 9 | findexfield | 索引字段 | varchar | 300 |  |  | ' ' | 索引字段 |
| 10 | fdbroutekey | 路由key | varchar | 50 |  |  | ' ' | 路由key |
| 11 | findexproperties | 索引属性 | varchar | 300 |  |  | ' ' | 索引属性 |
| 12 | flevel | ER等级 | int4 | 32 |  | √ | 0 | ER等级 |
| 13 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 14 | fshardfield | 分片字段 | varchar | 300 |  |  | ' ' | 分片字段 |
| 15 | fparenttable | 父表 | varchar | 50 |  |  | ' ' | 父表 |
| 16 | ftablename | 表名 | varchar | 50 |  | √ | ' ' | 表名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_detail_num |  | fentitynumber |
| 2 | pk_t_cbs_shard_detail |  | fid |
