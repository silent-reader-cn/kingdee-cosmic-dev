# 数据源字段配置-rdem_datasource_entry

## 数据源字段配置-主表 t_rdem_datasource_entry

- **表名称：** 数据源字段配置-主表
- **表名：** t_rdem_datasource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccessmap | faccessmap | int8 | 64 |  | √ | 0 |  |
| 2 | fid | 表ID | int8 | 64 |  | √ | 0 | 表ID |
| 3 | fwherestate | 过滤字段 | bpchar | 1 |  | √ | '0' | 过滤字段 |
| 4 | finspectionshowfield | 抽检展示字段 | bpchar | 1 |  | √ | '0' | 抽检展示字段 |
| 5 | fdescrice | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 6 | felementwhere | 抽检条件字段 | bpchar | 1 |  | √ | '0' | 抽检条件字段 |
| 7 | fsubname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 8 | faccesslogic | faccesslogic | varchar | 100 |  | √ | ' ' |  |
| 9 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 10 | fdrilldown | 下钻展示字段 | bpchar | 1 |  | √ | '0' | 下钻展示字段 |
| 11 | forgstate | 组织字段 | bpchar | 1 |  | √ | '0' | 组织字段 |
| 12 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 13 | fisamount | 金额字段 | bpchar | 1 |  | √ | '0' | 金额字段 |
| 14 | fyearstate | 年份字段 | bpchar | 1 |  | √ | '0' | 年份字段 |
| 15 | fmonthstate | 月份字段 | bpchar | 1 |  | √ | '0' | 月份字段 |
| 16 | fstate | 查询状态 | bpchar | 1 |  | √ | '1' | 查询状态 |
| 17 | fdatastate | 时间字段 | bpchar | 1 |  | √ | '0' | 时间字段 |
| 18 | fbizsubname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_datasource_entry |  | fentryid |
| 2 | idx_rdem_datasource_entry_fk |  | fid |
