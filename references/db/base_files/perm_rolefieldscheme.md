# 角色-字段权限方案关系-perm_rolefieldscheme

## 角色-字段权限方案关系-主表 t_perm_rolefieldscheme

- **表名称：** 角色-字段权限方案关系-主表
- **表名：** t_perm_rolefieldscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | froleid | 角色 | varchar | 18 |  | √ | ' ' | 通用角色 perm_role |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fentnum | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | ffieldpermschemeid | 字段权限方案 | int8 | 64 |  | √ | 0 | 字段权限方案 perm_fieldscheme |
| 8 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_rolefieldscheme |  | fid |
| 2 | idx_prfs_roleappent |  | froleid,fappid,fentnum |
