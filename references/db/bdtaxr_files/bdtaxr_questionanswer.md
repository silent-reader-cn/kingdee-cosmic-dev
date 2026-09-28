# 问卷答案-bdtaxr_questionanswer

## 问卷答案-主表 t_bdtaxr_questionanswer

- **表名称：** 问卷答案-主表
- **表名：** t_bdtaxr_questionanswer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fanswer | 答案 | varchar | 2000 |  | √ | ' ' | 答案 |
| 4 | ffinalscore | 最终得分 | int8 | 64 |  | √ | 0 | 最终得分 |
| 5 | fstandardscore | 标准分值 | int8 | 64 |  | √ | 0 | 标准分值 |
| 6 | foptionset | 选项设置 | varchar | 50 |  | √ | ' ' | 选项设置 |
| 7 | fproblemtype | 问题分类 | varchar | 50 |  | √ | ' ' | 问题分类,枚举: choice :选择题 inputscore :填空题 essayque :问答题 oneticketveto :一票否决题 |
| 8 | fquestionnaireid | 调查问卷id | varchar | 50 |  | √ | ' ' | 调查问卷id |
| 9 | fmetadataid | 元数据id | varchar | 50 |  | √ | ' ' | 元数据id |
| 10 | fquesclassif | 问题分类 | varchar | 50 |  | √ | ' ' | 问题分类 |
| 11 | fsourcechoiceid | 源选项id | varchar | 50 |  | √ | ' ' | 源选项id |
| 12 | fmetadataname | 元数据名称 | varchar | 50 |  | √ | ' ' | 元数据名称 |
| 13 | fproblemdesc | 问题描述 | varchar | 2000 |  | √ | ' ' | 问题描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_answer_fmetadataid |  | fmetadataid |
| 2 | pk_bdtaxr_questionanswer |  | fid |

---

## 单据体-多语言表 t_bdtaxr_answeroptions_l

- **表名称：** 单据体-多语言表
- **表名：** t_bdtaxr_answeroptions_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | foption | 选项 | varchar | 50 |  | √ | ' ' | 选项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_answeroptions_l |  | fpkid |
| 2 | idx_bdtaxr_answeroptions_l_0 |  | fentryid,flocaleid |

---

## 问卷答案-多语言表 t_bdtaxr_questionanswer_l

- **表名称：** 问卷答案-多语言表
- **表名：** t_bdtaxr_questionanswer_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fanswer | 答案 | varchar | 2000 |  | √ | ' ' | 答案 |
| 3 | fproblemdesc | 问题描述 | varchar | 2000 |  | √ | ' ' | 问题描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fquesclassif | 问题分类 | varchar | 50 |  | √ | ' ' | 问题分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_questionanswer_l |  | fpkid |
| 2 | idx_bdtaxr_questionanswer_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_bdtaxr_answeroptions

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_answeroptions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstandardscore | 标准得分 | int8 | 64 |  | √ | 0 | 标准得分 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | foption | 选项 | varchar | 50 |  | √ | ' ' | 选项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_answeroptions |  | fentryid |
| 2 | idx_bdtaxr_answeroptions_fk |  | fid |
