# 资金汇总表快照-cas_capitalsumrpt_bg

## 资金汇总表快照-主表 t_cas_capitalsumrpt_bg

- **表名称：** 资金汇总表快照-主表
- **表名：** t_cas_capitalsumrpt_bg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyeardebitloc | 本年收入-折本位币 | numeric | 23 | 10 | √ | 0 | 本年收入-折本位币 |
| 3 | fdebitamountloc | 本期收入-折本位币 | numeric | 23 | 10 | √ | 0 | 本期收入-折本位币 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdaybalanceloc | 日末余额-折本位币 | numeric | 23 | 10 | √ | 0 | 日末余额-折本位币 |
| 6 | fstandardcurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fyeardebit | 本年收入-原币 | numeric | 23 | 10 | √ | 0 | 本年收入-原币 |
| 8 | fyearcredit | 本年支出-原币 | numeric | 23 | 10 | √ | 0 | 本年支出-原币 |
| 9 | fdaystartloc | 日初余额-折本位币 | numeric | 23 | 10 | √ | 0 | 日初余额-折本位币 |
| 10 | fdaybalance | 日末余额-原币 | numeric | 23 | 10 | √ | 0 | 日末余额-原币 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | null | 创建日期 |
| 12 | facctstyle | 账户类型 | varchar | 30 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 13 | faccountcash | 现金账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 14 | fdaystart | 日初余额-原币 | numeric | 23 | 10 | √ | 0 | 日初余额-原币 |
| 15 | fyearcreditloc | 本年支出-折本位币 | numeric | 23 | 10 | √ | 0 | 本年支出-折本位币 |
| 16 | fmonthbalance | 期末余额-原币 | numeric | 23 | 10 | √ | 0 | 期末余额-原币 |
| 17 | fdaydebitamount | 借方-原币 | numeric | 23 | 10 | √ | 0 | 借方-原币 |
| 18 | fbank_cate_id | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 19 | ffilterenddate | 查询结束日期 | int8 | 64 |  | √ | 0 | 查询结束日期 |
| 20 | faccttype | 账户性质 | varchar | 30 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 21 | fdaycreditamountloc | 贷方-折本位币 | numeric | 23 | 10 | √ | 0 | 贷方-折本位币 |
| 22 | fcreditamountloc | 本期支出-折本位币 | numeric | 23 | 10 | √ | 0 | 本期支出-折本位币 |
| 23 | fdaydebitamountloc | 借方-折本位币 | numeric | 23 | 10 | √ | 0 | 借方-折本位币 |
| 24 | fyearstart | 年初余额-原币 | numeric | 23 | 10 | √ | 0 | 年初余额-原币 |
| 25 | facctname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 26 | ffilterstartdate | 查询开始日期 | int8 | 64 |  | √ | 0 | 查询开始日期 |
| 27 | faccountnumber | 账号 | varchar | 255 |  | √ | ' ' | 账号 |
| 28 | fcapitaltype | 资金类别 | varchar | 50 |  | √ | ' ' | 资金类别 |
| 29 | ffinorgtype | 金融机构类别 | varchar | 30 |  | √ | ' ' | 金融机构类别,枚举: 0 :银行 1 :结算中心 2 :非银行金融机构 3 :财务公司 4 :第三方支付机构 |
| 30 | fcreditamount | 本期支出-原币 | numeric | 23 | 10 | √ | 0 | 本期支出-原币 |
| 31 | fdebitamount | 本期收入-原币 | numeric | 23 | 10 | √ | 0 | 本期收入-原币 |
| 32 | faccountbank | 账户简称 | varchar | 255 |  | √ | ' ' | 账户简称 |
| 33 | fmonthstart | 期初余额-原币 | numeric | 23 | 10 | √ | 0 | 期初余额-原币 |
| 34 | faccountbank_id | 银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 35 | fyearstartloc | 年初余额-折本位币 | numeric | 23 | 10 | √ | 0 | 年初余额-折本位币 |
| 36 | flevel | 行级别 | varchar | 50 |  | √ | ' ' | 行级别 |
| 37 | facctpurpose | 账户用途 | varchar | 255 |  | √ | ' ' | 账户用途 |
| 38 | fdaycreditamount | 贷方-原币 | numeric | 23 | 10 | √ | 0 | 贷方-原币 |
| 39 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 40 | fmonthbalanceloc | 期末余额-折本位币 | numeric | 23 | 10 | √ | 0 | 期末余额-折本位币 |
| 41 | fsumlevel | 合计排序 | varchar | 50 |  | √ | ' ' | 合计排序 |
| 42 | fbankid | 银行 | varchar | 255 |  | √ | ' ' | 银行 |
| 43 | fmonthstartloc | 期初余额-折本位币 | numeric | 23 | 10 | √ | 0 | 期初余额-折本位币 |
| 44 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 45 | funit | 单位 | int4 | 32 |  | √ | 0 | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_capsum_bg_date |  | ffilterenddate |
| 2 | pk_t_cas_capitalsumrpt_bg |  | fid |
