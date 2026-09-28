# 环保税减免税明细表-totf_tcept_taxreducedtl

## 环保税减免税明细表-主表 t_totf_tcept_taxreducedtl

- **表名称：** 环保税减免税明细表-主表
- **表名：** t_totf_tcept_taxreducedtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsybh | 税源编码 | varchar | 50 |  | √ | ' ' | 税源编码 |
| 3 | fjmxzdm | 减免性质代码(减免项目名称) | varchar | 100 |  | √ | ' ' | 减免性质代码(减免项目名称) |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 |
| 5 | fstandard | 执行标准 | varchar | 100 |  | √ | ' ' | 执行标准 |
| 6 | fbqjmtax | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 7 | ftaxitem | 税目 | varchar | 100 |  | √ | ' ' | 税目 |
| 8 | funittax | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 9 | fwrwname | 污染物名称 | varchar | 200 |  | √ | ' ' | 污染物名称 |
| 10 | fjcsjyjnd | 监测数据月均浓度(毫克/升，毫克/标立方米) | numeric | 23 | 10 | √ | 0 | 监测数据月均浓度(毫克/升，毫克/标立方米) |
| 11 | fbzndz | 标准浓度值(毫克/升，毫克/标立方米) | numeric | 23 | 10 | √ | 0 | 标准浓度值(毫克/升，毫克/标立方米) |
| 12 | fwrwpfl | 污染物排放量(千克) | numeric | 23 | 10 | √ | 0 | 污染物排放量(千克) |
| 13 | fwrwpflcm | 污染物排放量计算方法 | varchar | 100 |  | √ | ' ' | 污染物排放量计算方法 |
| 14 | fjcsjzgnd | 监测数据最高浓度(毫克/升，毫克/标立方米) | numeric | 23 | 10 | √ | 0 | 监测数据最高浓度(毫克/升，毫克/标立方米) |
| 15 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 16 | fpfkname | 排放口名称 | varchar | 200 |  | √ | ' ' | 排放口名称 |
| 17 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 18 | fmonth | 月份 | varchar | 50 |  | √ | ' ' | 月份 |
| 19 | fwrdls | 污染当量数或综合利用量 | numeric | 23 | 10 | √ | 0 | 污染当量数或综合利用量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_tcept_taxreducedtl |  | fsbbid,fewblxh |
| 2 | pk_totf_tcept_taxreducedtl |  | fid |
