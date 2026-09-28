# 兜底优化配置-cbi_bottom_opt_config

## 兜底优化配置-主表 t_cbi_bottom_opt_config

- **表名称：** 兜底优化配置-主表
- **表名：** t_cbi_bottom_opt_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpersona | 人设 | varchar | 255 |  | √ | ' ' | 人设 |
| 3 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 4 | fhelpmarkdown_tag | 帮助文档_详情 | text | 0 |  |  | null | 帮助文档_详情 |
| 5 | fhelpmarkdown | 帮助文档 | varchar | 255 |  | √ | ' ' | 帮助文档 |
| 6 | fpersona_tag | 人设_详情 | text | 0 |  |  | null | 人设_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_bottom_opt_config |  | fid |
