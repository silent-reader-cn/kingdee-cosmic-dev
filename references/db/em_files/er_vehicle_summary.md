# 用车汇总-er_vehicle_summary

## 用车汇总-主表 t_er_vehicle_summary

- **表名称：** 用车汇总-主表
- **表名：** t_er_vehicle_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsummaryactivepeople | 活跃人数 | varchar | 50 |  | √ | ' ' | 活跃人数 |
| 3 | fotherdatasummary_tag | 其余信息汇总_详情 | text | 0 |  |  | ' ' | 其余信息汇总_详情 |
| 4 | forgid | 组织ID | varchar | 50 |  | √ | ' ' | 组织ID |
| 5 | fsummaryamount | 订单金额 | numeric | 23 | 10 | √ | 0 | 订单金额 |
| 6 | fsummaryend | 汇总结束日期 | timestamp | 0 |  |  | null | 汇总结束日期 |
| 7 | fordernums | 订单数 | varchar | 50 |  | √ | ' ' | 订单数 |
| 8 | fvehicletype | 用车类型 | varchar | 50 |  | √ | ' ' | 用车类型,枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 6 :招待用车 7 :会议用车 |
| 9 | forgtype | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 10 | fsummarystart | 汇总开始日期 | timestamp | 0 |  |  | null | 汇总开始日期 |
| 11 | fsummaryavmileprice | 里程均价 | numeric | 23 | 10 | √ | 0 | 里程均价 |
| 12 | fotherdatasummary | 其余信息汇总 | varchar | 255 |  | √ | ' ' | 其余信息汇总 |
| 13 | ftraveluser | 出行人集合 | varchar | 255 |  | √ | ' ' | 出行人集合 |
| 14 | ftraveluser_tag | 出行人集合_详情 | text | 0 |  |  | ' ' | 出行人集合_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vehicle_summary |  | fsummarystart,fsummaryend,forgid |
| 2 | pk_t_er_vehicle_summary |  | fid |
