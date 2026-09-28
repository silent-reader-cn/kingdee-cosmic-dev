# 调汇记录表-gl_adjustratelog

## 调汇记录表-主表 t_gl_adjustratelog

- **表名称：** 调汇记录表-主表
- **表名：** t_gl_adjustratelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | null 002 |
| 4 | fendlocal | 本位币余额 | numeric | 19 | 6 | √ | 0.000000 | 本位币余额 |
| 5 | fendfor | 原币余额 | numeric | 19 | 6 | √ | 0.000000 | 原币余额 |
| 6 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fcurrencyid | 原币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | faccountid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_adjustratelog_pkey |  | fid |
| 2 | idx_gl_adjustratelog |  | fvoucherid |
