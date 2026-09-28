# 应用权限管理-bos_app_isolation

## 授权应用-多选基础资料表 t_meta_isolationapp

- **表名称：** 授权应用-多选基础资料表
- **表名：** t_meta_isolationapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_meta_isolationapp |  | fpkid |
| 2 | idx_isolation_app_id |  | fid |

---

## 应用权限管理-主表 t_meta_isolation

- **表名称：** 应用权限管理-主表
- **表名：** t_meta_isolation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | faccounttype | 账号类型 | varchar | 50 |  | √ | ' ' | 账号类型,枚举: sys :苍穹账号 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faccount | 苍穹账号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fadmin | 管理员 | bpchar | 1 |  | √ | '1' | 管理员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_isolation_account |  | faccount |
| 2 | pk_t_meta_isolation |  | fid |
