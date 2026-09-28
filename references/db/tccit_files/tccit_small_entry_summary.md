# 小微企业优惠项目列表底稿-tccit_small_entry_summary

## 小微企业优惠项目列表底稿-主表 t_tccit_small_entry_sum

- **表名称：** 小微企业优惠项目列表底稿-主表
- **表名：** t_tccit_small_entry_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: quarter1 :第一季度 quarter2 :第二季度 quarter3 :第三季度 quarter4 :第四季度 yearavg :全年平均值/金额 match :满足情况 |
| 4 | ftaxyearamount | 年度应纳税所得额（元） | numeric | 23 | 10 | √ | 0 | 年度应纳税所得额（元） |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | ftotalamount | 资产总额（万元） | numeric | 23 | 10 | √ | 0 | 资产总额（万元） |
| 8 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 9 | fpeople | 从业人数 | numeric | 23 | 10 | √ | 0 | 从业人数 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_small_entry_sum_orgid |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_small_entry_sum |  | fid |
