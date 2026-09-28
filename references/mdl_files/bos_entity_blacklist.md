# 业务对象表单黑明单-bos_entity_blacklist

## 业务对象表单黑明单-主表 t_meta_entityblacklist

- **表名称：** 业务对象表单黑明单-主表
- **表名：** t_meta_entityblacklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitynum | 表单实体编码 | varchar | 100 |  | √ | ' ' | 表单实体编码 |
| 3 | fappnum | 应用编码 | varchar | 100 |  | √ | ' ' | 应用编码 |
| 4 | fentityid | 表单实体主键 | varchar | 100 |  | √ | ' ' | 表单实体主键 |
| 5 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_entityblacklist |  | fentityid |
| 2 | t_meta_entityblacklist_pkey |  | fid |
