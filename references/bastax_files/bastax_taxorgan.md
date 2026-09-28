# 税务机关-bastax_taxorgan

## 税务机关-多语言表 t_bastax_taxorgan_l

- **表名称：** 税务机关-多语言表
- **表名：** t_bastax_taxorgan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 税务机关名称 | varchar | 200 |  | √ | ' ' | 税务机关名称 |
| 3 | ffullname | 长名称 | varchar | 900 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxorgan_l |  | fpkid |
| 2 | idx_bastax_taxorgan_l_0 |  | fid,flocaleid |

---

## 税务机关-主表 t_bastax_taxorgan

- **表名称：** 税务机关-主表
- **表名：** t_bastax_taxorgan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fparentid | 上级税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 是否预设 | bpchar | 1 |  | √ | ' ' | 是否预设 |
| 13 | ftaxorganaddress | 税务机关所在地 | varchar | 50 |  | √ | ' ' | 税务机关所在地 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 税务机关编码 | varchar | 100 |  | √ | ' ' | 税务机关编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxorgan |  | fnumber |
| 2 | pk_bastax_taxorgan |  | fid |
