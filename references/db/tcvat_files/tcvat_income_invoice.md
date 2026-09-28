# 收入台账开票收入明细-tcvat_income_invoice

## 收入台账开票收入明细-主表 t_tcvat_income_invoice

- **表名称：** 收入台账开票收入明细-主表
- **表名：** t_tcvat_income_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftaxaccountid | ftaxaccountid | int8 | 64 |  | √ | 0 |  |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 8 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 9 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 10 | fdatastatus | 数据状态 | varchar | 10 |  | √ | '1' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 11 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 12 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 13 | fbizdimensiontype | 业务维度-废弃 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 15 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 16 | finvoicecode | finvoicecode | varchar | 100 |  | √ | ' ' |  |
| 17 | finvoicedata | finvoicedata | timestamp | 0 |  |  | null |  |
| 18 | finvoiceno | finvoiceno | varchar | 100 |  | √ | ' ' |  |
| 19 | fmaingoodsname | fmaingoodsname | varchar | 100 |  | √ | ' ' |  |
| 20 | ffiltercondition | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 21 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 22 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 23 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 24 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 25 | fbizdimensionname | 业务维度值-废弃 | varchar | 200 |  | √ | ' ' | 业务维度值-废弃 |
| 26 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 27 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 28 | ftaxruleid | ftaxruleid | int8 | 64 |  | √ | 0 |  |
| 29 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: 5 :增值税专用发票不含税收入 6 :增值税专用发票税额 |
| 30 | finvoicetype | finvoicetype | varchar | 30 |  | √ | ' ' |  |
| 31 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 32 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 33 | fsbbid | 底稿主表id | int8 | 64 |  | √ | 0 | 底稿主表id |
| 34 | fdifferenceinvoice | 差额发票 | bpchar | 1 |  | √ | '0' | 差额发票 |
| 35 | fbizdimensionid | 业务维度值ID-废弃 | varchar | 50 |  | √ | ' ' | 业务维度值ID-废弃 |
| 36 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_income_invoice_pkey |  | fid |
| 2 | idx_t_tcvat_income_invoice |  | forgid,ftaxperiod |

---

## 明细分录-子表 t_tcvat_income_detail_ent

- **表名称：** 明细分录-子表
- **表名：** t_tcvat_income_detail_ent

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
| 1 | pk_tcvat_income_detail_ent |  | fentryid |
