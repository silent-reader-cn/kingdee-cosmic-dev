# 一般纳税人减税项目-tcvat_ybnsr_jsxm

## 一般纳税人减税项目-主表 t_tcvat_ybnsr_jsxm

- **表名称：** 一般纳税人减税项目-主表
- **表名：** t_tcvat_ybnsr_jsxm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 |
| 3 | fswsxdmextval | 减免税扩展字段 | varchar | 100 |  | √ | ' ' | 减免税扩展字段 |
| 4 | fswsxdm | 减税性质代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 5 | fqcye | 期初余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额 |
| 6 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 7 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 8 | fbqydjse | 本期应抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应抵减税额 |
| 9 | fbqfse | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |
| 10 | fqmye | 期末余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额 |
| 11 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 12 | fbqsjdjse | 本期实际抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期实际抵减税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_ybnsr_jsxm_pkey |  | fid |
| 2 | idx_t_tcvat_ybnsr_jsxm_ssid |  | fsbbid |
| 3 | idx_t_tcvat_ybnsr_jsxm_ssid2 |  | fewblxh,fsbbid |
