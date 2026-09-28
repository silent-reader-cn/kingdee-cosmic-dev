# 财务风险模型单据-cfa_risk_financial_doc

## 总体风险水平单据体-子表 t_cfa_risk_financial_over

- **表名称：** 总体风险水平单据体-子表
- **表名：** t_cfa_risk_financial_over

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | friskscore | 得分 | int4 | 32 |  | √ | 0 | 得分 |
| 3 | frisklevel | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级,枚举: 1 :低风险 2 :中风险 3 :高风险 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fscorelevel | 得分等级 | varchar | 50 |  | √ | ' ' | 得分等级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 5 :5级 6 :6级 7 :7级 8 :8级 9 :9级 10 :10级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfa_risk_financial_over_fk |  | fid |
| 2 | pk_cfa_risk_financial_over |  | fentryid |

---

## 财务风险模型单据-主表 t_cfa_risk_financial

- **表名称：** 财务风险模型单据-主表
- **表名：** t_cfa_risk_financial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 3 | fname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 4 | frelativetheme | 关联主题 | varchar | 50 |  | √ | ' ' | 关联主题,枚举: 1 :公司财务分析 |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fmodifier | 修改人 | varchar | 50 |  | √ | ' ' | 修改人 |
| 8 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_risk_financial |  | fid |
| 2 | index_cfa_risk_financial |  | fnumber |

---

## 重要程度单据体-子表 t_cfa_risk_financial_impo

- **表名称：** 重要程度单据体-子表
- **表名：** t_cfa_risk_financial_impo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fimportancescore | 得分 | bpchar | 1 |  | √ | '1' | 得分 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fimportancelevel | 重要程度 | varchar | 50 |  | √ | ' ' | 重要程度,枚举: 1 :一般重要 2 :非常重要 3 :极其重要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfa_risk_financial_impo_fk |  | fid |
| 2 | pk_cfa_risk_financial_impo |  | fentryid |

---

## 风险类别单据体-子表 t_cfa_risk_financial_type

- **表名称：** 风险类别单据体-子表
- **表名：** t_cfa_risk_financial_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fhighestscore | 最高得分 | int4 | 32 |  | √ | 0 | 最高得分 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | frisktype | 风险类别 | varchar | 50 |  | √ | ' ' | 风险类别,枚举: 1 :资金风险 2 :偿债风险 3 :增长风险 4 :盈利风险 5 :运营风险 6 :费控风险 7 :其他风险 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_risk_financial_type |  | fentryid |
| 2 | idx_cfa_risk_financial_type_fk |  | fid |
