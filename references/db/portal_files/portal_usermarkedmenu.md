# 用户收藏菜单-portal_usermarkedmenu

## 用户收藏菜单-主表 t_bas_usermarkedmenus

- **表名称：** 用户收藏菜单-主表
- **表名：** t_bas_usermarkedmenus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 菜单名 | varchar | 100 |  | √ | ' ' | 菜单名 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fseq | 排序 | int8 | 64 |  | √ | 0 | 排序 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmenuid | 菜单 | varchar | 36 |  | √ | ' ' | 菜单 |
| 7 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_usermarkedmenus |  | fuserid |
| 2 | t_bas_usermarkedmenus_pkey |  | fid |
