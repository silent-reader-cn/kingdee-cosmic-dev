# 项目核算余额-pca_balance

## 项目核算余额-主表 t_pca_balance

- **表名称：** 项目核算余额-主表
- **表名：** t_pca_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatacreatetype | 数据创建方式 | varchar | 30 |  | √ | ' ' | 数据创建方式,枚举: 0 :结算生成 1 :成本计算生产 2 :核算对象删除 3 :人工成本核算单据删除 |
| 3 | ftotalamount | 期末累计投入 | numeric | 23 | 10 | √ | 0 | 期末累计投入 |
| 4 | fexcurroutamount | 本期转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期转出（不计入项目成本） |
| 5 | fstarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 6 | fexrdemamount | 本期研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期研发（不计入项目成本） |
| 7 | fexcurramount | 本期投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期投入（不计入项目成本） |
| 8 | fstartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 9 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 10 | fstartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 11 | fexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 12 | fexendrdemamount | 期末研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期末研发（不计入项目成本） |
| 13 | fendamount | 本期结余 | numeric | 23 | 10 | √ | 0 | 本期结余 |
| 14 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 15 | fcurramount | 本期投入 | numeric | 23 | 10 | √ | 0 | 本期投入 |
| 16 | fexendamount | 本期结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期结余（不计入项目成本） |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fendrdemamount | 期末研发 | numeric | 23 | 10 | √ | 0 | 期末研发 |
| 20 | fexstartrdemamount | 期初研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初研发（不计入项目成本） |
| 21 | fcurroutamount | 本期转出 | numeric | 23 | 10 | √ | 0 | 本期转出 |
| 22 | fendoutamount | 期末累计结转 | numeric | 23 | 10 | √ | 0 | 期末累计结转 |
| 23 | fstartrdemamount | 期初研发 | numeric | 23 | 10 | √ | 0 | 期初研发 |
| 24 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | frdemamount | 本期研发 | numeric | 23 | 10 | √ | 0 | 本期研发 |

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

---

## 子要素核算明细-子表 t_pca_balanceentry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_balanceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fendrdemamount | 期末研发 | numeric | 23 | 10 | √ | 0 | 期末研发 |
| 4 | fexstartrdemamount | 期初研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初研发（不计入项目成本） |
| 5 | fentryexcurramount | 本期投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期投入（不计入项目成本） |
| 6 | fentrystartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryendoutamount | 期末累计结转 | numeric | 23 | 10 | √ | 0 | 期末累计结转 |
| 9 | fentrytotalamount | 期末累计投入 | numeric | 23 | 10 | √ | 0 | 期末累计投入 |
| 10 | fexrdemamount | 本期研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期研发（不计入项目成本） |
| 11 | fentryexendamount | 本期结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期结余（不计入项目成本） |
| 12 | fentryexcurroutamount | 本期转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 本期转出（不计入项目成本） |
| 13 | fentrycurroutamount | 本期转出 | numeric | 23 | 10 | √ | 0 | 本期转出 |
| 14 | fentrycurramount | 本期投入 | numeric | 23 | 10 | √ | 0 | 本期投入 |
| 15 | fentryendamount | 本期结余 | numeric | 23 | 10 | √ | 0 | 本期结余 |
| 16 | fstartrdemamount | 期初研发 | numeric | 23 | 10 | √ | 0 | 期初研发 |
| 17 | fentryexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 18 | fentrystartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 19 | fentrystarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 20 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fexendrdemamount | 期末研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期末研发（不计入项目成本） |
| 23 | frdemamount | 本期研发 | numeric | 23 | 10 | √ | 0 | 本期研发 |

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
