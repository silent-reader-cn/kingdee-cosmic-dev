# 一般汇总附加税费分配表-tcvat_ybhz_fjsf_fpb

## 一般汇总附加税费分配表-主表 t_tcvat_ybhz_fjsf_fpb

- **表名称：** 一般汇总附加税费分配表-主表
- **表名：** t_tcvat_ybhz_fjsf_fpb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 sum :合计 |
| 3 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 4 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 5 | fzspm | 征收品目 | varchar | 50 |  | √ | ' ' | 征收品目 |
| 6 | flslfjzbl | 六税两费减征比例 | numeric | 23 | 2 | √ | 0 | 六税两费减征比例 |
| 7 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 8 | fbqybtse | 本期应补（退）税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税（费）额 |
| 9 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 10 | fjsyj | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 11 | flslfjze | 六税两费减征额 | numeric | 23 | 2 | √ | 0 | 六税两费减征额 |
| 12 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 13 | flslfjmxzdm | 六税两费减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | fsl | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_fjsf_fpb |  | fid |
| 2 | idx_tcvat_ybhz_fjsf_fpb_0 |  | fsbbid |
| 3 | idx_tcvat_ybhz_fjsf_fpb_1 |  | fewblxh,fsbbid |
