# PLM角色用户关联-plm_plmsm_roleuser

## PLM角色用户关联-主表 t_plmsm_role

- **表名称：** PLM角色用户关联-主表
- **表名：** t_plmsm_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 角色名称 | varchar | 50 |  | √ | ' ' | 角色名称 |
| 3 | froletype | 角色类型 | bpchar | 1 |  | √ | '8' | 角色类型,枚举: 0 :管理员角色 1 :内置角色 2 :业务角色 |
| 4 | fnumber | 角色编码 | varchar | 50 |  | √ | ' ' | 角色编码 |
| 5 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_role |  | fid |
| 2 | idx_plmsm_role_number |  | fnumber |

---

## 用户（组）-子表 t_plmsm_roleuser

- **表名称：** 用户（组）-子表
- **表名：** t_plmsm_roleuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelationid | 上下文标识 | int8 | 64 |  | √ | 0 | 上下文标识 |
| 3 | fuserorgroup | 用户或组 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fusergrouptype | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型,枚举: bos_user :人员 bos_usergroup :用户组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_roleuser |  | fentryid |
| 2 | idx_plmsm_roleuser_userrel |  | frelationid,fuserorgroup |

---

## PLM角色用户关联-多语言表 t_plmsm_role_l

- **表名称：** PLM角色用户关联-多语言表
- **表名：** t_plmsm_role_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 角色名称 | varchar | 50 |  | √ | ' ' | 角色名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_role_l |  | fpkid |
| 2 | idx_plmsm_role_l |  | fid,flocaleid |
