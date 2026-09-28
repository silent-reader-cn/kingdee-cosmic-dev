# 预缴台账下钻明细单据-tcvat_prepay_account_deta

## 预缴台账下钻明细单据-主表 t_tcvat_prepay_acc_detail

- **表名称：** 预缴台账下钻明细单据-主表
- **表名：** t_tcvat_prepay_acc_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 6 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 7 | fdeclareserialno | 申报编码 | varchar | 50 |  | √ | ' ' | 申报编码 |
| 8 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 9 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 10 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 11 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 12 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 13 | fdetailtype | 取数明细类型 | varchar | 50 |  | √ | ' ' | 取数明细类型,枚举: sales :销售额取数 deduction :扣除额取数 |
| 14 | ffiltercondition | 过滤条件设置 | varchar | 1000 |  | √ | ' ' | 过滤条件设置 |
| 15 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_prepay_acc_detail |  | ftaxaccountserialno,forgid,fskssqq,fskssqz |
| 2 | pk_tcvat_prepay_acc_detail |  | fid |
