# 模拟测试付款记录-aqap_bd_mock_payment

## 模拟测试付款记录-主表 t_aqap_bd_mock_payment

- **表名称：** 模拟测试付款记录-主表
- **表名：** t_aqap_bd_mock_payment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatch_seq | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 3 | fincome_branch_no | 收款开户行号 | varchar | 255 |  | √ | ' ' | 收款开户行号 |
| 4 | facc_no | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 5 | fdetail_seq | 分录明细号 | varchar | 50 |  | √ | ' ' | 分录明细号 |
| 6 | ferror_msg | 报错信息 | varchar | 255 |  | √ | ' ' | 报错信息 |
| 7 | fbiz_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 8 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 9 | finsert_time | 付款入库时间 | timestamp | 0 |  |  | null | 付款入库时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fincome_accno | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 13 | facc_name | 付款户名 | varchar | 255 |  | √ | ' ' | 付款户名 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | froute_rec_tag | 付款路由日志_详情 | text | 0 |  |  | null | 付款路由日志_详情 |
| 17 | fpay_status | 付款状态 | varchar | 50 |  | √ | ' ' | 付款状态,枚举: 7 :打包处理中 9 :提交银行中 10 :银行处理中 11 :交易未确认 12 :交易成功 13 :交易失败 |
| 18 | fabstract_msg | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsub_biz_type | 业务子类型 | varchar | 50 |  | √ | ' ' | 业务子类型 |
| 23 | fcurrency | ISO币种 | varchar | 50 |  | √ | ' ' | ISO币种 |
| 24 | fbank_batch_seq | 银行批次号 | varchar | 50 |  | √ | ' ' | 银行批次号 |
| 25 | fexplanation | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 26 | fmerge | 并笔支付 | varchar | 50 |  | √ | ' ' | 并笔支付 |
| 27 | fbank_currency | 银行币种 | varchar | 50 |  | √ | ' ' | 银行币种 |
| 28 | froute_rec | 付款路由日志 | varchar | 255 |  | √ | ' ' | 付款路由日志 |
| 29 | fbook_date | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 30 | fincome_branch_name | 收款开户行名 | varchar | 255 |  | √ | ' ' | 收款开户行名 |
| 31 | fincome_name | 收款户名 | varchar | 255 |  | √ | ' ' | 收款户名 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 34 | fbank_detail_seq | 银行明细号 | varchar | 50 |  | √ | ' ' | 银行明细号 |
| 35 | fincome_address | 收款账户开户地区 | varchar | 255 |  | √ | ' ' | 收款账户开户地区 |
| 36 | fbd_currency | 支付币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | furgent | 加急支付 | varchar | 50 |  | √ | ' ' | 加急支付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_bd_mock_payment |  | fid |
| 2 | idx_c_mock_payment |  | fnumber |

---

## 模拟测试付款记录-多语言表 t_aqap_bd_mock_payment_l

- **表名称：** 模拟测试付款记录-多语言表
- **表名：** t_aqap_bd_mock_payment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_bd_mock_payment_l |  | fpkid |
| 2 | idx_aqap_bd_mock_payment_l_0 |  | fid,flocaleid |
| 3 | idx_c_mock_payment_l |  | fname |
