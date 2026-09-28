# 行业要求单据-iq_industry_ask

## 单据体-子表 t_iq_iask_entry

- **表名称：** 单据体-子表
- **表名：** t_iq_iask_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fistraden | 是否所属行业 | bpchar | 1 |  | √ | '0' | 是否所属行业 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | findustryrequirements | 行业要求 | int8 | 64 |  | √ | 0 | [行业要求映射 iq_industry_requirements](../iq_files/iq_industry_requirements.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iask_entry_0 |  | fid |
| 2 | pk_iq_iask_entry |  | fentryid |

---

## 行业要求单据-主表 t_iq_industry_ask

- **表名称：** 行业要求单据-主表
- **表名：** t_iq_industry_ask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisask | 是否符合要求 | bpchar | 1 |  | √ | '0' | 是否符合要求 |
| 3 | fintelligencedetail | 测试明细单据 | int8 | 64 |  | √ | 0 | 智测测评明细 iq_intelligence_detail |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iq_industry_ask |  | fid |
| 2 | idx_iq_industry_ask_detail |  | fintelligencedetail |
