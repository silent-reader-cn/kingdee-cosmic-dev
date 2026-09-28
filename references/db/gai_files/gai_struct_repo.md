# 结构化知识库-gai_struct_repo

## 结构化知识库-使用范围表 t_gai_struct_repo_u

- **表名称：** 结构化知识库-使用范围表
- **表名：** t_gai_struct_repo_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_struct_repo_u_uo |  | fuseorgid |
| 2 | pk_t_gai_struct_repo_u |  | fdataid,fuseorgid |

---

## 结构化知识库-多语言表 t_gai_struct_repo_l

- **表名称：** 结构化知识库-多语言表
- **表名：** t_gai_struct_repo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_struct_repo_l |  | fid |
| 2 | pk_t_gai_struct_repo_l |  | fpkid |

---

## 字段单据体-子表 t_gai_struct_repo_fields

- **表名称：** 字段单据体-子表
- **表名：** t_gai_struct_repo_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | fsrcfieldkey | 源字段标识 | varchar | 200 |  | √ | ' ' | 源字段标识 |
| 4 | ffullindex | 构建全文索引 | bpchar | 1 |  | √ | ' ' | 构建全文索引 |
| 5 | ffieldindex | 字段索引 | int8 | 64 |  | √ | 0 | 字段索引 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fembedindex | 构建向量索引 | bpchar | 1 |  | √ | ' ' | 构建向量索引 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdatatype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_fk |  | fid |
| 2 | pk_t_gai_struct_repo_fields |  | fentryid |

---

## 结构化知识库-主表 t_gai_struct_repo

- **表名称：** 结构化知识库-主表
- **表名：** t_gai_struct_repo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frepotype | 知识库类型 | varchar | 50 |  | √ | ' ' | 知识库类型,枚举: level :层级知识库 table :表格知识库 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftokenizer | ES分词器 | varchar | 50 |  | √ | ' ' | ES分词器,枚举: standard :标准分词器 ik_max_word :ik-max-word ik_smart :ik-smart |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdatastatus | 向量化状态 | varchar | 50 |  | √ | ' ' | 向量化状态,枚举: processing :处理中 success :可用 failed :异常 none :未处理 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsrcbizobject | 来源业务对象 | varchar | 200 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fvectormodel | 向量模型 | varchar | 100 |  | √ | ' ' | 向量模型,枚举: |
| 15 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 19 | freponumber | 知识库编码 | varchar | 100 |  | √ | ' ' | 知识库编码 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdescription | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fvectormetrictype | 向量计算类型 | varchar | 50 |  | √ | 'cosine' | 向量计算类型,枚举: l2 :欧基里距离（L2） cosine :余弦相似度（COSINE） |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_struct_repo_createorg |  | fcreateorgid |
| 2 | pk_t_gai_struct_repo |  | fid |
| 3 | idx_gai_struct_repo |  | fnumber |
| 4 | idx_t_gai_struct_repo_master |  | fmasterid |
