# 远程SFTP文件-receipt_remote_sftp_file

## 远程SFTP文件-多语言表 t_receipt_remote_file_l

- **表名称：** 远程SFTP文件-多语言表
- **表名：** t_receipt_remote_file_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_remote_file_l_pkey |  | fpkid |
| 2 | idx_receipt_remote_file_l |  | fid,flocaleid |

---

## 远程SFTP文件-主表 t_receipt_remote_file

- **表名称：** 远程SFTP文件-主表
- **表名：** t_receipt_remote_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 5 | ffile_name | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 6 | fparentid | 上级 | int8 | 64 |  |  | null | [远程SFTP文件 receipt_remote_sftp_file](../receipt_files/receipt_remote_sftp_file.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 9 | ffile_path | 文件路径 | varchar | 2000 |  | √ | ' ' | 文件路径 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ffile_md5 | 文件MD5 | varchar | 255 |  | √ | ' ' | 文件MD5 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flevel | 级次 | int8 | 64 |  |  | null | 级次 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 16 | ffile_size | 文件大小 | varchar | 50 |  | √ | ' ' | 文件大小 |
| 17 | fext | 备用字段 | varchar | 255 |  | √ | ' ' | 备用字段 |
| 18 | fext_tag | 备用字段_详情 | text | 0 |  |  | null | 备用字段_详情 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_remote_file_pkey |  | fid |
