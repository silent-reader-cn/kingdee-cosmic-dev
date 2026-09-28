# 设置分片表单-bos_shard_strategy_set

## 设置分片表单-多语言表 t_bas_shardstrategy_set_l

- **表名称：** 设置分片表单-多语言表
- **表名：** t_bas_shardstrategy_set_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 表单名称 | varchar | 50 |  | √ | ' ' | 表单名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_shardstrategy_set_l_pkey |  | fpkid |
| 2 | idx_bas_shardstrategy_set_l_0 |  | fid,flocaleid |

---

## 设置分片表单-主表 t_bas_shardstrategy_set

- **表名称：** 设置分片表单-主表
- **表名：** t_bas_shardstrategy_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshardingenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 3 | fentitynumber | 选择分片表单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fstrategy | 分片策略值 | varchar | 50 |  | √ | ' ' | 分片策略值 |
| 5 | fprogress | 迁移进度 | varchar | 2000 |  | √ | ' ' | 迁移进度 |
| 6 | fcustomstrategyclass | 自定义策略类路径 | varchar | 255 |  |  | ' ' | 自定义策略类路径 |
| 7 | ffromshardingstatus | 初始状态 | varchar | 50 |  | √ | ' ' | 初始状态 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fstatus_flag | 状态标志 | varchar | 50 |  | √ | ' ' | 状态标志 |
| 11 | fstrategyparams | 分片策略参数 | varchar | 1000 |  | √ | ' ' | 分片策略参数 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmoving_record | 已迁移数量 | varchar | 50 |  | √ | ' ' | 已迁移数量 |
| 15 | ftotal_record | 总数据量 | varchar | 50 |  | √ | ' ' | 总数据量 |
| 16 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 17 | fshardingpaused | 是否暂停 | bpchar | 1 |  | √ | ' ' | 是否暂停 |
| 18 | fcustomstrategyparam | 自定义策略参数 | varchar | 1000 |  |  | ' ' | 自定义策略参数 |
| 19 | fshardpattern | 日期格式 | varchar | 50 |  | √ | ' ' | 日期格式,枚举: yyyy :yyyy yyyy-MM :yyyy-MM yyyy-MM-dd :yyyy-MM-dd |
| 20 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 21 | fstrategyzh_cn | 分片策略 | varchar | 50 |  | √ | ' ' | 分片策略 |
| 22 | fshardmod | 分片数量 | int8 | 64 |  | √ | 0 | 分片数量 |
| 23 | fprogressdesc | 进度描述 | varchar | 2000 |  | √ | ' ' | 进度描述 |
| 24 | findexpk | 启用ID映射分片表（更高性能） | bpchar | 1 |  | √ | ' ' | 启用ID映射分片表（更高性能） |
| 25 | fshardingexecuted | 是否执行 | bpchar | 1 |  | √ | ' ' | 是否执行 |
| 26 | fshardingcompleted | 数据转移完成 | bpchar | 1 |  | √ | ' ' | 数据转移完成 |
| 27 | ftoshardingstatus | 目标状态 | varchar | 50 |  | √ | ' ' | 目标状态 |
| 28 | fshardingfields | 选择分片属性 | varchar | 50 |  | √ | ' ' | 选择分片属性 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 表单编码 | varchar | 30 |  | √ | ' ' | 表单编码 |
| 31 | frwmark | 读写标志值 | varchar | 512 |  | √ | ' ' | 读写标志值 |
| 32 | foperationlog | 操作日志 | varchar | 2000 |  | √ | ' ' | 操作日志 |
| 33 | fshardingstatus | 分片状态 | varchar | 30 |  | √ | ' ' | 分片状态,枚举: sharding_none :未分片 uninitialized :分片分析 initializing :数据迁移 ready :已分片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_shardstrategy_set |  | fnumber |
| 2 | t_bas_shardstrategy_set_pkey |  | fid |

---

## 单据体-子表 t_bas_shardset_entry

- **表名称：** 单据体-子表
- **表名：** t_bas_shardset_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshard_moving_record | 已迁移数量 | varchar | 50 |  | √ | ' ' | 已迁移数量 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fshard_progress | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 6 | fshard_table | 分表名 | varchar | 50 |  | √ | ' ' | 分表名 |
| 7 | fshard_total_record | 预估数量 | varchar | 50 |  | √ | ' ' | 预估数量 |
| 8 | fshard_index | 分片表后缀 | varchar | 50 |  | √ | ' ' | 分片表后缀 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_shardset_entry_pkey |  | fentryid |
| 2 | idx_bas_shardset_entry |  | fid |
