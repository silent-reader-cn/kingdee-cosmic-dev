# 平台首次登入-bos_devp_firstlogin

## 平台首次登入-主表 t_meta_firstlogin

- **表名称：** 平台首次登入-主表
- **表名：** t_meta_firstlogin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpageid | 页面 | varchar | 100 |  | √ | ' ' | 页面 |
| 3 | fisfirstlogin | 首次登入 | varchar | 5 |  | √ | ' ' | 首次登入 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_firstlogin_pkey |  | fid |
| 2 | idx_kdp_firstlogin_userid |  | fuserid,fpageid |
