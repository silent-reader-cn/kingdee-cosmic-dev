# 软件、集成电路企业优惠有关情况底稿-tccit_soft_ic_yg_summary

## 软件、集成电路企业优惠有关情况底稿-主表 t_tccit_soft_ic_yg_sum

- **表名称：** 软件、集成电路企业优惠有关情况底稿-主表
- **表名：** t_tccit_soft_ic_yg_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 3 | fitemtype | 项目 | varchar | 200 |  | √ | ' ' | 项目 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | fjesl | 金额（数量等） | numeric | 23 | 10 | √ | 0.0000000000 | 金额（数量等） |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fitemname | 项目名称 | varchar | 200 |  | √ | ' ' | 项目名称 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_soft_ic_yg_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_soft_ic_yg_sum |  | fid |
