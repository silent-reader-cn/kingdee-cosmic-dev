# 知识库shcema-gai_repo_schema

## 知识库shcema-主表 t_gai_repo_schema

- **表名称：** 知识库shcema-主表
- **表名：** t_gai_repo_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvector_metric_type | 向量计算类型 | varchar | 50 |  | √ | 'cosine' | 向量计算类型,枚举: l2 :欧基里距离（L2） cosine :余弦相似度（COSINE） |
| 3 | fexternal | 是否为外部知识库 | bpchar | 1 |  | √ | '0' | 是否为外部知识库 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdata_failed_count | 保存失败的数据量 | int8 | 64 |  | √ | 0 | 保存失败的数据量 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ffull_search_type | 全文检索类型 | varchar | 50 |  | √ | ' ' | 全文检索类型,枚举: matchQuery :匹配查询(match) matchPhraseQuery :短语查询(matchPhraseQuery) matchPhrasePrefix :短语前缀查询(matchPhrasePrefix) multiMatchQuery :多字段查询(multiMatchQuery) |
| 10 | frepo_id | 知识库ID | varchar | 30 |  | √ | ' ' | 知识库ID |
| 11 | fvector_model | 向量模型 | varchar | 100 |  | √ | ' ' | 向量模型,枚举: |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | schema名称 | varchar | 200 |  | √ | ' ' | schema名称 |
| 14 | fmservice_call_back | 外部知识库回调微服务信息 | varchar | 2000 |  | √ | ' ' | 外部知识库回调微服务信息 |
| 15 | frepo_number | 知识库编码 | varchar | 30 |  | √ | ' ' | 知识库编码 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdata_success_count | 保存成功的数据量 | int8 | 64 |  | √ | 0 | 保存成功的数据量 |
| 18 | frepo_type | 知识库类型 | varchar | 50 |  | √ | ' ' | 知识库类型,枚举: table :表格知识库 level :层级知识库 |
| 19 | fdata_total_count | 总数据量 | int8 | 64 |  | √ | 0 | 总数据量 |
| 20 | fvector_db_type | 向量数据库类型 | varchar | 50 |  | √ | ' ' | 向量数据库类型,枚举: milvus :milvus |
| 21 | fdata_src_number | 数据源编码 | varchar | 200 |  | √ | ' ' | 数据源编码 |
| 22 | fsearch_type | 检索模式 | varchar | 50 |  | √ | ' ' | 检索模式,枚举: vector :向量检索 keyword :全文检索 hybrid :混合检索 |
| 23 | fvector_collection_name | 向量collection名 | varchar | 200 |  | √ | ' ' | 向量collection名 |
| 24 | frepo_name | 知识库名称 | varchar | 200 |  | √ | ' ' | 知识库名称 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | schema编码 | varchar | 30 |  | √ | ' ' | schema编码 |
| 27 | ftokenizer_type | ES分词器类型 | varchar | 200 |  | √ | ' ' | ES分词器类型 |
| 28 | ffull_search_index_name | 全文检索Index名称 | varchar | 200 |  | √ | ' ' | 全文检索Index名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_schema |  | fid |
| 2 | idx_gai_repo_schema_model |  | fvector_model |

---

## 知识库shcema-多语言表 t_gai_repo_schema_l

- **表名称：** 知识库shcema-多语言表
- **表名：** t_gai_repo_schema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | schema名称 | varchar | 200 |  | √ | ' ' | schema名称 |
| 3 | frepo_name | 知识库名称 | varchar | 200 |  | √ | ' ' | 知识库名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_schema_l |  | fpkid |
| 2 | idx_gai_repo_schema_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_gai_repo_sch_field_list

- **表名称：** 单据体-子表
- **表名：** t_gai_repo_sch_field_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvector_index_enable | 构建向量索引 | bpchar | 1 |  | √ | '0' | 构建向量索引 |
| 3 | ffield_id | 字段Id | varchar | 50 |  | √ | ' ' | 字段Id |
| 4 | ffield_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 |
| 5 | ffull_index_enable | 构建全文索引 | bpchar | 1 |  | √ | '0' | 构建全文索引 |
| 6 | ffield_key | 字段key | varchar | 50 |  | √ | ' ' | 字段key |
| 7 | ffield_name | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_repo_sch_field_list_fk |  | fid |
| 2 | pk_t_gai_repo_sch_field_list |  | fentryid |
