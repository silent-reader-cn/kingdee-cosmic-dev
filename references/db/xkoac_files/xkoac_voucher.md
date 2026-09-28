# 经营流水账-xkoac_voucher

## 单据体-子表 t_xkoac_voucherentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_voucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchange | 增减 | varchar | 10 |  | √ | '1' | 增减,枚举: 1 :增加 2 :减少 |
| 3 | fassgrp | 经营核算维度 | int8 | 64 |  | √ | 0 | null 008 |
| 4 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 8 | fqtyfield | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | fexplanation | 摘要 | varchar | 500 |  | √ | ' ' | 摘要 |
| 10 | famoeabcntid | 内部交易方/共享方/分摊方 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 11 | fsrcbillentryid | 来源单据分录行id | varchar | 36 |  | √ | ' ' | 来源单据分录行id |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | faccounttype | 经营要素 | varchar | 10 |  | √ | '-1' | 经营要素,枚举: -1 :收入 1 :费用 2 :资产 3 :负债 |
| 14 | famountfor | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fcurrencyid | 原币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | faccountid | 经营科目 | int8 | 64 |  | √ | 0 | 经营科目 xkoac_account |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_voucherentry |  | fid |
| 2 | pk_t_xkoac_voucherentry |  | fentryid |

---

## 单据体-多语言表 t_xkoac_voucherentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkoac_voucherentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexplanation | 摘要 | varchar | 500 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_voucherentry_l |  | fentryid,flocaleid |
| 2 | pk_t_xkoac_voucherentry_l |  | fpkid |

---

## 经营流水账-主表 t_xkoac_voucher

- **表名称：** 经营流水账-主表
- **表名：** t_xkoac_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 流水账类型 | varchar | 10 |  | √ | '2' | 流水账类型,枚举: 2 :收入 1 :费用 3 :转账 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 8 | fsourcesysid | 来源系统 | varchar | 36 |  | √ | ' ' | 业务应用列表 bos_devp_bizapplist |
| 9 | forgstructureid | 经营组织架构版本 | int8 | 64 |  | √ | 0 | 经营组织架构版本 xkoac_orgsystem |
| 10 | famoeabid | 经营单元 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fsrcbillid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 15 | fliabilitiesamount | 负债合计金额 | numeric | 23 | 10 | √ | 0 | 负债合计金额 |
| 16 | fsrcno | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fsourcesys | fsourcesys | int8 | 64 |  | √ | 0 |  |
| 19 | fassetsamount | 资产合计金额 | numeric | 23 | 10 | √ | 0 | 资产合计金额 |
| 20 | faccountbookid | 经营账簿 | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |
| 21 | fsourcebill | fsourcebill | int8 | 64 |  | √ | 0 |  |
| 22 | fexpenseamount | 费用合计金额 | numeric | 23 | 10 | √ | 0 | 费用合计金额 |
| 23 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 25 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 26 | fvchimptplan | 来源方案 | int8 | 64 |  | √ | 0 | 经营流水账来源方案 xkoac_voucherimptplan |
| 27 | fvchplanseq | 来源方案行编码 | int4 | 32 |  | √ | 0 | 来源方案行编码 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fbilltypeid | 交易类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fincomeamount | 收入合计金额 | numeric | 23 | 10 | √ | 0 | 收入合计金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_voucher |  | fid |
| 2 | idx_xkoac_voucher_bn |  | fbillno |
