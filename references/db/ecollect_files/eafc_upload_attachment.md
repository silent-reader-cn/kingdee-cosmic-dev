# 归档附件上传-eafc_upload_attachment

## 归档附件上传-主表 tk_eafc_upload_attachment

- **表名称：** 归档附件上传-主表
- **表名：** tk_eafc_upload_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_orgno | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 3 | fk_eafc_filename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 4 | fk_eafc_businesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 5 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fk_eafc_period | 期属 | varchar | 50 |  | √ | ' ' | 期属 |
| 7 | fk_eafc_fileurl | 文件路径 | varchar | 500 |  | √ | ' ' | 文件路径 |
| 8 | fk_eafc_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fk_eafc_filehash | 文件hash | varchar | 200 |  | √ | ' ' | 文件hash |
| 10 | fk_eafc_filesize | 文件大小（字节） | int8 | 64 |  |  | null | 文件大小（字节） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_upload_attachment_fk |  | fk_eafc_batch_num,fk_eafc_businesstype,fk_eafc_filename |
| 2 | idx_eafc_upload_atta_hash |  | fk_eafc_filehash |
| 3 | pk__eafc_upload_attachment |  | fid |
