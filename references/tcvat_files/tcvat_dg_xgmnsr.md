# 小规模底稿单据表-tcvat_dg_xgmnsr

## 小规模底稿单据表-主表 t_tcvat_dg_xgmnsr

- **表名称：** 小规模底稿单据表-主表
- **表名：** t_tcvat_dg_xgmnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 底稿主数据ID | int8 | 64 |  | √ | 0 | 底稿主数据ID |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 : |
| 3 | fbhsxse | 应征增值税不含税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 应征增值税不含税销售额 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 6 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 7 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 8 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 9 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 10 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 11 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 12 | fmsxse | 免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额 |
| 13 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 14 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_dg_xgmnsr |  | fid |
| 2 | pk_tcvat_dg_xgmnsr |  | fentryid |
| 3 | idx_tcvat_dg_xgmnsr_1 |  | fewblxh,fsbbid |
