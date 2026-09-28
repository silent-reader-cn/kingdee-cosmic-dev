# 物料单位换算-bd_multimeasureunit

## 物料单位换算-主表 t_bd_multimeasureunit

- **表名称：** 物料单位换算-主表
- **表名：** t_bd_multimeasureunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fdenominator | 源单位换算系数 | int8 | 64 |  |  | null | 源单位换算系数 |
| 3 | fprecision | 单位精度 | int8 | 64 |  | √ | 0 | 单位精度 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fappscen | 应用场景(废弃) | varchar | 10 |  |  | null | 应用场景(废弃),枚举: |
| 6 | fseq | 序号(废弃) | int8 | 64 |  |  | null | 序号(废弃) |
| 7 | fnumerator | 基本单位换算系数 | int8 | 64 |  |  | null | 基本单位换算系数 |
| 8 | fmeasureunitid | 源单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fconverttype | 换算类型 | varchar | 10 |  |  | null | 换算类型,枚举: 1 :固定 2 :浮动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_multimeasureunit_pkey |  | fid |
| 2 | idx_t_bd_multimeasureunit_mate |  | fmaterialid |
