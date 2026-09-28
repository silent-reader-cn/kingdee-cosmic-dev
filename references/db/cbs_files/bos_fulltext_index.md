# 全文索引自定义规则-bos_fulltext_index

## 全文索引自定义规则-主表 t_fulltext_custsync

- **表名称：** 全文索引自定义规则-主表
- **表名：** t_fulltext_custsync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffiltername | 过滤字段名 | varchar | 200 |  | √ | ' ' | 过滤字段名 |
| 3 | fentityname | 实体对象编码 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fisenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 5 | findextype | Type | varchar | 60 |  | √ | ' ' | Type |
| 6 | findexname | ElasticSearch IndexName | varchar | 200 |  | √ | ' ' | ElasticSearch IndexName |
| 7 | ffiltervalue | 过滤字段值 | varchar | 200 |  | √ | ' ' | 过滤字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fulltext_custsync_pkey |  | fid |
| 2 | idx_fulltext_custsync |  | fentityname |

---

## 单据体-子表 t_fulltext_custsync_detl

- **表名称：** 单据体-子表
- **表名：** t_fulltext_custsync_detl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fesfieldname | ElasticSearch-索引字段名称 | varchar | 200 |  | √ | ' ' | ElasticSearch-索引字段名称 |
| 3 | ffieldtype | 字段类型 | varchar | 60 |  | √ | ' ' | 字段类型 |
| 4 | fispk | 是否主键 | bpchar | 1 |  | √ | ' ' | 是否主键 |
| 5 | fisfieldenable | 是否同步 | bpchar | 1 |  | √ | ' ' | 是否同步 |
| 6 | fpropertydisplayname | 实体对象属性 | varchar | 200 |  | √ | ' ' | 实体对象属性 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 9 | fpropertyname | 实体对象属性编码 | varchar | 200 |  | √ | ' ' | 实体对象属性编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fulltext_custsync_detl_fk |  | fid |
| 2 | t_fulltext_custsync_detl_pkey |  | fpkid |
