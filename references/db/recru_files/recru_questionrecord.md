# AI面试问题记录-recru_questionrecord

## AI面试问题记录-主表 t_recru_questionrecord

- **表名称：** AI面试问题记录-主表
- **表名：** t_recru_questionrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fanswer | 回答 | varchar | 255 |  | √ | ' ' | 回答 |
| 5 | fqueryendtime | 提问结束时间 | timestamp | 0 |  |  | null | 提问结束时间 |
| 6 | fanalysistime | 候选人回答分析耗时 | int8 | 64 |  | √ | 0 | 候选人回答分析耗时 |
| 7 | finterview | AI面试管理 | int8 | 64 |  | √ | 0 | [AI面试管理 recru_ai_interview](../recru_files/recru_ai_interview.md) |
| 8 | fanswerendtime | 回答结束时间 | timestamp | 0 |  |  | null | 回答结束时间 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fquestion | 问题 | varchar | 2000 |  | √ | ' ' | 问题 |
| 11 | fanswer_tag | 回答_详情 | text | 0 |  |  | null | 回答_详情 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fprequestion | AI预设面试问题 | int8 | 64 |  | √ | 0 | [面试题管理 recru_prequestion](../recru_files/recru_prequestion.md) |
| 14 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fquestionseq | 问题序号 | varchar | 10 |  | √ | ' ' | 问题序号 |
| 16 | fquerystarttime | 提问开始时间 | timestamp | 0 |  |  | null | 提问开始时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | ftype | 问题类型 | varchar | 2 |  | √ | ' ' | 问题类型,枚举: 00 :开场白 10 :主问题 20 :追问问题 30 :结束语 |
| 20 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fanswerstarttime | 回答开始时间 | timestamp | 0 |  |  | null | 回答开始时间 |
| 22 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_questionrecord |  | fid |
| 2 | idx_finterview |  | finterview |

---

## AI面试问题记录-多语言表 t_recru_questionrecord_l

- **表名称：** AI面试问题记录-多语言表
- **表名：** t_recru_questionrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_questionrecord_l |  | fpkid |
| 2 | idx_recru_questionrecord_l |  | fid,flocaleid |
