# 业务定义分录(树)-rdem_bizdef_entry

## 业务定义分录(树)-主表 t_rdem_bizdef_entry

- **表名称：** 业务定义分录(树)-主表
- **表名：** t_rdem_bizdef_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主表id | int8 | 64 |  | √ | 0 | 主表id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 6 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 7 | fparentnumber | 大类编码 | varchar | 50 |  | √ | ' ' | 大类编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 10 | fprojectname | 项目名称 | varchar | 500 |  | √ | ' ' | 项目名称 |
| 11 | fexpired | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fparent | 上级 | int8 | 64 |  | √ | 0 | [业务定义分录(树) rdem_bizdef_entry](../rdem_files/rdem_bizdef_entry.md) |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fvalidfrom | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_bizdef_entry_m0 |  | fmasterid |
| 2 | pk_rdem_bizdef_entry |  | fentryid |

---

## 业务定义分录(树)-多语言表 t_rdem_bizdef_entry_l

- **表名称：** 业务定义分录(树)-多语言表
- **表名：** t_rdem_bizdef_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 2 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_bizdef_entry_l |  | fpkid |
| 2 | idx_rdem_bizdef_entry_l |  | fentryid,flocaleid |
