# 用户锁定应用-bos_portal_userfixedapp

## 用户锁定应用-主表 t_bas_userfixedapp

- **表名称：** 用户锁定应用-主表
- **表名：** t_bas_userfixedapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsortcode | 排序码 | int8 | 64 |  | √ | 0 | 排序码 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_userfixedapp_pkey |  | fid |
| 2 | idx_t_bas_userfixedapp_fuserid |  | fuserid |
