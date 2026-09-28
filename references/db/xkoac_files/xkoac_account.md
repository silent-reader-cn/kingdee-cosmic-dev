# 经营科目-xkoac_account

## 经营科目-主表 t_xkoac_account

- **表名称：** 经营科目-主表
- **表名：** t_xkoac_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexpensetype | 费用类型 | varchar | 10 |  | √ | ' ' | 费用类型,枚举: 1 :变动费用 2 :固定费用 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fleaf | 明细科目 | bpchar | 1 |  | √ | '1' | 明细科目 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | faccttblid | 经营科目表 | int8 | 64 |  | √ | 0 | [经营科目表 xkoac_accounttable](../xkoac_files/xkoac_accounttable.md) |
| 13 | flevel | 级次 | int4 | 32 |  | √ | 1 | 级次 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | faccounttype | 经营要素 | varchar | 10 |  | √ | ' ' | 经营要素,枚举: -1 :收入 1 :费用 2 :资产 3 :负债 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 20 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 22 | fisfundsaccount | 资金账户 | bpchar | 1 |  | √ | '0' | 资金账户 |
| 23 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_account |  | fnumber |
| 2 | pk_t_xkoac_account |  | fid |

---

## 经营科目-多语言表 t_xkoac_account_l

- **表名称：** 经营科目-多语言表
- **表名：** t_xkoac_account_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_account_l |  | fpkid |
| 2 | idx_xkoac_account_l |  | fid,flocaleid |

---

## 单据体-子表 t_xkoac_accountentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_accountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrp | 经营核算维度 | int8 | 64 |  | √ | 0 | [经营核算维度 xkoac_dimension](../basedata_files/xkoac_dimension.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frequire | 必录 | bpchar | 1 |  | √ | '1' | 必录 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_accountentry |  | fid |
| 2 | pk_t_xkoac_accountentry |  | fentryid |
