# 银企交易状态查询-aqap_query_pay

## 银企交易状态查询-多语言表 t_aqap_query_pay_l

- **表名称：** 银企交易状态查询-多语言表
- **表名：** t_aqap_query_pay_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_query_pay_l_pkey |  | fpkid |
| 2 | idx_aqap_query_pay_l_0 |  | fid,flocaleid |

---

## 银企交易状态查询-主表 t_aqap_query_pay

- **表名称：** 银企交易状态查询-主表
- **表名：** t_aqap_query_pay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fiso_currency_code | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 4 | fbatch_seq | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | facc_no | 付款方账号 | varchar | 50 |  | √ | ' ' | 付款方账号 |
| 7 | famount | 交易金额 | numeric | 23 | 10 |  | null | 交易金额 |
| 8 | ftrans_date | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbank_name | 付款方银行 | varchar | 50 |  | √ | ' ' | 付款方银行 |
| 13 | facc_name | 付款方账户名 | varchar | 50 |  | √ | ' ' | 付款方账户名 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 16 | fbank_acnt | 账号 | int8 | 64 |  |  | null | 银企账户 aqap_bank_acnt |
| 17 | fopp_acc_no | 收款方账号 | varchar | 50 |  | √ | ' ' | 收款方账号 |
| 18 | fopp_acc_name | 收款方账户名 | varchar | 50 |  | √ | ' ' | 收款方账户名 |
| 19 | fsubmit_time | 付款入库时间 | varchar | 50 |  | √ | ' ' | 付款入库时间 |
| 20 | fstatus_msg | 当前付款状态 | varchar | 50 |  | √ | ' ' | 当前付款状态,枚举: 7 :打包处理中 9 :正在提交银行 10 :银行处理中 11 :交易未确认 12 :交易成功 13 :交易失败 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_query_pay_pkey |  | fid |
