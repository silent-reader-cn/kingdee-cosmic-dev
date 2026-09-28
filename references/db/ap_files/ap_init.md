# 应付初始化-ap_init

## 分录-子表 t_ap_initentry

- **表名称：** 分录-子表
- **表名：** t_ap_initentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinessamount | 初始化暂估金额 | numeric | 19 | 6 | √ | 0.000000 | 初始化暂估金额 |
| 3 | finvoiceamount | 初始化应付金额 | numeric | 19 | 6 | √ | 0.000000 | 初始化应付金额 |
| 4 | ftotalamount | 初始化应付余额 | numeric | 19 | 6 | √ | 0.000000 | 初始化应付余额 |
| 5 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpaidamount | 初始化付款金额 | numeric | 19 | 6 | √ | 0.000000 | 初始化付款金额 |
| 8 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fpayrefundamount | 初始化付款退款金额 | numeric | 23 | 10 | √ | 0 | 初始化付款退款金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_initentry_pkey |  | fentryid |
| 2 | idx_ap_inite_fid |  | fid |

---

## 应付初始化-主表 t_ap_init

- **表名称：** 应付初始化-主表
- **表名：** t_ap_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcurrentdate | 当前日期 | timestamp | 0 |  |  | null | 当前日期 |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fxkisenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fisfinishinit | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 9 | fmigdata | 迁移数据 | varchar | 300 |  | √ | ' ' | 迁移数据 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 12 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fsettlemodel | 核销模型 | varchar | 30 |  | √ | ' ' | 核销模型,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fsettleseq | 当前结算序号 | int8 | 64 |  | √ | 0 | 当前结算序号 |
| 16 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fstartdate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 19 | fstacurrencyid | 业务主币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 21 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_init_pkey |  | fid |
| 2 | idx_ap_init_orgid |  | forgid |
