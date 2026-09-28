# 返利结算单F7-occpic_rebatestatementf7

## 返利结算单F7-主表 t_occpic_rebatestatement

- **表名称：** 返利结算单F7-主表
- **表名：** t_occpic_rebatestatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelsecondgroupid | fchannelsecondgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | ftotalrebamount | ftotalrebamount | numeric | 23 | 10 | √ | 0 |  |
| 4 | fsalesattrsid | fsalesattrsid | int8 | 64 |  | √ | 0 |  |
| 5 | fchncustomerid | fchncustomerid | int8 | 64 |  | √ | 0 |  |
| 6 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 7 | ftotalstateqty | ftotalstateqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fchannelfirstgroupid | fchannelfirstgroupid | int8 | 64 |  | √ | 0 |  |
| 9 | fdestcaculatetype | fdestcaculatetype | varchar | 20 |  | √ | ' ' |  |
| 10 | fsalechannelid | fsalechannelid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fsalesyearid | fsalesyearid | int8 | 64 |  | √ | 0 |  |
| 13 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fstatementdate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 16 | fstatementorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbusinessorgid | fbusinessorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fchannelid | 渠道ID | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 19 | fstmcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fofficeid | fofficeid | int8 | 64 |  | √ | 0 |  |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fidentify | fidentify | varchar | 80 |  | √ | ' ' |  |
| 23 | fisbatchsettle | fisbatchsettle | bpchar | 1 |  | √ | '0' |  |
| 24 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 25 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 27 | fincentivetype | fincentivetype | bpchar | 1 |  | √ | 'A' |  |
| 28 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 29 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 30 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fpaytype | 支付方式 | bpchar | 1 |  | √ | 'A' | 支付方式,枚举: A :开红票 B :下单抵扣 |
| 33 | fcontractsubjectid | fcontractsubjectid | int8 | 64 |  | √ | 0 |  |
| 34 | fincentivesubtype | fincentivesubtype | bpchar | 1 |  | √ | 'A' |  |
| 35 | fsalesmonthid | fsalesmonthid | int8 | 64 |  | √ | 0 |  |
| 36 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 37 | fbudgetcycle | fbudgetcycle | bpchar | 1 |  | √ | 'B' |  |
| 38 | frebatetype | frebatetype | bpchar | 1 |  | √ | 'A' |  |
| 39 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 40 | frebatepolicyid | frebatepolicyid | int8 | 64 |  | √ | 0 |  |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | faccountid | 激励账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 43 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 44 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatestatement_num |  | fbillno |
| 2 | pk_occpic_rebatestatement |  | fid |
