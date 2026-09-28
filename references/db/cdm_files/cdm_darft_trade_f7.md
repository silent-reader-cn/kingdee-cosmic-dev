# 票据业务处理单F7-cdm_darft_trade_f7

## 票据业务处理单F7-主表 t_cdm_drafttradebill

- **表名称：** 票据业务处理单F7-主表
- **表名：** t_cdm_drafttradebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcemigratedata | fsourcemigratedata | varchar | 80 |  | √ | ' ' |  |
| 3 | fdiscount_days | fdiscount_days | int4 | 32 |  |  | null |  |
| 4 | frecbodyid | frecbodyid | int8 | 64 |  | √ | 0 |  |
| 5 | fpledgeebase | fpledgeebase | int8 | 64 |  | √ | 0 |  |
| 6 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 7 | fisrejectrefundgen | fisrejectrefundgen | bpchar | 1 |  | √ | '0' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | frecbodyname | frecbodyname | varchar | 80 |  | √ | ' ' |  |
| 10 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fcredittype | fcredittype | int8 | 64 |  | √ | 0 |  |
| 12 | frate | frate | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fallbillsamount | fallbillsamount | numeric | 19 | 6 | √ | 0 |  |
| 14 | fdraftbilltranstatus | 票据交易状态 | varchar | 50 |  |  | null | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 porsuccess :部分成功 failing :交易失败 |
| 15 | fisfaildiscount | fisfaildiscount | bpchar | 1 |  | √ | '0' |  |
| 16 | fpledgeeaccount | fpledgeeaccount | varchar | 100 |  | √ | ' ' |  |
| 17 | fdraftcount | fdraftcount | varchar | 30 |  | √ | '0' |  |
| 18 | fdepositaccountid | fdepositaccountid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | bankcode | bankcode | varchar | 100 |  | √ | ' ' |  |
| 21 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 22 | fpledgeeaccounttext | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 23 | fsettleway | fsettleway | varchar | 50 |  | √ | ' ' |  |
| 24 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 26 | fbillstatus | fbillstatus | varchar | 80 |  | √ | ' ' |  |
| 27 | fpoundage | fpoundage | numeric | 19 | 6 |  | null |  |
| 28 | fdeposit | fdeposit | bpchar | 1 |  | √ | '0' |  |
| 29 | fpledgeeopenbanknumber | 质权人开户行行号 | varchar | 100 |  | √ | ' ' | 质权人开户行行号 |
| 30 | fpayeetype | fpayeetype | varchar | 80 |  | √ | ' ' |  |
| 31 | fvouchernum | fvouchernum | varchar | 150 |  |  | ' ' |  |
| 32 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 33 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 34 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 35 | fdeductamount | fdeductamount | numeric | 19 | 6 | √ | 0 |  |
| 36 | froughly_interest | froughly_interest | numeric | 19 | 6 | √ | 0 |  |
| 37 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 38 | fdiscamt | fdiscamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 39 | fbankid | fbankid | int8 | 64 |  | √ | 0 |  |
| 40 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 41 | fiseditdiscountentry | fiseditdiscountentry | bpchar | 1 |  | √ | '0' |  |
| 42 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 43 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fbankaccountid | fbankaccountid | int8 | 64 |  | √ | 0 |  |
| 45 | frefunddesc | frefunddesc | varchar | 50 |  | √ | ' ' |  |
| 46 | fpledgeetypebase | fpledgeetypebase | varchar | 50 |  | √ | ' ' |  |
| 47 | fisdrawfail | fisdrawfail | bpchar | 1 |  | √ | '0' |  |
| 48 | ftradetype | 业务处理 | varchar | 30 |  | √ | ' ' | 业务处理,枚举: pledge :票据质押 |
| 49 | fisrejectrefund | fisrejectrefund | bpchar | 1 |  | √ | '0' |  |
| 50 | famount | 合计金额 | numeric | 19 | 6 | √ | 0.000000 | 合计金额 |
| 51 | fsource | fsource | varchar | 30 |  | √ | ' ' |  |
| 52 | fbankacct | fbankacct | varchar | 80 |  | √ | ' ' |  |
| 53 | fcollection | fcollection | numeric | 19 | 6 |  | null |  |
| 54 | fisreverserec | fisreverserec | bpchar | 1 |  | √ | '0' |  |
| 55 | fstatus | fstatus | varchar | 80 |  | √ | ' ' |  |
| 56 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 57 | fpledgeetext | 质权人 | varchar | 100 |  | √ | ' ' | 质权人 |
| 58 | fisonlinecalc | fisonlinecalc | bpchar | 1 |  | √ | '0' |  |
| 59 | fdiscount_interest | fdiscount_interest | numeric | 19 | 6 |  | null |  |
| 60 | fpayeetypetext | fpayeetypetext | varchar | 80 |  | √ | ' ' |  |
| 61 | felectag | felectag | bpchar | 1 |  |  | null |  |
| 62 | fisrepay | fisrepay | bpchar | 1 |  |  | '0' |  |
| 63 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 64 | fdepositdeduct | fdepositdeduct | bpchar | 1 |  | √ | '0' |  |
| 65 | fbizfinishdate | fbizfinishdate | timestamp | 0 |  |  | null |  |
| 66 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 67 | fdeducttype | fdeducttype | varchar | 5 |  | √ | ' ' |  |
| 68 | fisalldiscount | fisalldiscount | bpchar | 1 |  | √ | '0' |  |
| 69 | fbusicontractno | fbusicontractno | varchar | 50 |  | √ | ' ' |  |
| 70 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他 bd_finorginfo :金融机构 |
| 71 | finterestday | finterestday | varchar | 30 |  | √ | ' ' |  |
| 72 | fcontractno | 质押合同号 | varchar | 80 |  | √ | ' ' | 质押合同号 |
| 73 | fisrepaygen | fisrepaygen | bpchar | 1 |  | √ | '0' |  |
| 74 | fbeendorsorid | fbeendorsorid | int8 | 64 |  | √ | 0 |  |
| 75 | fcleartype | fcleartype | varchar | 50 |  | √ | ' ' |  |
| 76 | fcreditlimited | fcreditlimited | int8 | 64 |  | √ | 0 |  |
| 77 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 78 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 79 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 80 | frptype | frptype | varchar | 30 |  | √ | ' ' |  |
| 81 | fbeendorsortext | fbeendorsortext | varchar | 512 |  | √ | ' ' |  |
| 82 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 83 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |
| 84 | fdepositamount | fdepositamount | numeric | 19 | 6 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_drafttradebill_pkey |  | fid |
| 2 | idx_drafttradebill_billno |  | fbillno |
| 3 | idx_cdm_drafttrad_allocentid |  | fallocbillentryid |
