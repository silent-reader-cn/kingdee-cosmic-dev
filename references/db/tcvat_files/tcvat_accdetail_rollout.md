# 进项税额转出台账取数明细单据-tcvat_accdetail_rollout

## 进项税额转出台账取数明细单据-主表 t_tcvat_accdetail_rollout

- **表名称：** 进项税额转出台账取数明细单据-主表
- **表名：** t_tcvat_accdetail_rollout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhfbl | 划分比例 | numeric | 23 | 10 | √ | 0.0000000000 | 划分比例 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fjzjtrolloutamount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退进项税额 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 9 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 10 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | fjzjtxse | 即征即退销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退销售额 |
| 12 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 13 | fdatastatus | 数据状态 | varchar | 10 |  | √ | '1' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 14 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 15 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 16 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 17 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 18 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 19 | fsbbid | 底稿主表id | int8 | 64 |  | √ | 0 | 底稿主表id |
| 20 | ffiltercondition | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 21 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 22 | fxsehe | 销售额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额合计 |
| 23 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_accdetail_rollout |  | forgid,fskssqq,fskssqz |
| 2 | t_tcvat_accdetail_rollout_pkey |  | fid |

---

## 明细分录-子表 t_tcvat_rollout_detail_en

- **表名称：** 明细分录-子表
- **表名：** t_tcvat_rollout_detail_en

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
| 1 | pk_tcvat_rollout_detail_en |  | fentryid |
