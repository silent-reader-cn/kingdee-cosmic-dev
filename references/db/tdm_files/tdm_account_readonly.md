# 科目_只读（废弃）-tdm_account_readonly

## 科目_只读（废弃）-主表 t_tdm_account_code_read

- **表名称：** 科目_只读（废弃）-主表
- **表名：** t_tdm_account_code_read

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 100 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | faccountgrade | 科目级次 | int8 | 64 |  | √ | 0 | 科目级次 |
| 5 | fparentid | 上级 | varchar | 36 |  | √ | ' ' | [科目_只读（废弃） tdm_account_readonly](../tdm_files/tdm_account_readonly.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccounttable | 科目表 | varchar | 50 |  | √ | ' ' | 科目表 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 10 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 11 | fbalancetype | 余额方向 | varchar | 50 |  | √ | ' ' | 余额方向 |
| 12 | faccounttableid | 科目表ID | varchar | 50 |  | √ | ' ' | 科目表ID |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | forggroup | 组织分组 | text | 0 |  |  | null | 组织分组 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 19 | faccounttype | 科目类型 | varchar | 50 |  | √ | ' ' | 科目类型 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | faccountcode | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_account_code_read |  | faccountcode |
| 2 | t_tdm_account_code_read_pkey |  | fid |

---

## 科目_只读（废弃）-多语言表 t_tdm_account_code_read_l

- **表名称：** 科目_只读（废弃）-多语言表
- **表名：** t_tdm_account_code_read_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 100 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_account_code_read_l_0 |  | fid,flocaleid |
| 2 | t_tdm_account_code_read_l_pkey |  | fpkid |
