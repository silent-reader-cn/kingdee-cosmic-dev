# 辅助属性值-bd_flexauxprop

## 辅助属性值-主表 t_bd_flexauxpropdata

- **表名称：** 辅助属性值-主表
- **表名：** t_bd_flexauxpropdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 维度值 | varchar | 512 |  | √ | ' ' | 维度值 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_flexauxpropdata_pkey |  | fid |
| 2 | idx_bd_flexauxpy_fvalue |  | fvalue |
