# 编码组织实体-bos_coderule_orgentity

## 编码组织实体-主表 t_cr_apporg

- **表名称：** 编码组织实体-主表
- **表名：** t_cr_apporg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 编码规则 | varchar | 36 |  | √ | ' ' | [编码规则 bos_coderule](../base_files/bos_coderule.md) |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | ' ' | 包含下级 |
| 3 | forgid | 编码组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cr_apporg_pkey |  | fentryid |
| 2 | idx_t_cr_apporg_fid |  | fid,forgid |
