# 一般纳税人计提进项待抵扣明细单据-tcvat_waitdeduct_det_sjjt

## 一般纳税人计提进项待抵扣明细单据-主表 t_tcvat_waitdeduct_det_jt

- **表名称：** 一般纳税人计提进项待抵扣明细单据-主表
- **表名：** t_tcvat_waitdeduct_det_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 5 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: amount :金额 taxamount :税额 |
| 7 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 10 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | ffiltercondition | 过滤条件设置 | varchar | 1000 |  | √ | ' ' | 过滤条件设置 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_waitdeduct_det_jt |  | fid |
| 2 | idx_waitdeduct_det_serialno |  | forgid,fskssqq,fskssqz |
