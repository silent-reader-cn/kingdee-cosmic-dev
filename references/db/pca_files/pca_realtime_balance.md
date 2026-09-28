# 项目即时余额-pca_realtime_balance

## 子要素核算明细-子表 t_pca_rt_balanceentry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_rt_balanceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fentryrtamount | 即时投入 | numeric | 23 | 10 | √ | 0 | 即时投入 |
| 4 | fentrystartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryendoutamount | 即时累计结转 | numeric | 23 | 10 | √ | 0 | 即时累计结转 |
| 7 | fentrytotalamount | 即时累计投入 | numeric | 23 | 10 | √ | 0 | 即时累计投入 |
| 8 | fentryrtoutamount | 即时转出 | numeric | 23 | 10 | √ | 0 | 即时转出 |
| 9 | fentryexrtoutamount | 即时转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时转出（不计入项目成本） |
| 10 | fentryexendamount | 即时结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时结余（不计入项目成本） |
| 11 | fentryendamount | 即时结余 | numeric | 23 | 10 | √ | 0 | 即时结余 |
| 12 | fentryexrtamount | 即时投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时投入（不计入项目成本） |
| 13 | fentryexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 14 | fentrystartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 15 | fentrystarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 16 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_rt_balancee_fk |  | fid |
| 2 | idx_pca_rt_balancee_subele |  | fconvsubelementid |
| 3 | pk_pca_rt_balanceentry |  | fentryid |

---

## 项目即时余额-主表 t_pca_rt_balance

- **表名称：** 项目即时余额-主表
- **表名：** t_pca_rt_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendamount | 即时结余 | numeric | 23 | 10 | √ | 0 | 即时结余 |
| 3 | fdatacreatetype | fdatacreatetype | varchar | 30 |  | √ | ' ' |  |
| 4 | fexendamount | 即时结余（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时结余（不计入项目成本） |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | ftotalamount | 即时累计投入 | numeric | 23 | 10 | √ | 0 | 即时累计投入 |
| 7 | fstarttotalamount | 期初累计投入 | numeric | 23 | 10 | √ | 0 | 期初累计投入 |
| 8 | fstartperiodid | 基准期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 9 | fmodifytime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 10 | fexrtamount | 即时投入（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时投入（不计入项目成本） |
| 11 | fendoutamount | 即时累计结转 | numeric | 23 | 10 | √ | 0 | 即时累计结转 |
| 12 | fstartoutamount | 期初累计结转 | numeric | 23 | 10 | √ | 0 | 期初累计结转 |
| 13 | frtamount | 即时投入 | numeric | 23 | 10 | √ | 0 | 即时投入 |
| 14 | frtoutamount | 即时转出 | numeric | 23 | 10 | √ | 0 | 即时转出 |
| 15 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 16 | fstartamount | 期初 | numeric | 23 | 10 | √ | 0 | 期初 |
| 17 | fexstartamount | 期初（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 期初（不计入项目成本） |
| 18 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 19 | fexrtoutamount | 即时转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时转出（不计入项目成本） |
| 20 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_rt_balance |  | fid |
| 2 | idx_pca_rt_balance_acct |  | fcostaccountid |
| 3 | idx_pca_rt_balance_co |  | fcostobjectid |
