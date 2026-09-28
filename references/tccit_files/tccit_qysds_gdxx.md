# 其他股东情况-tccit_qysds_gdxx

## 其他股东情况-主表 t_tccit_qysds_gdxx

- **表名称：** 其他股东情况-主表
- **表名：** t_tccit_qysds_gdxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 3 | fcggdzwmc | 1.持股股东中文名称 | varchar | 600 |  | √ | ' ' | 1.持股股东中文名称 |
| 4 | fqyfeqsrq | 7.权益份额的起始日期 | timestamp | 0 |  |  | null | 7.权益份额的起始日期 |
| 5 | fjzdhcldww | 4.居住地或成立地外文 | varchar | 600 |  | √ | ' ' | 4.居住地或成立地外文 |
| 6 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 7 | fcggdwwmc | 2.持股股东外文名称 | varchar | 600 |  | √ | ' ' | 2.持股股东外文名称 |
| 8 | fjzdhcldzw | 3.居住地或成立地中文 | varchar | 600 |  | √ | ' ' | 3.居住地或成立地中文 |
| 9 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 10 | fcglx | 5.持股类型 | varchar | 100 |  | √ | ' ' | 5.持股类型 |
| 11 | fcgbl | 6.持股比例 | numeric | 23 | 10 | √ | 0.0000000000 | 6.持股比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_gdxx |  | fsbbid |
| 2 | t_tccit_qysds_gdxx_pkey |  | fid |
| 3 | idx_tccit_qysds_gdxx_1 |  | fewblxh,fsbbid |
