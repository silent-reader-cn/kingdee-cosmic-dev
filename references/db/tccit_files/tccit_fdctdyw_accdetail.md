# 房地产特地业务台账明细-tccit_fdctdyw_accdetail

## 房地产特地业务台账明细-主表 t_tccit_fdctdyw_accdetail

- **表名称：** 房地产特地业务台账明细-主表
- **表名：** t_tccit_fdctdyw_accdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | 高级配置JSON | text | 0 |  |  | null | 高级配置JSON |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件JSON | text | 0 |  |  | null | 过滤条件JSON |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 8 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 9 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 11 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 12 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 13 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 15 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 16 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fruleid | 规则id | int8 | 64 |  | √ | 0 | [其它取数规则 tccit_other_rule](../tccit_files/tccit_other_rule.md) |
| 18 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 19 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 20 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_fdctdyw_accdetail |  | fid |
| 2 | idx_tccit_fdctdyw_accdeta |  | forgid,fskssqq,fskssqz |
