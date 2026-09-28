# 新增知识问答-dhc_knowledge_add

## 新增知识问答-主表 t_dhc_knowledge_add

- **表名称：** 新增知识问答-主表
- **表名：** t_dhc_knowledge_add

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finquirybillid | 共享问询工单id | int8 | 64 |  | √ | 0 | 共享问询工单id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dhc_knowledge_add |  | fid |
| 2 | idx_dhc_knowledge_add_fibid |  | finquirybillid |

---

## 知识问答单据体-子表 t_dhc_knowledge_entry

- **表名称：** 知识问答单据体-子表
- **表名：** t_dhc_knowledge_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fknowledgeid | 知识问答 | int8 | 64 |  | √ | 0 | 知识问答 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fareaid | 知识领域 | int8 | 64 |  | √ | 0 | [知识库管理 som_knowledge_area](../som_files/som_knowledge_area.md) |
| 5 | fknowledgenum | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsubjectid | 知识类目 | int8 | 64 |  | √ | 0 | [知识类目f7专用 som_knowledge_subject_f7](../som_files/som_knowledge_subject_f7.md) |
| 8 | fknowledgename | 问题名称/知识名称 | varchar | 80 |  | √ | ' ' | 问题名称/知识名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_knowledge_entry_fid |  | fid |
| 2 | pk_dhc_knowledge_entry |  | fentryid |
