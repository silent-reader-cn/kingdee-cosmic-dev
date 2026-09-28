# 最近使用的应用-bos_portal_current_app

## 最近使用的应用-主表 t_bas_portal_current_app

- **表名称：** 最近使用的应用-主表
- **表名：** t_bas_portal_current_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcurrentapp | 最近使用应用 | varchar | 1024 |  | √ | ' ' | 最近使用应用 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisnewportal | 是否新版 | varchar | 10 |  | √ | ' ' | 是否新版,枚举: 0 :否 1 :是 |
| 6 | fcurrentmenu | 最近使用菜单 | text | 0 |  |  | ' ' | 最近使用菜单 |
| 7 | fmenuid | 菜单ID | varchar | 100 |  | √ | ' ' | 菜单ID |
| 8 | fappid | 应用ID | varchar | 100 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_portal_current_app |  | fid |
| 2 | t_bas_portal_current_app_index |  | fuserid |
