# 银企云4.0许可表-aqap_license_file

## 银企云4.0许可表-主表 t_aqap_license_file

- **表名称：** 银企云4.0许可表-主表
- **表名：** t_aqap_license_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | flicense_file_tag | 许可文件_详情 | text | 0 |  |  | null | 许可文件_详情 |
| 3 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 4 | fupload_time | 上传时间 | timestamp | 0 |  |  | null | 上传时间 |
| 5 | fexpire_time | 许可过期时间 | timestamp | 0 |  |  | null | 许可过期时间 |
| 6 | flicense_file | 许可文件 | varchar | 255 |  | √ | ' ' | 许可文件 |
| 7 | flicense_count | 许可数量 | int8 | 64 |  |  | null | 许可数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_license_file_unique |  | fcustom_id |
| 2 | t_aqap_license_file_pkey |  | fid |
