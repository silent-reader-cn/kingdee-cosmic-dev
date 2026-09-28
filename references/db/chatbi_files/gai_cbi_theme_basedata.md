# 主题基础资料-gai_cbi_theme_basedata

## 主题基础资料-主表 t_gai_cbi_single_scheme

- **表名称：** 主题基础资料-主表
- **表名：** t_gai_cbi_single_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasetid | 数据集 | int8 | 64 |  | √ | 0 | [数据集 gai_cbi_dataset](../chatbi_files/gai_cbi_dataset.md) |
| 3 | fname | 主题名称 | varchar | 50 |  | √ | ' ' | 主题名称 |
| 4 | finputprompt | finputprompt | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatedatefield | fcreatedatefield | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 6 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 7 | fpicture | fpicture | varchar | 255 |  | √ | ' ' |  |
| 8 | fstatus | 主题状态 | varchar | 50 |  | √ | ' ' | 主题状态,枚举: offLine :已下线 unannounced :待发布 announced :已发布 |
| 9 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 11 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 12 | foriginpicture | foriginpicture | varchar | 255 |  | √ | ' ' |  |
| 13 | fpredatapic | fpredatapic | varchar | 50 |  | √ | ' ' |  |
| 14 | fscheme | 主题类型 | varchar | 50 |  | √ | ' ' | 主题类型 |
| 15 | fdesc | 主题描述 | varchar | 50 |  | √ | ' ' | 主题描述 |
| 16 | fnumber | fnumber | varchar | 255 |  | √ | ' ' |  |
| 17 | ficoninfo | ficoninfo | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_cbi_single_scheme_id |  | fid |
