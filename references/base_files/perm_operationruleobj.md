# 特殊操作权限分配对象-perm_operationruleobj

## 特殊操作权限分配对象-主表 t_perm_operationruleobj

- **表名称：** 特殊操作权限分配对象-主表
- **表名：** t_perm_operationruleobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fobjenabled | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | foperationruleid | 特殊操作权限 | varchar | 18 |  | √ | ' ' | 特殊数据权限规则 perm_operationrule |
| 5 | fentitytypeid | 运行时业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_operationruleobj_pkey |  | fid |
| 2 | ix_perm_00000007 |  | fentitytypeid,fobjenabled |

---

## 单据体-子表 t_perm_opruleobjorg

- **表名称：** 单据体-子表
- **表名：** t_perm_opruleobjorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_opruleobjorg_pkey |  | fentryid |
| 2 | idx_t_perm_opruleobjorg |  | fid,forgid |
