# 分片配置模板-bos_cbs_shard_config_tpl

## 分片配置模板-多语言表 t_cbs_shard_config_tpl_l

- **表名称：** 分片配置模板-多语言表
- **表名：** t_cbs_shard_config_tpl_l

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
| 1 | idx_cbs_shard_config_tpl_l |  | fid,flocaleid |
| 2 | pk_cbs_shard_config_tpl_l |  | fpkid |

---

## 分片配置模板-主表 t_cbs_shard_config_tpl

- **表名称：** 分片配置模板-主表
- **表名：** t_cbs_shard_config_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstrategyzh_cn | 分片策略 | varchar | 100 |  | √ | ' ' | 分片策略 |
| 3 | fstrategyparams | 分片策略参数 | varchar | 1000 |  | √ | ' ' | 分片策略参数 |
| 4 | fentitynumber | 表单 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fshardingfields | 分片属性 | varchar | 200 |  | √ | ' ' | 分片属性 |
| 6 | fstrategy | 分片策略值 | varchar | 50 |  | √ | ' ' | 分片策略值 |
| 7 | fnumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 8 | fisoem | 是否原厂 | bpchar | 1 |  | √ | ' ' | 是否原厂 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_config_tpl |  | fid |
| 2 | idx_cbs_shard_config_tpl_num |  | fentitynumber |
