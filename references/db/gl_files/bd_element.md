# 会计要素-bd_element

## 会计要素-多语言表 t_bd_accounttype_l

- **表名称：** 会计要素-多语言表
- **表名：** t_bd_accounttype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
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

## 会计要素-主表 t_bd_accounttype

- **表名称：** 会计要素-主表
- **表名：** t_bd_accounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclassify | fclassify | bpchar | 1 |  | √ | '0' |  |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 6 | fparentid | 上级会计要素 | int8 | 64 |  | √ | 0 | 会计要素 bd_element |
| 7 | fdc | 余额方向 | varchar | 30 |  | √ | ' ' | 余额方向,枚举: 1 :借 -1 :贷 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 10 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 11 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 12 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 13 | felementid | 会计要素表 | int8 | 64 |  | √ | 0 | 会计要素表 bd_element_table |
| 14 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fpid | fpid | varchar | 30 |  | √ | ' ' |  |
| 21 | faccounttype | 类别 | bpchar | 1 |  | √ | '0' | 类别,枚举: 0 :资产 1 :负债 2 :权益 3 :成本 4 :损益 5 :表外 6 :共同 7 :其它 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accounttype_pkey |  | fid |
| 2 | idx_bd_accounttype_fparentid |  | fparentid |
