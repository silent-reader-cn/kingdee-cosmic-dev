# 未按权责发生制确认收入台账-tccit_not_taccrual_basis

## 未按权责发生制确认收入台账-主表 t_tccit_not_taccrual_bas

- **表名称：** 未按权责发生制确认收入台账-主表
- **表名：** t_tccit_not_taccrual_bas

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fljtaxincome | 累计税收收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税收收入金额 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcontractstart | 合同期间.开始 | timestamp | 0 |  |  | null | 合同期间.开始 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsyjzamount | 剩余结转金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余结转金额 |
| 12 | ftotalamt | 合同总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同总金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcontractend | 合同期间.结束 | timestamp | 0 |  |  | null | 合同期间.结束 |
| 15 | fincometype | 收入类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 16 | fbillno | 项目编号 | varchar | 30 |  | √ | ' ' | 项目编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fljbookincome | 累计账载收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计账载收入金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_not_taccrual_bas |  | fbillno,forgid |
| 2 | pk_tccit_not_taccrual_bas |  | fid |

---

## 税收收入登记台账-子表 t_tccit_tax_income_reg

- **表名称：** 税收收入登记台账-子表
- **表名：** t_tccit_tax_income_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookeddate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | faccountingdoc | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_tax_income_reg |  | fentryid |
| 2 | idx_tccit_tax_income_reg_fk |  | fid |

---

## 账载收入登记台账-子表 t_tccit_book_income_reg

- **表名称：** 账载收入登记台账-子表
- **表名：** t_tccit_book_income_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookeddate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | faccountingdoc | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_book_income_reg_fk |  | fid |
| 2 | pk_tccit_book_income_reg |  | fentryid |
