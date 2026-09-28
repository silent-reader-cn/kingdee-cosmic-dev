# 凭证现金流量日志-gl_cashflow_log

## 凭证现金流量日志-主表 t_gl_cashflow_log

- **表名称：** 凭证现金流量日志-主表
- **表名：** t_gl_cashflow_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 来源凭证ID | int8 | 64 |  | √ | 0 | 来源凭证ID |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 4 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | 核算项目 |
| 5 | fcfitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcalculated | 是否已算余额 | bpchar | 1 |  | √ | '0' | 是否已算余额 |
| 8 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 核算主体 |
| 9 | famount | 本期发生 | numeric | 24 | 6 | √ | 0.000000 | 本期发生 |
| 10 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 11 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 |
| 12 | foperation | 执行操作 | varchar | 30 |  | √ | ' ' | 执行操作,枚举: submit :提交 enable :生效 disable :作废 delete :删除 |
| 13 | fcount | 凭证分录数 | int8 | 64 |  | √ | 0 | 凭证分录数 |
| 14 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_cashflow_log_caled |  | fcalculated,forgid,fbooktypeid |
| 2 | t_gl_cashflow_log_pkey |  | fid |
| 3 | idx_gl_cashflow_log |  | fbookid,fcalculated |
