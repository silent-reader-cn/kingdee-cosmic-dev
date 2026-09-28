# 印花税税率（树）-tctb_tcsd_taxratetree

## 印花税税率（树）-多语言表 t_tpo_tcsd_taxrateentry_l

- **表名称：** 印花税税率（树）-多语言表
- **表名：** t_tpo_tcsd_taxrateentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 2 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tpo_tcsd_taxrateentry_l_pkey |  | fpkid |
| 2 | idx_tpo_tcsd_taxrateentry_l_0 |  | fentryid,flocaleid |

---

## 印花税税率（树）-主表 t_tpo_tcsd_taxrateentry

- **表名称：** 印花税税率（树）-主表
- **表名：** t_tpo_tcsd_taxrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 税目及税率期间 | int8 | 64 |  | √ | 0 | 税目及税率期间 |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 5 | ftaxrate | 税率 | varchar | 100 |  | √ | ' ' | 税率 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fdescription | 说明 | varchar | 500 |  | √ | ' ' | 说明 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | frange | 范围 | varchar | 200 |  | √ | ' ' | 范围 |
| 17 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 18 | fparent | 上级 | int8 | 64 |  | √ | 0 | [印花税税率（树） tctb_tcsd_taxratetree](../tctb_files/tctb_tcsd_taxratetree.md) |
| 19 | fnsr | 纳税人 | varchar | 100 |  | √ | ' ' | 纳税人 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tpo_tcsd_taxrateentry_pkey |  | fentryid |
| 2 | idx_tpo_tcsd_taxrateentry |  | fnumber |
