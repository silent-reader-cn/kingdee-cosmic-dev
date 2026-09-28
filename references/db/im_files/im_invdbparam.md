# 后台参数-im_invdbparam

## 后台参数-主表 t_im_invdbparam

- **表名称：** 后台参数-主表
- **表名：** t_im_invdbparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 30 |  | √ | ' ' | 值 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 4 | fkey | key标识 | varchar | 30 |  | √ | ' ' | key标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invparam_foid |  | forgid |
| 2 | t_im_invdbparam_pkey |  | fid |
