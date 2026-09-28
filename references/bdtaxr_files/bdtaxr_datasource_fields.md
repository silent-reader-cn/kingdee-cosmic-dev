# 自定义数据源字段-bdtaxr_datasource_fields

## 自定义数据源字段-主表 t_bdtaxr_custom_entrydata

- **表名称：** 自定义数据源字段-主表
- **表名：** t_bdtaxr_custom_entrydata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 表ID | int8 | 64 |  | √ | 0 | 表ID |
| 2 | forgfield | 组织字段 | bpchar | 1 |  | √ | ' ' | 组织字段 |
| 3 | famountfield | 金额字段 | bpchar | 1 |  | √ | ' ' | 金额字段 |
| 4 | fsubname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 5 | ffilterfield | 过滤字段 | bpchar | 1 |  | √ | ' ' | 过滤字段 |
| 6 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 7 | fmouthfield | 月份字段 | bpchar | 1 |  | √ | ' ' | 月份字段 |
| 8 | fdatefield | 时间字段 | bpchar | 1 |  | √ | ' ' | 时间字段 |
| 9 | fcjtjfield | 抽检条件字段 | bpchar | 1 |  | √ | ' ' | 抽检条件字段 |
| 10 | fcjzsfield | 抽检展示字段 | bpchar | 1 |  | √ | ' ' | 抽检展示字段 |
| 11 | fentityname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 12 | fyearfield | 年份字段 | bpchar | 1 |  | √ | ' ' | 年份字段 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_custom_entrydata |  | fid |
| 2 | pk_bdtaxr_custom_entrydata |  | fentryid |
