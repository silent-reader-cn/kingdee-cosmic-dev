# 项目核算余额-pca_balance

## 子要素核算明细-子表 t_pca_balanceentry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_balanceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fentryexcurramount | 本期投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期投入（不计入项目成本） |
| 4 | fentrystartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryendoutamount | 期末累计结转 | numeric | 23 | 10 | √ | 0 | 期末累计结转 |
| 7 | fentrytotalamount | 期末累计投入 | numeric | 23 | 10 | √ | 0 | 期末累计投入 |
| 8 | fentryexendamount | 本期结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期结余（不计入项目成本） |
| 9 | fentryexcurroutamount | 本期转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期转出（不计入项目成本） |
| 10 | fentrycurroutamount | 本期转出 | numeric | 23 | 10 | √ | 0 | 本期转出 |
| 11 | fentrycurramount | 本期投入 | numeric | 23 | 10 | √ | 0 | 本期投入 |
| 12 | fentryendamount | 本期结余 | numeric | 23 | 10 | √ | 0 | 本期结余 |
| 13 | fentryexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 14 | fentrystartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 15 | fentrystarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 16 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_balanceentry |  | fentryid |
| 2 | idx_pca_balanceentry_fk |  | fid |
| 3 | idx_pca_balanceentry_convsubelement |  | fconvsubelementid |

---

## 项目核算余额-主表 t_pca_balance

- **表名称：** 项目核算余额-主表
- **表名：** t_pca_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendamount | 本期结余 | numeric | 23 | 10 | √ | 0 | 本期结余 |
| 3 | fdatacreatetype | 数据创建方式 | varchar | 30 |  | √ | ' ' | 数据创建方式,枚举: 0 :结算生成 1 :成本计算生产 |
| 4 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fcurramount | 本期投入 | numeric | 23 | 10 | √ | 0 | 本期投入 |
| 6 | fexendamount | 本期结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期结余（不计入项目成本） |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftotalamount | 期末累计投入 | numeric | 23 | 10 | √ | 0 | 期末累计投入 |
| 9 | fcurroutamount | 本期转出 | numeric | 23 | 10 | √ | 0 | 本期转出 |
| 10 | fexcurroutamount | 本期转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期转出（不计入项目成本） |
| 11 | fstarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 12 | fexcurramount | 本期投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期投入（不计入项目成本） |
| 13 | fendoutamount | 期末累计结转 | numeric | 23 | 10 | √ | 0 | 期末累计结转 |
| 14 | fstartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 15 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 16 | fstartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 17 | fexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 18 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 项目成本核算对象 pca_costobject |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_balance |  | fid |
| 2 | idx_pca_balance_costaccount |  | fcostaccountid,fperiodid |
| 3 | idx_pca_balance_fcostobject |  | fcostobjectid |
