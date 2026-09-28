# 银行存款对账-cas_bankvccheck

## 银行存款对账-主表 t_cas_bankvccheck

- **表名称：** 银行存款对账-主表
- **表名：** t_cas_bankvccheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbizdateend | 过滤条件结束日期 | timestamp | 0 |  |  | null | 过滤条件结束日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpageid | pageid | varchar | 100 |  | √ | ' ' | pageid |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fjournalamt | 银行日记账余额 | numeric | 19 | 6 | √ | 0.000000 | 银行日记账余额 |
| 12 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 13 | fadjuststatus | 生成余额调节表 | bpchar | 1 |  | √ | '0' | 生成余额调节表 |
| 14 | fstmtamt | 银行对账单余额 | numeric | 19 | 6 | √ | 0.000000 | 银行对账单余额 |
| 15 | fbankcgsetting | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 16 | fbaladjust | 余额调节表 | varchar | 80 |  | √ | ' ' | 余额调节表 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fverifystatus | 是否存在未勾对数据 | bpchar | 1 |  | √ | '0' | 是否存在未勾对数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_check_pageid |  | fpageid |
| 2 | t_cas_bankvccheck_pkey |  | fid |
