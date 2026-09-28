# 选择货币对-bd_exrate_currpair

## 选择货币对-主表 t_bd_exrate_currpair

- **表名称：** 选择货币对-主表
- **表名：** t_bd_exrate_currpair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigcur | 原币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 4 | ftargetcur | 目标币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_ex_pair |  | fnumber |
| 2 | pk_t_bd_exrate_currpair |  | fid |
