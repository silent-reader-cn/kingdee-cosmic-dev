# 应用配置单-ut_app_set

## 应用配置单-主表 t_ut_app_set

- **表名称：** 应用配置单-主表
- **表名：** t_ut_app_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresponser | 负责人 | varchar | 300 |  |  | null | 负责人 |
| 3 | fgitusername | git用户名 | varchar | 50 |  | √ | ' ' | git用户名 |
| 4 | fgitbranch | Git远程分支 | varchar | 100 |  | √ | ' ' | Git远程分支 |
| 5 | fsvnpath | SVN路径 | varchar | 1000 |  |  | null | SVN路径 |
| 6 | fgitrootpath | 元数据目录 | varchar | 255 |  | √ | ' ' | 元数据目录 |
| 7 | fgitrepository | 本地仓库地址 | varchar | 500 |  | √ | ' ' | 本地仓库地址 |
| 8 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fgiturl | Git远程地址 | varchar | 500 |  | √ | ' ' | Git远程地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ut_app_set_fappid |  | fappid |
| 2 | t_ut_app_set_pkey |  | fid |
