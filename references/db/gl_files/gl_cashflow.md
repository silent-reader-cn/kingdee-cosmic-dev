# 现金流量-gl_cashflow

## 现金流量-主表 t_gl_cashflow

- **表名称：** 现金流量-主表
- **表名：** t_gl_cashflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fyearamount | 本年累计 | numeric | 24 | 6 | √ | 0.000000 | 本年累计 |
| 5 | fcfitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 6 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | [核算项目组合 gl_assist](../gl_files/gl_assist.md) |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 9 | famount | 本期发生 | numeric | 24 | 6 | √ | 0.000000 | 本期发生 |
| 10 | fcount | 凭证分录数 | int8 | 64 |  | √ | 0 | 凭证分录数 |
| 11 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 12 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_cashflow_pkey |  | fid |
| 2 | idx_gl_cfbip |  | fbookid,fendperiodid,fcfitemid,fassgrpid,fcurrencyid |
| 3 | idx_gl_cashflow_cforg |  | fcfitemid,forgid |
