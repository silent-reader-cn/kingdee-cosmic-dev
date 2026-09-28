# 风险指标详情历史记录表-tctrc_risk_detail_record

## 风险指标详情历史记录表-主表 t_tctrc_risk_detai_record

- **表名称：** 风险指标详情历史记录表-主表
- **表名：** t_tctrc_risk_detai_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsbbid | 关联id | int8 | 64 |  | √ | 0 | 关联id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_risk_detai_record |  | fid |
| 2 | idx_tctrc_rdre_sbbid |  | fsbbid |

---

## 单据体-子表 t_tctrc_risk_d_record_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_d_record_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | friskexpression | 指标表达式 | varchar | 2000 |  | √ | ' ' | 指标表达式 |
| 3 | friskpoint | 风险疑点 | varchar | 2000 |  | √ | ' ' | 风险疑点 |
| 4 | frisklevel | 风险等级 | varchar | 2000 |  | √ | ' ' | 风险等级 |
| 5 | friskresult | 指标结果 | varchar | 2000 |  | √ | ' ' | 指标结果 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnumber | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 8 | fskssqq | 所属期 | varchar | 50 |  | √ | ' ' | 所属期 |
| 9 | friskdes | 指标描述 | varchar | 2000 |  | √ | ' ' | 指标描述 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | friskname | 指标名称 | varchar | 2000 |  | √ | ' ' | 指标名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_d_record_djt_fk |  | fid |
| 2 | pk_tctrc_risk_d_record_djt |  | fentryid |
