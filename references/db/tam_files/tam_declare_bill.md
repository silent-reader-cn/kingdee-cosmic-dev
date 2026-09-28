# 申报表单据列表-tam_declare_bill

## 单据体-子表 t_tam_declare_entry

- **表名称：** 单据体-子表
- **表名：** t_tam_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 3 | fzerodeclare | 是否零申报 | varchar | 50 |  | √ | ' ' | 是否零申报,枚举: true :是 false :否 |
| 4 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 7 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_declare_entry |  | fentryid |
| 2 | idx_tam_declare_entry_fk |  | fid |

---

## 申报表单据列表-主表 t_tctb_declare_main

- **表名称：** 申报表单据列表-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fclearstatus | fclearstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fversiontype | 版本类型 | varchar | 50 |  | √ | ' ' | 版本类型,枚举: zcsb :正常申报 gzsb :更正申报 sjxz :税局下载 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 8 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税收入 |
| 9 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 10 | fbqybtse | 合计本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计本期应补（退）税额 |
| 11 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 14 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 15 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 |
| 24 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 25 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 28 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 29 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 30 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 33 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 35 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 36 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: qysdsjb :预缴申报 qysds_hdzs_jb :核定预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_nb :核定汇算清缴 zzsybnsr :一般纳税人增值税及附加税费 zzsxgmnsr :小规模增值税及附加税费 fjsf :附加税费 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 zzsybnsr_yz_fzjg :一般企业汇总申报预征方式分支机构 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 zzsyjskb :增值税预缴税款表 ccxws :财产行为税 whsyjsf :文化事业建设费 qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 FR0001 :一般企业会计准则（未执行） FR0002 :一般企业会计准则（已执行） FR0003 :小企业会计准则 FR0004 :企业会计制度 szys_a :水资源税Ａ szys_b :水资源税Ｂ FR0011 :金融企业会计准则 |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 |
| 40 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 41 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 42 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 43 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 44 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fbusinesstype | fbusinesstype | varchar | 50 |  | √ | ' ' |  |
| 46 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 47 | fhistoryversion | 历史版本 | varchar | 50 |  | √ | ' ' | 历史版本,枚举: 1 :历史版本 |
| 48 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 49 | fclearedtime | fclearedtime | timestamp | 0 |  |  | null |  |
| 50 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: undeclare :● 未编制 editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 importing :● 已申报未导入 declared :● 申报成功 declarefailed :● 申报失败 |
| 51 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 nopay :● 无需缴款 yypaid :● 预约成功 submitted :● 已提交待缴款 paying :● 缴款中 paid :● 缴款成功 partpaid :● 部分缴款 yypayfailed :● 预约失败 payfailed :● 缴款失败 |
| 52 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 53 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 56 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 57 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 58 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 59 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 60 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 61 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 63 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 64 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fcleartime | fcleartime | timestamp | 0 |  |  | null |  |
| 67 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 68 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 69 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 70 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 71 | fisxxwlqy | fisxxwlqy | varchar | 10 |  | √ | ' ' |  |
| 72 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 73 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 74 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 75 | flogsummary | flogsummary | varchar | 255 |  | √ | ' ' |  |
| 76 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 77 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 78 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 79 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 80 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_main |  | fid |
| 2 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
