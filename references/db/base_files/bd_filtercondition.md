# 基础数据过滤方案-bd_filtercondition

## 基础数据过滤方案-多语言表 t_bd_filtercondition_l

- **表名称：** 基础数据过滤方案-多语言表
- **表名：** t_bd_filtercondition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 过滤条件名称 | varchar | 255 |  | √ | ' ' | 过滤条件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_filtercondition_l |  | fpkid |
| 2 | idx_bd_filtercondition_l_id |  | fid,flocaleid |

---

## 基础数据过滤方案-主表 t_bd_filtercondition

- **表名称：** 基础数据过滤方案-主表
- **表名：** t_bd_filtercondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 过滤条件名称 | varchar | 255 |  | √ | ' ' | 过滤条件名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fentityid | 基础资料标识 | varchar | 36 |  | √ | ' ' | 基础资料标识 |
| 7 | ffiltercondition | 过滤方案 | text | 0 |  |  | ' ' | 过滤方案 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_filtercond_entity |  | fentityid |
| 2 | pk_t_bd_filtercondition |  | fid |
