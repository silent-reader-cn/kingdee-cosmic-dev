# 首页常用操作-gl_myoperation

## 首页常用操作-主表 t_gl_myoperation

- **表名称：** 首页常用操作-主表
- **表名：** t_gl_myoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmenuid | 菜单id | varchar | 36 |  | √ | ' ' | 业务应用菜单 bos_devportal_menu |
| 6 | fbizappid | 应用id | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_myoperation |  | fcreatorid,forgid |
| 2 | t_gl_myoperation_pkey |  | fid |
