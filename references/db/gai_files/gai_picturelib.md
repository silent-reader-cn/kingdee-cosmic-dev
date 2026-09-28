# 图片字段导出-gai_picturelib

## 图片字段导出-主表 t_gai_picturelib

- **表名称：** 图片字段导出-主表
- **表名：** t_gai_picturelib

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicture | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 3 | fpicture_tag | 图片_详情 | text | 0 |  |  | null | 图片_详情 |
| 4 | fsrcid | 原单ID | varchar | 50 |  | √ | ' ' | 原单ID |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_picturelib |  | ftype,fsrcid |
| 2 | pk_gai_picturelib |  | fid |
