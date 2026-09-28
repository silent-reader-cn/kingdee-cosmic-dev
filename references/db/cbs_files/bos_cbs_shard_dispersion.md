# 离散度计算-bos_cbs_shard_dispersion

## 单据体-子表 t_cbs_shard_disperse_info

- **表名称：** 单据体-子表
- **表名：** t_cbs_shard_disperse_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalctime | 计算时间点 | timestamp | 0 |  |  | null | 计算时间点 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdispersion | 离散度（%） | numeric | 23 | 10 | √ | 0.0000000000 | 离散度（%） |
| 6 | ffields | 属性 | varchar | 50 |  | √ | ' ' | 属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_disperse_info_fk |  | fid |
| 2 | pk_cbs_shard_disperse_info |  | fentryid |

---

## 离散度计算-主表 t_cbs_shard_dispersion

- **表名称：** 离散度计算-主表
- **表名：** t_cbs_shard_dispersion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fentitynumber | 表单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fshardingfields | 选择属性列 | varchar | 50 |  | √ | ' ' | 选择属性列 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_dispersion |  | fid |
| 2 | idx_cbs_shard_disperse_num |  | fentitynumber |
