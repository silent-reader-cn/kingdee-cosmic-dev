# 词条-cts_wordentry

## 词条-主表 t_cts_wordentry

- **表名称：** 词条-主表
- **表名：** t_cts_wordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 64 |  | √ | ' ' | id |
| 2 | fbillnumber | 单据标识 | varchar | 64 |  | √ | ' ' | 单据标识 |
| 3 | fstatus | 数据状态 | varchar | 64 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | varchar | 64 |  | √ | ' ' | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 64 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 10 | fformitemtype | 字段类型 | int8 | 64 |  | √ | 0 | 词条字段类型 cts_word_itemtype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_wordentry |  | fid |
| 2 | idx_t_cts_wordentry |  | fnumber |

---

## 词条-多语言表 t_cts_wordentry_l

- **表名称：** 词条-多语言表
- **表名：** t_cts_wordentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 64 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fnewname | 新名称 | varchar | 255 |  | √ | ' ' | 新名称 |
| 4 | flocaleid | flocaleid | varchar | 32 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_wordentry_l |  | fpkid |
| 2 | idx_t_cts_wordentryl |  | fid |
