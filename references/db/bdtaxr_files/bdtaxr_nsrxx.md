# 纳税申报表基础资料-bdtaxr_nsrxx

## 纳税申报表基础资料-主表 t_tctb_declare_main

- **表名称：** 纳税申报表基础资料-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 7 | fyssr | fyssr | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 9 | fbqybtse | fbqybtse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 12 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 13 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 16 | ftemplateid | ftemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 19 | ftaxlimit | ftaxlimit | varchar | 50 |  | √ | ' ' |  |
| 20 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 21 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 24 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 25 | fdeclarer | fdeclarer | int8 | 64 |  | √ | 0 |  |
| 26 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 28 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 29 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fnsrtype | fnsrtype | varchar | 36 |  | √ | ' ' |  |
| 34 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 35 | ffddbrxm | ffddbrxm | varchar | 50 |  | √ | ' ' |  |
| 36 | fscjydz | fscjydz | varchar | 300 |  | √ | ' ' |  |
| 37 | fphonenum | fphonenum | varchar | 50 |  | √ | ' ' |  |
| 38 | fpayer | fpayer | int8 | 64 |  | √ | 0 |  |
| 39 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 declarefailed :● 申报失败 |
| 41 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 43 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 46 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 47 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 48 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 49 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 50 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 53 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 54 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fsbrq | fsbrq | timestamp | 0 |  |  | null |  |
| 57 | fdeclaretype | fdeclaretype | varchar | 50 |  | √ | ' ' |  |
| 58 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 59 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 60 | fpaytype | fpaytype | varchar | 50 |  | √ | ' ' |  |
| 61 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 62 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 63 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 64 | fbusinessno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
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
