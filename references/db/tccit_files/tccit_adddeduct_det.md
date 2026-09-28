# 加计扣除取数明细-tccit_adddeduct_det

## 加计扣除取数明细-主表 t_tccit_adddeduct_det

- **表名称：** 加计扣除取数明细-主表
- **表名：** t_tccit_adddeduct_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | fadvancedconfjson | 高级配置JSON | text | 0 |  |  | null | 高级配置JSON |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftabletype | 取数表 | varchar | 50 |  | √ | ' ' | 取数表,枚举: tpo_tcvat_balancetype :科目余额表 tpo_tcvat_vouchertype :凭证 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件JSON | text | 0 |  |  | null | 过滤条件JSON |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 12 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 13 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 14 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 15 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 16 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 17 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 优惠项目取数规则 tccit_preferential_item |
| 19 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 20 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 21 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 22 | fdatatype | 取数方式 | int8 | 64 |  | √ | 0 | 科目余额取数方式 tpo_tcvat_balancetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_adddeduct_det |  | fid |
| 2 | idx_adddeduct_det |  | forgid,fskssqq,fskssqz |
