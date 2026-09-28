# 科目-tdm_account

## 科目-主表 t_tdm_account_code

- **表名称：** 科目-主表
- **表名：** t_tdm_account_code

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 100 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | faccountgrade | 科目级次 | int8 | 64 |  | √ | 1 | 科目级次 |
| 5 | fparentid | 上级 | varchar | 100 |  | √ | ' ' | 科目 tdm_account |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | faccountname | faccountname | varchar | 500 |  | √ | ' ' |  |
| 9 | faccounttable | 科目表 | varchar | 100 |  | √ | ' ' | 科目表 |
| 10 | flongnumber | 长编码 | varchar | 300 |  | √ | ' ' | 长编码 |
| 11 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 12 | fbalancetype | 余额方向 | varchar | 20 |  | √ | ' ' | 余额方向 |
| 13 | faccounttableid | 科目表ID | varchar | 50 |  | √ | ' ' | 科目表ID |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 19 | faccounttype | 科目类型 | varchar | 20 |  | √ | ' ' | 科目类型 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | faccountcode | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 22 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_account_code |  | forgid |
| 2 | t_tdm_account_code_pkey |  | fid |
| 3 | idx_t_tdm_account_code2 |  | faccountcode |

---

## 科目-多语言表 t_tdm_account_code_l

- **表名称：** 科目-多语言表
- **表名：** t_tdm_account_code_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 100 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_account_code_l_fid |  | fid |
| 2 | t_tdm_account_code_l_pkey |  | fpkid |
