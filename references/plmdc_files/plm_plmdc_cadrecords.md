# cad上传记录-plm_plmdc_cadrecords

## cad上传记录-主表 t_plmdc_cadrecords

- **表名称：** cad上传记录-主表
- **表名：** t_plmdc_cadrecords

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | filename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 3 | fcadid | cadid | varchar | 50 |  | √ | ' ' | cadid |
| 4 | funiquekey | 批次 | varchar | 50 |  | √ | ' ' | 批次 |
| 5 | fworkonstatus | 生效状态 | varchar | 50 |  | √ | ' ' | 生效状态 |
| 6 | fcaddocumentid | CAD文档id | int8 | 64 |  | √ | 0 | CAD文档id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_cadrecords |  | funiquekey,fcadid |
| 2 | pk_t_plmdc_cadrecords |  | fid |
