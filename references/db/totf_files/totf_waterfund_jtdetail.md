# 水利建设基金台账计提取数明细-totf_waterfund_jtdetail

## 水利建设基金台账计提取数明细-主表 t_totf_waterfund_jtdetail

- **表名称：** 水利建设基金台账计提取数明细-主表
- **表名：** t_totf_waterfund_jtdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | 高级配置JSON | varchar | 2000 |  | √ | ' ' | 高级配置JSON |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 8 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 9 | flongruleid | 规则ID | int8 | 64 |  | √ | 0 | [水利基金不含税收入规则 totf_rule_waterfund](../totf_files/totf_rule_waterfund.md) |
| 10 | fmappingid | 映射字段 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :临时 2 :正式 |
| 12 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 13 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 14 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 15 | fmappingtype | 映射类型 | varchar | 50 |  | √ | ' ' | 映射类型,枚举: bos_org :业务单元 |
| 16 | ftaxaccountserialno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 17 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 18 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 20 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 21 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_waterfund_jtdetail |  | fid |
| 2 | idx_t_totf_waterfund_jtdetail |  | ftaxaccountserialno |
