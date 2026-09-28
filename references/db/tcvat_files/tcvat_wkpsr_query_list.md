# 未开票收入台账查询-tcvat_wkpsr_query_list

## 单据体-子表 t_tcvat_wkpsr_listentry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_wkpsr_listentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbqyysbdwkjfpxsehj | 本期用于申报的未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 本期用于申报的未开具发票销售额合计 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fyssrhj | 应税收入合计 | numeric | 23 | 10 | √ | 0 | 应税收入合计 |
| 4 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 5 | fwkjfpxsetzlhj | 未开具发票销售额调整列合计 | numeric | 23 | 10 | √ | 0 | 未开具发票销售额调整列合计 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 8 | fbqsjsbwkjfpsehj | 本期实际申报未开具发票税额合计 | numeric | 23 | 10 | √ | 0 | 本期实际申报未开具发票税额合计 |
| 9 | fqcwkjfpxsehj | 期初未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 期初未开具发票销售额合计 |
| 10 | fqmwkjfpxseyehj | 期末未开具发票销售额余额合计 | numeric | 23 | 10 | √ | 0 | 期末未开具发票销售额余额合计 |
| 11 | fbqsjwkjfpxsehj | 本期实际未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 本期实际未开具发票销售额合计 |
| 12 | fbqyysbdwkjfpxselms | fbqyysbdwkjfpxselms | varchar | 50 |  | √ | ' ' |  |
| 13 | fykpsrhj | 已开票收入合计 | numeric | 23 | 10 | √ | 0 | 已开票收入合计 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_wkpsr_listentry |  | fentryid |
| 2 | idx_tcvat_wkpsr_listentry_fk |  | fid |

---

## 未开票收入台账查询-主表 t_tctb_declare_main

- **表名称：** 未开票收入台账查询-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fclearstatus | fclearstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 8 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税收入 |
| 9 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 10 | fbqybtse | fbqybtse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 14 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 15 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 |
| 24 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
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
| 38 | fnsrtype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: zzstz :增值税台账 |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 3 :税局下载 |
| 40 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 41 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 42 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 43 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 44 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fbusinesstype | fbusinesstype | varchar | 50 |  | √ | ' ' |  |
| 46 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 47 | fhistoryversion | fhistoryversion | varchar | 50 |  | √ | ' ' |  |
| 48 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 49 | fclearedtime | fclearedtime | timestamp | 0 |  |  | null |  |
| 50 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 declared :● 申报成功 declarefailed :● 申报失败 importing :● 已申报未导入 |
| 51 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 submitted :● 已提交待缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 yypaid :● 预约成功 yypayfailed :● 预约失败 |
| 52 | fsblx | fsblx | varchar | 50 |  | √ | ' ' |  |
| 53 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 56 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 57 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 58 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 59 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 60 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 61 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 63 | fdeclaredate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 64 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fcleartime | fcleartime | timestamp | 0 |  |  | null |  |
| 67 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 68 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 69 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 70 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 71 | fisxxwlqy | fisxxwlqy | varchar | 10 |  | √ | ' ' |  |
| 72 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 73 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 74 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 75 | flogsummary | flogsummary | varchar | 255 |  | √ | ' ' |  |
| 76 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 77 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 78 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 79 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 80 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
| 2 | pk_tctb_declare_main |  | fid |
