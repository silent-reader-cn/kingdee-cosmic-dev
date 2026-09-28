# 余额表-gl_balance

## 余额表-主表 t_gl_balance

- **表名称：** 余额表-主表
- **表名：** t_gl_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebitfor | 原币借方 | numeric | 24 | 6 | √ | 0.000000 | 原币借方 |
| 3 | fendlocal | 本位币期末余额 | numeric | 24 | 6 | √ | 0.000000 | 本位币期末余额 |
| 4 | fcreditlocal | 本位币贷方 | numeric | 24 | 6 | √ | 0.000000 | 本位币贷方 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreditqty | 贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方数量 |
| 7 | fbeginlocal | 本位币期初余额 | numeric | 24 | 6 | √ | 0.000000 | 本位币期初余额 |
| 8 | fbeginqty | 期初数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量 |
| 9 | fyeardebitqty | 本年累计借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方数量 |
| 10 | fcount | 凭证分录数 | int8 | 64 |  | √ | 0 | 凭证分录数 |
| 11 | fyearcreditfor | 本年累计贷方原币 | numeric | 24 | 6 | √ | 0.000000 | 本年累计贷方原币 |
| 12 | fyeardebitlocal | 本年累计借方本位币 | numeric | 24 | 6 | √ | 0.000000 | 本年累计借方本位币 |
| 13 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 14 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | null 002 |
| 15 | fendfor | 原币期末余额 | numeric | 24 | 6 | √ | 0.000000 | 原币期末余额 |
| 16 | fyearcreditqty | 本年累计贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方数量 |
| 17 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 18 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 19 | fbeginfor | 原币期初余额 | numeric | 24 | 6 | √ | 0.000000 | 原币期初余额 |
| 20 | fdebitlocal | 本位币借方 | numeric | 24 | 6 | √ | 0.000000 | 本位币借方 |
| 21 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 22 | fendqty | 期末数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末数量 |
| 23 | fyeardebitfor | 本年累计借方原币 | numeric | 24 | 6 | √ | 0.000000 | 本年累计借方原币 |
| 24 | fendperiodid | 结束期间 | int8 | 64 |  | √ | '99999999999' | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 25 | fdebitqty | 借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 借方数量 |
| 26 | fyearcreditlocal | 本年累计贷方本位币 | numeric | 24 | 6 | √ | 0.000000 | 本年累计贷方本位币 |
| 27 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fcreditfor | 原币贷方 | numeric | 24 | 6 | √ | 0.000000 | 原币贷方 |
| 30 | faccountid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_balance_aop |  | faccountid,fbookid,fperiodid |
| 2 | idx_gl_balance_assgrp |  | fassgrpid |
| 3 | idx_gl_balance_2 |  | fbookid,fendperiodid,fperiodid,faccountid |
| 4 | idx_gl_balance_1 |  | fbookid,forgid,fbooktypeid,faccounttableid,fendperiodid,faccountid,fassgrpid,fcurrencyid,fmeasureunitid |
| 5 | idx_gl_balance2 |  | forgid,fendperiodid,fperiodid,faccountid |
| 6 | t_gl_balance_pkey |  | fid |
