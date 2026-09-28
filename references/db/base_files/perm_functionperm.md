# 功能权限-perm_functionperm

## 功能权限-主表 t_perm_functionperm

- **表名称：** 功能权限-主表
- **表名：** t_perm_functionperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fdentitytypeid | 业务对象的ID | varchar | 36 |  | √ | ' ' | 业务对象的ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_functionperm_dentitytype |  | fdentitytypeid |
| 2 | ix_functionperm_entityperm |  | fentitytypeid,fpermitemid |
| 3 | t_perm_functionperm_pkey |  | fid |
