# 资源税减免税计算明细表-totf_zys_taxreducedtl

## 资源税减免税计算明细表-主表 t_totf_zys_taxreducedtl

- **表名称：** 资源税减免税计算明细表-主表
- **表名：** t_totf_zys_taxreducedtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjmxzdm | 减免性质代码 | numeric | 23 | 10 | √ | 0 | 减免性质代码 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | fjmxmname | 减免项目名称 | varchar | 200 |  | √ | ' ' | 减免项目名称 |
| 6 | fbqjmse | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 7 | fsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目 |
| 8 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 9 | fjmsxse | 减免税销售额 | numeric | 23 | 10 | √ | 0 | 减免税销售额 |
| 10 | fjldw | 计量单位 | numeric | 23 | 10 | √ | 0 | 计量单位 |
| 11 | fjmsxsl | 减免税销售量 | numeric | 23 | 10 | √ | 0 | 减免税销售量 |
| 12 | fsysl | 适用税率 | numeric | 23 | 10 | √ | 0 | 适用税率 |
| 13 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 14 | fsmbl | 减免比例 | numeric | 23 | 10 | √ | 0 | 减免比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_zys_taxreducedtl |  | fsbbid,fewblxh |
| 2 | pk_totf_zys_taxreducedtl |  | fid |
