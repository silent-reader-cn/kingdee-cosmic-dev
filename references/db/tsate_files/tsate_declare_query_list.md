# 一键报税-tsate_declare_query_list

## 一键报税-主表 t_tctb_declare_main

- **表名称：** 一键报税-主表
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
| 11 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
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
| 25 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 28 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 29 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fnsrtype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: zzsybnsr :一般纳税人增值税及附加税费 zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsxgmnsr :小规模增值税及附加税费 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcscztdsys :房产和城镇土地使用税 ccxws :财产行为税 FR0001 :财务报表（一般企业_未执行） FR0002 :财务报表（一般企业_已执行） FR0003 :财务报表（小企业会计准则） FR0004 :财务报表（企业会计制度） FR0011 :财务报表（金融企业会计准则） zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 qtsf_fsstysbb :非税收入通用申报表 qtsf_tysbb :通用申报表（税及附征税费） zdsybs_yd :重点税源表（月度） |
| 34 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |
| 35 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 36 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 37 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 38 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: undeclare :未编制 editing :未申报 submitted :已提交待申报 declaring :申报中 importing :已申报未导入 declared :申报成功 declarefailed :申报失败 |
| 41 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :未缴款 nopay :无需缴款 yypaid :预约成功 submitted :已提交待缴款 paying :缴款中 paid :缴款成功 partpaid :部分缴款 yypayfailed :预约失败 payfailed :缴款失败 |
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
| 52 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 53 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 54 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 57 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 58 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 59 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 60 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 2 :预约缴款 |
| 61 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 62 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 63 | friskstatus | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: 0 :正常 1 :异常 |
| 64 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 65 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 66 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_main |  | fid |
| 2 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
