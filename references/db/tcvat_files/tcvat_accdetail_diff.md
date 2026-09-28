# 差额扣除台账取数明细单据-tcvat_accdetail_diff

## 差额扣除台账取数明细单据-主表 t_tcvat_accdetail_diff

- **表名称：** 差额扣除台账取数明细单据-主表
- **表名：** t_tcvat_accdetail_diff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 10 | fdatastatus | 数据状态 | varchar | 10 |  | √ | '1' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 11 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: currentamount :本期发生额 deductamount :本期实际扣除额 jzjtdeductamount :即征即退实际扣除额 |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 14 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 15 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 16 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 17 | fsbbid | 底稿主表id | int8 | 64 |  | √ | 0 | 底稿主表id |
| 18 | ffiltercondition | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 19 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 20 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_accdetail_diff_pkey |  | fid |
| 2 | idx_tcvat_accdetail_diff |  | forgid,fskssqq,fskssqz |

---

## 明细分录-子表 t_tcvat_diff_detail_entry

- **表名称：** 明细分录-子表
- **表名：** t_tcvat_diff_detail_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizdimensionfilter | 业务维度过滤条件 | varchar | 1050 |  | √ | ' ' | 业务维度过滤条件 |
| 3 | fbizdimensionfilter_tag | 业务维度过滤条件_详情 | text | 0 |  |  | null | 业务维度过滤条件_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_diff_detail_entry |  | fentryid |
