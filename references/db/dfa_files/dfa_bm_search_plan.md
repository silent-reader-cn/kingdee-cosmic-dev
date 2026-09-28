# 对标分析查询方案-dfa_bm_search_plan

## 对标分析查询方案-主表 t_dfa_bm_searchplan

- **表名称：** 对标分析查询方案-主表
- **表名：** t_dfa_bm_searchplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecordtitle | 历史记录标题 | varchar | 500 |  | √ | ' ' | 历史记录标题 |
| 3 | frelationid | 关联id | varchar | 50 |  | √ | ' ' | 关联id |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fservicename | 页面标识 | varchar | 255 |  | √ | ' ' | 页面标识 |
| 6 | fvalues_tag | 查询方案_详情 | text | 0 |  |  | null | 查询方案_详情 |
| 7 | fvalues | 查询方案 | varchar | 255 |  | √ | ' ' | 查询方案 |
| 8 | fuserid | 用户id | varchar | 255 |  | √ | ' ' | 用户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_bm_searchplan |  | fid |
| 2 | idx_dfa_bm_searchplan_m0 |  | frelationid |
