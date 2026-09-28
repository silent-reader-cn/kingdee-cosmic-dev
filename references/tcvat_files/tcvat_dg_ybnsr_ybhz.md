# 汇总一般企业底稿单据-tcvat_dg_ybnsr_ybhz

## 汇总一般企业底稿单据-主表 t_tcvat_dg_ybnsr_ybhz

- **表名称：** 汇总一般企业底稿单据-主表
- **表名：** t_tcvat_dg_ybnsr_ybhz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 底稿主数据ID | int8 | 64 |  | √ | 0 | 底稿主数据ID |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 : |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 7 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 8 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 9 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 10 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 11 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 12 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 15 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 16 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已缴税额 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr_ybhz |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_ybhz |  | fsbbid |
| 3 | idx_tcvat_dg_ybnsr_ybhz_1 |  | fewblxh,fsbbid |
