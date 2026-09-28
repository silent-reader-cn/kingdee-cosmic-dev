# 上市公司_全量(包含港股/美股等境外公司)-dfa_listed_company_all

## 上市公司_全量(包含港股/美股等境外公司)-多语言表 t_dfa_listed_company_all_l

- **表名称：** 上市公司_全量(包含港股/美股等境外公司)-多语言表
- **表名：** t_dfa_listed_company_all_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcompanyname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fstocktype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_lca_l_pkid |  | fid |
| 2 | pk_dfa_listed_company_all_l |  | fpkid |

---

## 上市公司_全量(包含港股/美股等境外公司)-主表 t_dfa_listed_company_all

- **表名称：** 上市公司_全量(包含港股/美股等境外公司)-主表
- **表名：** t_dfa_listed_company_all

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcompanyname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | freportdate | 报告期 | varchar | 2000 |  | √ | ' ' | 报告期 |
| 7 | fstocktype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_listed_company_all |  | fid |
| 2 | idx_dfa_company_all_number |  | fnumber |
