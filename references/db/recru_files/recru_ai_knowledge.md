# ai招聘结构化知识库-recru_ai_knowledge

## ai招聘结构化知识库-多语言表 t_recru_ai_knowledgeconf_l

- **表名称：** ai招聘结构化知识库-多语言表
- **表名：** t_recru_ai_knowledgeconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ai_knowledgeconf_l |  | fpkid |
| 2 | idx_recru_ai_knowledgeconf_l |  | fid,flocaleid |

---

## 单据体-子表 t_recru_ai_knowfield

- **表名称：** 单据体-子表
- **表名：** t_recru_ai_knowfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 20 |  | √ | ' ' | 类型,枚举: string :文本 |
| 3 | ffullindex | 构建全文索引 | bpchar | 1 |  | √ | '0' | 构建全文索引 |
| 4 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fembedindex | 构建向量索引 | bpchar | 1 |  | √ | '0' | 构建向量索引 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ai_knowfield_fid |  | fid |
| 2 | pk_recru_ai_knowfield |  | fentryid |

---

## ai招聘结构化知识库-主表 t_recru_ai_knowledgeconf

- **表名称：** ai招聘结构化知识库-主表
- **表名：** t_recru_ai_knowledgeconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frepotype | 知识库类型 | varchar | 20 |  | √ | ' ' | 知识库类型,枚举: table :表格知识库 level :层级知识库 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finitstatus | 初始化状态 | varchar | 10 |  | √ | ' ' | 初始化状态,枚举: 0 :进行中 1 :已验证 2 :已完成 |
| 7 | fdescription | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 8 | finitbatch | 初始化批次 | int8 | 64 |  | √ | 0 | 初始化批次 |
| 9 | ftpsys | 第三方系统 | varchar | 10 |  | √ | ' ' | 第三方系统,枚举: KD :金蝶 MK :摩卡 BS :北森 DY :大易 |
| 10 | fschemanumber | schema码 | varchar | 100 |  | √ | ' ' | schema码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 3 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftptenantid | 第三方租户ID | varchar | 50 |  | √ | ' ' | 第三方租户ID |
| 16 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: person :人员 position :岗位 |
| 17 | ftpdatanum | 第三方数据编码 | varchar | 50 |  | √ | ' ' | 第三方数据编码 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | finitdatasource | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :初始化 2 :外部集成 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fvectormodel | 向量模型 | varchar | 100 |  | √ | ' ' | 向量模型,枚举: |
| 22 | fdimension | 维度 | varchar | 50 |  | √ | ' ' | 维度,枚举: experience :工作经验 skill :专业技能 major :专业 language :语言能力 latestexp :最近一段工作经历 |
| 23 | ftpdataid | 第三方数据ID | varchar | 50 |  | √ | ' ' | 第三方数据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ai_knowledgeconf_nu |  | fnumber |
| 2 | idx_recru_ai_knowledgeconf_sch |  | fschemanumber |
| 3 | pk_recru_ai_knowledgeconf |  | fid |
