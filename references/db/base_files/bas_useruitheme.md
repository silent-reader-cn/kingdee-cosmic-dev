# 用户界面主题-bas_useruitheme

## 用户界面主题-主表 t_bas_useruitheme

- **表名称：** 用户界面主题-主表
- **表名：** t_bas_useruitheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fthemeid | 主题 | int8 | 64 |  | √ | 0 | [主题定制 bas_uitheme](../base_files/bas_uitheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_useruitheme_user |  | fuserid |
| 2 | t_bas_useruitheme_pkey |  | fid |
