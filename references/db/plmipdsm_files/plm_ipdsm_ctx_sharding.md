# 上下文分表配置-plm_ipdsm_ctx_sharding

## 分表配置-子表 t_plm_ipdsm_ctx_shard_e

- **表名称：** 分表配置-子表
- **表名：** t_plm_ipdsm_ctx_shard_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprefix | 实体前缀 | varchar | 500 |  | √ | ' ' | 实体前缀 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fshardingkey | 分表标识 | varchar | 200 |  | √ | ' ' | 分表标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_ctx_shard_e |  | fentryid |
| 2 | idx_t_plm_ipdsm_ctx_shard_e |  | fid,fprefix,fshardingkey |

---

## 上下文分表配置-主表 t_plm_ipdsm_ctx_shard

- **表名称：** 上下文分表配置-主表
- **表名：** t_plm_ipdsm_ctx_shard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | des | des | varchar | 50 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_ipdsm_ctx_shard |  | fid |
| 2 | idx_plm_ipdsm_ctx_shard |  | des |
