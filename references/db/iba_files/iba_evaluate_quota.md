# 财务评价模型指标-iba_evaluate_quota

## 财务评价模型指标-主表 t_iba_evaluate_quota

- **表名称：** 财务评价模型指标-主表
- **表名：** t_iba_evaluate_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fquotaweigh | 指标权重 | numeric | 23 | 10 |  | null | 指标权重 |
| 4 | fcoremethod | 评分方式 | varchar | 50 |  | √ | ' ' | 评分方式,枚举: 0 :比例 1 :区间 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fquotatype | 能力项(冗余) | int8 | 64 |  | √ | 0 | [指标分类目录 ipo_quota_type](../ipobase_files/ipo_quota_type.md) |
| 7 | fevaluatetype | 评价模型类型 | int8 | 64 |  | √ | 0 | [财务评价模型类型 iba_evaluate_type](../iba_files/iba_evaluate_type.md) |
| 8 | fquota | 指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_evaluate_quota |  | fid |
| 2 | idx_iba_evaluate_quota_uq |  | fevaluatetype,fquota |

---

## 评分规则-子表 t_iba_evaluate_core_rule

- **表名称：** 评分规则-子表
- **表名：** t_iba_evaluate_core_rule

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
| 1 | idx_iba_evaluate_core_rule_id |  | fid |
| 2 | pk_iba_evaluate_core_rule |  | fentryid |
