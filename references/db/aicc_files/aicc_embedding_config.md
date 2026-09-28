# embedding配置-aicc_embedding_config

## embedding配置-多语言表 t_aicc_embedding_config_l

- **表名称：** embedding配置-多语言表
- **表名：** t_aicc_embedding_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_embeddingconfig_l_0 |  | fid,flocaleid |
| 2 | pk_aicc_embedding_config_l |  | fpkid |

---

## embedding配置-主表 t_aicc_embedding_config

- **表名称：** embedding配置-主表
- **表名：** t_aicc_embedding_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisapidimension | 是否可通过入参修改向量维度 | bpchar | 1 |  | √ | '0' | 是否可通过入参修改向量维度 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fchunktoken | 分块最大字符数 | int8 | 64 |  | √ | 0 | 分块最大字符数 |
| 7 | fbatchsize | 单次调用最大分块数量 | int8 | 64 |  | √ | 0 | 单次调用最大分块数量 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fdesc | 模型描述 | varchar | 1024 |  | √ | ' ' | 模型描述 |
| 16 | fdimension | 向量维度 | int8 | 64 |  | √ | 0 | 向量维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aicc_embedding_config |  | fid |
| 2 | idx_aicc_embedding_conf_number |  | fnumber |
