# 采购清单阶梯报价-src_purlist_tiered

## 采购清单阶梯报价-主表 t_src_purlistentrysub

- **表名称：** 采购清单阶梯报价-主表
- **表名：** t_src_purlistentrysub

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
| 11 | fentryid | 采购清单分录 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlistentrysub |  | fdetailid |
| 2 | idx_src_purlistentrysub_eid |  | fentryid |
