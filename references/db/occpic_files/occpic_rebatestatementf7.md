# 返利结算单F7-occpic_rebatestatementf7

## 返利结算单F7-主表 t_occpic_rebatestatement

- **表名称：** 返利结算单F7-主表
- **表名：** t_occpic_rebatestatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesattrsid | fsalesattrsid | int8 | 64 |  | √ | 0 |  |
| 3 | fchncustomerid | fchncustomerid | int8 | 64 |  | √ | 0 |  |
| 4 | ftotalstateqty | ftotalstateqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | frebateclassid | frebateclassid | int8 | 64 |  | √ | 0 |  |
| 6 | fdestcaculatetype | fdestcaculatetype | varchar | 20 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 11 | fofficeid | fofficeid | int8 | 64 |  | √ | 0 |  |
| 12 | ftotallocaltax | ftotallocaltax | numeric | 23 | 10 | √ | 0 |  |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fisbatchsettle | fisbatchsettle | bpchar | 1 |  | √ | '0' |  |
| 15 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 16 | fincentivetype | fincentivetype | bpchar | 1 |  | √ | 'A' |  |
| 17 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 20 | fbudgetcycle | fbudgetcycle | bpchar | 1 |  | √ | 'B' |  |
| 21 | frebatetype | frebatetype | bpchar | 1 |  | √ | 'A' |  |
| 22 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 23 | frebatepolicyid | frebatepolicyid | int8 | 64 |  | √ | 0 |  |
| 24 | ftotalapprovedamt | ftotalapprovedamt | numeric | 23 | 10 | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | faccountid | 激励账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 27 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 28 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 29 | fchannelsecondgroupid | fchannelsecondgroupid | int8 | 64 |  | √ | 0 |  |
| 30 | ftotalrebamount | ftotalrebamount | numeric | 23 | 10 | √ | 0 |  |
| 31 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 32 | fchannelfirstgroupid | fchannelfirstgroupid | int8 | 64 |  | √ | 0 |  |
| 33 | fsalechannelid | fsalechannelid | int8 | 64 |  | √ | 0 |  |
| 34 | fsalesyearid | fsalesyearid | int8 | 64 |  | √ | 0 |  |
| 35 | ftotaltax | ftotaltax | numeric | 23 | 10 | √ | 0 |  |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fstatementdate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 38 | fstatementorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fchannelid | 渠道ID | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 41 | fstmcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fidentify | fidentify | varchar | 80 |  | √ | ' ' |  |
| 43 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | ftotallocalrebateamount | ftotallocalrebateamount | numeric | 23 | 10 | √ | 0 |  |
| 46 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 47 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 48 | fpaytype | 支付方式 | bpchar | 1 |  | √ | 'A' | 支付方式,枚举: A :开红票 B :下单抵扣 |
| 49 | fcontractsubjectid | fcontractsubjectid | int8 | 64 |  | √ | 0 |  |
| 50 | fincentivesubtype | fincentivesubtype | bpchar | 1 |  | √ | 'A' |  |
| 51 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 52 | fsalesmonthid | fsalesmonthid | int8 | 64 |  | √ | 0 |  |
| 53 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestatement_num |  | fbillno |
| 2 | pk_occpic_rebatestatement |  | fid |
