# 分片配置运行时信息-bos_cbs_shard_runtimeold

## 分片配置运行时信息-主表 t_cbs_shard_runtimeinfo

- **表名称：** 分片配置运行时信息-主表
- **表名：** t_cbs_shard_runtimeinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' | id |
| 2 | flevel | 等级 | varchar | 50 |  | √ | ' ' | 等级 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :表头 1 :表头多语言表 2 :表头扩展表 3 :分录 4 :分录多语言表 5 :分录扩展表 6 :子分录 7 :子分录多语言表 8 :子分录扩展表 9 :关联追踪表 A :反写记录表 B :表头关联表 C :分录关联表 D :子分录关联表 E :表头隐私表 F :分录隐私表 G :子分录隐私表 |
| 4 | fexists | 是否存在 | bpchar | 1 |  | √ | '0' | 是否存在 |
| 5 | fshardfields | 分片属性 | varchar | 50 |  | √ | ' ' | 分片属性 |
| 6 | ftable | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 7 | fip | IP | varchar | 50 |  | √ | ' ' | IP |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_sr_ftable |  | ftable |
| 2 | pk_cbs_shard_runtimeinfo |  | fid |
