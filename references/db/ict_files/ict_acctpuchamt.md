# 科目对账表-ict_acctpuchamt

## 科目对账表-主表 t_ict_acctpuchamt

- **表名称：** 科目对账表-主表
- **表名：** t_ict_acctpuchamt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpyearcreditfor | 本年累计贷方原币 | numeric | 25 | 10 | √ | 0 | 本年累计贷方原币 |
| 3 | fcurcdebitlocal | 本位币当期借方 | numeric | 23 | 10 | √ | 0 | 本位币当期借方 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpcreditlocal | 本位币贷方 | numeric | 25 | 10 | √ | 0 | 本位币贷方 |
| 6 | fschemeid | 对账方案 | int8 | 64 |  | √ | 0 | [内部交易对账方案 ict_verifyscheme](../ict_files/ict_verifyscheme.md) |
| 7 | fcurncreditfor | 当期未勾稽贷方 | numeric | 23 | 10 | √ | 0 | 当期未勾稽贷方 |
| 8 | fcurndebitlocal | 本位币当期未勾稽借方 | numeric | 23 | 10 | √ | 0 | 本位币当期未勾稽借方 |
| 9 | fpdebitfor | 原币借方 | numeric | 25 | 10 | √ | 0 | 原币借方 |
| 10 | fpendfor | 原币期末余额 | numeric | 25 | 10 | √ | 0 | 原币期末余额 |
| 11 | fpcreditfor | 原币贷方 | numeric | 25 | 10 | √ | 0 | 原币贷方 |
| 12 | fpyeardebitfor | 本年累计借方原币 | numeric | 25 | 10 | √ | 0 | 本年累计借方原币 |
| 13 | fcurncreditlocal | 本位币当期未勾稽贷方 | numeric | 23 | 10 | √ | 0 | 本位币当期未勾稽贷方 |
| 14 | fcyeardebitfor | 本年累计借方原币 | numeric | 25 | 10 | √ | 0 | 本年累计借方原币 |
| 15 | fcendfor | 原币期末余额 | numeric | 25 | 10 | √ | 0 | 原币期末余额 |
| 16 | fcdebitlocal | 本位币借方 | numeric | 25 | 10 | √ | 0 | 本位币借方 |
| 17 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | null 002 |
| 20 | fcendlocal | 本位币期末余额 | numeric | 25 | 10 | √ | 0 | 本位币期末余额 |
| 21 | fcbeginlocal | 本位币期初余额 | numeric | 25 | 10 | √ | 0 | 本位币期初余额 |
| 22 | fcdebitfor | 原币借方 | numeric | 25 | 10 | √ | 0 | 原币借方 |
| 23 | fccreditfor | 原币贷方 | numeric | 25 | 10 | √ | 0 | 原币贷方 |
| 24 | fcurccreditfor | 当期贷方 | numeric | 23 | 10 | √ | 0 | 当期贷方 |
| 25 | fcurccreditlocal | 本位币当期贷方 | numeric | 23 | 10 | √ | 0 | 本位币当期贷方 |
| 26 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 27 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 28 | fpbeginfor | 原币期初余额 | numeric | 25 | 10 | √ | 0 | 原币期初余额 |
| 29 | fcyearcreditfor | 本年累计贷方原币 | numeric | 25 | 10 | √ | 0 | 本年累计贷方原币 |
| 30 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 31 | fpyeardebitlocal | 本年累计借方本位币 | numeric | 25 | 10 | √ | 0 | 本年累计借方本位币 |
| 32 | fpdebitlocal | 本位币借方 | numeric | 25 | 10 | √ | 0 | 本位币借方 |
| 33 | fcyeardebitlocal | 本年累计借方本位币 | numeric | 25 | 10 | √ | 0 | 本年累计借方本位币 |
| 34 | fcyearcreditlocal | 本年累计贷方本位币 | numeric | 25 | 10 | √ | 0 | 本年累计贷方本位币 |
| 35 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 36 | fpendlocal | 本位币期末余额 | numeric | 25 | 10 | √ | 0 | 本位币期末余额 |
| 37 | fpbeginlocal | 本位币期初余额 | numeric | 25 | 10 | √ | 0 | 本位币期初余额 |
| 38 | fcurcdebitfor | 当期借方 | numeric | 23 | 10 | √ | 0 | 当期借方 |
| 39 | fpyearcreditlocal | 本年累计贷方本位币 | numeric | 25 | 10 | √ | 0 | 本年累计贷方本位币 |
| 40 | fcurndebitfor | 当期未勾稽借方 | numeric | 23 | 10 | √ | 0 | 当期未勾稽借方 |
| 41 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fcbeginfor | 原币期初余额 | numeric | 25 | 10 | √ | 0 | 原币期初余额 |
| 43 | fccreditlocal | 本位币贷方 | numeric | 25 | 10 | √ | 0 | 本位币贷方 |
| 44 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ict_acctpuchamt_op |  | forgid,fperiodid |
| 2 | pk_t_ict_acctpuchamt |  | fid |
