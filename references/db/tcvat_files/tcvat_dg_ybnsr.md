# 底稿单据表-tcvat_dg_ybnsr

## 底稿单据表-主表 t_tcvat_dg_ybnsr

- **表名称：** 底稿单据表-主表
- **表名：** t_tcvat_dg_ybnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 底稿主数据ID | int8 | 64 |  | √ | 0 | 底稿主数据ID |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 : |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 7 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 8 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 9 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 10 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 11 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 12 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 13 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 14 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 16 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 17 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 18 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 19 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已缴税额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_1 |  | fewblxh,fsbbid |
| 3 | idx_tcvat_dg_ybnsr |  | fid |
