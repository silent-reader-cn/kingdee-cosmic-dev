# 商旅看板费用同比汇总-er_yoy_summary

## 商旅看板费用同比汇总-主表 t_er_yoy_summary

- **表名称：** 商旅看板费用同比汇总-主表
- **表名：** t_er_yoy_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsummaryyear | 汇总年份 | varchar | 50 |  | √ | ' ' | 汇总年份 |
| 3 | fotherdatasummary_tag | 其余信息汇总_详情 | text | 0 |  |  | ' ' | 其余信息汇总_详情 |
| 4 | forgid | 组织ID | varchar | 50 |  | √ | ' ' | 组织ID |
| 5 | fotherdatasummary | 其余信息汇总 | varchar | 255 |  | √ | ' ' | 其余信息汇总 |
| 6 | fsummaryend | 汇总结束日期 | timestamp | 0 |  |  | null | 汇总结束日期 |
| 7 | forgtype | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 8 | fsummarystart | 汇总开始日期 | timestamp | 0 |  |  | null | 汇总开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_yoy_summary |  | fid |
| 2 | idx_er_yoy_summary |  | fsummarystart,fsummaryend,forgid |
| 3 | idx_er_yoy_summaryyear |  | fsummaryyear,forgid |
