# 资源税纳税申报表-totf_zys_declare

## 资源税纳税申报表-主表 t_totf_zys_declare

- **表名称：** 资源税纳税申报表-主表
- **表名：** t_totf_zys_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjsxse | 计税销售额 | numeric | 23 | 10 | √ | 0 | 计税销售额 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | fbqjmse | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 6 | fsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目 |
| 7 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 8 | fjldw | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |
| 9 | fsysl | 适用税率 | numeric | 23 | 10 | √ | 0 | 适用税率 |
| 10 | fxgmnsrjze | 本期增值税小规模纳税人减征额 | numeric | 23 | 10 | √ | 0 | 本期增值税小规模纳税人减征额 |
| 11 | fbqybse | 本期应补(退)税额 | numeric | 23 | 10 | √ | 0 | 本期应补(退)税额 |
| 12 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 13 | fjsxsl | 计税销售量 | numeric | 23 | 10 | √ | 0 | 计税销售量 |
| 14 | fbqynse | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 15 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_zys_declare |  | fid |
| 2 | idx_totf_zys_declare |  | fsbbid,fewblxh |
