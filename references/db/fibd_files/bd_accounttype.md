# 科目类型-bd_accounttype

## 科目类型-多语言表 t_bd_accounttype_l

- **表名称：** 科目类型-多语言表
- **表名：** t_bd_accounttype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  |  | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_acttype_l_fid |  | fid,flocaleid |
| 2 | t_bd_accounttype_l_pkey |  | fpkid |

---

## 科目类型-主表 t_bd_accounttype

- **表名称：** 科目类型-主表
- **表名：** t_bd_accounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fpid | fpid | varchar | 30 |  | √ | ' ' |  |
| 9 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 10 | fclassify | 分类 | bpchar | 1 |  | √ | '0' | 分类,枚举: 0 :无 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 13 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [科目类型 bd_accounttype](../fibd_files/bd_accounttype.md) |
| 14 | fdc | fdc | varchar | 30 |  | √ | ' ' |  |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 17 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 18 | fispreyearspl | fispreyearspl | bpchar | 1 |  | √ | '0' |  |
| 19 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 20 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 21 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 22 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 23 | faccounttype | 科目属性 | bpchar | 1 |  | √ | '0' | 科目属性,枚举: 0 :资产 1 :负债 2 :权益 3 :成本 4 :损益 5 :表外 6 :共同 7 :其它 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accounttype_pkey |  | fid |
| 2 | idx_bd_accounttype_fparentid |  | fparentid |
