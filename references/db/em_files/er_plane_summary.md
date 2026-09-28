# 机票汇总-er_plane_summary

## 机票汇总-主表 t_er_plane_summary

- **表名称：** 机票汇总-主表
- **表名：** t_er_plane_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffullticketsummary_tag | 全价机票统计_详情 | text | 0 |  |  | ' ' | 全价机票统计_详情 |
| 3 | fotherdatasummary_tag | 其余信息汇总_详情 | text | 0 |  |  | ' ' | 其余信息汇总_详情 |
| 4 | forgid | 组织ID | varchar | 50 |  | √ | ' ' | 组织ID |
| 5 | fsummarydiscount | 平均折扣（%） | numeric | 23 | 10 | √ | 0 | 平均折扣（%） |
| 6 | fotherdatasummary | 其余信息汇总 | varchar | 255 |  | √ | ' ' | 其余信息汇总 |
| 7 | fsummaryamount | 汇总金额 | numeric | 23 | 10 | √ | 0 | 汇总金额 |
| 8 | fsummaryend | 汇总结束日期 | timestamp | 0 |  |  | null | 汇总结束日期 |
| 9 | ffullticketsummary | 全价机票统计 | varchar | 255 |  | √ | ' ' | 全价机票统计 |
| 10 | forgtype | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 11 | fsummarystart | 汇总开始日期 | timestamp | 0 |  |  | null | 汇总开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_plane_summary |  | fsummarystart,fsummaryend,forgid |
| 2 | pk_t_er_plane_summary |  | fid |
