# svn管理-svnmanage

## svn管理-主表 t_meta_svnmanage

- **表名称：** svn管理-主表
- **表名：** t_meta_svnmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsvnurl | SVN地址 | varchar | 500 |  | √ | ' ' | SVN地址 |
| 3 | fmobilealone | 移动端独立SVN | bpchar | 1 |  | √ | '0' | 移动端独立SVN |
| 4 | fbizunitid | 应用分组ID | varchar | 36 |  | √ | ' ' | 应用分组ID |
| 5 | fgitbranch | Git远程分支 | varchar | 100 |  | √ | ' ' | Git远程分支 |
| 6 | fgitrepository | 仓库地址 | varchar | 500 |  |  | null | 仓库地址 |
| 7 | fbizappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 8 | fsvnserver | SVN服务器 | varchar | 50 |  | √ | ' ' | SVN服务器,枚举: nextserver :下一代SVN服务器 customserver :自定义SVN服务器 |
| 9 | fgitusername | git用户名 | varchar | 50 |  | √ | ' ' | git用户名 |
| 10 | fmobilesvnurl | 移动SVN地址 | varchar | 500 |  | √ | ' ' | 移动SVN地址 |
| 11 | fgitrootpath | 元数据目录 | varchar | 255 |  | √ | ' ' | 元数据目录 |
| 12 | fmanagetype | 管理类型 | varchar | 5 |  | √ | ' ' | 管理类型 |
| 13 | fgiturl | GIT地址 | varchar | 500 |  |  | null | GIT地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_svnmanage_pkey |  | fid |
| 2 | idx_kdp_svnmanager_bizappid |  | fbizappid |
