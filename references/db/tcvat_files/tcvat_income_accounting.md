# 收入台账未开票收入明细-tcvat_income_accounting

## 收入台账未开票收入明细-主表 t_tcvat_accounting_detail

- **表名称：** 收入台账未开票收入明细-主表
- **表名：** t_tcvat_accounting_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 3 | ftaxaccountid | ftaxaccountid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 7 | ftabletype | ftabletype | varchar | 30 |  | √ | ' ' |  |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 9 | fsubjectid | fsubjectid | varchar | 100 |  | √ | ' ' |  |
| 10 | ftaxruleid | ftaxruleid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 12 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 13 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 14 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 15 | ffiltercondition | 过滤条件设置 | varchar | 510 |  | √ | ' ' | 过滤条件设置 |
| 16 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_accounting_detail |  | forgid,ftaxperiod |
| 2 | t_tcvat_accounting_detail_pkey |  | fid |
