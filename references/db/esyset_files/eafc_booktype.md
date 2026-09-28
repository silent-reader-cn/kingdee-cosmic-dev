# 账薄类型-eafc_booktype

## 账薄类型-主表 tk_eafc_booktype

- **表名称：** 账薄类型-主表
- **表名：** tk_eafc_booktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_book_name | fk_eafc_book_name | varchar | 50 |  |  | null |  |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fk_eafc_book_no | 账薄编码 | varchar | 30 |  | √ | ' ' | 账薄编码 |
| 10 | fk_eafc_book_nature | 账薄性质 | varchar | 50 |  | √ | ' ' | 账薄性质 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_booktype |  | fid |

---

## 账薄类型-多语言表 tk_eafc_booktype_l

- **表名称：** 账薄类型-多语言表
- **表名：** tk_eafc_booktype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fk_eafc_book_name | 账薄名称 | varchar | 50 |  | √ | ' ' | 账薄名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_booktype_l |  | fpkid |
| 2 | idx_eafc_booktype_l_fk |  | fid |
