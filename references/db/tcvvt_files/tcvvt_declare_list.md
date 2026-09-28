# 申报查询-tcvvt_declare_list

## 申报查询-主表 t_tctb_declare_main

- **表名称：** 申报查询-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 7 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税收入 |
| 8 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 12 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 13 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 16 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 19 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 false :—— |
| 20 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 21 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 24 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 25 | fdeclarer | fdeclarer | int8 | 64 |  | √ | 0 |  |
| 26 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 28 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 29 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: qysdsyb :月度预缴 qysdsjb :季度预缴 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_yb :核定月度预缴 qysds_hdzs_jb :核定季度预缴 qysds_hdzs_nb :核定汇算清缴 |
| 34 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |
| 35 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 36 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 37 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 38 | fpayer | fpayer | int8 | 64 |  | √ | 0 |  |
| 39 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 41 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 43 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 46 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 47 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 48 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
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
