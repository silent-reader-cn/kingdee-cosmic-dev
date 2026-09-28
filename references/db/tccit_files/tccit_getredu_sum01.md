# 其他项目所得减免底稿-tccit_getredu_sum01

## 其他项目所得减免底稿-主表 t_tccit_getredu_sum01

- **表名称：** 其他项目所得减免底稿-主表
- **表名：** t_tccit_getredu_sum01

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行号 count :合计 |
| 4 | fsheetname | 底稿的页签名称 | varchar | 50 |  | √ | ' ' | 底稿的页签名称 |
| 5 | fparentorgid | 汇总组织id | int8 | 64 |  | √ | 0 | 汇总组织id |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fqjfyfte | 期间费用分摊额 | numeric | 23 | 10 | √ | 0 | 期间费用分摊额 |
| 8 | fyhsxmc | 优惠事项名称 | varchar | 50 |  | √ | ' ' | 优惠事项名称 |
| 9 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fyhfs | 优惠方式 | varchar | 50 |  | √ | ' ' | 优惠方式 |
| 11 | fbillno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 12 | fnstz | 纳税调整额 | numeric | 23 | 10 | √ | 0 | 纳税调整额 |
| 13 | fqzjbsd | 其中：减半所得 | numeric | 23 | 10 | √ | 0 | 其中：减半所得 |
| 14 | freducename | 减免事项的id | int8 | 64 |  | √ | 0 | 减免事项的id |
| 15 | fxmsde | 项目所得额 | numeric | 23 | 10 | √ | 0 | 项目所得额 |
| 16 | fincome | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |
| 17 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 18 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 19 | fdnyhbl | 优惠比例 | varchar | 50 |  | √ | ' ' | 优惠比例 |
| 20 | fprojectname | 减免项目名称 | varchar | 250 |  | √ | ' ' | 减免项目名称 |
| 21 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 22 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 23 | frelaxtax | 相关税费 | numeric | 23 | 10 | √ | 0 | 相关税费 |
| 24 | fjmsde | 减免所得额 | numeric | 23 | 10 | √ | 0 | 减免所得额 |
| 25 | fcost | 项目成本 | numeric | 23 | 10 | √ | 0 | 项目成本 |
| 26 | fqzmssd | 其中：免税所得 | numeric | 23 | 10 | √ | 0 | 其中：免税所得 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_getredu_sum01 |  | fsbbid |
| 2 | pk_tccit_getredu_sum01 |  | fid |
