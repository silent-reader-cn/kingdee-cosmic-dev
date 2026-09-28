# 知识库保存历史文件-plm_pdm_kw_history

## 知识库保存历史文件-主表 t_plm_pdm_kwhistory

- **表名称：** 知识库保存历史文件-主表
- **表名：** t_plm_pdm_kwhistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpageid | pageId | varchar | 100 |  | √ | ' ' | pageId |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ffilename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffilehash | 文件hash值 | varchar | 128 |  | √ | ' ' | 文件hash值 |
| 8 | fdocument_revision_id | 所属文档 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 9 | ffilepath | 文件路径 | varchar | 255 |  | √ | ' ' | 文件路径 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_kwhistory |  | fid |
| 2 | idx_t_plm_pdm_kwhistory_doc |  | fdocument_revision_id |
