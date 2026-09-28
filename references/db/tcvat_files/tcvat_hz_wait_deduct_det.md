# 总机构进项待抵扣台账取数明细单据-tcvat_hz_wait_deduct_det

## 总机构进项待抵扣台账取数明细单据-主表 t_tcvat_hz_waitdeduct_det

- **表名称：** 总机构进项待抵扣台账取数明细单据-主表
- **表名：** t_tcvat_hz_waitdeduct_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 5 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 6 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 8 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 9 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: amount :金额 taxamount :税额 |
| 10 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 12 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 13 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 15 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 16 | fsuborg | 分支机构组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | ffiltercondition | 过滤条件设置 | varchar | 2000 |  | √ | ' ' | 过滤条件设置 |
| 18 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 19 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_waitdeduct_det |  | ftaxaccountserialno,ftype |
| 2 | pk_tcvat_hz_waitdeduct_det |  | fid |
