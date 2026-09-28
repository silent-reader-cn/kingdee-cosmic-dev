# 归因数据存储-didc_impute_data

## 归因数据存储-主表 t_didc_impute_data

- **表名称：** 归因数据存储-主表
- **表名：** t_didc_impute_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrentdate | 本期日期范围 | varchar | 100 |  | √ | ' ' | 本期日期范围 |
| 3 | fupdate_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fquestionid | 对话id | varchar | 100 |  | √ | ' ' | 对话id |
| 5 | fuser | 用户id | varchar | 50 |  | √ | ' ' | 用户id |
| 6 | ftree_data | 指标树 | varchar | 2000 |  | √ | ' ' | 指标树 |
| 7 | ffilterstr | 过滤条件 | varchar | 512 |  | √ | ' ' | 过滤条件 |
| 8 | funique_value | 唯一值 | varchar | 512 |  | √ | ' ' | 唯一值 |
| 9 | fsessionid | 会话id | varchar | 100 |  | √ | ' ' | 会话id |
| 10 | fcomparedate | 对比期日期范围 | varchar | 100 |  | √ | ' ' | 对比期日期范围 |
| 11 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | ftree_data_tag | 指标树_详情 | text | 0 |  |  | null | 指标树_详情 |
| 13 | ftreeid | 指标树id | varchar | 50 |  | √ | ' ' | 指标树id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_didc_impute_data |  | fsessionid |
| 2 | pk_t_didc_impute_data |  | fid |
