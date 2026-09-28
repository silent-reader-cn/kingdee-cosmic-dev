# 知识问答-som_knowledge_info

## 知识问答-多语言表 t_tk_scs_detail_l

- **表名称：** 知识问答-多语言表
- **表名：** t_tk_scs_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类目名称 | varchar | 50 |  | √ | ' ' | 类目名称 |
| 3 | fanswer | 答案/知识 | varchar | 900 |  | √ | ' ' | 答案/知识 |
| 4 | fquestion | 问题名称/知识名称 | varchar | 80 |  | √ | ' ' | 问题名称/知识名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 7 | flinktitle | 标题 | varchar | 80 |  | √ | ' ' | 标题 |
| 8 | fkeyword | 关键词 | varchar | 20 |  | √ | ' ' | 关键词 |

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

## 单据体-多语言表 t_tk_scs_simques_l

- **表名称：** 单据体-多语言表
- **表名：** t_tk_scs_simques_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsimilarques | 相似问法 | varchar | 100 |  | √ | ' ' | 相似问法 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_scs_simques_l |  | fpkid |
| 2 | idx_ssc_scs_simques_l |  | fentryid,flocaleid |

---

## 附件-附件表 t_tk_scs_attach

- **表名称：** 附件-附件表
- **表名：** t_tk_scs_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scs_infoattach |  | fid,fbasedataid |
| 2 | pk_t_tk_scs_attach |  | fpkid |

---

## 单据体-子表 t_tk_scs_simques

- **表名称：** 单据体-子表
- **表名：** t_tk_scs_simques

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scs_simques_fid |  | fid |
| 2 | pk_t_tk_scs_simques |  | fentryid |

---

## 知识问答-主表 t_tk_scs_detail

- **表名称：** 知识问答-主表
- **表名：** t_tk_scs_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 类目 | int8 | 64 |  | √ | 0 | [知识问答 som_knowledge_info](../som_files/som_knowledge_info.md) |
| 4 | faisubjectid | AI类目id | int8 | 64 |  | √ | 0 | AI类目id |
| 5 | frebortuse | 允许被机器人调用 | bpchar | 1 |  | √ | '0' | 允许被机器人调用 |
| 6 | fsubject | 类目 | bpchar | 1 |  | √ | '0' | 类目 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsynattachment | 是否已同步附件 | bpchar | 1 |  | √ | '0' | 是否已同步附件 |
| 9 | fsubjectnum | 类目编码 | varchar | 50 |  | √ | ' ' | 类目编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | flink | 链接 | varchar | 300 |  | √ | ' ' | 链接 |
| 12 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | farea | 知识领域 | int8 | 64 |  | √ | 0 | [知识库管理 som_knowledge_area](../som_files/som_knowledge_area.md) |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | faiquestionid | AI问答id | int8 | 64 |  | √ | 0 | AI问答id |

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
