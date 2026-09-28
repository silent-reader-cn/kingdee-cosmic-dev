# 财务健康度_行业评价-dfa_health_industry_score

## 财务健康度_行业评价-主表 t_dfa_health_ind_score

- **表名称：** 财务健康度_行业评价-主表
- **表名：** t_dfa_health_ind_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fevaluate_type | 评价模型类型 | int8 | 64 |  | √ | 0 | [财务健康度评价模型类型 dfa_health_evaluate_type](../dfa_files/dfa_health_evaluate_type.md) |
| 4 | findustry_info | 证监会行业 | int8 | 64 |  | √ | 0 | [证监会行业 csrc_industry_info](../ipobase_files/csrc_industry_info.md) |
| 5 | fquarterly_period | 季报报告期 | varchar | 50 |  | √ | ' ' | 季报报告期 |
| 6 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fscore_result | 模型得分结果 | varchar | 2000 |  | √ | ' ' | 模型得分结果 |
| 8 | fmodel_update_time | 缓存时_模型更新时间 | timestamp | 0 |  |  | null | 缓存时_模型更新时间 |
| 9 | fscore_result_tag | 模型得分结果_详情 | text | 0 |  |  | null | 模型得分结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_ind_score |  | fid |
| 2 | idx_dfa_health_ind_score |  | fevaluate_type |
