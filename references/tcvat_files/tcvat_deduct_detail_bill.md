# 进项抵扣明细单据-tcvat_deduct_detail_bill

## 进项抵扣明细单据-主表 t_tcvat_deduct_detail_bil

- **表名称：** 进项抵扣明细单据-主表
- **表名：** t_tcvat_deduct_detail_bil

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 5 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 6 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 8 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: amount :金额 taxamount :税额 count :份数 |
| 9 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 11 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 12 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 13 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 14 | ffiltercondition | 过滤条件设置 | varchar | 1000 |  | √ | ' ' | 过滤条件设置 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_deduct_detail_serialno_1 |  | ftaxaccountserialno |
| 2 | pk_tcvat_deduct_detail_bil |  | fid |
