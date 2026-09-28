# 获取上传文件id-fpy_get_file_id_model

## 获取上传文件id-主表 tk_fpy_get_file_id_model

- **表名称：** 获取上传文件id-主表
- **表名：** tk_fpy_get_file_id_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_archivescode | 归档编号 | varchar | 50 |  | √ | ' ' | 归档编号 |
| 3 | fk_fpy_batchnumber | 上传批次号 | varchar | 50 |  | √ | ' ' | 上传批次号 |
| 4 | fk_fpy_accountbookno | 账簿编号/财务组织 | varchar | 50 |  | √ | ' ' | 账簿编号/财务组织 |
| 5 | fk_fpy_period | 期属 | varchar | 50 |  | √ | ' ' | 期属 |
| 6 | fk_fpy_filename | 某单据.pdf | varchar | 500 |  | √ | ' ' | 某单据.pdf |
| 7 | fk_fpy_filemd5 | 文件MD5 | varchar | 50 |  | √ | ' ' | 文件MD5 |
| 8 | fk_accountbookname | 账簿名称 | varchar | 50 |  | √ | ' ' | 账簿名称 |
| 9 | fk_fpy_businesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_get_file_id_model |  | fid |
