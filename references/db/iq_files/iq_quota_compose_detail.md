# 组合指标明细单据-iq_quota_compose_detail

## 组合指标明细单据-主表 t_iq_qcompose_detail

- **表名称：** 组合指标明细单据-主表
- **表名：** t_iq_qcompose_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintelligencedeta | 指标明细 | int8 | 64 |  | √ | 0 | 智测测评明细 iq_intelligence_detail |
| 3 | fisask | 是否符合要求 | bpchar | 1 |  | √ | '0' | 是否符合要求 |
| 4 | factualvalueshow | 实际值格式 | varchar | 50 |  | √ | ' ' | 实际值格式 |
| 5 | factualvalue | 实际值 | numeric | 23 | 10 |  | null | 实际值 |
| 6 | fquotaid | 指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcompose_detail_quota |  | fquotaid |
| 2 | pk_iq_qcompose_detail |  | fid |

---

## 标准内容-子表 t_iq_compose_detail

- **表名称：** 标准内容-子表
- **表名：** t_iq_compose_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsatisfy | 是否满足 | int8 | 64 |  | √ | 0 | 是否满足 |
| 3 | fstandardnum | 标准号 | int8 | 64 |  | √ | 0 | 标准号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fstandardvalue | 标准值 | numeric | 23 | 10 |  | null | 标准值 |
| 6 | fquitesymbol | 比较符号 | varchar | 50 |  | √ | ' ' | 比较符号,枚举: 0 :>= 1 :> 2 :< 3 :<= 4 :是(1)/否(0) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fstandardformat | 标准值格式 | varchar | 50 |  | √ | ' ' | 标准值格式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iq_compose_detail |  | fentryid |
| 2 | idx_compose_detail_0 |  | fid |
