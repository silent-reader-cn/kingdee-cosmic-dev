# 进项税额转出台账取数明细单据-tcvat_accdetail_rollout

## 进项税额转出台账取数明细单据-主表 t_tcvat_accdetail_rollout

- **表名称：** 进项税额转出台账取数明细单据-主表
- **表名：** t_tcvat_accdetail_rollout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhfbl | 划分比例 | numeric | 23 | 10 | √ | 0.0000000000 | 划分比例 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fjzjtrolloutamount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退进项税额 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fjzjtxse | 即征即退销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退销售额 |
| 10 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 12 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 13 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 15 | ffiltercondition | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 16 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fxsehe | 销售额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额合计 |
| 18 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_accdetail_rollout |  | forgid,fskssqq,fskssqz |
| 2 | t_tcvat_accdetail_rollout_pkey |  | fid |
