# 成本中心余额-cca_costcenterbal

## 成本中心余额-主表 t_cca_costcenterbal

- **表名称：** 成本中心余额-主表
- **表名：** t_cca_costcenterbal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftotalamount | 总余额 | numeric | 23 | 10 | √ | 0 | 总余额 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | ftotaldebitamount | 总借方金额 | numeric | 23 | 10 | √ | 0 | 总借方金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | ftotalcreditamount | 总贷方金额 | numeric | 23 | 10 | √ | 0 | 总贷方金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_costcenterbal |  | fid |
| 2 | idx_cca_costcenterbal_m0 |  | fbillno |

---

## 单据体-子表 t_cca_costcenterbalentry

- **表名称：** 单据体-子表
- **表名：** t_cca_costcenterbalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcreditamount | 贷方金额 | numeric | 23 | 10 | √ | 0 | 贷方金额 |
| 5 | faccountview | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 6 | famount | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 7 | fdebitamount | 借方金额 | numeric | 23 | 10 | √ | 0 | 借方金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_costcenterbalentry |  | fentryid |
| 2 | idx_cca_costcenterbalentry_fk |  | fid |
