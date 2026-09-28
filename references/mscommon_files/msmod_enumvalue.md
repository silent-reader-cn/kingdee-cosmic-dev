# 单据字段枚举值-msmod_enumvalue

## 单据字段枚举值-主表 t_msmod_enumvalue

- **表名称：** 单据字段枚举值-主表
- **表名：** t_msmod_enumvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdbvalue | 后台值 | varchar | 128 |  | √ | ' ' | 后台值 |
| 3 | fcolvalue | 枚举值 | varchar | 50 |  | √ | ' ' | 枚举值 |
| 4 | fenumcolname | fenumcolname | varchar | 50 |  | √ | ' ' |  |
| 5 | fenumcolflag | 枚举字段标识 | varchar | 128 |  | √ | ' ' | 枚举字段标识 |
| 6 | fentityid | 实体 | varchar | 128 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_enumvalue |  | fid |
| 2 | idx_msmod_enumvalue_entityid |  | fentityid |

---

## 单据字段枚举值-多语言表 t_msmod_enumvalue_l

- **表名称：** 单据字段枚举值-多语言表
- **表名：** t_msmod_enumvalue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolvalue | 枚举值 | varchar | 50 |  | √ | ' ' | 枚举值 |
| 3 | fenumcolname | 枚举字段名称 | varchar | 50 |  | √ | ' ' | 枚举字段名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_enumvalue_l_fid |  | fid,flocaleid |
| 2 | pk_t_msmod_enumvalue_l |  | fpkid |
