# 开发助手-bos_corpus_assistant

## 技能配置-子表 t_corpus_skillconf

- **表名称：** 技能配置-子表
- **表名：** t_corpus_skillconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fskillid | 编码 | int8 | 64 |  | √ | 0 | 技能管理 bos_skillcorpus |
| 3 | fskillenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_corpus_skillconf |  | fid,fskillid |
| 2 | pk_corpus_skillconf |  | fentryid |

---

## 知识库-多选基础资料表 t_corpus_assistant_libs

- **表名称：** 知识库-多选基础资料表
- **表名：** t_corpus_assistant_libs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 知识管理 corpus_libs |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_corpus_assistant_libs |  | fpkid |
| 2 | idx_corpus_assistant_libs |  | fid |

---

## 开发助手-多语言表 t_corpus_assistant_l

- **表名称：** 开发助手-多语言表
- **表名：** t_corpus_assistant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fdes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_corpus_assistant_l |  | fpkid |
| 2 | idx_corpus_assistant_l |  | fid,flocaleid |

---

## 预置问题分录-子表 t_corpus_question

- **表名称：** 预置问题分录-子表
- **表名：** t_corpus_question

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | varchar | 50 |  | √ | ' ' | 分录行号 |
| 3 | fquestion | 预置问题 | varchar | 50 |  | √ | ' ' | 预置问题 |
| 4 | fquestionenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_corpus_question |  | fid |
| 2 | pk_corpus_question |  | fentryid |

---

## 开发助手-主表 t_corpus_assistant

- **表名称：** 开发助手-主表
- **表名：** t_corpus_assistant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintention | 意图匹配 | varchar | 50 |  | √ | ' ' | 意图匹配 |
| 3 | fdeploytohome | 发布到应用首页 | bpchar | 1 |  | √ | '1' | 发布到应用首页 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ficon | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fstarttips | 开场白文案 | varchar | 255 |  | √ | ' ' | 开场白文案 |
| 14 | fllm | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型,枚举: |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fprompt | 提示词 | varchar | 50 |  | √ | ' ' | 提示词,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_corpus_assistant |  | fid |
| 2 | idx_t_corpus_assistant |  | fnumber |
