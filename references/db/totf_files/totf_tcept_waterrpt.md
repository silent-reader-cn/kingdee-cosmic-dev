# 按月计算报表（水污染物适用）-totf_tcept_waterrpt

## 按月计算报表（水污染物适用）-主表 t_totf_tcept_waterrpt

- **表名称：** 按月计算报表（水污染物适用）-主表
- **表名：** t_totf_tcept_waterrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsybh | 税源编码 | varchar | 50 |  | √ | ' ' | 税源编码 |
| 3 | fwrdlz | 污染当量值(千克或吨) | numeric | 23 | 10 | √ | 0 | 污染当量值(千克或吨) |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 |
| 5 | fwrwname | 污染物名称 | varchar | 200 |  | √ | ' ' | 污染物名称 |
| 6 | fpwxsjspwxs | 排污系数计算.排污系数 | numeric | 23 | 10 | √ | 0 | 排污系数计算.排污系数 |
| 7 | fwrwpfl | 污染物排放量(千克或吨) | numeric | 23 | 10 | √ | 0 | 污染物排放量(千克或吨) |
| 8 | fwrwpflcm | 污染物排放量计算方法 | varchar | 50 |  | √ | ' ' | 污染物排放量计算方法 |
| 9 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 10 | fpfkname | 排放口名称 | varchar | 200 |  | √ | ' ' | 排放口名称 |
| 11 | fjcjsscndz | 监测计算实测浓度值(毫克/升) | numeric | 23 | 10 | √ | 0 | 监测计算实测浓度值(毫克/升) |
| 12 | fpwxsjscwxs | 排污系数计算.产污系数 | numeric | 23 | 10 | √ | 0 | 排污系数计算.产污系数 |
| 13 | fjcjswspfl | 监测计算污水排放量(吨) | numeric | 23 | 10 | √ | 0 | 监测计算污水排放量(吨) |
| 14 | fpwxsjsjsjs | 排污系数计算.计算基数 | numeric | 23 | 10 | √ | 0 | 排污系数计算.计算基数 |
| 15 | ftype | 种类 | varchar | 50 |  | √ | ' ' | 种类 |
| 16 | fpwxsjswrwdw | 排污系数计算.污染物单位 | varchar | 50 |  | √ | ' ' | 排污系数计算.污染物单位 |
| 17 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 18 | fmonth | 月份 | varchar | 50 |  | √ | ' ' | 月份 |
| 19 | fwrdls | 污染当量数 | numeric | 23 | 10 | √ | 0 | 污染当量数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_tcept_waterrpt |  | fid |
| 2 | idx_totf_tcept_waterrpt |  | fsbbid,fewblxh |
