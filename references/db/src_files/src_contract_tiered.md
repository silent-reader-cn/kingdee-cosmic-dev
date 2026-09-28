# 签约单阶梯报价-src_contract_tiered

## 签约单阶梯报价-主表 t_src_contractentrysub

- **表名称：** 签约单阶梯报价-主表
- **表名：** t_src_contractentrysub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftieredprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 2 | ftieredunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | ftieredtaxamount | 阶梯价税合计 | numeric | 23 | 10 | √ | 0 | 阶梯价税合计 |
| 4 | fseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 5 | ftieredprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 6 | ftieredamount | 阶梯未税金额 | numeric | 23 | 10 | √ | 0 | 阶梯未税金额 |
| 7 | ftieredqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 8 | ftieredqty | 阶梯数量 | numeric | 23 | 10 | √ | 0 | 阶梯数量 |
| 9 | ftieredtaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | ftierednote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | ftieredcurrid | 报价币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | ftieredqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 14 | fentryid | 签约分录 | int8 | 64 |  | √ | 0 | [签约分录(采购清单) src_contractentry](../src_files/src_contractentry.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentrysub_eid |  | fentryid |
| 2 | pk_src_contractentrysub |  | fdetailid |
| 3 | idx_src_contractentrysub_pid |  | ftieredprojectid |
