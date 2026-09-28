# 个人数据汇总-er_user_summary

## 个人数据汇总-主表 t_er_user_summary

- **表名称：** 个人数据汇总-主表
- **表名：** t_er_user_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsummaryyear | 汇总年份 | varchar | 50 |  | √ | ' ' | 汇总年份 |
| 3 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fsummary_tag | 汇总数据_详情 | text | 0 |  |  | null | 汇总数据_详情 |
| 5 | fuserid | 用户id | varchar | 50 |  | √ | ' ' | 用户id |
| 6 | fsummaryend | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fsummary | 汇总数据 | varchar | 255 |  | √ | ' ' | 汇总数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_user_summary |  | fid |
| 2 | idx_userid_summaryend_index |  | fuserid,fsummaryyear |
