# 财务健康度评价模型指标-dfa_health_evaluate_quota

## 评分规则-子表 t_dfa_health_evaluaterule

- **表名称：** 评分规则-子表
- **表名：** t_dfa_health_evaluaterule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fminvalue | 最小值 | numeric | 23 | 10 |  | null | 最小值 |
| 3 | fmaxvalue | 最大值 | numeric | 23 | 10 |  | null | 最大值 |
| 4 | fcomparevalue | 比较值 | numeric | 23 | 10 |  | null | 比较值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_evaluaterule |  | fentryid |
| 2 | idx_dfa_health_evaluaterule_fk |  | fid |

---

## 财务健康度评价模型指标-主表 t_dfa_health_evaluate_quo

- **表名称：** 财务健康度评价模型指标-主表
- **表名：** t_dfa_health_evaluate_quo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fquotaweigh | 指标权重 | numeric | 23 | 10 |  | null | 指标权重 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcoremethod | 评分方式 | varchar | 50 |  | √ | ' ' | 评分方式,枚举: 0 :比例 1 :区间 |
| 6 | fcapacity_type | 能力项(冗余) | varchar | 50 |  | √ | ' ' | 能力项(冗余),枚举: 0 :现金流 1 :偿债能力 2 :成长能力 3 :盈利能力 4 :营运能力 5 :资产质量 |
| 7 | fevaluatetype | 评价模型类型 | int8 | 64 |  | √ | 0 | [财务健康度评价模型类型 dfa_health_evaluate_type](../dfa_files/dfa_health_evaluate_type.md) |
| 8 | fquota | 指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_evaluate_quo |  | fid |
| 2 | idx_dfa_health_evaluate_quo |  | fevaluatetype |
