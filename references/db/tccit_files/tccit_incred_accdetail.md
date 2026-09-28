# 所得减免台账会计明细-tccit_incred_accdetail

## 所得减免台账会计明细-主表 t_tccit_incred_accdetail

- **表名称：** 所得减免台账会计明细-主表
- **表名：** t_tccit_incred_accdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | 高级配置JSON | text | 0 |  |  | null | 高级配置JSON |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftabletype | 取数表 | varchar | 30 |  | √ | ' ' | 取数表,枚举: tpo_tcvat_balancetype :科目余额表 tpo_tcvat_vouchertype :凭证 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件JSON | text | 0 |  |  | null | 过滤条件JSON |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | fsubjectid | fsubjectid | varchar | 100 |  | √ | ' ' |  |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 12 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 13 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 14 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 15 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 16 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 17 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 18 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fruleid | 规则id | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 20 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 21 | ffiltercondition | 过滤条件 | varchar | 510 |  | √ | ' ' | 过滤条件 |
| 22 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 23 | fdatatype | 取数方式 | int8 | 64 |  | √ | 0 | 科目余额取数方式 tpo_tcvat_balancetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_incred_accdetail |  | ftaxaccountserialno |
| 2 | t_tccit_incred_accdetail_pkey |  | fid |
