# 买方付息-lc_buyerint

## 买方付息-反写记录表 t_lc_buyerint_wb

- **表名称：** 买方付息-反写记录表
- **表名：** t_lc_buyerint_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_buyerint_wb |  | fentryid |
| 2 | idx_lc_buyerint_wb_fk |  | fid |

---

## 到单信息-子表 t_lc_buyerint_entry

- **表名称：** 到单信息-子表
- **表名：** t_lc_buyerint_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelaydays | 计息顺延天数 | int4 | 32 |  | √ | 0 | 计息顺延天数 |
| 3 | fterm | 融资期限（ymd） | varchar | 50 |  | √ | ' ' | 融资期限（ymd） |
| 4 | fintamount | 付息金额 | numeric | 23 | 10 | √ | 0 | 付息金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | feffectdate | 融资生效日期 | timestamp | 0 |  |  | null | 融资生效日期 |
| 7 | fexchangerate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 8 | fenddate | 融资到期日期 | timestamp | 0 |  |  | null | 融资到期日期 |
| 9 | farrivalamt | 到单金额 | numeric | 23 | 10 | √ | 0 | 到单金额 |
| 10 | frate | 融资利率（%） | numeric | 23 | 10 | √ | 0 | 融资利率（%） |
| 11 | farrivalid | 单据编号 | int8 | 64 |  | √ | 0 | [到单处理F7 lc_arrival_f7](../lc_files/lc_arrival_f7.md) |
| 12 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual_360 :Actual/360 Actual_365 :Actual/365 |
| 13 | fobversionamt | 付息金额（折付息币种） | numeric | 23 | 10 | √ | 0 | 付息金额（折付息币种） |
| 14 | faccountamt | 到账净额 | numeric | 23 | 10 | √ | 0 | 到账净额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffinanceamt | 融资金额 | numeric | 23 | 10 | √ | 0 | 融资金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_buyerint_entry |  | fentryid |
| 2 | idx_lc_buyerint_entry |  | fid |

---

## 买方付息-关联追踪表 t_lc_buyerint_tc

- **表名称：** 买方付息-关联追踪表
- **表名：** t_lc_buyerint_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_buyerint_tc_tid |  | ftid |
| 2 | pk_lc_buyerint_tc |  | fid |
| 3 | idx_lc_buyerint_tc_tbill |  | ftbillid |

---

## 买方付息-主表 t_lc_buyerint

- **表名称：** 买方付息-主表
- **表名：** t_lc_buyerint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farrivalcurrencyid | 到单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffinancingtype | 对方融资类型 | varchar | 30 |  | √ | ' ' | 对方融资类型,枚举: forfaiting :福费廷 agent_forfaiting :代理福费廷 export_discount :出口贴现 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | facceptbanktext | 对方融资受理银行 | varchar | 255 |  | √ | ' ' | 对方融资受理银行 |
| 9 | fregisterdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 10 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | famount | 总付息金额 | numeric | 23 | 10 | √ | 0 | 总付息金额 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | farrivalbankid | 到单银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 15 | facceptbankid | 对方融资受理银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | flockamount | 锁定金额 | numeric | 23 | 10 | √ | 0 | 锁定金额 |
| 18 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 19 | fbenefiter | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 20 | fcurrencyid | 付息币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_buyerint |  | fbillno |
| 2 | pk_t_lc_buyerint |  | fid |

---

## 关联子实体-子表 t_lc_buyerint_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_buyerint_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_buyerint_entry_lk |  | fpkid |
| 2 | idx_lc_buyerint_entry_lk_fk |  | fentryid |
