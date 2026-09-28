# 自定义全功能菜单-xkbos_customize_menu

## 自定义全功能菜单-主表 t_xkbos_customize_menu

- **表名称：** 自定义全功能菜单-主表
- **表名：** t_xkbos_customize_menu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdata_tag | 自定义数据_详情 | text | 0 |  |  | ' ' | 自定义数据_详情 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 7 | fdata | 自定义数据 | varchar | 255 |  | √ | ' ' | 自定义数据 |
| 8 | fadmin | 是否管理员数据 | int4 | 32 |  | √ | 2 | 是否管理员数据 |
| 9 | fdatatype | 数据类型 | int4 | 32 |  | √ | 0 | 数据类型 |
| 10 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_user_app_admin_id |  | fuserid,fadmin,fdatatype,fappid |
| 2 | pk_t_xkbos_customize_menu |  | fid |
