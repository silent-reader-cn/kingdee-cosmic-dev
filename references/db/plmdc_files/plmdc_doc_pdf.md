# 文档和pdf文件映射-plmdc_doc_pdf

## 文档和pdf文件映射-主表 t_plmdc_doc_pdf_map

- **表名称：** 文档和pdf文件映射-主表
- **表名：** t_plmdc_doc_pdf_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmark | 唯一标记 | varchar | 50 |  | √ | ' ' | 唯一标记 |
| 3 | fsourcepdfid | 原pdf文件id | int8 | 64 |  | √ | 0 | 原pdf文件id |
| 4 | fdocid | 文档版本id | int8 | 64 |  | √ | 0 | 文档版本id |
| 5 | fpdffileid | pdf文件id | int8 | 64 |  | √ | 0 | pdf文件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_doc_pdf_map_fmark |  | fmark |
| 2 | pk_t_plmdc_doc_pdf_map |  | fid |
