# 经营余额表-xkoac_balance

## 经营余额表-主表 t_xkoac_balance

- **表名称：** 经营余额表-主表
- **表名：** t_xkoac_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgstructureid | 经营组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 3 | fbeginfromcurr | 期初余额（原币） | numeric | 23 | 10 | √ | 0 | 期初余额（原币） |
| 4 | ftocurrdecrease | 本期减少（本位币） | numeric | 23 | 10 | √ | 0 | 本期减少（本位币） |
| 5 | ftocurrincrease | 本期增加（本位币） | numeric | 23 | 10 | √ | 0 | 本期增加（本位币） |
| 6 | fyeardecrease | 本年累计减少（本位币） | numeric | 23 | 10 | √ | 0 | 本年累计减少（本位币） |
| 7 | fassgrp | 经营核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 8 | fyearincrease | 本年累计增加（本位币） | numeric | 23 | 10 | √ | 0 | 本年累计增加（本位币） |
| 9 | ftocurr | 本位币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fbegintocurr | 期初余额（本位币） | numeric | 23 | 10 | √ | 0 | 期初余额（本位币） |
| 11 | ffromcurrdecrease | 本期减少（原币） | numeric | 23 | 10 | √ | 0 | 本期减少（原币） |
| 12 | famoeabcntid | 内部交易方 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 13 | ffromcurrincrease | 本期增加（原币） | numeric | 23 | 10 | √ | 0 | 本期增加（原币） |
| 14 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | fendtocurr | 期末余额（本位币） | numeric | 23 | 10 | √ | 0 | 期末余额（本位币） |
| 16 | fendfromcurr | 期末余额（原币） | numeric | 23 | 10 | √ | 0 | 期末余额（原币） |
| 17 | fendqty | 期末数量 | numeric | 23 | 10 | √ | 0 | 期末数量 |
| 18 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 19 | fbeginqty | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 20 | ffromcurr | 原币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | foperatingbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 22 | fambaunitid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 23 | faccountid | 经营科目 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 24 | fbilltypeid | 交易类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_balance |  | fid |
| 2 | idx_xkoac_balance |  | foperatingbookid,fperiod |
