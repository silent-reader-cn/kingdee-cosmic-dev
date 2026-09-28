# 上市公司_全量-ipo_listed_company_all

## 上市公司_全量-主表 t_ipo_listed_company_all

- **表名称：** 上市公司_全量-主表
- **表名：** t_ipo_listed_company_all

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 股票名称 | varchar | 50 |  | √ | ' ' | 股票名称 |
| 4 | fcompanyname | 公司名称 | varchar | 50 |  | √ | ' ' | 公司名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fischampion | 是否单项冠军 | bpchar | 1 |  | √ | '0' | 是否单项冠军 |
| 7 | fislittlegaint | 是否小巨人 | bpchar | 1 |  | √ | '0' | 是否小巨人 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :三板 1 :A股 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 股票代码 | varchar | 30 |  | √ | ' ' | 股票代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_listed_company_all |  | fid |
| 2 | idx_ipo_company_all_number |  | fnumber |

---

## 上市公司_全量-多语言表 t_ipo_listed_company_all_l

- **表名称：** 上市公司_全量-多语言表
- **表名：** t_ipo_listed_company_all_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 股票名称 | varchar | 50 |  | √ | ' ' | 股票名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_listed_company_all_l |  | fpkid |
| 2 | idx_ipo_lca_l_pkid |  | fid |
