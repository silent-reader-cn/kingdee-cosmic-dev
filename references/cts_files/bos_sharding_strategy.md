# 分片策略-bos_sharding_strategy

## 单据体-多语言表 t_bas_shardstrategyfctl_l

- **表名称：** 单据体-多语言表
- **表名：** t_bas_shardstrategyfctl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 分片策略-主表 t_bas_shardstrategy

- **表名称：** 分片策略-主表
- **表名：** t_bas_shardstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fshardingenable | 是否分表 | bpchar | 1 |  | √ | '1' | 是否分表 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fprogressdesc | fprogressdesc | varchar | 255 |  | √ | ' ' |  |
| 6 | fentitynumber | 实体名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fstrategy | 分片策略 | varchar | 30 |  | √ | ' ' | 分片策略,枚举: ModHashStrategy :模哈希 LongValueStrategy :Long值 DateHashStrategy :日期哈希 ConsistentHashStrategy :一致性哈希 RangeValueStrategy :值范围 MapValueStrategy :值映射 |
| 8 | fprogress | fprogress | varchar | 255 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 10 | ffromshardingstatus | ffromshardingstatus | varchar | 100 |  | √ | ' ' |  |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fstrategyparams | fstrategyparams | varchar | 2000 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fshardingcompleted | fshardingcompleted | bpchar | 1 |  | √ | '0' |  |
| 16 | ftoshardingstatus | ftoshardingstatus | varchar | 100 |  | √ | ' ' |  |
| 17 | fprogresssign | fprogresssign | text | 0 |  |  | null |  |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fshardingfields | fshardingfields | varchar | 100 |  | √ | ' ' |  |
| 20 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 21 | foperationlog | foperationlog | varchar | 2000 |  | √ | ' ' |  |
| 22 | fshardingstatus | 当前状态 | varchar | 30 |  | √ | ' ' | 当前状态,枚举: sharding_none :未分片 sharding_uninitialized :分片尚未初始化 sharding_initing :分片正在初始化 sharding_ready :准备分片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_shardstrategy_pkey |  | fid |
| 2 | idx_bas_shardstrategy |  | fnumber |

---

## 单据体-子表 t_bas_shardstrategyfctl

- **表名称：** 单据体-子表
- **表名：** t_bas_shardstrategyfctl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 分片策略-多语言表 t_bas_shardstrategy_l

- **表名称：** 分片策略-多语言表
- **表名：** t_bas_shardstrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_shardstrategy_l_pkey |  | fpkid |
| 2 | idx_bas_shardstrategy_l |  | fid,flocaleid |
