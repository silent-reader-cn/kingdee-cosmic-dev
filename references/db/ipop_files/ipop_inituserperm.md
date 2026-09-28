# 用户权限维护（废弃）-ipop_inituserperm

## 用户权限维护（废弃）-多语言表 t_ipop_inituserperm_l

- **表名称：** 用户权限维护（废弃）-多语言表
- **表名：** t_ipop_inituserperm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_inituserperm_l |  | fpkid |
| 2 | idx_ipop_inituserperm_l |  | fid,flocaleid |

---

## 用户权限维护（废弃）-主表 t_ipop_inituserperm

- **表名称：** 用户权限维护（废弃）-主表
- **表名：** t_ipop_inituserperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fappnumber | 应用简码 | varchar | 50 |  | √ | ' ' | 应用简码 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmarkfinish | 标记完成 | bpchar | 1 |  | √ | ' ' | 标记完成 |
| 7 | fformid | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 8 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_inituserperm |  | fid |
| 2 | idx_ipop_inituserperm_app |  | fappnumber |
| 3 | idx_ipop_inituserperm_id |  | fformid |
