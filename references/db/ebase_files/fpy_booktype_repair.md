# 账簿修复页面数据存储-fpy_booktype_repair

## 账簿修复页面数据存储-主表 tk_fpy_booktype_repair

- **表名称：** 账簿修复页面数据存储-主表
- **表名：** tk_fpy_booktype_repair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_batch_no | 修复批次 | varchar | 50 |  | √ | ' ' | 修复批次 |
| 3 | fk_fpy_tar_booktype | 新账簿 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fk_fpy_file_code | 文件编号 | varchar | 50 |  | √ | ' ' | 文件编号 |
| 5 | fk_fpy_textfield | 文本4 | varchar | 50 |  | √ | ' ' | 文本4 |
| 6 | fk_fpy_file_name | 文件名称 | varchar | 50 |  | √ | ' ' | 文件名称 |
| 7 | fk_fpy_date | 修复时间 | timestamp | 0 |  |  | null | 修复时间 |
| 8 | fk_fpy_uniqueid | 唯一编号 | varchar | 50 |  | √ | ' ' | 唯一编号 |
| 9 | fk_fpy_volume_num | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 10 | fk_fpy_src_booktype | 原账簿 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 11 | fk_fpy_volume_pk | 案卷id | int8 | 64 |  | √ | 0 | 案卷id |
| 12 | fk_fpy_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fk_fpy_backup_pk | 备份id | int8 | 64 |  | √ | 0 | 备份id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_booktype_repair |  | fid |
