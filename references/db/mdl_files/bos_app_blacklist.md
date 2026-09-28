# 应用黑名单-bos_app_blacklist

## 应用黑名单-主表 t_meta_appblacklist

- **表名称：** 应用黑名单-主表
- **表名：** t_meta_appblacklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnum | 应用编码 | varchar | 100 |  | √ | ' ' | 应用编码 |
| 3 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |
| 4 | fappid | 应用主键 | varchar | 100 |  | √ | ' ' | 应用主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_appblacklist_pkey |  | fid |
| 2 | idx_kdp_appblacklist |  | fappid |
