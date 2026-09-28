# 项目核算期初余额-pca_balance_start

## 子要素核算明细-子表 t_pca_balancestart_entry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_balancestart_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fexstartrdemamount | 期初研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初研发（不计入项目成本） |
| 4 | fstartrdemamount | 期初研发 | numeric | 23 | 10 | √ | 0 | 期初研发 |
| 5 | fentryexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 6 | fentrystartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 7 | fentrystartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrystarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 10 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_balancestartentry_fk |  | fid |
| 2 | pk_pca_balancestart_entry |  | fentryid |
| 3 | idx_pca_balancestartentry_convsubelement |  | fconvsubelementid |

---

## 项目核算期初余额-主表 t_pca_balancestart

- **表名称：** 项目核算期初余额-主表
- **表名：** t_pca_balancestart

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexstartrdemamount | 期初研发（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初研发（不计入项目成本） |
| 6 | fstarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 7 | fstartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 8 | fstartrdemamount | 期初研发 | numeric | 23 | 10 | √ | 0 | 期初研发 |
| 9 | fcostaccountid | 项目成本主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 10 | fstartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 11 | fexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 12 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_balancestart |  | fid |
| 2 | idx_pca_balancestart_fcostobject |  | fcostobjectid |
| 3 | idx_pca_balancestart_costaccount |  | fcostaccountid,fperiodid |
