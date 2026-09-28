# 知识类目f7专用-som_knowledge_subject_f7

## 知识类目f7专用-多语言表 t_tk_scs_detail_l

- **表名称：** 知识类目f7专用-多语言表
- **表名：** t_tk_scs_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类目名称 | varchar | 50 |  | √ | ' ' | 类目名称 |
| 3 | fanswer | fanswer | varchar | 900 |  | √ | ' ' |  |
| 4 | fquestion | fquestion | varchar | 80 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 7 | flinktitle | flinktitle | varchar | 80 |  | √ | ' ' |  |
| 8 | fkeyword | fkeyword | varchar | 20 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_scs_detail_l |  | fpkid |
| 2 | idx_ssc_scs_detail_l |  | fid,flocaleid |

---

## 知识类目f7专用-主表 t_tk_scs_detail

- **表名称：** 知识类目f7专用-主表
- **表名：** t_tk_scs_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | faisubjectid | faisubjectid | int8 | 64 |  | √ | 0 |  |
| 5 | frebortuse | frebortuse | bpchar | 1 |  | √ | '0' |  |
| 6 | fsubject | 是否类目 | bpchar | 1 |  | √ | '0' | 是否类目 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsynattachment | fsynattachment | bpchar | 1 |  | √ | '0' |  |
| 9 | fsubjectnum | 类目编码 | varchar | 50 |  | √ | ' ' | 类目编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | flink | flink | varchar | 300 |  | √ | ' ' |  |
| 12 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | farea | 知识领域 | int8 | 64 |  | √ | 0 | [知识库管理 som_knowledge_area](../som_files/som_knowledge_area.md) |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | faiquestionid | faiquestionid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scs_ques_area |  | farea |
| 2 | idx_ssc_scs_quesnum |  | fnumber |
| 3 | idx_ssc_scs_ques_subnum |  | fsubjectnum |
| 4 | pk_t_tk_scs_detail |  | fid |
