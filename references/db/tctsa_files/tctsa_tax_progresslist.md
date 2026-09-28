# 申报进度明细-tctsa_tax_progresslist

## 申报进度明细-主表 t_tctb_declare_main

- **表名称：** 申报进度明细-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fclearstatus | fclearstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 8 | fyssr | fyssr | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 10 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 11 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 14 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 15 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 18 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | ftemplateid | ftemplateid | varchar | 50 |  | √ | ' ' |  |
| 21 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 22 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxlimit | ftaxlimit | varchar | 50 |  | √ | ' ' |  |
| 24 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 25 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 26 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 27 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 28 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 29 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 30 | fdeclarer | fdeclarer | int8 | 64 |  | √ | 0 |  |
| 31 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 33 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 35 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 36 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 37 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 38 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） |
| 39 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
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
| 50 | fdeclarestatus | 申报表状态 | varchar | 50 |  | √ | ' ' | 申报表状态,枚举: editing :未申报 declaring :申报中 declared :申报成功 undeclare :未编制 declarefailed :申报失败 |
| 51 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 52 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 53 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 54 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 55 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 56 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 57 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 58 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 59 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 60 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 61 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 62 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 63 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 64 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 65 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 66 | fcleartime | fcleartime | timestamp | 0 |  |  | null |  |
| 67 | fsbrq | fsbrq | timestamp | 0 |  |  | null |  |
| 68 | fdeclaretype | fdeclaretype | varchar | 50 |  | √ | ' ' |  |
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
| 1 | pk_tctb_declare_main |  | fid |
| 2 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
