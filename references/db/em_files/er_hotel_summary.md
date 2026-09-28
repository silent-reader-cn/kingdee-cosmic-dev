# 酒店汇总-er_hotel_summary

## 酒店汇总-主表 t_er_hotel_summary

- **表名称：** 酒店汇总-主表
- **表名：** t_er_hotel_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fotherdatasummary_tag | 其余信息汇总_详情 | text | 0 |  |  | ' ' | 其余信息汇总_详情 |
| 3 | forgid | 组织ID | varchar | 50 |  | √ | ' ' | 组织ID |
| 4 | fotherdatasummary | 其余信息汇总 | varchar | 255 |  | √ | ' ' | 其余信息汇总 |
| 5 | fsummaryamount | 订单金额 | numeric | 23 | 10 | √ | 0 | 订单金额 |
| 6 | ftraveluser | 出行人集合 | varchar | 255 |  | √ | ' ' | 出行人集合 |
| 7 | fsummaryend | 汇总结束日期 | timestamp | 0 |  |  | null | 汇总结束日期 |
| 8 | ftraveluser_tag | 出行人集合_详情 | text | 0 |  |  | ' ' | 出行人集合_详情 |
| 9 | forgtype | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 10 | fsummarystart | 汇总开始日期 | timestamp | 0 |  |  | null | 汇总开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_hotel_summary |  | fsummarystart,fsummaryend,forgid |
| 2 | pk_t_er_hotel_summary |  | fid |
