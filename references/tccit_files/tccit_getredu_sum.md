# 项目所得减免底稿-tccit_getredu_sum

## 项目所得减免底稿-主表 t_tccit_getredu_sum

- **表名称：** 项目所得减免底稿-主表
- **表名：** t_tccit_getredu_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnstz | 纳税调整额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整额 |
| 3 | fqzjbsd | 其中：减半所得 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：减半所得 |
| 4 | freducename | 减免事项的id | int8 | 64 |  | √ | 0 | 减免事项的id |
| 5 | fsheetname | 底稿的页签名称 | varchar | 50 |  | √ | ' ' | 底稿的页签名称 |
| 6 | fparentorgid | 汇总组织id | int8 | 64 |  | √ | 0 | 汇总组织id |
| 7 | fxmsde | 项目所得额 | numeric | 23 | 10 | √ | 0.0000000000 | 项目所得额 |
| 8 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 9 | fincome | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |
| 10 | fqjfyfte | 期间费用分摊额 | numeric | 23 | 10 | √ | 0.0000000000 | 期间费用分摊额 |
| 11 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fdnyhbl | 优惠比例 | varchar | 50 |  | √ | ' ' | 优惠比例 |
| 13 | fprojectname | 减免项目名称 | varchar | 50 |  | √ | ' ' | 减免项目名称 |
| 14 | fyhsxmc | 优惠事项名称 | varchar | 200 |  | √ | ' ' | 优惠事项名称 |
| 15 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 17 | fyhfs | 优惠方式 | varchar | 50 |  | √ | ' ' | 优惠方式 |
| 18 | frelaxtax | 相关税费 | numeric | 23 | 10 | √ | 0.0000000000 | 相关税费 |
| 19 | fjmsde | 减免所得额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免所得额 |
| 20 | fbillno | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |
| 21 | fcost | 项目成本 | numeric | 23 | 10 | √ | 0.0000000000 | 项目成本 |
| 22 | fqzmssd | 其中：免税所得 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：免税所得 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_getredu_sum |  | fid |
| 2 | idx_tccit_getredu_sum |  | forgid |
