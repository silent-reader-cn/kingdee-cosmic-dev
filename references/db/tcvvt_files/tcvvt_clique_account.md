# 科目-tcvvt_clique_account

## 科目-主表 t_tcvvt_clique_account

- **表名称：** 科目-主表
- **表名：** t_tcvvt_clique_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 科目名称 | varchar | 500 |  | √ | ' ' | 科目名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 5 | fparentid | 父级科目代码 | int8 | 64 |  | √ | 0 | [科目 tcvvt_clique_account](../tcvvt_files/tcvvt_clique_account.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fnd_dm | 年度代码 | varchar | 4 |  | √ | ' ' | 年度代码 |
| 9 | flongnumber | 长编码 | varchar | 400 |  | √ | ' ' | 长编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fkmfx | 科目方向 | varchar | 50 |  | √ | ' ' | 科目方向,枚举: 1 :借方 2 :贷方 3 :其他 9 :未知 |
| 16 | fyear | 年度代码 | timestamp | 0 |  |  | null | 年度代码 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :自动采集 |
| 19 | fnumber | 科目代码 | varchar | 100 |  | √ | ' ' | 科目代码 |
| 20 | fkmlx | 科目类型 | varchar | 50 |  | √ | ' ' | 科目类型,枚举: 1 :资产 2 :负债 3 :共同 4 :权益 5 :成本 6 :损益 7 :其他 9 :未知 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_clique_account |  | forgid,fnumber |
| 2 | pk_tcvvt_clique_account |  | fid |

---

## 科目-多语言表 t_tcvvt_clique_account_l

- **表名称：** 科目-多语言表
- **表名：** t_tcvvt_clique_account_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 科目名称 | varchar | 500 |  | √ | ' ' | 科目名称 |
| 3 | ffullname | 长名称 | varchar | 1500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_clique_account_l |  | fpkid |
| 2 | idx_tcvvt_clique_account_l_0 |  | fid,flocaleid |
