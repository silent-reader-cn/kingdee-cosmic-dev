# 应用自定义常用权限项-xkbizapp_usepermitem

## 应用自定义常用权限项-主表 t_base_appusepermitem

- **表名称：** 应用自定义常用权限项-主表
- **表名：** t_base_appusepermitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdata | 文本 | text | 0 |  |  | null | 文本 |
| 4 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_base_appusepermitem |  | fid |
| 2 | idx_base_appusepermitem |  | fuserid,fbizappid |
