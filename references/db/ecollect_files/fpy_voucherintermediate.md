# 凭证中间表(五菱)-fpy_voucherintermediate

## 单据体-子表 tk_fpy_wl_file

- **表名称：** 单据体-子表
- **表名：** tk_fpy_wl_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_lhqb_ismainfile | isMainFile | varchar | 50 |  | √ | ' ' | isMainFile |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fk_lhqb_filename | fileName | varchar | 50 |  | √ | ' ' | fileName |
| 5 | fk_lhqb_download | download | varchar | 50 |  | √ | ' ' | download |
| 6 | fk_lhqb_srcname | srcName | varchar | 50 |  | √ | ' ' | srcName |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_wl_file |  | fentryid |

---

## 单据体-子表 tk_fpy_wl_uppervoucherli

- **表名称：** 单据体-子表
- **表名：** tk_fpy_wl_uppervoucherli

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_lhqb_voucherid | voucherId | varchar | 50 |  | √ | ' ' | voucherId |
| 3 | fk_lhqb_modifierfield1 | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fk_lhqb_modifydatefield1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_wl_uppervoucherli |  | fentryid |

---

## 单据体-子表 tk_fpy_wl_item

- **表名称：** 单据体-子表
- **表名：** tk_fpy_wl_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_lhqb_debit | debit | numeric | 23 | 10 |  | null | debit |
| 3 | fk_lhqb_totaldebittra | totaldebittrat | numeric | 23 | 10 |  | null | totaldebittrat |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_lhqb_modifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fk_lhqb_credit | credit | numeric | 23 | 10 |  | null | credit |
| 7 | fk_lhqb_totalcredittra | totalCreditTra | numeric | 23 | 10 |  | null | totalCreditTra |
| 8 | fk_lhqb_modifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_lhqb_totalcreditloc | totalCreditLoc | numeric | 23 | 10 |  | null | totalCreditLoc |
| 10 | fk_lhqb_desc | desc | varchar | 50 |  | √ | ' ' | desc |
| 11 | fk_lhqb_accountcodes | accountcode | varchar | 50 |  | √ | ' ' | accountcode |
| 12 | fk_lhqb_accountname | accountname | varchar | 50 |  | √ | ' ' | accountname |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_wl_item |  | fentryid |

---

## 凭证中间表(五菱)-主表 tk_fpy_voucherintermed

- **表名称：** 凭证中间表(五菱)-主表
- **表名：** tk_fpy_voucherintermed

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_lhqb_updatetime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 3 | fk_lhqb_vouchernum | voucherNum | varchar | 50 |  | √ | ' ' | voucherNum |
| 4 | fk_lhqb_datefield | period | timestamp | 0 |  |  | null | period |
| 5 | fk_lhqb_voucherorganizati | voucherOrganizationName | varchar | 50 |  | √ | ' ' | voucherOrganizationName |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_lhqb_cashier | cashier | varchar | 50 |  | √ | ' ' | cashier |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_lhqb_qperiodd | qperiodd | varchar | 50 |  | √ | ' ' | qperiodd |
| 10 | fk_lhqb_accountdate | accountDate | timestamp | 0 |  |  | null | accountDate |
| 11 | fk_lhqb_review | review | varchar | 50 |  | √ | ' ' | review |
| 12 | fk_lhqb_rate | rate | numeric | 23 | 10 |  | null | rate |
| 13 | fbillno | 凭证编码 | varchar | 30 |  | √ | ' ' | 凭证编码 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fk_lhqb_period | qperiod | varchar | 50 |  | √ | ' ' | qperiod |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fk_lhqb_auditing | auditing | varchar | 50 |  | √ | ' ' | auditing |
| 19 | fk_lhqb_creater | creater | varchar | 50 |  | √ | ' ' | creater |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fk_lhqb_textfield | currency | varchar | 50 |  | √ | ' ' | currency |
| 22 | fk_lhqb_voucherorgnumber | voucherOrgNumber | varchar | 50 |  | √ | ' ' | voucherOrgNumber |
| 23 | fk_lhqb_title | title | varchar | 50 |  | √ | ' ' | title |
| 24 | fk_lhqb_vouchertype | vouchertype | varchar | 50 |  | √ | ' ' | vouchertype |
| 25 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fk_lhqb_id | id | varchar | 50 |  | √ | ' ' | id |
| 27 | fk_lhqb_posting | posting | varchar | 50 |  | √ | ' ' | posting |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_voucherintermed |  | fid |
