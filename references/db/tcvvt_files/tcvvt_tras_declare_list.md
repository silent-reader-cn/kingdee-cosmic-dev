# 重点税源报表查询-tcvvt_tras_declare_list

## 重点税源报表查询-主表 t_tctb_declare_main

- **表名称：** 重点税源报表查询-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fclearstatus | fclearstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 8 | fyssr | fyssr | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 10 | fbqybtse | fbqybtse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 14 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 15 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | ftemplateid | ftemplateid | varchar | 50 |  | √ | ' ' |  |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 |
| 24 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 25 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 28 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 29 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 30 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 33 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 35 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 36 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: zdsybs_yd :重点税源报表(月度) zdsybs_jd :重点税源报表(季度) |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据导入 |
| 40 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 41 | ffddbrxm | ffddbrxm | varchar | 50 |  | √ | ' ' |  |
| 42 | fscjydz | fscjydz | varchar | 300 |  | √ | ' ' |  |
| 43 | fphonenum | fphonenum | varchar | 50 |  | √ | ' ' |  |
| 44 | fpayer | fpayer | int8 | 64 |  | √ | 0 |  |
| 45 | fbusinesstype | fbusinesstype | varchar | 50 |  | √ | ' ' |  |
| 46 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 47 | fhistoryversion | fhistoryversion | varchar | 50 |  | √ | ' ' |  |
| 48 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 49 | fclearedtime | fclearedtime | timestamp | 0 |  |  | null |  |
| 50 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 submitted :已提交待申报 declaring :申报中 importing :已申报未导入 declared :申报成功 declarefailed :申报失败 |
| 51 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 52 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 53 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 56 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 57 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 58 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 59 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 60 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 61 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 62 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 63 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 64 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 65 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 66 | fcleartime | fcleartime | timestamp | 0 |  |  | null |  |
| 67 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 68 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 69 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 70 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 71 | fisxxwlqy | fisxxwlqy | varchar | 10 |  | √ | ' ' |  |
| 72 | fpaytype | fpaytype | varchar | 50 |  | √ | ' ' |  |
| 73 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 74 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 75 | flogsummary | flogsummary | varchar | 255 |  | √ | ' ' |  |
| 76 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 77 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 78 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 79 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 80 | fpaydate | fpaydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
| 2 | pk_tctb_declare_main |  | fid |
