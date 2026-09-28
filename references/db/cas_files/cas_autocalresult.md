# 自动匹配结果存储-cas_autocalresult

## 自动匹配结果存储-多语言表 t_cas_autocalresult_l

- **表名称：** 自动匹配结果存储-多语言表
- **表名：** t_cas_autocalresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_autocal_l |  | flocaleid,fid |
| 2 | t_cas_autocalresult_l_pkey |  | fpkid |

---

## 单据体-子表 t_cas_autocalresult_e

- **表名称：** 单据体-子表
- **表名：** t_cas_autocalresult_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctname | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: |
| 4 | forgid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsettlenumber | 结算号 | varchar | 50 |  | √ | ' ' | 结算号 |
| 7 | famount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 8 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 9 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 10 | fnum | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fpaytypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 12 | facct | 对方账号 | varchar | 50 |  | √ | ' ' | 对方账号 |
| 13 | fsettlestyleid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 14 | frectypeid | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 15 | fbillentryid | 对应单据分录id | varchar | 50 |  | √ | ' ' | 对应单据分录id |
| 16 | frecord | 记录 | varchar | 30 |  | √ | ' ' | 记录,枚举: 0 :交易明细 1 :收款单 2 :付款单 3 :代发单 4 :上划单 5 :下拨单 6 :付款交易处理单 7 :代发退款单 |
| 17 | fbizdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 18 | fbillid | 对应单据id | varchar | 30 |  | √ | ' ' | 对应单据id |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fbankacctid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_autocalresult_e |  | fid |
| 2 | t_cas_autocalresult_e_pkey |  | fentryid |

---

## 自动匹配结果存储-主表 t_cas_autocalresult

- **表名称：** 自动匹配结果存储-主表
- **表名：** t_cas_autocalresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fruleentryid | 规则分录id | int8 | 64 |  | √ | 0 | 规则分录id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsmartmatchid | 智能匹配 | int8 | 64 |  | √ | 0 | [自动匹配业务单据规则 cas_smartmatch](../cas_files/cas_smartmatch.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fmatchstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :可匹配 1 :已匹配 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | frulename | 适用规则 | varchar | 100 |  | √ | ' ' | 适用规则 |
| 15 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_autocalresult |  | fnumber |
| 2 | t_cas_autocalresult_pkey |  | fid |
