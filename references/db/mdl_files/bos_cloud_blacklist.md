# 云黑名单-bos_cloud_blacklist

## 云黑名单-主表 t_meta_cloudblacklist

- **表名称：** 云黑名单-主表
- **表名：** t_meta_cloudblacklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloudnum | 云编码 | varchar | 100 |  | √ | ' ' | 云编码 |
| 3 | fcloudid | 云主键 | varchar | 100 |  | √ | ' ' | 云主键 |
| 4 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_cloudblacklist_pkey |  | fid |
| 2 | idx_kdp_cloudblacklist |  | fcloudid |
