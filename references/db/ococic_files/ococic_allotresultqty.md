# 可销量-ococic_allotresultqty

## 可销量-主表 t_ococic_allotresultqty

- **表名称：** 可销量-主表
- **表名：** t_ococic_allotresultqty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | favbbaseqty | 可用量(基本单位) | numeric | 23 | 10 | √ | 0 | 可用量(基本单位) |
| 3 | freservebaseqty | 占用量(基本单位) | numeric | 23 | 10 | √ | 0 | 占用量(基本单位) |
| 4 | fresultqtykey | 可销量唯一标识 | varchar | 80 |  | √ | ' ' | 可销量唯一标识 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fbaseqty | 数量(基本单位) | numeric | 23 | 10 | √ | 0 | 数量(基本单位) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotresultqty |  | fid |
| 2 | idx_ococic_allotresultqty_key |  | fresultqtykey |
