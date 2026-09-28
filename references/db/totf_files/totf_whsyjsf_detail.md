# 文化事业建设费自动取数明细-totf_whsyjsf_detail

## 文化事业建设费自动取数明细-主表 t_totf_whsyjsf_detail

- **表名称：** 文化事业建设费自动取数明细-主表
- **表名：** t_totf_whsyjsf_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 5 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 6 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 7 | flongruleid | 规则ID | int8 | 64 |  | √ | 0 | 文化事业建设费应征收入规则 totf_rule_whsyjsf |
| 8 | fmappingid | 映射字段 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 11 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 12 | fmappingtype | 映射类型 | varchar | 50 |  | √ | ' ' | 映射类型,枚举: bos_org :业务单元 |
| 13 | ftaxaccountserialno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 15 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 17 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 18 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_whsyjsf_detail |  | fid |
| 2 | idx_totf_whsydeta_serialno |  | ftaxaccountserialno |
