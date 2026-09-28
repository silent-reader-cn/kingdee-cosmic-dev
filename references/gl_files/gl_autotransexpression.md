# 取数公式-gl_autotransexpression

## 取数公式-主表 t_gl_autotransexp

- **表名称：** 取数公式-主表
- **表名：** t_gl_autotransexp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fautorowid | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 4 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fperiodrange | 期间范围 | bpchar | 1 |  | √ | '0' | 期间范围,枚举: 1 :本期 2 :本季 3 :半年 4 :本年 |
| 8 | famounttype | 金额类型 | bpchar | 1 |  | √ | ' ' | 金额类型,枚举: 1 :余额 2 :借方发生额 3 :贷方发生额 |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | faccountid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_autotransexp_pkey |  | fid |
| 2 | idx_gl_autotrans_exp |  | forgid,fautorowid |
