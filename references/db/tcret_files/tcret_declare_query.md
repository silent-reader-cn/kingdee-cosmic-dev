# 房产和土地使用税查询-tcret_declare_query

## 房产和土地使用税查询-主表 t_tctb_declare_main

- **表名称：** 房产和土地使用税查询-主表
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
| 15 | fapanage | 属地管理 | varchar | 50 |  | √ | ' ' | 属地管理 |
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
| 28 | ftcrettype | 申报表内容 | varchar | 50 |  | √ | ' ' | 申报表内容,枚举: fcs :房产税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 cztdsys :城镇土地使用税 |
| 29 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: fcscztdsys :房产和城镇土地使用税 |
| 34 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 |
| 35 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 36 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 37 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 38 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 declared :● 申报成功 declarefailed :● 申报失败 importing :● 已申报未导入 |
| 41 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 submitted :● 已提交待缴款 paying :● 缴款中 paid :● 缴款成功 payfailed :● 缴款失败 nopay :● 无需缴款 yypaid :● 预约成功 yypayfailed :● 预约失败 |
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
| 56 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 57 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 58 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 59 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 60 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 61 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 62 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 63 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 64 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 65 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
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
