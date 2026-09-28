# 行业洞察历史纪录-dfa_industry_insight_his

## 行业洞察历史纪录-主表 t_dfa_industry_his

- **表名称：** 行业洞察历史纪录-主表
- **表名：** t_dfa_industry_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fquery_json | 查询记录 | varchar | 255 |  | √ | ' ' | 查询记录 |
| 3 | ftype | 场景 | varchar | 255 |  | √ | ' ' | 场景,枚举: industryProfile :行业画像 industryCompare :行业对比 industryAverage :行业均值 |
| 4 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 5 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fquery_json_tag | 查询记录_详情 | text | 0 |  |  | null | 查询记录_详情 |
| 7 | fmodify_date | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fscenario | fscenario | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_dfa_industry_his_user |  | fuser |
| 2 | pk_dfa_industry_his |  | fid |
