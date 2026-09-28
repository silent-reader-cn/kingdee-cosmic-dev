# 千户集团报表查询-tcvvt_month_declare_list

## 千户集团报表查询-主表 t_tctb_declare_main

- **表名称：** 千户集团报表查询-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 7 | fyssr | fyssr | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 9 | fbqybtse | fbqybtse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 12 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 13 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 15 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 16 | ftemplateid | ftemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 19 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 |
| 20 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 21 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 24 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 25 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 28 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 29 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: qhjtydbs :千户集团报送 |
| 34 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 |
| 35 | ffddbrxm | ffddbrxm | varchar | 50 |  | √ | ' ' |  |
| 36 | fscjydz | fscjydz | varchar | 300 |  | √ | ' ' |  |
| 37 | fphonenum | fphonenum | varchar | 50 |  | √ | ' ' |  |
| 38 | fpayer | fpayer | int8 | 64 |  | √ | 0 |  |
| 39 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 submitted :已提交待申报 declaring :申报中 importing :已申报未导入 declared :申报成功 declarefailed :申报失败 |
| 41 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 43 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 46 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 47 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 48 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 49 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 50 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 53 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 54 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 55 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 56 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 57 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 58 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 59 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 60 | fpaytype | fpaytype | varchar | 50 |  | √ | ' ' |  |
| 61 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 62 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 63 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 64 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 65 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 66 | fpaydate | fpaydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_main |  | fid |
| 2 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
