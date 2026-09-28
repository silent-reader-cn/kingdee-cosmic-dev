# 分片配置-bos_cbs_shard_config

## 分片配置-多语言表 t_cbs_shard_config_l

- **表名称：** 分片配置-多语言表
- **表名：** t_cbs_shard_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_config_l |  | fid,flocaleid |
| 2 | pk_cbs_shard_config_l |  | fpkid |

---

## 分片配置-主表 t_cbs_shard_config

- **表名称：** 分片配置-主表
- **表名：** t_cbs_shard_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstrategyzh_cn | 分片策略 | varchar | 100 |  | √ | ' ' | 分片策略 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fentitynumber | 实体名称 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fstrategy | 分片策略值 | varchar | 50 |  | √ | ' ' | 分片策略值 |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fstrategyparams | 分片参数 | varchar | 1000 |  | √ | ' ' | 分片参数 |
| 8 | fconfigstatus | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用,枚举: 0 :未启用 1 :启用中 2 :已启用 3 :还原中 4 :索引迁移中 5 :分表归档中 |
| 9 | fshardingfields | 分片属性 | varchar | 200 |  | √ | ' ' | 分片属性 |
| 10 | fnumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 11 | frwmark | 读写标志值 | varchar | 512 |  | √ | ' ' | 读写标志值 |
| 12 | foperationlog | 操作日志 | varchar | 2000 |  | √ | ' ' | 操作日志 |
| 13 | fversion | 变更版本号 | int8 | 64 |  | √ | 0 | 变更版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_config |  | fid |
| 2 | idx_cbs_shard_config_num |  | fentitynumber |
