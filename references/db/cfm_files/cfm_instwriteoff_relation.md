# 付息冲销关系表-cfm_instwriteoff_relation

## 付息冲销关系表-主表 t_cfm_instwriteoff_r

- **表名称：** 付息冲销关系表-主表
- **表名：** t_cfm_instwriteoff_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchnoid | 冲销批次号id | int8 | 64 |  | √ | 0 | 冲销批次号id |
| 3 | fpreinstbillid | 预提单id | int8 | 64 |  | √ | 0 | 预提单id |
| 4 | famount | 冲销利息 | numeric | 19 | 6 | √ | 0 | 冲销利息 |
| 5 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_instwriteoff_r |  | fid |
| 2 | idx_cfm_instwriteoff_r |  | fbatchnoid |
