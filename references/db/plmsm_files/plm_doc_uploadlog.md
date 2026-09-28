# PLM文档上传结果-plm_doc_uploadlog

## PLM文档上传结果-主表 t_plmsm_uploadlog

- **表名称：** PLM文档上传结果-主表
- **表名：** t_plmsm_uploadlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frownumber | 当前行号 | int8 | 64 |  | √ | 0 | 当前行号 |
| 3 | fbatchnumber | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 4 | ffolderid | 文件夹 | varchar | 50 |  | √ | ' ' | 文件夹 |
| 5 | fuploadmsg | 上传结果 | varchar | 50 |  | √ | ' ' | 上传结果 |
| 6 | ftemplateurl | 模版地址 | varchar | 255 |  | √ | ' ' | 模版地址 |
| 7 | fphysicalfile | 物理文件id | varchar | 50 |  | √ | ' ' | 物理文件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_uploadlog |  | fid |
| 2 | idx_plm_uploadlog_template |  | ftemplateurl |
