# 分表归档配置-bos_cbs_shard_archi

## 分表归档配置-主表 t_cbs_shard_archi

- **表名称：** 分表归档配置-主表
- **表名：** t_cbs_shard_archi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 配置状态 | varchar | 50 |  | √ | ' ' | 配置状态,枚举: 0 :可配置 1 :启用中 |
| 3 | fconfigid | 分片配置 | int8 | 64 |  | √ | 0 | [分片配置 bos_cbs_shard_config](../cbs_files/bos_cbs_shard_config.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 6 | frwmark | 读写标志值 | varchar | 512 |  | √ | ' ' | 读写标志值 |
| 7 | farchivefield | 归档属性 | varchar | 50 |  | √ | ' ' | 归档属性,枚举: |
| 8 | foperationlog | 操作日志 | varchar | 2000 |  | √ | ' ' | 操作日志 |
| 9 | fversion | 变更版本 | int8 | 64 |  |  | null | 变更版本 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_shard_archi |  | fid |
| 2 | idx_cbs_shard_archi_configid |  | fconfigid |

---

## 单据体-子表 t_cbs_shard_archi_condi

- **表名称：** 单据体-子表
- **表名：** t_cbs_shard_archi_condi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farchicondidesc | 归档条件 | varchar | 200 |  | √ | ' ' | 归档条件 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | farchicondijson | 归档条件json | varchar | 200 |  | √ | ' ' | 归档条件json |
| 6 | farchivefield | 归档属性 | varchar | 50 |  | √ | ' ' | 归档属性 |
| 7 | fcreateflag | 新增标志位 | int8 | 64 |  |  | null | 新增标志位 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fleft_value | 归档条件开始值 | varchar | 200 |  | √ | ' ' | 归档条件开始值 |
| 10 | fright_value | 归档条件结束值 | varchar | 200 |  | √ | ' ' | 归档条件结束值 |
| 11 | fconditioncode | 条件枚举 | int8 | 64 |  |  | null | 条件枚举 |
| 12 | ftarget_route | 目标库 | varchar | 50 |  | √ | ' ' | 目标库,枚举: |
| 13 | frangejudgecode | 时间范围重叠判断码 | int8 | 64 |  |  | null | 时间范围重叠判断码 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_archi_condi_fk |  | fid |
| 2 | pk_t_cbs_shard_archi_condi |  | fentryid |
