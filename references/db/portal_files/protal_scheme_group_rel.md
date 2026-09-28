# 方案与用户组关系-protal_scheme_group_rel

## 方案与用户组关系-主表 t_bas_mainpagelayoutgroup

- **表名称：** 方案与用户组关系-主表
- **表名：** t_bas_mainpagelayoutgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 用户组 | int8 | 64 |  | √ | 0 | [用户组 portal_scheme_group](../portal_files/portal_scheme_group.md) |
| 3 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | [首页方案 portal_scheme](../portal_files/portal_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_mainpagelayout_group |  | fgroupid |
| 2 | t_bas_mainpagelayoutgroup_pkey |  | fid |
