# 进项税额转出台账会计明细-tcvat_roll_out_accounting

## 进项税额转出台账会计明细-主表 t_tcvat_roll_out_accounti

- **表名称：** 进项税额转出台账会计明细-主表
- **表名：** t_tcvat_roll_out_accounti

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 3 | ftaxaccountid | ftaxaccountid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 7 | fdatatable | fdatatable | varchar | 30 |  | √ | ' ' |  |
| 8 | ftabletype | ftabletype | varchar | 30 |  | √ | ' ' |  |
| 9 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 10 | fsubjectid | fsubjectid | varchar | 100 |  | √ | ' ' |  |
| 11 | ftaxruleid | ftaxruleid | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 15 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 16 | ffiltercondition | 过滤条件设置 | varchar | 510 |  | √ | ' ' | 过滤条件设置 |
| 17 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 18 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_roll_out_accounti |  | forgid,ftaxperiod |
| 2 | t_tcvat_roll_out_accounti_pkey |  | fid |
