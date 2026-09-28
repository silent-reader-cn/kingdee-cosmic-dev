# 计量单位映射-tdm_setting_jldw

## 计量单位映射-主表 t_tdm_setting_jldw

- **表名称：** 计量单位映射-主表
- **表名：** t_tdm_setting_jldw

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjldwname | 通道计量单位名称 | varchar | 50 |  | √ | ' ' | 通道计量单位名称 |
| 3 | fsuppliernumber | 通道编码 | varchar | 50 |  | √ | ' ' | 通道编码 |
| 4 | funitfield | 系统计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fjldwnumber | 通道计量单位编码 | varchar | 50 |  | √ | ' ' | 通道计量单位编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_setting_jldw |  | fid |
| 2 | idx_tdm_setjldw_unit |  | funitfield |
