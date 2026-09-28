# 基础资料控制业务角色用户差异-xkbd_auth_diff_role_user

## 应用用户-多选基础资料表 t_perm_log_diff_bd_user

- **表名称：** 应用用户-多选基础资料表
- **表名：** t_perm_log_diff_bd_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | 用户信息 bos_usergroup_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_log_diff_bd_user_fk |  | fid |
| 2 | pk_perm_log_diff_bd_user |  | fpkid |

---

## 受控字段-多选基础资料表 t_perm_log_diff_bd_field

- **表名称：** 受控字段-多选基础资料表
- **表名：** t_perm_log_diff_bd_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | 业务单据关联基础资字段 perm_bdauth_field |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_bd_field |  | fpkid |
| 2 | idx_perm_log_diff_bd_field_fk |  | fid |

---

## 例外角色-多选基础资料表 t_perm_log_diff_bd_exrole

- **表名称：** 例外角色-多选基础资料表
- **表名：** t_perm_log_diff_bd_exrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | 通用角色 perm_role |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_bd_exrole |  | fpkid |
| 2 | idx_perm_log_diff_bd_exrole_fk |  | fid |

---

## 基础资料控制业务角色用户差异-主表 t_perm_log_diff_bd_ru

- **表名称：** 基础资料控制业务角色用户差异-主表
- **表名：** t_perm_log_diff_bd_ru

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 日志id | int8 | 64 |  | √ | 0 | 日志id |
| 5 | fopdesc | 操作描述 | varchar | 20 |  | √ | ' ' | 操作描述 |
| 6 | fdatachange_type | 数据变更类型枚举类 | int8 | 64 |  | √ | 0 | 数据变更类型枚举类 |
| 7 | fcontroltype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 0 :修改前 1 :修改后 |
| 8 | fentity_name | 业务对象名称 | varchar | 200 |  | √ | ' ' | 业务对象名称 |
| 9 | fentityid | 业务对象id | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 10 | fappid | 应用id | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_log_diff_bd_ru |  | fid |
| 2 | idx_t_perm_log_diff_bd_ru |  | fperm_logid |

---

## 例外用户-多选基础资料表 t_perm_log_diff_bd_exuser

- **表名称：** 例外用户-多选基础资料表
- **表名：** t_perm_log_diff_bd_exuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | 用户信息 bos_usergroup_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_log_diff_bd_exuser_fk |  | fid |
| 2 | pk_perm_log_diff_bd_exuser |  | fpkid |

---

## 应用角色-多选基础资料表 t_perm_log_diff_bd_role

- **表名称：** 应用角色-多选基础资料表
- **表名：** t_perm_log_diff_bd_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | 通用角色 perm_role |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_bd_role |  | fpkid |
| 2 | idx_perm_log_diff_bd_role_fk |  | fid |

---

## 受控权限项-多选基础资料表 t_perm_log_diff_bd_perm

- **表名称：** 受控权限项-多选基础资料表
- **表名：** t_perm_log_diff_bd_perm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | 权限项 perm_permitem |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_bd_perm |  | fpkid |
| 2 | idx_perm_log_diff_bd_perm_fk |  | fid |
