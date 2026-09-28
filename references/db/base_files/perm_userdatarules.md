# 用户数据规则-perm_userdatarules

## 用户数据规则-主表 t_perm_userdatarules

- **表名称：** 用户数据规则-主表
- **表名：** t_perm_userdatarules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdatarulesid | 数据规则方案集合 | int8 | 64 |  | √ | 0 | [数据规则方案集合 perm_datarules](../base_files/perm_datarules.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_userdatarules_pkey |  | fid |
| 2 | idx_perm_userdatarules |  | fuserid |

---

## 单据体-子表 t_perm_userdatarules_dim

- **表名称：** 单据体-子表
- **表名：** t_perm_userdatarules_dim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimtypenum | 权限类型编码 | varchar | 50 |  | √ | ' ' | 权限类型编码 |
| 3 | fdimobjid | 隔离维度对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型,枚举: bos_org :业务单元 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fisincludesub | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_userdatarules_dim |  | fdimtype,fdimobjid,fid |
| 2 | pk_t_perm_userdatarules_dim |  | fentryid |
