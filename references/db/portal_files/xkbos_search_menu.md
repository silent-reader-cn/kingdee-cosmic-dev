# 搜索菜单-xkbos_search_menu

## 搜索菜单-主表 t_xkbos_search_menu

- **表名称：** 搜索菜单-主表
- **表名：** t_xkbos_search_menu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmenuentitynumber | 菜单实体编码 | varchar | 50 |  | √ | ' ' | 菜单实体编码 |
| 4 | fappnumber | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 8 | fmenuid | 菜单id | varchar | 36 |  | √ | ' ' | 菜单id |
| 9 | fappid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbos_search_menu |  | fid |
| 2 | idx_user_app_menu |  | fuserid,fmenuid |
