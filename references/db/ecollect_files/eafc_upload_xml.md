# 归档xml上传-eafc_upload_xml

## 归档xml上传-主表 tk_eafc_upload_xml

- **表名称：** 归档xml上传-主表
- **表名：** tk_eafc_upload_xml

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_orgno | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 3 | fk_eafc_filename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 4 | fk_eafc_businesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 5 | fk_eafc_period | 期属 | varchar | 50 |  | √ | ' ' | 期属 |
| 6 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 7 | fk_eafc_fileurl | 文件路径 | varchar | 500 |  | √ | ' ' | 文件路径 |
| 8 | fk_eafc_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fk_eafc_current_data | 当前data位置 | int4 | 32 |  | √ | 0 | 当前data位置 |
| 10 | fk_eafc_filehash | 文件hash | varchar | 200 |  | √ | ' ' | 文件hash |
| 11 | fk_eafc_filesize | 文件大小（字节） | int8 | 64 |  |  | null | 文件大小（字节） |
| 12 | fk_eafc_status | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 1 :未解析 2 :已解析 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_upload_xml |  | fid |
| 2 | idx_eafc_upload_xml_name |  | fk_eafc_batch_num,fk_eafc_businesstype,fk_eafc_filename |
| 3 | idx_eafc_upload_xml_hash |  | fk_eafc_filehash |
