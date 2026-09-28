# 文档类型权限-mpm_doctypeperm

## 文档类型权限-主表 t_mpm_doctypeperm

- **表名称：** 文档类型权限-主表
- **表名：** t_mpm_doctypeperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 3 | fdoctypeid | 文档类型 | int8 | 64 |  | √ | 0 | [文档类型 mpm_documenttype](../mpm_files/mpm_documenttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm__doctypeperm |  | fdoctypeid |
| 2 | pk_t_mpm_doctypeperm |  | fid |

---

## 单据体-子表 t_mpm_doctypepermentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_doctypepermentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | froleid | 通用角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_doctypepermentry |  | fentryid |
| 2 | idx_mpm_doctypepermentry |  | froleid |
