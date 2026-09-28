# 按月计算报表（噪声适用）-totf_tcept_noiserpt

## 按月计算报表（噪声适用）-主表 t_totf_tcept_noiserpt

- **表名称：** 按月计算报表（噪声适用）-主表
- **表名：** t_totf_tcept_noiserpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsybh | 税源编码 | varchar | 50 |  | √ | ' ' | 税源编码 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 |
| 4 | fzssd | 噪声时段 | varchar | 100 |  | √ | ' ' | 噪声时段 |
| 5 | flczscb | 两处以上噪声超标 | varchar | 100 |  | √ | ' ' | 两处以上噪声超标 |
| 6 | fwrwname | 污染物名称 | varchar | 200 |  | √ | ' ' | 污染物名称 |
| 7 | fjcfbs | 监测分贝数 | numeric | 23 | 10 | √ | 0 | 监测分贝数 |
| 8 | fbzxz | 标准限值 | numeric | 23 | 10 | √ | 0 | 标准限值 |
| 9 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 10 | fzsyname | 噪声源名称 | varchar | 200 |  | √ | ' ' | 噪声源名称 |
| 11 | fbjcbxs | 边界超标系数 | numeric | 23 | 10 | √ | 0 | 边界超标系数 |
| 12 | fcbbz | 超标不足15天 | varchar | 100 |  | √ | ' ' | 超标不足15天 |
| 13 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 14 | fmonth | 月份 | varchar | 50 |  | √ | ' ' | 月份 |
| 15 | fcbtsxs | 超标天数系数 | numeric | 23 | 10 | √ | 0 | 超标天数系数 |
| 16 | fcbfbs | 超标分贝数 | numeric | 23 | 10 | √ | 0 | 超标分贝数 |
| 17 | fcbzszhxs | 超标噪声综合系数 | numeric | 23 | 10 | √ | 0 | 超标噪声综合系数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_tcept_noiserpt |  | fsbbid,fewblxh |
| 2 | pk_totf_tcept_noiserpt |  | fid |
