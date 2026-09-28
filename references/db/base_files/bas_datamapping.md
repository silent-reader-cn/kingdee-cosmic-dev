# 数据映射-bas_datamapping

## 数据映射-主表 t_bas_datamapping

- **表名称：** 数据映射-主表
- **表名：** t_bas_datamapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fdatatypeid | 数据类型 | int8 | 64 |  | √ | 0 | 数据类型定义 bas_datatype |
| 4 | fextdataid | 外部数据ID | varchar | 45 |  | √ | ' ' | 外部数据ID |
| 5 | fdataid | 内部数据ID | int8 | 64 |  | √ | 0 | 内部数据ID |
| 6 | fnumber | 内部数据编码 | varchar | 50 |  | √ | ' ' | 内部数据编码 |
| 7 | fextname | fextname | varchar | 50 |  | √ | ' ' |  |
| 8 | fextnumber | 外部数据编码 | varchar | 50 |  | √ | ' ' | 外部数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_datamapping_bdtype |  | fdatatypeid |
| 2 | t_bas_datamapping_pkey |  | fid |

---

## 数据映射-多语言表 t_bas_datamapping_l

- **表名称：** 数据映射-多语言表
- **表名：** t_bas_datamapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 内部数据名称 | varchar | 255 |  | √ | ' ' | 内部数据名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fextname | 外部数据名称 | varchar | 255 |  | √ | ' ' | 外部数据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_datamapping_l_pkey |  | fpkid |
| 2 | idx_t_bas_datamapping_l_fid |  | fid |
