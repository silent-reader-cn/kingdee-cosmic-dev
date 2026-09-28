# 简历面试评分-recru_interviewscore

## 简历面试评分-多语言表 t_recru_interviewscore_l

- **表名称：** 简历面试评分-多语言表
- **表名：** t_recru_interviewscore_l

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
| 1 | pk_recru_interviewscore_l |  | fpkid |
| 2 | idx_recru_interviewscore_l_fid |  | fid,flocaleid |

---

## 技能知识单据体-子表 t_recru_iskillscore

- **表名称：** 技能知识单据体-子表
- **表名：** t_recru_iskillscore

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
| 1 | idx_recru_iskillscore_fid |  | fid |
| 2 | pk_recru_iskillscore |  | fentryid |

---

## 简历面试评分-主表 t_recru_interviewscore

- **表名称：** 简历面试评分-主表
- **表名：** t_recru_interviewscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fscoredatetime | 评分时间 | timestamp | 0 |  |  | null | 评分时间 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fresumeid | 简历 | int8 | 64 |  | √ | 0 | [简历库 recru_resume](../recru_files/recru_resume.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_interviewscore |  | fid |
| 2 | idx_recru_interviewscore_resum |  | fresumeid |

---

## 经验评分单据体-子表 t_recru_iexperiencescore

- **表名称：** 经验评分单据体-子表
- **表名：** t_recru_iexperiencescore

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
| 1 | pk_recru_iexperiencescore |  | fentryid |
| 2 | idx_recru_iexperiencescore_fid |  | fid |

---

## 能力评分单据体-子表 t_recru_iabilityscore

- **表名称：** 能力评分单据体-子表
- **表名：** t_recru_iabilityscore

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
| 1 | idx_recru_iabilityscore_fid |  | fid |
| 2 | pk_recru_iabilityscore |  | fentryid |

---

## 知识评分单据体-子表 t_recru_iknowledgescore

- **表名称：** 知识评分单据体-子表
- **表名：** t_recru_iknowledgescore

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
| 1 | idx_recru_iknowledgescore_fid |  | fid |
| 2 | pk_recru_iknowledgescore |  | fentryid |
