# PDF批注-plm_plmdc_pdf_annotations

## PDF批注-多语言表 t_plmdc_pdf_annotations_l

- **表名称：** PDF批注-多语言表
- **表名：** t_plmdc_pdf_annotations_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_pdf_annotations_l |  | fpkid |
| 2 | idx_plmdc_pdf_annotations_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_plmdc_pdf_anno_entity

- **表名称：** 单据体-子表
- **表名：** t_plmdc_pdf_anno_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcedocversion | 文档版本 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 3 | fannotationfile | 批注文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 4 | fsourcepdfid | 源PdfId | int8 | 64 |  | √ | 0 | 源PdfId |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fannotator | 批注人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fanotatdate | 批注日期 | timestamp | 0 |  |  | null | 批注日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_pdf_anno_entity |  | fid |
| 2 | pk_t_plmdc_pdf_anno_entity |  | fentryid |

---

## PDF批注-主表 t_plmdc_pdf_annotations

- **表名称：** PDF批注-主表
- **表名：** t_plmdc_pdf_annotations

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdocument | 文档 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fannotator | 批注人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fanotationpath | 批注路径 | varchar | 500 |  | √ | ' ' | 批注路径 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fflow | 流程 | int8 | 64 |  | √ | 0 | [流程单据 plm_pdm_flow](../plmsm_files/plm_pdm_flow.md) |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fisannotate | 是否正在批注 | bpchar | 1 |  | √ | '0' | 是否正在批注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_pdf_annotations |  | fid |
| 2 | idx_plmdc_pdf_annotations_num |  | fnumber |
