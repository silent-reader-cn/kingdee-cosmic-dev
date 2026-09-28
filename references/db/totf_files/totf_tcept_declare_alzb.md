# 环保税纳税申报表A类主表-totf_tcept_declare_alzb

## 环保税纳税申报表A类主表-主表 t_totf_tcept_declare_alzb

- **表名称：** 环保税纳税申报表A类主表-主表
- **表名：** t_totf_tcept_declare_alzb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsybh | 税源编码 | varchar | 50 |  | √ | ' ' | 税源编码 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 |
| 4 | ftaxitem | 税目 | varchar | 100 |  | √ | ' ' | 税目 |
| 5 | fwrwname | 污染物名称 | varchar | 200 |  | √ | ' ' | 污染物名称 |
| 6 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 7 | fbqjmse | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 8 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 9 | fpfkhzsyname | 排放口名称或噪声源名称 | varchar | 200 |  | √ | ' ' | 排放口名称或噪声源名称 |
| 10 | fbqybse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 11 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 12 | fbqynse | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 13 | fjsyjzhxs | 计税依据或超标噪声综合系数 | numeric | 23 | 10 | √ | 0 | 计税依据或超标噪声综合系数 |
| 14 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_tcept_declare_alzb |  | fid |
| 2 | idx_totf_tcept_declare_alzb |  | fsbbid,fewblxh |
