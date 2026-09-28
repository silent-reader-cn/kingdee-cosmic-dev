# 资源备份仓库配置-isc_res_backup_git_cfg

## 资源备份仓库配置-主表 t_iscb_backup_git_cfg

- **表名称：** 资源备份仓库配置-主表
- **表名：** t_iscb_backup_git_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbranch | 分支 | varchar | 50 |  |  | ' ' | 分支,枚举: |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 5 | fproject_id | 项目全名 | varchar | 50 |  |  | ' ' | 项目全名 |
| 6 | fprivate_token | 访问令牌 | varchar | 50 |  |  | ' ' | 访问令牌 |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 8 | fdomain | 远程仓库域名 | varchar | 100 |  |  | ' ' | 远程仓库域名 |
| 9 | fproject_name | 项目名称 | varchar | 50 |  |  | ' ' | 项目名称 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_backup_git_cfg |  | fid |
| 2 | idx_backup_git_cfg |  | fproject_name |
