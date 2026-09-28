# 简历评分-recru_resumescore

## 简历评分-多语言表 t_recru_resumescore_l

- **表名称：** 简历评分-多语言表
- **表名：** t_recru_resumescore_l

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
| 1 | pk_recru_resumescore_l |  | fpkid |
| 2 | idx_recru_resumescore_l_fid |  | fid,flocaleid |

---

## 能力评分单据体-子表 t_recru_abilityscore

- **表名称：** 能力评分单据体-子表
- **表名：** t_recru_abilityscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 等级 | varchar | 255 |  | √ | ' ' | 等级 |
| 3 | fbasis_tag | 评价依据_详情 | text | 0 |  |  | null | 评价依据_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbasis | 评价依据 | varchar | 255 |  | √ | ' ' | 评价依据 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscore | 分数 | numeric | 23 | 10 | √ | 0 | 分数 |
| 8 | fdimension | 维度 | varchar | 2000 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_abilityscore_fid |  | fid |
| 2 | pk_recru_abilityscore |  | fentryid |

---

## 知识评分单据体-子表 t_recru_knowledgescore

- **表名称：** 知识评分单据体-子表
- **表名：** t_recru_knowledgescore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 等级 | varchar | 255 |  | √ | ' ' | 等级 |
| 3 | fbasis_tag | 评价依据_详情 | text | 0 |  |  | null | 评价依据_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbasis | 评价依据 | varchar | 255 |  | √ | ' ' | 评价依据 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscore | 分数 | numeric | 23 | 10 | √ | 0 | 分数 |
| 8 | fdimension | 维度 | varchar | 2000 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_knowledgescore_fid |  | fid |
| 2 | pk_recru_knowledgescore |  | fentryid |

---

## 经验评分单据体-子表 t_recru_experiencescore

- **表名称：** 经验评分单据体-子表
- **表名：** t_recru_experiencescore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 等级 | varchar | 255 |  | √ | ' ' | 等级 |
| 3 | fbasis_tag | 评价依据_详情 | text | 0 |  |  | null | 评价依据_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbasis | 评价依据 | varchar | 255 |  | √ | ' ' | 评价依据 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscore | 分数 | numeric | 23 | 10 | √ | 0 | 分数 |
| 8 | fdimension | 维度 | varchar | 2000 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_experiencescore_fid |  | fid |
| 2 | pk_recru_experiencescore |  | fentryid |

---

## 简历评分-主表 t_recru_resumescore

- **表名称：** 简历评分-主表
- **表名：** t_recru_resumescore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fparsedata_tag | 解析后的数据_详情 | text | 0 |  |  | null | 解析后的数据_详情 |
| 6 | fresumeid | 简历 | int8 | 64 |  | √ | 0 | [简历库 recru_resume](../recru_files/recru_resume.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fparsedata | 解析后的数据 | varchar | 255 |  | √ | ' ' | 解析后的数据 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fscoredatetime | 评分时间 | timestamp | 0 |  |  | null | 评分时间 |
| 13 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_resumescore |  | fid |
| 2 | idx_recru_resumescore_resume |  | fresumeid |

---

## 技能知识单据体-子表 t_recru_skillscore

- **表名称：** 技能知识单据体-子表
- **表名：** t_recru_skillscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 等级 | varchar | 255 |  | √ | ' ' | 等级 |
| 3 | fbasis_tag | 评价依据_详情 | text | 0 |  |  | null | 评价依据_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbasis | 评价依据 | varchar | 255 |  | √ | ' ' | 评价依据 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscore | 分数 | numeric | 23 | 10 | √ | 0 | 分数 |
| 8 | fdimension | 维度 | varchar | 2000 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_skillscore_fid |  | fid |
| 2 | pk_recru_skillscore |  | fentryid |
