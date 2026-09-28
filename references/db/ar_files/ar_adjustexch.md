# 应收期末调汇-ar_adjustexch

## 单据体-子表 t_ap_adjustexchentry

- **表名称：** 单据体-子表
- **表名：** t_ap_adjustexchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotation | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 3 | ffromcurrid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | ftocurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 8 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_adjustexchentry |  | fentryid |
| 2 | idx_ap_adjustexch_pid |  | fid |

---

## 应收期末调汇-主表 t_ap_adjustexch

- **表名称：** 应收期末调汇-主表
- **表名：** t_ap_adjustexch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fperiodid | 调汇期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fadjexchdate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 6 | fadjexchmode | 调汇方式 | varchar | 30 |  | √ | ' ' | 调汇方式,枚举: realtime :按实时汇率 assign :按指定汇率 assigndate :按指定日期汇率 |
| 7 | fbizsystem | 业务系统 | varchar | 30 |  | √ | ' ' | 业务系统,枚举: AR :应收 AP :应付 |
| 8 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | flistperiod | 调汇期间 | varchar | 512 |  | √ | ' ' | 调汇期间 |
| 10 | fisadjexch | 已调汇 | bpchar | 1 |  | √ | '0' | 已调汇 |
| 11 | fisperiod | 是否期初 | bpchar | 1 |  | √ | '0' | 是否期初 |
| 12 | fgainloss | 汇损金额 | numeric | 23 | 10 | √ | 0 | 汇损金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_adjustexch |  | fid |
| 2 | idx_ap_adjustexch_orgid |  | forgid,fperiodid,fbizsystem |
