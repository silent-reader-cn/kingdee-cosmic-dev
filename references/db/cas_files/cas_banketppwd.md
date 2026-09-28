# 银企密码实体-cas_banketppwd

## 银企密码实体-主表 t_cas_banketppwd

- **表名称：** 银企密码实体-主表
- **表名：** t_cas_banketppwd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 4 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpassword | 密码 | varchar | 255 |  | √ | ' ' | 密码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_banketppwd |  | fid |
| 2 | idx_cas_banketppwd_fuser |  | fuser |
