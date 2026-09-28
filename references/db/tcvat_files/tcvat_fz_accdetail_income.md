# 收入台账未开票明细单据-tcvat_fz_accdetail_income

## 收入台账未开票明细单据-主表 t_tcvat_fz_accdetail_in

- **表名称：** 收入台账未开票明细单据-主表
- **表名：** t_tcvat_fz_accdetail_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 8 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 10 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 12 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | ffiltercondition | 过滤条件设置 | varchar | 1000 |  | √ | ' ' | 过滤条件设置 |
| 14 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_accdetail_in |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_fz_accdetail_in |  | fid |
