# 文件下载记录-rim_download_file

## 文件下载记录-主表 t_rim_download_file

- **表名称：** 文件下载记录-主表
- **表名：** t_rim_download_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffile_url | 文件url | varchar | 300 |  | √ | ' ' | 文件url |
| 3 | fhttp_url | httpurl | varchar | 400 |  | √ | ' ' | httpurl |
| 4 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ffileid | 文件id | varchar | 100 |  | √ | ' ' | 文件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_download_file |  | ffileid |
| 2 | pk_rim_download_file |  | fid |
