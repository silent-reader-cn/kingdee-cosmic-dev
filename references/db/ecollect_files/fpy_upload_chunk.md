# 分块上传文件-fpy_upload_chunk

## 分块上传文件-主表 tk_fpy_upload_chunk

- **表名称：** 分块上传文件-主表
- **表名：** tk_fpy_upload_chunk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_chunkmd5 | 分块MD5 | varchar | 50 |  | √ | ' ' | 分块MD5 |
| 3 | fk_fpy_chunksize | 分块大小 | varchar | 50 |  | √ | ' ' | 分块大小 |
| 4 | fk_fpy_total | 分块总数 | varchar | 50 |  | √ | ' ' | 分块总数 |
| 5 | fk_fpy_filemd5 | 文件MD5 | varchar | 50 |  | √ | ' ' | 文件MD5 |
| 6 | fk_fpy_bytes2_tag | 分块字节数组_详情 | varchar | 50 |  | √ | ' ' | 分块字节数组_详情 |
| 7 | fk_fpy_server_url2 | 文件服务器地址 | varchar | 2000 |  | √ | ' ' | 文件服务器地址 |
| 8 | fk_fpy_current | 当前分块数 | varchar | 50 |  | √ | ' ' | 当前分块数 |
| 9 | fk_fpy_bytes2 | 分块字节数组 | varchar | 255 |  | √ | ' ' | 分块字节数组 |
| 10 | fk_fpy_uploadid | 上传id | varchar | 50 |  | √ | ' ' | 上传id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_upload_chunk |  | fid |
