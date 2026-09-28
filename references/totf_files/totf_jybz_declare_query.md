# 残疾人就业保障金缴费申报查询-totf_jybz_declare_query

## 残疾人就业保障金缴费申报查询-主表 t_tpo_declare_main_tsc

- **表名称：** 残疾人就业保障金缴费申报查询-主表
- **表名：** t_tpo_declare_main_tsc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 5 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 6 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 7 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 8 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fismodified | fismodified | varchar | 50 |  | √ | ' ' |  |
| 11 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 14 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 17 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: |
| 18 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 19 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 22 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 23 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 25 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 26 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 27 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 28 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 29 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 3 :税局下载 |
| 32 | ffddbrxm | ffddbrxm | varchar | 50 |  | √ | ' ' |  |
| 33 | fscjydz | fscjydz | varchar | 300 |  | √ | ' ' |  |
| 34 | fphonenum | fphonenum | varchar | 50 |  | √ | ' ' |  |
| 35 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 37 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 importing :● 已申报未导入 declared :● 申报成功 declarefailed :● 申报失败 |
| 38 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 yypaid :● 预约成功 yypayfailed :● 预约失败 |
| 39 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 40 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 43 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 44 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 45 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 46 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 47 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 48 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 49 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 50 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 51 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 52 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 53 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 54 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 55 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 56 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 57 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 58 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 59 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 60 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 61 | fdeclaremethod | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 62 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_declare_main_tsc_fbillno |  | fbillno |
| 2 | pk_tpo_declare_main_tsc |  | fid |

---

## 单据体-子表 t_totf_jybz_declare

- **表名称：** 单据体-子表
- **表名：** t_totf_jybz_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeclaredate | 申报编制日期 | timestamp | 0 |  |  | null | 申报编制日期 |
| 3 | fismodified | 是否修改 | varchar | 50 |  | √ | ' ' | 是否修改,枚举: 1 :是 0 :否 |
| 4 | fqjje | 欠缴费额 | numeric | 23 | 10 | √ | 0 | 欠缴费额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsjje | 本期已缴费额 | numeric | 23 | 10 | √ | 0 | 本期已缴费额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbqdybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_jybz_declare |  | fentryid |
| 2 | idx_totf_jybz_declare_fk |  | fid |
