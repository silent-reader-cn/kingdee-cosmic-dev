# 分表归档看板-bos_cbs_shard_archikanban

## 分表归档看板-主表 t_cbs_shard_archikanban

- **表名称：** 分表归档看板-主表
- **表名：** t_cbs_shard_archikanban

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfigid | 实体名称 | int8 | 64 |  | √ | 0 | [分片配置 bos_cbs_shard_config](../cbs_files/bos_cbs_shard_config.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 5 | flastexectime | 最近一次启用 | timestamp | 0 |  |  | null | 最近一次启用 |
| 6 | farchiconfig | 分库配置 | int8 | 64 |  | √ | 0 | [分表归档配置 bos_cbs_shard_archi](../cbs_files/bos_cbs_shard_archi.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_kanban_entity |  | fentitynumber |
| 2 | pk_t_cbs_shard_archikanban |  | fid |
| 3 | idx_cbs_shard_kanban_archiid |  | farchiconfig |

---

## 单据体-子表 t_cbs_shard_archikanbanrd

- **表名称：** 单据体-子表
- **表名：** t_cbs_shard_archikanbanrd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshardtable | 分片表 | varchar | 50 |  | √ | ' ' | 分片表 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftabletype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: 0 :表头 1 :表头多语言表 2 :表头扩展表 3 :分录 4 :分录多语言表 5 :分录拓展表 6 :子分录 7 :子分录多语言表 8 :子分录扩展表 9 :关联追踪表 A :反写记录表 B :表头关联表 C :分录关联表 D :子分录关联表 E :表头隐私表 F :分录隐私表 G :子分录隐私表 |
| 5 | froute | 当前路由 | varchar | 50 |  | √ | ' ' | 当前路由 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx3_cbs_shard_kanbanrt_tb |  | fshardtable |
| 2 | pk3_t_cbs_shard_archikanbanrd |  | fentryid |
