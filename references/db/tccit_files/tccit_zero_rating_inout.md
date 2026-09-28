# 不征税收入及支出台账-tccit_zero_rating_inout

## 不征税收入及支出台账-主表 t_tccit_zero_rating_inout

- **表名称：** 不征税收入及支出台账-主表
- **表名：** t_tccit_zero_rating_inout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fgovname | 政府主管部门 | varchar | 50 |  | √ | ' ' | 政府主管部门 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsumregisterpay | 累计登记支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计登记支出金额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprojectname | 所属项目名称 | varchar | 50 |  | √ | ' ' | 所属项目名称 |
| 11 | fincomedate | 收入日期 | timestamp | 0 |  |  | null | 收入日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: specialfund :专项用途财政性资金 other :其他 |
| 14 | fzeroratingamount | 其中：不征税收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：不征税收入金额 |
| 15 | fbizdesc | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 16 | ffiscalamount | 财政性资金 | numeric | 23 | 10 | √ | 0.0000000000 | 财政性资金 |
| 17 | fsumfinancial | 累计上缴财政金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计上缴财政金额 |
| 18 | fprojectno | 所属项目号 | varchar | 50 |  | √ | ' ' | 所属项目号 |
| 19 | fsumregisterincome | 累计登记收益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计登记收益金额 |
| 20 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 21 | fsumincludedtaxable | 累计计入应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 累计计入应税收入 |
| 22 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbalanceamount | 结余可用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结余可用金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_zero_rating_inout |  | fid |
| 2 | idx_tccit_zero_rating_inout |  | fbillno |

---

## 结余金额计入应税收入登记-子表 t_tccit_balance_reg

- **表名称：** 结余金额计入应税收入登记-子表
- **表名：** t_tccit_balance_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalanceregdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | fbalanceregvoucher | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 4 | fbalanceregdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbalanceregamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_balance_reg_fk |  | fid |
| 2 | pk_tccit_balance_reg |  | fentryid |

---

## 计入收益登记-子表 t_tccit_in_income_reg

- **表名称：** 计入收益登记-子表
- **表名：** t_tccit_in_income_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fincomeregdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fincomeregvoucher | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 5 | fincomeregamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fincomeregdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_in_income_reg_fk |  | fid |
| 2 | pk_tccit_in_income_reg |  | fentryid |

---

## 支出情况登记-子表 t_tccit_pay_reg

- **表名称：** 支出情况登记-子表
- **表名：** t_tccit_pay_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayregvoucher | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 3 | fpayregdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | frefcardno | 关联资产卡片号 | varchar | 50 |  | √ | ' ' | 关联资产卡片号 |
| 5 | fpayregdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: 1 :资本化 2 :费用化 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpayregamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_pay_reg_fk |  | fid |
| 2 | pk_tccit_pay_reg |  | fentryid |

---

## 上缴财政登记-子表 t_tccit_financial_reg

- **表名称：** 上缴财政登记-子表
- **表名：** t_tccit_financial_reg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffinancialregdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | ffinancialregdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffinancialregvoucher | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffinancialregamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_financial_reg_fk |  | fid |
| 2 | pk_tccit_financial_reg |  | fentryid |
