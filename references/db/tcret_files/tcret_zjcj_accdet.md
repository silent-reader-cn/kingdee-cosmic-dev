# 租金采集取数明细-tcret_zjcj_accdet

## 租金采集取数明细-主表 t_tcret_zjcj_accdet

- **表名称：** 租金采集取数明细-主表
- **表名：** t_tcret_zjcj_accdet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | forgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 8 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 9 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 10 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 11 | ftaxaccountserialno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 12 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 13 | fruleid | 规则id | int8 | 64 |  | √ | 0 | [房产出租租金 tcret_rule_fcczzj](../tcret_files/tcret_rule_fcczzj.md) |
| 14 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 15 | frentid | 租金项目id | varchar | 50 |  | √ | ' ' | 租金项目id |
| 16 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zjcj_accdet |  | fid |
| 2 | idx_taxc_tza_frentid |  | frentid |
| 3 | idx_tza_ftaxaccountserialno |  | ftaxaccountserialno,fskssqq,fskssqz,forgid |
