# 现金流量对账表-ict_cfpuchamt

## 现金流量对账表-主表 t_ict_cfpuchamt

- **表名称：** 现金流量对账表-主表
- **表名：** t_ict_cfpuchamt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpyearamount | 本年累计 | numeric | 25 | 10 | √ | 0 | 本年累计 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcfitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 6 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | null 002 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fschemeid | 对账方案 | int8 | 64 |  | √ | 0 | [内部交易对账方案 ict_verifyscheme](../ict_files/ict_verifyscheme.md) |
| 9 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 10 | fpamount | 本期发生 | numeric | 25 | 10 | √ | 0 | 本期发生 |
| 11 | fcamount | 本期发生 | numeric | 25 | 10 | √ | 0 | 本期发生 |
| 12 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 13 | fcyearamount | 本年累计 | numeric | 25 | 10 | √ | 0 | 本年累计 |
| 14 | fcuramount | 今当期发生 | numeric | 23 | 10 | √ | 0 | 今当期发生 |
| 15 | fcurnamount | 仅当期未发生 | numeric | 23 | 10 | √ | 0 | 仅当期未发生 |
| 16 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 17 | fnocheckamount | 本期剩余金额 | numeric | 23 | 10 | √ | 0 | 本期剩余金额 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ict_cfpuchamt |  | fid |
| 2 | idx_ict_cfpuchamt_op |  | forgid,fperiodid |
