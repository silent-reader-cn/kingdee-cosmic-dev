# 新增云白名单-cloudwhitelist_new

## 新增云白名单-主表 t_meta_cloudwhitelist

- **表名称：** 新增云白名单-主表
- **表名：** t_meta_cloudwhitelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloudnum | 云编码 | varchar | 36 |  | √ | ' ' | 云编码 |
| 3 | fcloudid | 云ID | varchar | 36 |  | √ | ' ' | 云ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_cldwhite_fcloudid |  | fcloudid |
| 2 | pk_t_meta_cloudwhitelist |  | fid |
