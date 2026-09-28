# 备份种类-fpy_backup_category

## 备份种类-主表 tk_fpy_backup_category

- **表名称：** 备份种类-主表
- **表名：** tk_fpy_backup_category

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_category_no | 类别号 | varchar | 50 |  | √ | ' ' | 类别号 |
| 3 | fk_fpy_file_num | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 4 | fk_fpy_category_name | 类别名称 | varchar | 50 |  | √ | ' ' | 类别名称 |
| 5 | fk_fpy_volume_num | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 6 | fk_fpy_billno | 备份单号 | varchar | 50 |  | √ | ' ' | 备份单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_backup_category |  | fid |
