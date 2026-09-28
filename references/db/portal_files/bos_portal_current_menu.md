# 最近使用菜单-bos_portal_current_menu

## 最近使用菜单-主表 t_bas_portal_current_menu

- **表名称：** 最近使用菜单-主表
- **表名：** t_bas_portal_current_menu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmenuid | 最近使用菜单 | varchar | 36 |  | √ | ' ' | 最近使用菜单 |
| 5 | fappid | 最近使用应用 | varchar | 36 |  | √ | ' ' | 最近使用应用 |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_portal_current_menu |  | fid |
| 2 | idx_portal_current_menu_userid |  | fuserid |
