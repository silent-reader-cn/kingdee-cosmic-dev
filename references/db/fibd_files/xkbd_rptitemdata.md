# 项目数据-xkbd_rptitemdata

## 报表ID-多选基础资料表 t_xkrpt_iteminrpt

- **表名称：** 报表ID-多选基础资料表
- **表名：** t_xkrpt_iteminrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 报表 xkrpt_report |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_iteminrpt_itemdataid |  | fid |
| 2 | pk_xkrpt_iteminrpt |  | fpkid |
| 3 | idx_xkrpt_iteminrpt_rptid |  | fbasedataid |

---

## 项目数据-主表 t_xkrpt_rptitemdata

- **表名称：** 项目数据-主表
- **表名：** t_xkrpt_rptitemdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | 金额单位 xkbd_amountunit |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fshared | 是否共享 | bpchar | 1 |  | √ | '0' | 是否共享 |
| 7 | frptitemid | 报表项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 8 | felimtypeid | 抵消类型 | int8 | 64 |  | √ | 0 | 抵销类型 xkcr_eliminationtype |
| 9 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 10 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 11 | fitemformulatype | 公式类型 | bpchar | 1 |  | √ | ' ' | 公式类型,枚举: 0 :Item 1 :DItem |
| 12 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 13 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 14 | fformula | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 15 | frptdimension | 项目维度 | text | 0 |  |  | ' ' | 项目维度 |
| 16 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 17 | fdatadirect | 取数方 | int4 | 32 |  | √ | 0 | 取数方 |
| 18 | fcycleid | 周期 | bpchar | 1 |  | √ | ' ' | 周期,枚举: 2 :日报 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 19 | frpttype | 报表类型 | bpchar | 10 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :穿透报表 3 :报表模板 4 :自定义报表 10 :合并报表_个别报表模板 11 :合并报表_合并报表模板 12 :合并报表_汇总报表模板 13 :合并报表_工作底稿模板 14 :合并报表_汇总报表 15 :合并报表_合并报表 16 :合并报表_工作底稿 17 :合并报表_个别报表 20 :调整报表 30 :合并报表_抵消表模板 31 :合并报表_抵消表 60 :预算报表模板 61 :预算报表 62 :预算实际数模板 63 :预算实际数报表 64 :预算汇总报表（周期性） 65 :预算汇总表 66 :预算调整表 |
| 20 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | ftranstypeid | 交易种类 | int8 | 64 |  | √ | 0 | 交易类型 xkcr_transactiontype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rptitemdata |  | fid |
| 2 | idx_xkrpt_rptid_yearperiod |  | fyear,fperiod |
| 3 | idx_xkrpt_rptid_rptitemid |  | frptitemid |
