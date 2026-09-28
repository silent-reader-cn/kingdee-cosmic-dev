# 现金盘点-cas_cash_verification

## 账户核对明细-子表 t_cas_cashverifiadjentry

- **表名称：** 账户核对明细-子表
- **表名：** t_cas_cashverifiadjentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustmentitem | 调整项 | varchar | 50 |  | √ | ' ' | 调整项,枚举: 1 :加：已入账未付款 2 :加：未入账已收款 3 :减：已入账未收款 4 :减：未入账已付款 |
| 3 | fcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fadjustmentamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cashverifiadjentry_fid |  | fid |
| 2 | t_cas_cashverifiadjentry_pkey |  | fentryid |

---

## 现金盘点-主表 t_cas_cashverification

- **表名称：** 现金盘点-主表
- **表名：** t_cas_cashverification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frealcashamountrmk | 实点现金备注 | varchar | 255 |  | √ | ' ' | 实点现金备注 |
| 3 | fadjustbalancermk | 调整后现金余额备注 | varchar | 255 |  | √ | ' ' | 调整后现金余额备注 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finventorydeficitrmk | 盘亏备注 | varchar | 255 |  | √ | ' ' | 盘亏备注 |
| 6 | fcashaccountid | 现金账户 | int8 | 64 |  | √ | 0 | 现金账户F7 cas_accountcashtreelistf7 |
| 7 | funbookedreceivedrmk | 加：未入账已收款备注 | varchar | 255 |  | √ | ' ' | 加：未入账已收款备注 |
| 8 | funbookedpaid | 减：未入账已付款 | numeric | 23 | 10 | √ | 0.0000000000 | 减：未入账已付款 |
| 9 | finventorysurplus | 盘盈 | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbookedunreceivedrmk | 减：已入账未收款备注 | varchar | 255 |  | √ | ' ' | 减：已入账未收款备注 |
| 12 | fbookedunpaid | 加：已入账未付款 | numeric | 23 | 10 | √ | 0.0000000000 | 加：已入账未付款 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcheckresult | 现金盘点结果 | varchar | 30 |  | √ | '0' | 现金盘点结果,枚举: 0 :待盘点 1 :盘盈 2 :盘亏 3 :账实相符 |
| 15 | finventorydeficit | 盘亏 | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏 |
| 16 | faccountbalancermk | 盘点日账户余额备注 | varchar | 255 |  | √ | ' ' | 盘点日账户余额备注 |
| 17 | fcheckdate | 盘点日期 | timestamp | 0 |  |  | null | 盘点日期 |
| 18 | funbookedreceived | 加：未入账已收款 | numeric | 23 | 10 | √ | 0.0000000000 | 加：未入账已收款 |
| 19 | fbookedunpaidrmk | 加：已入账未付款备注 | varchar | 255 |  | √ | ' ' | 加：已入账未付款备注 |
| 20 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | frealcashamount | 实点现金 | numeric | 23 | 10 | √ | 0.0000000000 | 实点现金 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fbookedunreceived | 减：已入账未收款 | numeric | 23 | 10 | √ | 0.0000000000 | 减：已入账未收款 |
| 28 | faccountbalance | 盘点日账户余额 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点日账户余额 |
| 29 | funbookedpaidrmk | 减：未入账已付款备注 | varchar | 255 |  | √ | ' ' | 减：未入账已付款备注 |
| 30 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 31 | finventorysurplusrmk | 盘盈备注 | varchar | 255 |  | √ | ' ' | 盘盈备注 |
| 32 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fadjustbalance | 调整后现金余额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整后现金余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cashverifi_forgid |  | forgid |
| 2 | t_cas_cashverification_pkey |  | fid |
| 3 | idx_cas_cashverifi_fbillno |  | fbillno |

---

## 现金盘点及账户核对情况分录-子表 t_cas_cashverificashentry

- **表名称：** 现金盘点及账户核对情况分录-子表
- **表名：** t_cas_cashverificashentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcashqty | 张数 | int8 | 64 |  | √ | 0 | 张数 |
| 3 | fcurrencyfventryid | 面额分录id | int8 | 64 |  | √ | 0 | 面额分录id |
| 4 | fdenomination | 面额 | varchar | 50 |  | √ | ' ' | 面额 |
| 5 | fcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fconversionratio | 换算值 | numeric | 23 | 10 | √ | 0.0000000000 | 换算值 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcashamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cv_fcurrencyfventryid |  | fcurrencyfventryid |
| 2 | t_cas_cashverificashentry_pkey |  | fentryid |
| 3 | idx_cas_cashverficashentry_fid |  | fid |
