# 附件文件类型魔数-bos_filetype_magicnumber

## 附件文件类型魔数-主表 t_bas_filetype_magicnum

- **表名称：** 附件文件类型魔数-主表
- **表名：** t_bas_filetype_magicnum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffileheader | 文件头 | varchar | 36 |  | √ | null | 文件头 |
| 3 | ffiletypes | 文件类型 | varchar | 255 |  | √ | null | 文件类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_filetype_magicnum |  | fid |
