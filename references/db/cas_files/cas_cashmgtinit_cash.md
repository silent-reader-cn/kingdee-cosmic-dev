# 现金期初-cas_cashmgtinit_cash

## 现金分录-子表 t_cas_cashmgcash

- **表名称：** 现金分录-子表
- **表名：** t_cas_cashmgcash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyeardebitloc | 本年累计收款本位币 | numeric | 23 | 10 | √ | 0 | 本年累计收款本位币 |
| 3 | faccountcashid | 现金账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fyeardebit | 本年收款累计 | numeric | 23 | 10 | √ | 0 | 本年收款累计 |
| 6 | fyearcredit | 本年付款累计 | numeric | 23 | 10 | √ | 0 | 本年付款累计 |
| 7 | fbalancececurr | 期初余额本位币 | numeric | 23 | 10 | √ | 0 | 期初余额本位币 |
| 8 | fquotation | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | fbalance | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 10 | fyearcreditloc | 本年累计付款本位币 | numeric | 23 | 10 | √ | 0 | 本年累计付款本位币 |
| 11 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cash_fpid |  | fid |
| 2 | pk_cas_cashmgcash |  | fentryid |

---

## 现金期初-主表 t_cas_cashmgtinit_cash

- **表名称：** 现金期初-主表
- **表名：** t_cas_cashmgtinit_cash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 8 | fdatefield | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fstacurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_cashmgtinit_cash |  | fid |
| 2 | cash_init_org |  | forgid |
