# 统计表单详情-bos_cbs_shard_stat_detail

## 单据体-子表 t_cbs_shard_stat_det_ety

- **表名称：** 单据体-子表
- **表名：** t_cbs_shard_stat_det_ety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :表头 1 :表头多语言表 2 :表头扩展表 3 :分录 4 :分录多语言表 5 :分录扩展表 6 :子分录 7 :子分录多语言表 8 :子分录扩展表 9 :关联追踪表 A :反写记录表 B :表头关联表 C :分录关联表 D :子分录关联表 E :表头隐私表 F :分录隐私表 G :子分录隐私表 |
| 3 | ftable | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | foriginaltable | 原表名 | varchar | 50 |  | √ | ' ' | 原表名 |
| 6 | fcount | 行数 | int8 | 64 |  | √ | 0 | 行数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_stat_det_ety |  | fentryid |
| 2 | idx_cbs_shard_stat_det_ety_fk |  | fid |

---

## 统计表单详情-主表 t_cbs_shard_stat_detail

- **表名称：** 统计表单详情-主表
- **表名：** t_cbs_shard_stat_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatisticid | 统计表单ID | int8 | 64 |  | √ | 0 | 统计表单ID |
| 3 | fcreatetime | 统计时间 | timestamp | 0 |  |  | null | 统计时间 |
| 4 | fshardingcount | 分片数 | int8 | 64 |  | √ | 0 | 分片数 |
| 5 | fsharding | 是否分表 | bpchar | 1 |  | √ | ' ' | 是否分表,枚举: 0 :否 1 :是 |
| 6 | foriginaltablecount | 原表数 | int8 | 64 |  | √ | 0 | 原表数 |
| 7 | fentitynumber | 表单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | ftotalcount | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 9 | ftablecount | 总表数 | int8 | 64 |  | √ | 0 | 总表数 |
| 10 | fcost | 统计耗时（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 统计耗时（秒） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_stat_detail |  | fid |
| 2 | idx_cbs_shard_stat_detail_num |  | fentitynumber |
