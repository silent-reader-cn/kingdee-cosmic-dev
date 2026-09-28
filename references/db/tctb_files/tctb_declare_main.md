# 纳税申报主表-tctb_declare_main

## 纳税申报主表-主表 t_tctb_declare_main

- **表名称：** 纳税申报主表-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 集团名册id | int8 | 64 |  | √ | 0 | 集团名册id |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fclearstatus | fclearstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 8 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税收入 |
| 9 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 10 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 11 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 14 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 15 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fapanage | 属地管理 | varchar | 50 |  | √ | ' ' | 属地管理 |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | ftemplateid | 申报表模板主键 | varchar | 50 |  | √ | ' ' | 申报表模板主键 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 23 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: |
| 24 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 25 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 28 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 29 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 30 | fdeclarer | fdeclarer | int8 | 64 |  | √ | 0 |  |
| 31 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 33 | ftcrettype | 房产申报表类型 | varchar | 50 |  | √ | ' ' | 房产申报表类型,枚举: fcscztdsys :房产和城镇土地使用税 |
| 34 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 35 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 36 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fnsrtype | 模板类型 | varchar | 36 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: |
| 40 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 41 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 42 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 43 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 44 | fpayer | fpayer | int8 | 64 |  | √ | 0 |  |
| 45 | fbusinesstype | fbusinesstype | varchar | 50 |  | √ | ' ' |  |
| 46 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 47 | fhistoryversion | fhistoryversion | varchar | 50 |  | √ | ' ' |  |
| 48 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 49 | fclearedtime | fclearedtime | timestamp | 0 |  |  | null |  |
| 50 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: |
| 51 | fpaystatus | fpaystatus | varchar | 50 |  | √ | ' ' |  |
| 52 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 53 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 56 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 57 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 58 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 59 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 60 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 61 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 63 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 64 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fcleartime | fcleartime | timestamp | 0 |  |  | null |  |
| 67 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
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
