# 资源税申报计算明细表-totf_zys_declaredetail

## 资源税申报计算明细表-主表 t_totf_zys_declaredetail

- **表名称：** 资源税申报计算明细表-主表
- **表名：** t_totf_zys_declaredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 3 | fcpgjl | 准予扣减的外购应税产品购进数量 | numeric | 23 | 10 | √ | 0 | 准予扣减的外购应税产品购进数量 |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | fsalesvolume | 销售量 | numeric | 23 | 10 | √ | 0 | 销售量 |
| 6 | fsalesamount | 销售额 | numeric | 23 | 10 | √ | 0 | 销售额 |
| 7 | fsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目 |
| 8 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 9 | fyzf | 准予扣除的运杂费 | numeric | 23 | 10 | √ | 0 | 准予扣除的运杂费 |
| 10 | ftaxsalesvolume | 计税销售量 | numeric | 23 | 10 | √ | 0 | 计税销售量 |
| 11 | fjldw | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |
| 12 | fcpgjje | 准予扣减的外购应税产品购进金额 | numeric | 23 | 10 | √ | 0 | 准予扣减的外购应税产品购进金额 |
| 13 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 14 | fbqxse | 本期销售额 | numeric | 23 | 10 | √ | 0 | 本期销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_zys_declaredetail |  | fsbbid,fewblxh |
| 2 | pk_totf_zys_declaredetail |  | fid |
