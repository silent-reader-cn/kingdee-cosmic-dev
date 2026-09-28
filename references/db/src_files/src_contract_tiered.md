# 签约单阶梯报价-src_contract_tiered

## 签约单阶梯报价-主表 t_src_contractentrysub

- **表名称：** 签约单阶梯报价-主表
- **表名：** t_src_contractentrysub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftieredqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 2 | ftieredtaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 3 | ftieredprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 4 | ftieredunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | ftieredprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 7 | ftierednote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | ftieredcurrid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | ftieredqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 11 | fentryid | 签约分录 | int8 | 64 |  | √ | 0 | 签约分录(采购清单) src_contractentry |

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
