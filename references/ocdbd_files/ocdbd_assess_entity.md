# 营销周期-ocdbd_assess_entity

## 营销周期-主表 t_ocdbd_assess_entity

- **表名称：** 营销周期-主表
- **表名：** t_ocdbd_assess_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 2 | fmonthname | 月度名称 | varchar | 80 |  | √ | ' ' | 月度名称 |
| 3 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 4 | fentrymonth | 月份 | int4 | 32 |  | √ | 0 | 月份 |
| 5 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fseason | 季度 | int4 | 32 |  | √ | 0 | 季度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_assessentity_fid |  | fid |
| 2 | pk_ocdbd_assess_entity |  | fentryid |
