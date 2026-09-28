# 项目核算期初余额-pca_balance_start

## 子要素核算明细-子表 t_pca_balancestart_entry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_balancestart_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fentryexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 4 | fentrystartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 5 | fentrystartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrystarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 8 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 2 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 3 | fstartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcostaccountid | 项目成本主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 6 | fstartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 7 | fexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 8 | fstarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 9 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 项目成本核算对象 pca_costobject |
| 10 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
