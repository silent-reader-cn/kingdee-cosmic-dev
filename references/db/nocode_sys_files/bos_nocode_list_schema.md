# 表单列表视图-bos_nocode_list_schema

## 表单列表视图-主表 t_nocode_list_schema

- **表名称：** 表单列表视图-主表
- **表名：** t_nocode_list_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 视图名称 | varchar | 50 |  | √ | ' ' | 视图名称 |
| 3 | forderinfo | 排序项配置 | text | 0 |  |  | null | 排序项配置 |
| 4 | flistitems | 列表项配置 | text | 0 |  |  | null | 列表项配置 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 7 | ftimemode | 时间尺度 | bpchar | 1 |  | √ | '0' | 时间尺度,枚举: 0 :天 1 :周 2 :月 3 :季 4 :年 |
| 8 | ffilterrows | 筛选项配置 | text | 0 |  |  | null | 筛选项配置 |
| 9 | fschematype | 视图类型 | bpchar | 1 |  | √ | '0' | 视图类型,枚举: 0 :列表 1 :甘特图 |
| 10 | fstatcards | 统计卡片配置 | text | 0 |  |  | null | 统计卡片配置 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fganttconfig | 甘特图配置 | text | 0 |  |  | null | 甘特图配置 |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fhidden | 隐藏标记 | varchar | 50 |  | √ | ' ' | 隐藏标记 |
| 16 | fpagesize | 分页 | int8 | 64 |  | √ | 0 | 分页 |
| 17 | fformid | 表单 | varchar | 50 |  | √ | ' ' | 表单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_list_schema |  | fid |
| 2 | idx_nc_ls_fformid |  | fformid |
