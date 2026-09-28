# 电商对账数据-pur_thirddata

## 电商对账数据-主表 t_pur_thirddata

- **表名称：** 电商对账数据-主表
- **表名：** t_pur_thirddata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 8 | fsource | 电商平台 | varchar | 10 |  | √ | ' ' | 电商平台,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_thirddata_pkey |  | fid |
| 2 | idx_pur_thirddata_fnumber |  | fnumber |

---

## 单据体-子表 t_pur_thirddataentry

- **表名称：** 单据体-子表
- **表名：** t_pur_thirddataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freturnstatus | 售后状态 | bpchar | 1 |  | √ | ' ' | 售后状态,枚举: A :待确认 B :已确认 C :已打回 E :取消 F :完成 |
| 3 | fparentorder | 电商订单号 | varchar | 80 |  | √ | ' ' | 电商订单号 |
| 4 | forderamount | 订单金额 | numeric | 19 | 6 | √ | 0.000000 | 订单金额 |
| 5 | freturnamount | 退款金额 | numeric | 19 | 6 | √ | 0.000000 | 退款金额 |
| 6 | fplatform | fplatform | varchar | 10 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbilldate | 订单时间 | timestamp | 0 |  |  | null | 订单时间 |
| 9 | funpayamount | 签收金额 | numeric | 19 | 6 | √ | 0.000000 | 签收金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fchildorder | 电商子订单号 | varchar | 80 |  | √ | ' ' | 电商子订单号 |
| 12 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | ' ' | 对账状态,枚举: 0 :未对账 1 :已对账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_thirddataentry_fid |  | fid |
| 2 | t_pur_thirddataentry_pkey |  | fentryid |
