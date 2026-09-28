# 数据源字段配置-bdtaxr_datasource_entry

## 数据源字段配置-主表 t_bdtaxr_datasource_entry

- **表名称：** 数据源字段配置-主表
- **表名：** t_bdtaxr_datasource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 表ID | int8 | 64 |  | √ | 0 | 表ID |
| 2 | fwherestate | 过滤字段 | bpchar | 1 |  | √ | ' ' | 过滤字段 |
| 3 | finspectionshowfield | 抽检展示字段 | bpchar | 1 |  | √ | ' ' | 抽检展示字段 |
| 4 | fdescrice | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 5 | fsubname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 6 | felementwhere | 抽检条件字段 | bpchar | 1 |  | √ | ' ' | 抽检条件字段 |
| 7 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 8 | forgstate | 组织字段 | bpchar | 1 |  | √ | ' ' | 组织字段 |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | fisamount | 金额字段 | bpchar | 1 |  | √ | ' ' | 金额字段 |
| 11 | fyearstate | 年份字段 | bpchar | 1 |  | √ | ' ' | 年份字段 |
| 12 | fmonthstate | 月份字段 | bpchar | 1 |  | √ | ' ' | 月份字段 |
| 13 | fstate | 查询状态 | bpchar | 1 |  | √ | ' ' | 查询状态 |
| 14 | fdatastate | 时间字段 | bpchar | 1 |  | √ | ' ' | 时间字段 |
| 15 | fbizsubname | 业务名称 | varchar | 127 |  | √ | ' ' | 业务名称 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_datasource_entry |  | fentryid |
| 2 | idx_bdtaxr_datasource_entry |  | fid |
